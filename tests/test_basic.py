"""
Basic tests for minecraft-server-utility
"""
import unittest
from unittest.mock import patch, MagicMock

from minecraft_server_utility import ServerPinger, BedrockPinger, MojangAPI
from minecraft_server_utility.exceptions import ServerOfflineException, MojangAPIException


class TestServerPinger(unittest.TestCase):
    """Test ServerPinger class"""

    def test_initialization(self):
        """Test ServerPinger initialization"""
        pinger = ServerPinger("example.com", 25565, 5)
        self.assertEqual(pinger.host, "example.com")
        self.assertEqual(pinger.port, 25565)
        self.assertEqual(pinger.timeout, 5)

    def test_default_values(self):
        """Test default values"""
        pinger = ServerPinger("example.com")
        self.assertEqual(pinger.port, 25565)
        self.assertEqual(pinger.timeout, 5)

    @patch('socket.socket')
    def test_is_online_false(self, mock_socket):
        """Test is_online returns False for invalid server"""
        mock_socket.return_value.connect.side_effect = ConnectionRefusedError
        pinger = ServerPinger("invalid.server", 25565, timeout=1)
        self.assertFalse(pinger.is_online())

    @patch('socket.socket')
    def test_get_player_count_offline(self, mock_socket):
        """Test get_player_count returns 0 when server is offline"""
        mock_socket.return_value.connect.side_effect = ConnectionRefusedError
        pinger = ServerPinger("invalid.server", 25565, timeout=1)
        self.assertEqual(pinger.get_player_count(), 0)

    def test_string_representation(self):
        """Test string representation"""
        pinger = ServerPinger("mc.hypixel.net", 25565)
        self.assertIn("mc.hypixel.net", str(pinger))
        self.assertIn("25565", str(pinger))


class TestBedrockPinger(unittest.TestCase):
    """Test BedrockPinger class"""

    def test_initialization(self):
        pinger = BedrockPinger("example.com", 19132, 5)
        self.assertEqual(pinger.host, "example.com")
        self.assertEqual(pinger.port, 19132)

    @patch('socket.socket')
    def test_ping_offline_does_not_crash_on_socket_creation_failure(self, mock_socket):
        """A failure creating the socket itself must not raise UnboundLocalError."""
        mock_socket.side_effect = OSError("network unreachable")
        pinger = BedrockPinger("invalid.server", 19132, timeout=1)
        self.assertFalse(pinger.is_online())

    def test_parse_response_reads_semicolon_delimited_fields(self):
        """Bedrock's unconnected pong payload is semicolon-delimited, not JSON."""
        pinger = BedrockPinger("example.com")
        server_id = "MCPE;My Server;622;1.20.10;5;20;123456789;Bedrock level;Survival;1;19132;19133;"
        # Build a minimal fake response payload matching the real wire format
        import struct as _struct
        payload = bytearray()
        payload += b'\x1c'  # header byte
        payload += _struct.pack('>Q', 1234567890)  # server guid
        payload += b'\x00' * 16  # magic
        sid_bytes = server_id.encode('utf-8')
        payload += _struct.pack('>H', len(sid_bytes))
        payload += sid_bytes

        result = pinger._parse_response(bytes(payload))
        self.assertEqual(result['edition'], "MCPE")
        self.assertEqual(result['motd'], "My Server")
        self.assertEqual(result['version'], "1.20.10")
        self.assertEqual(result['online_players'], 5)
        self.assertEqual(result['max_players'], 20)


class TestMojangAPI(unittest.TestCase):
    """Test MojangAPI class"""

    def test_initialization(self):
        """Test MojangAPI initialization"""
        api = MojangAPI(timeout=10)
        self.assertEqual(api.timeout, 10)

    @patch('requests.Session.get')
    def test_get_uuid_success(self, mock_get):
        """Test successful UUID lookup"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": "069a79f444e94726a5befca90e38aaf5",
            "name": "TestPlayer"
        }
        mock_get.return_value = mock_response

        api = MojangAPI()
        uuid = api.get_uuid("TestPlayer")

        self.assertEqual(uuid, "069a79f444e94726a5befca90e38aaf5")
        mock_get.assert_called_once_with(
            "https://api.mojang.com/users/profiles/minecraft/TestPlayer",
            timeout=10
        )

    @patch('requests.Session.get')
    def test_get_uuid_not_found(self, mock_get):
        """Test UUID lookup for non-existent player"""
        mock_response = MagicMock()
        mock_response.status_code = 204  # No content
        mock_get.return_value = mock_response

        api = MojangAPI()
        uuid = api.get_uuid("NonExistentPlayer123")

        self.assertIsNone(uuid)

    @patch('requests.Session.get')
    def test_get_uuid_error(self, mock_get):
        """Test UUID lookup with API error"""
        import requests
        mock_get.side_effect = requests.RequestException("Network error")

        api = MojangAPI()

        with self.assertRaises(MojangAPIException):
            api.get_uuid("TestPlayer")

    @patch('requests.Session.get')
    def test_get_profile_success(self, mock_get):
        """Test successful profile lookup"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": "069a79f444e94726a5befca90e38aaf5",
            "name": "TestPlayer"
        }
        mock_get.return_value = mock_response

        api = MojangAPI()
        profile = api.get_profile("069a79f444e94726a5befca90e38aaf5")

        self.assertEqual(profile["id"], "069a79f444e94726a5befca90e38aaf5")
        self.assertEqual(profile["name"], "TestPlayer")

    @patch('requests.Session.get')
    def test_get_name_history_deprecated_endpoint_returns_empty_list(self, mock_get):
        """Mojang removed this endpoint; a 404/410 should not raise."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        api = MojangAPI()
        history = api.get_name_history("069a79f444e94726a5befca90e38aaf5")
        self.assertEqual(history, [])

    @patch('requests.Session.get')
    def test_search_player_survives_name_history_failure(self, mock_get):
        """search_player should still return uuid/profile/skin even if name history 404s."""
        def side_effect(url, timeout):
            resp = MagicMock()
            if "users/profiles/minecraft" in url:
                resp.status_code = 200
                resp.json.return_value = {"id": "abc123"}
            elif "session/minecraft/profile" in url:
                resp.status_code = 200
                resp.json.return_value = {"id": "abc123", "name": "TestPlayer"}
            elif "user/profiles" in url and "/names" in url:
                resp.status_code = 404
            return resp

        mock_get.side_effect = side_effect

        api = MojangAPI()
        result = api.search_player("TestPlayer")

        self.assertTrue(result['found'])
        self.assertEqual(result['uuid'], "abc123")
        self.assertEqual(result['name_history'], [])


class TestExceptions(unittest.TestCase):
    """Test custom exceptions"""

    def test_server_offline_exception(self):
        """Test ServerOfflineException"""
        with self.assertRaises(ServerOfflineException) as context:
            raise ServerOfflineException("Server is offline")

        self.assertEqual(str(context.exception), "Server is offline")
        self.assertTrue(isinstance(context.exception, Exception))


if __name__ == '__main__':
    unittest.main()

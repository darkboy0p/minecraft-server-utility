"""
Basic tests for minecraft-server-utility
"""
import unittest
from unittest.mock import patch, MagicMock

# Import from the package
from minecraft_server_utility import ServerPinger, MojangAPI
from minecraft_server_utility.exceptions import ServerOfflineException


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
        mock_get.side_effect = Exception("Network error")
        
        api = MojangAPI()
        
        with self.assertRaises(Exception):
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

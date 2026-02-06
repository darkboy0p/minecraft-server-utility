"""
Basic tests for minecraft-server-utility
"""
import unittest
from unittest.mock import patch, MagicMock
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
    
    @patch('requests.Session.get')
    def test_get_uuid_not_found(self, mock_get):
        """Test UUID lookup for non-existent player"""
        mock_response = MagicMock()
        mock_response.status_code = 204  # No content
        mock_get.return_value = mock_response
        
        api = MojangAPI()
        uuid = api.get_uuid("NonExistentPlayer123")
        
        self.assertIsNone(uuid)

class TestExceptions(unittest.TestCase):
    """Test custom exceptions"""
    
    def test_exception_messages(self):
        """Test exception messages"""
        with self.assertRaises(ServerOfflineException) as context:
            raise ServerOfflineException("Server is offline")
        
        self.assertEqual(str(context.exception), "Server is offline")

if __name__ == '__main__':
    unittest.main()

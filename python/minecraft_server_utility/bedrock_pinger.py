import socket
import struct
import json
import time
from typing import Dict, Any, Optional
from .exceptions import ServerOfflineException

class BedrockPinger:
    """Ping Minecraft Bedrock Edition servers"""
    
    def __init__(self, host: str, port: int = 19132, timeout: int = 5):
        self.host = host
        self.port = port
        self.timeout = timeout
        
    def ping(self) -> Dict[str, Any]:
        """Ping Bedrock server"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(self.timeout)
            
            # Create unconnected ping packet
            packet = bytearray()
            packet.extend(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78')
            
            # Add client GUID
            packet.extend(b'\x00\x00\x00\x00\x00\x00\x00\x00')
            
            # Send ping
            start_time = time.time()
            sock.sendto(bytes(packet), (self.host, self.port))
            
            # Receive response
            data, _ = sock.recvfrom(1024)
            latency = (time.time() - start_time) * 1000
            
            # Parse response
            response = self._parse_response(data)
            response['latency'] = round(latency, 2)
            response['online'] = True
            response['host'] = self.host
            response['port'] = self.port
            
            return response
            
        except socket.timeout:
            raise ServerOfflineException(f"Bedrock server {self.host}:{self.port} is offline")
        except Exception as e:
            raise ServerOfflineException(f"Error pinging bedrock server: {str(e)}")
        finally:
            sock.close()
    
    def _parse_response(self, data: bytes) -> Dict[str, Any]:
        """Parse Bedrock server response"""
        # Skip header (1 byte)
        offset = 1
        
        # Read server GUID (8 bytes)
        server_guid = struct.unpack_from('>Q', data, offset)[0]
        offset += 8
        
        # Read magic (16 bytes)
        offset += 16
        
        # Read server ID length
        server_id_len = struct.unpack_from('>H', data, offset)[0]
        offset += 2
        
        # Read server ID
        server_id = data[offset:offset + server_id_len].decode('utf-8')
        offset += server_id_len
        
        # Parse server info from JSON
        server_info = json.loads(server_id.split(';')[0])
        
        return {
            'server_guid': server_guid,
            'edition': server_info.get('edition', 'Unknown'),
            'motd': server_info.get('motd', ''),
            'version': server_info.get('version', ''),
            'protocol': server_info.get('protocol', 0),
            'max_players': server_info.get('maxPlayers', 0),
            'online_players': server_info.get('players', 0),
            'server_id': server_info.get('serverId', ''),
            'gamemode': server_info.get('gamemode', 'Unknown'),
            'port_v4': server_info.get('portIPv4', 0),
            'port_v6': server_info.get('portIPv6', 0)
        }
    
    def is_online(self) -> bool:
        """Check if Bedrock server is online"""
        try:
            self.ping()
            return True
        except ServerOfflineException:
            return False

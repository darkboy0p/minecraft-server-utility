import socket
import struct
import json
import time
from typing import Dict, Any, Optional
from .exceptions import ServerOfflineException, BedrockException

class BedrockPinger:
    """Ping Minecraft Bedrock Edition servers"""

    def __init__(self, host: str, port: int = 19132, timeout: int = 5):
        self.host = host
        self.port = port
        self.timeout = timeout

    def ping(self) -> Dict[str, Any]:
        """Ping Bedrock server"""
        sock = None
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
        except (socket.gaierror, OSError) as e:
            raise ServerOfflineException(f"Bedrock server {self.host}:{self.port} is unreachable: {e}")
        except ServerOfflineException:
            raise
        except Exception as e:
            raise BedrockException(f"Error pinging bedrock server: {str(e)}")
        finally:
            if sock is not None:
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
        fields = server_id.split(';')
        server_info = {
            'edition': fields[0] if len(fields) > 0 else 'Unknown',
            'motd': fields[1] if len(fields) > 1 else '',
            'protocol': int(fields[2]) if len(fields) > 2 and fields[2].isdigit() else 0,
            'version': fields[3] if len(fields) > 3 else '',
            'players': int(fields[4]) if len(fields) > 4 and fields[4].isdigit() else 0,
            'maxPlayers': int(fields[5]) if len(fields) > 5 and fields[5].isdigit() else 0,
            'serverId': fields[6] if len(fields) > 6 else '',
            'gamemode': fields[8] if len(fields) > 8 else 'Unknown',
            'portIPv4': int(fields[10]) if len(fields) > 10 and fields[10].isdigit() else 0,
            'portIPv6': int(fields[11]) if len(fields) > 11 and fields[11].isdigit() else 0,
        }

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

    def __repr__(self) -> str:
        return f"BedrockPinger(host={self.host!r}, port={self.port}, timeout={self.timeout})"

    def __str__(self) -> str:
        return f"BedrockPinger({self.host}:{self.port})"

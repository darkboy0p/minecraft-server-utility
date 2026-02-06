import socket
import json
import struct
import time
from typing import Dict, List, Optional, Any
from .exceptions import ServerOfflineException, InvalidServerException

class ServerPinger:
    """Ping Minecraft Java Edition servers"""
    
    def __init__(self, host: str, port: int = 25565, timeout: int = 5):
        self.host = host
        self.port = port
        self.timeout = timeout
        
    def ping(self) -> Dict[str, Any]:
        """Ping server and return comprehensive information"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            sock.connect((self.host, self.port))
            
            # Send handshake packet
            handshake = self._create_handshake()
            self._send_packet(sock, handshake)
            
            # Send status request
            self._send_packet(sock, b'\x01\x00')
            
            # Read response
            response = self._read_response(sock)
            sock.close()
            
            if not response:
                raise ServerOfflineException(f"Server {self.host}:{self.port} is offline")
            
            # Parse JSON response
            data = json.loads(response)
            
            return {
                'online': True,
                'host': self.host,
                'port': self.port,
                'version': data.get('version', {}).get('name', 'Unknown'),
                'protocol': data.get('version', {}).get('protocol', -1),
                'players': {
                    'online': data.get('players', {}).get('online', 0),
                    'max': data.get('players', {}).get('max', 0),
                    'list': data.get('players', {}).get('sample', [])
                },
                'motd': self._parse_motd(data.get('description', {})),
                'favicon': data.get('favicon'),
                'latency': self._measure_latency(),
                'raw_response': data
            }
            
        except (socket.timeout, ConnectionRefusedError):
            raise ServerOfflineException(f"Server {self.host}:{self.port} is offline")
        except Exception as e:
            raise InvalidServerException(f"Error pinging server: {str(e)}")
    
    def _create_handshake(self) -> bytes:
        """Create handshake packet"""
        host_bytes = self.host.encode('utf-8')
        packet = b''
        
        # Packet ID (0x00 for handshake)
        packet += b'\x00'
        
        # Protocol version (varint)
        packet += self._pack_varint(762)  # 1.19.4 protocol
        
        # Server address (varint + string)
        packet += self._pack_varint(len(host_bytes))
        packet += host_bytes
        
        # Server port (unsigned short)
        packet += struct.pack('>H', self.port)
        
        # Next state (1 for status)
        packet += b'\x01'
        
        # Prepend length
        length = self._pack_varint(len(packet))
        return length + packet
    
    def _send_packet(self, sock: socket.socket, data: bytes):
        """Send packet to socket"""
        sock.sendall(data)
    
    def _read_response(self, sock: socket.socket) -> str:
        """Read response from socket"""
        # Read packet length
        length = self._read_varint(sock)
        
        # Read packet ID
        packet_id = self._read_varint(sock)
        
        if packet_id != 0x00:
            return ""
        
        # Read string length
        string_length = self._read_varint(sock)
        
        # Read JSON string
        data = b''
        while len(data) < string_length:
            chunk = sock.recv(string_length - len(data))
            if not chunk:
                break
            data += chunk
        
        return data.decode('utf-8')
    
    def _pack_varint(self, value: int) -> bytes:
        """Pack integer as varint"""
        result = bytearray()
        while True:
            byte = value & 0x7F
            value >>= 7
            if value != 0:
                byte |= 0x80
            result.append(byte)
            if value == 0:
                break
        return bytes(result)
    
    def _read_varint(self, sock: socket.socket) -> int:
        """Read varint from socket"""
        result = 0
        shift = 0
        while True:
            byte = sock.recv(1)
            if not byte:
                break
            byte = byte[0]
            result |= (byte & 0x7F) << shift
            shift += 7
            if not (byte & 0x80):
                break
        return result
    
    def _parse_motd(self, motd_data: Any) -> str:
        """Parse MOTD from server response"""
        if isinstance(motd_data, str):
            return motd_data
        elif isinstance(motd_data, dict):
            # Extract text from JSON motd
            text = motd_data.get('text', '')
            if 'extra' in motd_data:
                for extra in motd_data.get('extra', []):
                    text += extra.get('text', '')
            return text.strip()
        return str(motd_data)
    
    def _measure_latency(self) -> float:
        """Measure ping latency in milliseconds"""
        try:
            start = time.time()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            sock.connect((self.host, self.port))
            sock.close()
            return round((time.time() - start) * 1000, 2)
        except:
            return -1.0
    
    def is_online(self) -> bool:
        """Check if server is online"""
        try:
            self.ping()
            return True
        except ServerOfflineException:
            return False
    
    def get_player_count(self) -> int:
        """Get online player count"""
        try:
            info = self.ping()
            return info['players']['online']
        except ServerOfflineException:
            return 0
    
    def get_player_list(self) -> List[str]:
        """Get list of online players"""
        try:
            info = self.ping()
            players = info['players']['list']
            return [player['name'] for player in players]
        except (ServerOfflineException, KeyError):
            return []
    
    def get_motd(self) -> str:
        """Get server MOTD"""
        try:
            info = self.ping()
            return info['motd']
        except ServerOfflineException:
            return ""
    
    def get_version(self) -> str:
        """Get server version"""
        try:
            info = self.ping()
            return info['version']
        except ServerOfflineException:
            return "Unknown"

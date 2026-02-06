import requests
import base64
import json
from typing import Dict, List, Optional, Any
from .exceptions import MojangAPIException

class MojangAPI:
    """Interact with Mojang API for player data"""
    
    BASE_URL = "https://api.mojang.com"
    SESSION_URL = "https://sessionserver.mojang.com"
    
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.session = requests.Session()
    
    def get_uuid(self, username: str) -> Optional[str]:
        """Get UUID from username"""
        try:
            response = self.session.get(
                f"{self.BASE_URL}/users/profiles/minecraft/{username}",
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('id')
            elif response.status_code == 204:
                return None
            else:
                raise MojangAPIException(f"API error: {response.status_code}")
                
        except requests.RequestException as e:
            raise MojangAPIException(f"Failed to get UUID: {str(e)}")
    
    def get_username(self, uuid: str) -> Optional[str]:
        """Get username from UUID"""
        try:
            response = self.session.get(
                f"{self.SESSION_URL}/session/minecraft/profile/{uuid}",
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('name')
            else:
                raise MojangAPIException(f"API error: {response.status_code}")
                
        except requests.RequestException as e:
            raise MojangAPIException(f"Failed to get username: {str(e)}")
    
    def get_profile(self, uuid: str) -> Optional[Dict[str, Any]]:
        """Get full player profile including skin"""
        try:
            response = self.session.get(
                f"{self.SESSION_URL}/session/minecraft/profile/{uuid}",
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Decode textures
                if 'properties' in data:
                    for prop in data['properties']:
                        if prop.get('name') == 'textures':
                            textures_data = base64.b64decode(prop['value'])
                            textures = json.loads(textures_data)
                            data['textures'] = textures
                            break
                
                return data
            else:
                raise MojangAPIException(f"API error: {response.status_code}")
                
        except requests.RequestException as e:
            raise MojangAPIException(f"Failed to get profile: {str(e)}")
    
    def get_name_history(self, uuid: str) -> List[Dict[str, str]]:
        """Get player's name history"""
        try:
            response = self.session.get(
                f"{self.BASE_URL}/user/profiles/{uuid}/names",
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise MojangAPIException(f"API error: {response.status_code}")
                
        except requests.RequestException as e:
            raise MojangAPIException(f"Failed to get name history: {str(e)}")
    
    def get_skin_url(self, uuid: str) -> Optional[str]:
        """Get player's skin URL"""
        try:
            profile = self.get_profile(uuid)
            if profile and 'textures' in profile:
                textures = profile['textures']
                if 'SKIN' in textures.get('textures', {}):
                    return textures['textures']['SKIN'].get('url')
            return None
        except MojangAPIException:
            return None
    
    def search_player(self, username: str) -> Dict[str, Any]:
        """Search for player and return comprehensive info"""
        result = {
            'username': username,
            'found': False,
            'uuid': None,
            'profile': None,
            'name_history': [],
            'skin_url': None
        }
        
        try:
            uuid = self.get_uuid(username)
            if uuid:
                result['found'] = True
                result['uuid'] = uuid
                result['profile'] = self.get_profile(uuid)
                result['name_history'] = self.get_name_history(uuid)
                result['skin_url'] = self.get_skin_url(uuid)
                
        except MojangAPIException as e:
            result['error'] = str(e)
        
        return result

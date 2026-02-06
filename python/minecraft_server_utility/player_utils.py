from typing import List, Dict, Any, Optional
from .mojang_api import MojangAPI

class PlayerUtils:
    """Player-related utilities"""
    
    def __init__(self):
        self.mojang_api = MojangAPI()
    
    def search_player_in_server(self, server_info: Dict[str, Any], 
                               player_name: str) -> Optional[Dict[str, Any]]:
        """Search for specific player in server player list"""
        if not server_info.get('online', False):
            return None
        
        players = server_info.get('players', {}).get('list', [])
        for player in players:
            if player.get('name', '').lower() == player_name.lower():
                return player
        
        return None
    
    def get_player_uuid(self, username: str) -> Optional[str]:
        """Get UUID for a player"""
        try:
            return self.mojang_api.get_uuid(username)
        except:
            return None
    
    def get_player_skin(self, identifier: str, is_uuid: bool = False) -> Optional[str]:
        """Get player's skin URL"""
        try:
            if is_uuid:
                uuid = identifier
            else:
                uuid = self.mojang_api.get_uuid(identifier)
            
            if uuid:
                return self.mojang_api.get_skin_url(uuid)
        except:
            pass
        return None
    
    def format_player_list(self, players: List[Dict[str, Any]]) -> str:
        """Format player list as readable string"""
        if not players:
            return "No players online"
        
        names = [player.get('name', 'Unknown') for player in players]
        return ", ".join(names)
    
    def get_player_count_by_game_mode(self, server_info: Dict[str, Any]) -> Dict[str, int]:
        """Count players by game mode (if available)"""
        # This is a placeholder - actual implementation depends on server data
        # Some servers include gamemode in player samples
        return {
            'survival': 0,
            'creative': 0,
            'adventure': 0,
            'spectator': 0
        }

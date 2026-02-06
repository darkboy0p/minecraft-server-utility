from minecraft_server_utility import ServerPinger, BedrockPinger, MojangAPI, PlayerUtils

def basic_example():
    """Basic usage examples"""
    
    # Ping Java Edition server
    print("=== Java Server Example ===")
    java_pinger = ServerPinger("mc.hypixel.net", 25565)
    java_info = java_pinger.ping()
    
    print(f"Online: {java_info['online']}")
    print(f"Version: {java_info['version']}")
    print(f"Players: {java_info['players']['online']}/{java_info['players']['max']}")
    print(f"MOTD: {java_info['motd']}")
    print(f"Latency: {java_info['latency']}ms")
    
    # Quick methods
    print(f"\nIs online: {java_pinger.is_online()}")
    print(f"Player count: {java_pinger.get_player_count()}")
    print(f"Player list: {java_pinger.get_player_list()}")
    
    # Ping Bedrock server
    print("\n=== Bedrock Server Example ===")
    bedrock_pinger = BedrockPinger("play.hyperlandsmc.net", 19132)
    try:
        bedrock_info = bedrock_pinger.ping()
        print(f"Online: {bedrock_info['online']}")
        print(f"Edition: {bedrock_info['edition']}")
        print(f"MOTD: {bedrock_info['motd']}")
    except Exception as e:
        print(f"Bedrock server error: {e}")
    
    # Mojang API examples
    print("\n=== Mojang API Example ===")
    mojang = MojangAPI()
    
    # Get UUID from username
    uuid = mojang.get_uuid("Notch")
    print(f"Notch's UUID: {uuid}")
    
    # Get player profile
    if uuid:
        profile = mojang.get_profile(uuid)
        print(f"Username: {profile.get('name')}")
        print(f"Skin URL: {mojang.get_skin_url(uuid)}")
    
    # Search player
    print("\n=== Player Search Example ===")
    player_search = mojang.search_player("Technoblade")
    if player_search['found']:
        print(f"Found: {player_search['username']}")
        print(f"UUID: {player_search['uuid']}")
        print(f"Skin URL: {player_search['skin_url']}")

if __name__ == "__main__":
    basic_example()

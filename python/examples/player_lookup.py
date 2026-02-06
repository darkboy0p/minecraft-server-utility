from minecraft_server_utility import MojangAPI, PlayerUtils

def player_lookup_demo():
    """Demonstrate player lookup capabilities"""
    mojang = MojangAPI()
    player_utils = PlayerUtils()
    
    print("=== Player Lookup System ===")
    
    while True:
        print("\nOptions:")
        print("1. Lookup player by username")
        print("2. Get player UUID")
        print("3. Get player skin")
        print("4. Get name history")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == "1":
            username = input("Enter username: ").strip()
            result = mojang.search_player(username)
            
            if result['found']:
                print(f"\n✅ Player Found!")
                print(f"Username: {result['username']}")
                print(f"UUID: {result['uuid']}")
                
                if result['skin_url']:
                    print(f"Skin URL: {result['skin_url']}")
                    print("(Open this URL in a browser to view the skin)")
                
                # Show name history
                if result['name_history']:
                    print("\nName History:")
                    for name_record in result['name_history']:
                        name = name_record.get('name', 'Unknown')
                        changed_at = name_record.get('changedToAt', 'Original')
                        if changed_at == 'Original':
                            print(f"  - {name} (Original)")
                        else:
                            from datetime import datetime
                            date = datetime.fromtimestamp(changed_at/1000).strftime('%Y-%m-%d')
                            print(f"  - {name} (Changed on: {date})")
            else:
                print(f"\n❌ Player '{username}' not found")
        
        elif choice == "2":
            username = input("Enter username: ").strip()
            uuid = mojang.get_uuid(username)
            if uuid:
                print(f"\nUUID for {username}: {uuid}")
                # Format UUID with hyphens
                formatted_uuid = f"{uuid[:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:]}"
                print(f"Formatted UUID: {formatted_uuid}")
            else:
                print(f"\nPlayer '{username}' not found")
        
        elif choice == "3":
            identifier = input("Enter username or UUID: ").strip()
            
            # Check if it's a UUID (has hyphens or is 32 chars)
            if '-' in identifier or len(identifier) == 32:
                is_uuid = True
            else:
                is_uuid = False
            
            skin_url = player_utils.get_player_skin(identifier, is_uuid)
            
            if skin_url:
                print(f"\n🎭 Skin URL: {skin_url}")
                print("Instructions:")
                print("1. Copy the URL above")
                print("2. Open it in a web browser")
                print("3. Right-click the image and 'Save as...'")
                print("4. Use it as your Minecraft skin!")
            else:
                print(f"\n❌ Could not find skin for {identifier}")
        
        elif choice == "4":
            username = input("Enter username: ").strip()
            uuid = mojang.get_uuid(username)
            
            if uuid:
                history = mojang.get_name_history(uuid)
                if history:
                    print(f"\n📜 Name history for {username}:")
                    for i, record in enumerate(history):
                        name = record.get('name', 'Unknown')
                        changed_at = record.get('changedToAt')
                        
                        if changed_at is None:
                            print(f"  {i+1}. {name} (Original name)")
                        else:
                            from datetime import datetime
                            date = datetime.fromtimestamp(changed_at/1000)
                            print(f"  {i+1}. {name} (Changed on: {date.strftime('%Y-%m-%d %H:%M:%S')})")
                else:
                    print(f"\nNo name history found for {username}")
            else:
                print(f"\nPlayer '{username}' not found")
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    player_lookup_demo()

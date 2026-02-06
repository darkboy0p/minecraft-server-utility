import time
from minecraft_server_utility import ServerPinger, PlayerUtils

class ServerMonitor:
    def __init__(self, servers):
        self.servers = servers
        self.player_utils = PlayerUtils()
    
    def monitor_all(self, interval=60):
        """Monitor multiple servers at regular intervals"""
        print(f"Monitoring {len(self.servers)} servers every {interval} seconds")
        print("-" * 50)
        
        while True:
            for server_name, server_info in self.servers.items():
                host = server_info['host']
                port = server_info.get('port', 25565)
                
                pinger = ServerPinger(host, port)
                
                try:
                    info = pinger.ping()
                    
                    print(f"\n[{time.strftime('%H:%M:%S')}] {server_name}")
                    print(f"  Status: {'ONLINE' if info['online'] else 'OFFLINE'}")
                    
                    if info['online']:
                        print(f"  Players: {info['players']['online']}/{info['players']['max']}")
                        print(f"  Version: {info['version']}")
                        print(f"  Latency: {info['latency']}ms")
                        
                        # Check for specific player
                        target_player = server_info.get('monitor_player')
                        if target_player:
                            player_data = self.player_utils.search_player_in_server(info, target_player)
                            if player_data:
                                print(f"  🔍 {target_player} is online!")
                    
                except Exception as e:
                    print(f"\n[{time.strftime('%H:%M:%S')}] {server_name}")
                    print(f"  Status: ERROR - {e}")
            
            print("\n" + "=" * 50)
            time.sleep(interval)

# Example usage
if __name__ == "__main__":
    servers_to_monitor = {
        "Hypixel": {
            "host": "mc.hypixel.net",
            "port": 25565,
            "monitor_player": "Technoblade"  # Optional: track specific player
        },
        "Mineplex": {
            "host": "us.mineplex.com",
            "port": 25565
        },
        "Local Server": {
            "host": "localhost",
            "port": 25565
        }
    }
    
    monitor = ServerMonitor(servers_to_monitor)
    # Run for 5 minutes (300 seconds) for demo
    for _ in range(5):
        monitor.monitor_all(interval=10)
        time.sleep(50)

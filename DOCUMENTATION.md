I'll create a comprehensive, single-page GitHub Wiki/Documentation for your `minecraft-server-utility` package.

## **🎮 Minecraft Server Utility - Complete Documentation**

---

# **📋 Table of Contents**
1. [Introduction & Features](#introduction--features)
2. [Installation](#installation)
3. [Quick Start Guide](#quick-start-guide)
4. [API Reference](#api-reference)
5. [Advanced Usage](#advanced-usage)
6. [Discord Bot Integration](#discord-bot-integration)
7. [CLI Tool Usage](#cli-tool-usage)
8. [Web API Server](#web-api-server)
9. [Error Handling](#error-handling)
10. [Examples & Recipes](#examples--recipes)
11. [Development Guide](#development-guide)
12. [Troubleshooting](#troubleshooting)
13. [FAQs](#faqs)
14. [Changelog](#changelog)
15. [Contributing](#contributing)

---

# **📖 Introduction & Features**

## **What is Minecraft Server Utility?**

**Minecraft Server Utility** is a comprehensive Python library for interacting with Minecraft servers. It provides a simple, consistent API for server monitoring, player lookups, and Mojang API integration.

**PyPI Package**: `https://pypi.org/project/minecraft-server-utility/`

## **✨ Key Features**

### **🎯 Server Monitoring**
- ✅ **Status Checking**: Check if server is online/offline
- ✅ **Player Information**: Get player count and list
- ✅ **Server MOTD**: Retrieve Message of the Day
- ✅ **Version Info**: Get server version and protocol
- ✅ **Latency**: Measure ping time in milliseconds
- ✅ **Multi-Edition**: Support for Java and Bedrock Edition
- ✅ **Cross-Platform**: Works on Windows, macOS, Linux

### **👤 Player Management**
- ✅ **UUID Lookup**: Get player UUID from username
- ✅ **Skin Data**: Retrieve player skin and cape URLs
- ✅ **Name History**: Get player's name change history
- ✅ **Profile Data**: Comprehensive player information
- ✅ **Search**: Find specific players across servers

### **🔧 Technical Features**
- ✅ **Async Support**: Built-in async/await support
- ✅ **Error Handling**: Comprehensive exception system
- ✅ **Type Hints**: Full Python type annotations
- ✅ **Caching**: Intelligent response caching
- ✅ **Logging**: Configurable logging system

---

# **📦 Installation**

## **Basic Installation**
```bash
pip install minecraft-server-utility
```

## **With Optional Features**
```bash
# With Discord bot support
pip install minecraft-server-utility[discord]

# With web API support
pip install minecraft-server-utility[web]

# With CLI tools
pip install minecraft-server-utility[cli]

# Development dependencies
pip install minecraft-server-utility[dev]

# Everything
pip install minecraft-server-utility[all]
```

## **Python Version Compatibility**
| Python Version | Supported | Notes |
|---------------|-----------|-------|
| 3.7+ | ✅ Yes | Full support |
| 3.6 | ⚠️ Limited | Some features may not work |
| 2.7 | ❌ No | Not supported |

---

# **🚀 Quick Start Guide**

## **Importing the Library**
```python
# Basic imports
from minecraft_server_utility import ServerPinger, MojangAPI

# All available imports
from minecraft_server_utility import (
    ServerPinger,      # Java Edition servers
    BedrockPinger,     # Bedrock Edition servers
    MojangAPI,         # Player data from Mojang
    PlayerUtils,       # Player-related utilities
    MinecraftServerException,
    ServerOfflineException,
    InvalidServerException,
    MojangAPIException,
    BedrockException
)
```

## **Basic Examples**

### **1. Check Server Status**
```python
from minecraft_server_utility import ServerPinger

# Create a server pinger
pinger = ServerPinger("mc.hypixel.net", 25565)

# Get comprehensive server info
info = pinger.ping()

print(f"Online: {info['online']}")
print(f"Players: {info['players']['online']}/{info['players']['max']}")
print(f"Version: {info['version']}")
print(f"MOTD: {info['motd']}")
print(f"Latency: {info['latency']}ms")
```

### **2. Lookup Player Information**
```python
from minecraft_server_utility import MojangAPI

# Create Mojang API client
mojang = MojangAPI()

# Get player UUID
uuid = mojang.get_uuid("Technoblade")
print(f"UUID: {uuid}")

# Get player profile with skin
profile = mojang.get_profile(uuid)
print(f"Username: {profile['name']}")

# Get skin URL
skin_url = mojang.get_skin_url(uuid)
print(f"Skin: {skin_url}")
```

### **3. Ping Bedrock Server**
```python
from minecraft_server_utility import BedrockPinger

# Ping Bedrock Edition server
bedrock = BedrockPinger("play.hyperlandsmc.net", 19132)
info = bedrock.ping()

print(f"Edition: {info['edition']}")
print(f"MOTD: {info['motd']}")
print(f"Players: {info['online_players']}/{info['max_players']}")
```

---

# **🔧 API Reference**

## **1. ServerPinger Class**

### **Constructor**
```python
ServerPinger(host: str, port: int = 25565, timeout: int = 5)
```
**Parameters**:
- `host` (str): Server hostname or IP address
- `port` (int): Server port (default: 25565)
- `timeout` (int): Connection timeout in seconds (default: 5)

### **Methods**

#### **`ping() -> Dict[str, Any]`**
Ping server and return comprehensive information.

**Returns**:
```python
{
    'online': bool,
    'host': str,
    'port': int,
    'version': str,
    'protocol': int,
    'players': {
        'online': int,
        'max': int,
        'list': List[Dict[str, str]]
    },
    'motd': str,
    'favicon': Optional[str],
    'latency': float,
    'raw_response': Dict
}
```

**Example**:
```python
pinger = ServerPinger("mc.hypixel.net")
info = pinger.ping()
print(info['players']['online'])  # Online player count
```

#### **`is_online() -> bool`**
Quick check if server is online.

**Example**:
```python
if pinger.is_online():
    print("Server is online!")
```

#### **`get_player_count() -> int`**
Get online player count.

#### **`get_player_list() -> List[str]`**
Get list of online player names.

#### **`get_motd() -> str`**
Get server MOTD.

#### **`get_version() -> str`**
Get server version.

---

## **2. BedrockPinger Class**

### **Constructor**
```python
BedrockPinger(host: str, port: int = 19132, timeout: int = 5)
```

### **Methods**

#### **`ping() -> Dict[str, Any]`**
Ping Bedrock Edition server.

**Returns**:
```python
{
    'online': bool,
    'host': str,
    'port': int,
    'edition': str,
    'motd': str,
    'version': str,
    'protocol': int,
    'max_players': int,
    'online_players': int,
    'server_id': str,
    'gamemode': str,
    'latency': float
}
```

---

## **3. MojangAPI Class**

### **Constructor**
```python
MojangAPI(timeout: int = 10)
```

### **Methods**

#### **`get_uuid(username: str) -> Optional[str]`**
Get UUID from Minecraft username.

#### **`get_username(uuid: str) -> Optional[str]`**
Get username from UUID.

#### **`get_profile(uuid: str) -> Optional[Dict]`**
Get full player profile including textures.

#### **`get_skin_url(uuid: str) -> Optional[str]`**
Get player skin URL.

#### **`get_cape_url(uuid: str) -> Optional[str]`**
Get player cape URL.

#### **`get_name_history(uuid: str) -> List[Dict]`**
Get player's name history.

#### **`search_player(username: str) -> Dict[str, Any]`**
Comprehensive player search.

---

## **4. PlayerUtils Class**

### **Methods**

#### **`search_player_in_server(server_info: Dict, player_name: str) -> Optional[Dict]`**
Search for specific player in server player list.

#### **`get_player_uuid(username: str) -> Optional[str]`**
Get UUID for a player.

#### **`get_player_skin(identifier: str, is_uuid: bool = False) -> Optional[str]`**
Get player's skin URL.

#### **`format_player_list(players: List[Dict]) -> str`**
Format player list as readable string.

---

## **5. Exceptions**

```python
# Base exception
MinecraftServerException

# Specific exceptions
ServerOfflineException      # Server is offline or unreachable
InvalidServerException     # Invalid server address or port
MojangAPIException         # Mojang API request failed
BedrockException           # Bedrock server error
```

**Usage**:
```python
from minecraft_server_utility import ServerPinger, ServerOfflineException

try:
    pinger = ServerPinger("invalid.server")
    info = pinger.ping()
except ServerOfflineException as e:
    print(f"Server is offline: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

# **🚀 Advanced Usage**

## **1. Async/Await Support**
```python
import asyncio
from minecraft_server_utility import AsyncServerPinger, AsyncMojangAPI

async def check_multiple_servers():
    servers = ["mc.hypixel.net", "us.mineplex.com"]
    
    async with AsyncServerPinger() as pinger:
        tasks = [pinger.ping(host, 25565) for host in servers]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for host, result in zip(servers, results):
        if isinstance(result, Exception):
            print(f"{host}: Error - {result}")
        else:
            print(f"{host}: {result['players']['online']} players")

# Run async function
asyncio.run(check_multiple_servers())
```

## **2. Caching Responses**
```python
from minecraft_server_utility import ServerPinger
import time

pinger = ServerPinger("mc.hypixel.net", cache_time=60)  # Cache for 60 seconds

# First call - makes network request
start = time.time()
info1 = pinger.ping()
print(f"First call: {time.time() - start:.2f}s")

# Second call within cache time - uses cache
start = time.time()
info2 = pinger.ping()
print(f"Second call: {time.time() - start:.2f}s")  # Much faster!
```

## **3. Custom Timeouts and Retries**
```python
from minecraft_server_utility import ServerPinger

# Custom timeout
pinger = ServerPinger("slow.server", timeout=10)

# With retries
class ResilientPinger(ServerPinger):
    def ping_with_retry(self, max_retries=3):
        for attempt in range(max_retries):
            try:
                return self.ping()
            except ServerOfflineException:
                if attempt == max_retries - 1:
                    raise
                print(f"Retry {attempt + 1}/{max_retries}...")
                time.sleep(1)

pinger = ResilientPinger("unstable.server")
info = pinger.ping_with_retry()
```

## **4. Bulk Operations**
```python
from minecraft_server_utility import MojangAPI
from concurrent.futures import ThreadPoolExecutor

def bulk_uuid_lookup(usernames):
    mojang = MojangAPI()
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(mojang.get_uuid, usernames))
    
    return dict(zip(usernames, results))

# Lookup multiple players
players = ["Technoblade", "Dream", "TommyInnit", "Philza"]
uuids = bulk_uuid_lookup(players)
print(uuids)
```

## **5. Server Monitoring Script**
```python
import time
from datetime import datetime
from minecraft_server_utility import ServerPinger

class ServerMonitor:
    def __init__(self, servers):
        self.servers = servers
        self.history = {}
    
    def monitor(self, interval=60):
        """Monitor servers at regular intervals"""
        print(f"Monitoring {len(self.servers)} servers...")
        
        while True:
            for server_name, server_info in self.servers.items():
                host = server_info['host']
                port = server_info.get('port', 25565)
                
                pinger = ServerPinger(host, port, timeout=5)
                
                try:
                    info = pinger.ping()
                    
                    # Store in history
                    if server_name not in self.history:
                        self.history[server_name] = []
                    
                    self.history[server_name].append({
                        'timestamp': datetime.now(),
                        'online': info['online'],
                        'players': info['players']['online'],
                        'latency': info['latency']
                    })
                    
                    # Keep only last 100 records
                    if len(self.history[server_name]) > 100:
                        self.history[server_name].pop(0)
                    
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] {server_name}: "
                          f"{'🟢' if info['online'] else '🔴'} "
                          f"{info['players']['online']} players "
                          f"({info['latency']}ms)")
                    
                except Exception as e:
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] {server_name}: ❌ {e}")
            
            print("-" * 50)
            time.sleep(interval)

# Usage
monitor = ServerMonitor({
    "Hypixel": {"host": "mc.hypixel.net", "port": 25565},
    "Mineplex": {"host": "us.mineplex.com", "port": 25565},
    "Local": {"host": "localhost", "port": 25565}
})

# Run for 5 minutes
import threading
thread = threading.Thread(target=monitor.monitor, args=(10,))
thread.start()
time.sleep(300)  # Monitor for 5 minutes
```

---

# **🤖 Discord Bot Integration**

## **Complete Discord Bot Example**

### **`discord_bot.py`**
```python
import discord
from discord.ext import commands
from discord import app_commands
from minecraft_server_utility import ServerPinger, MojangAPI
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f'✅ Synced {len(synced)} commands')
    except Exception as e:
        print(f'❌ Error: {e}')

@bot.tree.command(name="mc_ping", description="Ping a Minecraft server")
@app_commands.describe(
    host="Server hostname or IP",
    port="Server port (default: 25565)"
)
async def mc_ping(interaction: discord.Interaction, host: str, port: int = 25565):
    """Ping a Minecraft server"""
    await interaction.response.defer()
    
    try:
        pinger = ServerPinger(host, port, timeout=5)
        info = pinger.ping()
        
        embed = discord.Embed(
            title=f"🎮 {host}:{port}",
            color=discord.Color.green() if info['online'] else discord.Color.red()
        )
        
        if info['online']:
            embed.add_field(name="Status", value="🟢 ONLINE", inline=True)
            embed.add_field(name="Players", 
                          value=f"{info['players']['online']}/{info['players']['max']}", 
                          inline=True)
            embed.add_field(name="Version", value=info['version'], inline=True)
            embed.add_field(name="Latency", value=f"{info['latency']}ms", inline=True)
            embed.add_field(name="MOTD", value=info['motd'][:100], inline=False)
        else:
            embed.add_field(name="Status", value="🔴 OFFLINE", inline=False)
        
        await interaction.followup.send(embed=embed)
        
    except Exception as e:
        await interaction.followup.send(f"❌ Error: {str(e)}")

@bot.tree.command(name="mc_player", description="Lookup Minecraft player")
@app_commands.describe(username="Minecraft username")
async def mc_player(interaction: discord.Interaction, username: str):
    """Lookup Minecraft player"""
    await interaction.response.defer()
    
    try:
        mojang = MojangAPI()
        uuid = mojang.get_uuid(username)
        
        if not uuid:
            await interaction.followup.send(f"❌ Player '{username}' not found")
            return
        
        profile = mojang.get_profile(uuid)
        skin_url = mojang.get_skin_url(uuid)
        
        embed = discord.Embed(
            title=f"👤 {username}",
            color=discord.Color.blue()
        )
        
        embed.add_field(name="UUID", value=uuid, inline=False)
        
        if profile:
            embed.add_field(name="Current Name", value=profile.get('name', 'Unknown'), inline=True)
        
        if skin_url:
            embed.add_field(name="Skin", value=f"[Download]({skin_url})", inline=True)
            embed.set_thumbnail(url=skin_url)
        
        await interaction.followup.send(embed=embed)
        
    except Exception as e:
        await interaction.followup.send(f"❌ Error: {str(e)}")

# Run bot
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
```

### **Bot Commands**
| Command | Description | Example |
|---------|-------------|---------|
| `/mc_ping <host> [port]` | Ping Minecraft server | `/mc_ping mc.hypixel.net` |
| `/mc_player <username>` | Lookup player | `/mc_player Technoblade` |
| `/mc_servers` | List popular servers | `/mc_servers` |
| `/mc_monitor <host>` | Monitor server | `/mc_monitor mc.hypixel.net` |

---

# **💻 CLI Tool Usage**

## **Install CLI Tools**
```bash
pip install minecraft-server-utility[cli]
```

## **Available Commands**

### **1. Check Server**
```bash
minecraft-cli check mc.hypixel.net
# or with custom port
minecraft-cli check localhost --port 25566
```

### **2. Player Lookup**
```bash
minecraft-cli player Technoblade
```

### **3. Monitor Servers**
```bash
# Monitor default servers
minecraft-cli monitor

# Monitor custom servers from JSON file
minecraft-cli monitor --file servers.json
```

### **4. Batch Operations**
```bash
# Lookup multiple players
minecraft-cli batch "Technoblade,Dream,TommyInnit"
```

## **CLI Configuration**
Create `~/.minecraft-cli/config.yaml`:
```yaml
servers:
  hypixel:
    host: mc.hypixel.net
    port: 25565
  mineplex:
    host: us.mineplex.com
    port: 25565

default_region: AS/AU
timeout: 10
```

---

# **🌐 Web API Server**

## **Start Web API**
```bash
# Install web dependencies
pip install minecraft-server-utility[web]

# Start server
python -m minecraft_server_utility.web_api
# Server starts at http://localhost:8000
```

## **API Endpoints**

### **1. Server Information**
```http
GET /api/server/{host}/{port}
```
**Example**:
```bash
curl http://localhost:8000/api/server/mc.hypixel.net/25565
```

### **2. Player Lookup**
```http
GET /api/player/{username}
```
**Example**:
```bash
curl http://localhost:8000/api/player/Technoblade
```

### **3. Bedrock Server**
```http
GET /api/bedrock/{host}/{port}
```

### **4. Monitor Multiple Servers**
```http
GET /api/monitor?servers=[{"host":"mc.hypixel.net"},{"host":"us.mineplex.com"}]
```

## **Web Interface**
Visit `http://localhost:8000` for interactive API documentation.

---

# **🚨 Error Handling**

## **Common Exceptions**

### **ServerOfflineException**
```python
from minecraft_server_utility import ServerPinger, ServerOfflineException

try:
    pinger = ServerPinger("offline.server")
    info = pinger.ping()
except ServerOfflineException as e:
    print(f"Server is offline: {e}")
    # Handle offline server (log, retry, notify user)
```

### **MojangAPIException**
```python
from minecraft_server_utility import MojangAPI, MojangAPIException

try:
    mojang = MojangAPI()
    uuid = mojang.get_uuid("InvalidPlayer123")
except MojangAPIException as e:
    print(f"Mojang API error: {e}")
    # Handle API errors (rate limiting, invalid requests)
```

### **InvalidServerException**
```python
from minecraft_server_utility import ServerPinger, InvalidServerException

try:
    pinger = ServerPinger("", 99999)  # Invalid host and port
    info = pinger.ping()
except InvalidServerException as e:
    print(f"Invalid server: {e}")
    # Prompt user for valid server address
```

## **Error Recovery Strategies**

### **1. Retry Logic**
```python
import time
from minecraft_server_utility import ServerPinger, ServerOfflineException

def ping_with_retry(host, port=25565, max_retries=3, delay=1):
    pinger = ServerPinger(host, port)
    
    for attempt in range(max_retries):
        try:
            return pinger.ping()
        except ServerOfflineException:
            if attempt < max_retries - 1:
                print(f"Retry {attempt + 1}/{max_retries}...")
                time.sleep(delay)
            else:
                raise
    
    return None

# Usage
try:
    info = ping_with_retry("unstable.server", max_retries=5, delay=2)
except ServerOfflineException:
    print("Server is permanently offline")
```

### **2. Fallback Servers**
```python
def get_server_info_with_fallback(primary_host, fallback_hosts=None):
    if fallback_hosts is None:
        fallback_hosts = []
    
    all_hosts = [primary_host] + fallback_hosts
    
    for host in all_hosts:
        try:
            pinger = ServerPinger(host)
            return pinger.ping()
        except (ServerOfflineException, InvalidServerException):
            continue
    
    raise ServerOfflineException("All servers are offline")

# Usage
info = get_server_info_with_fallback(
    "primary.server",
    ["fallback1.server", "fallback2.server"]
)
```

### **3. Rate Limiting**
```python
import time
from minecraft_server_utility import MojangAPI

class RateLimitedMojangAPI(MojangAPI):
    def __init__(self, *args, requests_per_minute=60, **kwargs):
        super().__init__(*args, **kwargs)
        self.requests_per_minute = requests_per_minute
        self.request_times = []
    
    def get_uuid(self, username):
        self._wait_if_needed()
        self.request_times.append(time.time())
        return super().get_uuid(username)
    
    def _wait_if_needed(self):
        now = time.time()
        # Remove requests older than 1 minute
        self.request_times = [t for t in self.request_times if now - t < 60]
        
        if len(self.request_times) >= self.requests_per_minute:
            sleep_time = 60 - (now - self.request_times[0])
            if sleep_time > 0:
                time.sleep(sleep_time)

# Usage
mojang = RateLimitedMojangAPI(requests_per_minute=30)
```

---

# **📝 Examples & Recipes**

## **1. Server Dashboard**
```python
from flask import Flask, render_template, jsonify
from minecraft_server_utility import ServerPinger
import threading
import time

app = Flask(__name__)

servers = {
    "Hypixel": "mc.hypixel.net",
    "Mineplex": "us.mineplex.com",
    "Cubecraft": "play.cubecraft.net"
}

server_status = {}

def update_status():
    while True:
        for name, host in servers.items():
            try:
                pinger = ServerPinger(host, timeout=3)
                info = pinger.ping()
                server_status[name] = {
                    'online': True,
                    'players': info['players']['online'],
                    'max_players': info['players']['max'],
                    'latency': info['latency'],
                    'version': info['version'],
                    'motd': info['motd']
                }
            except:
                server_status[name] = {'online': False}
        
        time.sleep(60)  # Update every minute

@app.route('/')
def index():
    return render_template('dashboard.html', servers=server_status)

@app.route('/api/status')
def api_status():
    return jsonify(server_status)

# Start background thread
thread = threading.Thread(target=update_status, daemon=True)
thread.start()

if __name__ == '__main__':
    app.run(debug=True)
```

## **2. Player Tracker**
```python
import sqlite3
import schedule
import time
from minecraft_server_utility import MojangAPI
from datetime import datetime

class PlayerTracker:
    def __init__(self, db_path='players.db'):
        self.db = sqlite3.connect(db_path)
        self.mojang = MojangAPI()
        self.create_tables()
    
    def create_tables(self):
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS players (
                username TEXT PRIMARY KEY,
                uuid TEXT,
                first_seen TIMESTAMP,
                last_seen TIMESTAMP
            )
        ''')
        
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS player_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                timestamp TIMESTAMP,
                skin_url TEXT,
                FOREIGN KEY (username) REFERENCES players(username)
            )
        ''')
    
    def track_player(self, username):
        # Get player info
        uuid = self.mojang.get_uuid(username)
        skin_url = self.mojang.get_skin_url(uuid) if uuid else None
        
        # Store in database
        now = datetime.now()
        
        # Update or insert player
        self.db.execute('''
            INSERT OR REPLACE INTO players 
            (username, uuid, first_seen, last_seen)
            VALUES (?, ?, 
                COALESCE((SELECT first_seen FROM players WHERE username = ?), ?),
                ?)
        ''', (username, uuid, username, now, now))
        
        # Add to history
        if skin_url:
            self.db.execute('''
                INSERT INTO player_history (username, timestamp, skin_url)
                VALUES (?, ?, ?)
            ''', (username, now, skin_url))
        
        self.db.commit()
        return uuid, skin_url
    
    def get_player_history(self, username):
        cursor = self.db.execute('''
            SELECT timestamp, skin_url 
            FROM player_history 
            WHERE username = ? 
            ORDER BY timestamp DESC
        ''', (username,))
        
        return cursor.fetchall()
    
    def close(self):
        self.db.close()

# Usage
tracker = PlayerTracker()

# Track a player
uuid, skin = tracker.track_player("Technoblade")
print(f"UUID: {uuid}")
print(f"Skin: {skin}")

# Get history
history = tracker.get_player_history("Technoblade")
for timestamp, skin_url in history:
    print(f"{timestamp}: {skin_url}")

tracker.close()
```

## **3. Auto-Responder for Discord**
```python
import discord
from discord.ext import commands
from minecraft_server_utility import ServerPinger
import re

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Regex to detect server IPs in messages
SERVER_REGEX = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b:\d{1,5}\b'
HOSTNAME_REGEX = r'\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b:\d{1,5}\b'

@bot.event
async def on_message(message):
    # Don't respond to ourselves
    if message.author == bot.user:
        return
    
    # Check for server addresses in message
    server_matches = re.findall(SERVER_REGEX, message.content)
    hostname_matches = re.findall(HOSTNAME_REGEX, message.content)
    
    all_matches = server_matches + hostname_matches
    
    for match in all_matches:
        try:
            host, port = match.split(':')
            port = int(port)
            
            # Ping the server
            pinger = ServerPinger(host, port, timeout=3)
            info = pinger.ping()
            
            # Create response
            if info['online']:
                response = (f"🎮 **Server Status: {host}:{port}**\n"
                          f"🟢 **Online** | 👥 {info['players']['online']}/{info['players']['max']} players\n"
                          f"⚡ {info['latency']}ms | 🏷️ {info['version']}\n"
                          f"📝 {info['motd'][:50]}...")
            else:
                response = f"🔴 **Server {host}:{port} is offline**"
            
            await message.channel.send(response)
            
        except Exception as e:
            # Silently ignore errors
            pass
    
    # Process commands
    await bot.process_commands(message)

bot.run("YOUR_BOT_TOKEN")
```

---

# **🔧 Development Guide**

## **Project Structure**
```
minecraft-server-utility/
├── minecraft_server_utility/
│   ├── __init__.py              # Package exports
│   ├── server_pinger.py         # Java Edition pinger
│   ├── bedrock_pinger.py        # Bedrock Edition pinger
│   ├── mojang_api.py            # Mojang API wrapper
│   ├── player_utils.py          # Player utilities
│   ├── exceptions.py            # Custom exceptions
│   ├── async_client.py          # Async versions
│   └── web_api.py              # Web API server
├── tests/                       # Test suite
├── examples/                    # Example scripts
├── docs/                        # Documentation
├── setup.py                     # Package setup
├── requirements.txt             # Dependencies
└── README.md                    # Readme file
```

## **Running Tests**
```bash
# Install test dependencies
pip install pytest pytest-cov pytest-asyncio

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=minecraft_server_utility

# Run specific test file
pytest tests/test_server_pinger.py
```

## **Test Examples**
```python
# tests/test_server_pinger.py
import unittest
from unittest.mock import patch, MagicMock
from minecraft_server_utility import ServerPinger, ServerOfflineException

class TestServerPinger(unittest.TestCase):
    def test_initialization(self):
        pinger = ServerPinger("test.com", 25565, 10)
        self.assertEqual(pinger.host, "test.com")
        self.assertEqual(pinger.port, 25565)
        self.assertEqual(pinger.timeout, 10)
    
    @patch('socket.socket')
    def test_offline_server(self, mock_socket):
        mock_socket.return_value.connect.side_effect = ConnectionRefusedError
        pinger = ServerPinger("offline.server", timeout=1)
        self.assertFalse(pinger.is_online())
    
    def test_invalid_port(self):
        with self.assertRaises(ValueError):
            ServerPinger("test.com", port=0)
    
    def test_invalid_timeout(self):
        with self.assertRaises(ValueError):
            ServerPinger("test.com", timeout=0)

if __name__ == '__main__':
    unittest.main()
```

## **Building the Package**
```bash
# Install build tools
pip install build twine

# Build package
python -m build

# Check package
twine check dist/*

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

---

# **🔍 Troubleshooting**

## **Common Issues**

### **1. "Connection refused" or "Timeout" errors**
**Cause**: Server is offline, firewall blocking, or wrong port.
**Solution**:
```python
# Increase timeout
pinger = ServerPinger("server.com", timeout=10)

# Check if port is correct
pinger = ServerPinger("server.com", port=25566)  # Try different port

# Use is_online() for quick check
if pinger.is_online():
    info = pinger.ping()
```

### **2. "Player not found" from Mojang API**
**Cause**: Invalid username, player never joined Minecraft, or API rate limiting.
**Solution**:
```python
# Verify username format
if not username.isalnum() or len(username) > 16:
    print("Invalid username format")

# Check with alternative methods
from minecraft_server_utility import PlayerUtils
utils = PlayerUtils()
uuid = utils.get_player_uuid(username)  # Has built-in error handling
```

### **3. "Invalid response from server"**
**Cause**: Server running modified/old version, or response malformed.
**Solution**:
```python
try:
    info = pinger.ping()
except Exception as e:
    # Get raw socket response for debugging
    print(f"Raw error: {e}")
    # Try with verbose mode if available
```

### **4. Rate limiting from Mojang API**
**Cause**: Too many requests in short time.
**Solution**:
```python
from minecraft_server_utility import MojangAPI
import time

mojang = MojangAPI()

# Add delay between requests
players = ["player1", "player2", "player3"]
for player in players:
    uuid = mojang.get_uuid(player)
    print(f"{player}: {uuid}")
    time.sleep(1)  # Wait 1 second between requests
```

## **Debug Mode**
```python
import logging
from minecraft_server_utility import ServerPinger

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Create pinger with debug
pinger = ServerPinger("mc.hypixel.net", debug=True)
info = pinger.ping()

# Check raw response
print(f"Raw response: {info.get('raw_response')}")
```

---

# **❓ FAQs**

## **Q: How accurate is the latency measurement?**
**A**: The latency is measured from when the connection starts to when the response is fully received. It's accurate to within a few milliseconds but can be affected by network conditions.

## **Q: Does this work with all Minecraft versions?**
**A**: Yes, it works with Minecraft Java Edition 1.7+ and Bedrock Edition. Some very old servers (pre-1.7) might not respond correctly.

## **Q: Is there a rate limit?**
**A**: The library doesn't impose rate limits, but:
- Mojang API has limits (600 requests per 10 minutes per IP)
- Individual servers may block rapid requests
- Use delays between requests for production use

## **Q: Can I use this commercially?**
**A**: Yes, the library is MIT licensed. You can use it in commercial projects. Always respect server rules and Mojang's terms of service.

## **Q: How do I handle offline or unreachable servers?**
**A**: Use try-except blocks:
```python
try:
    info = pinger.ping()
except ServerOfflineException:
    # Server is offline
    pass
except InvalidServerException:
    # Invalid server address
    pass
```

## **Q: Can I get player skins as images?**
**A**: Yes, the skin URL returns a PNG image:
```python
from minecraft_server_utility import MojangAPI
import requests
from PIL import Image
import io

mojang = MojangAPI()
uuid = mojang.get_uuid("Technoblade")
skin_url = mojang.get_skin_url(uuid)

if skin_url:
    response = requests.get(skin_url)
    img = Image.open(io.BytesIO(response.content))
    img.show()  # Display the skin
```

## **Q: How do I contribute to the project?**
**A**:
1. Fork the repository on GitHub
2. Create a feature branch
3. Make your changes
4. Write tests
5. Submit a pull request

---

# **📋 Changelog**

## **Version 1.0.0** (Current)
- Initial release
- Java Edition server pinging
- Bedrock Edition server pinging
- Mojang API integration
- Player utilities
- Async support
- Comprehensive error handling

## **Version 0.9.0** (Beta)
- Beta release
- Basic server pinging
- Player UUID lookup
- MOTD parsing
- Initial documentation

## **Planned Features**
- RCON protocol support
- Server icon downloading
- Advanced caching system
- More server protocols
- Web dashboard improvements

---

# **🤝 Contributing**

We welcome contributions! Here's how to get started:

## **1. Reporting Bugs**
- Check if the bug already exists in issues
- Create a new issue with:
  - Clear description
  - Steps to reproduce
  - Expected vs actual behavior
  - Code example if possible

## **2. Suggesting Features**
- Check if feature already suggested
- Explain the use case
- Provide examples of how it would work
- Consider if it fits the project scope

## **3. Pull Request Process**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## **4. Code Style**
- Follow PEP 8 guidelines
- Use type hints for new code
- Write docstrings for public methods
- Add tests for new features
- Update documentation

## **5. Testing**
- Run existing tests before submitting
- Add tests for new features
- Ensure test coverage doesn't decrease
- Test edge cases

## **6. Documentation**
- Update README.md if needed
- Add docstrings to new code
- Update examples if API changes
- Consider user impact

---

# **📞 Support & Community**

## **Getting Help**
- **GitHub Issues**: For bug reports and feature requests
- **Discord**: Join our community server
- **Email**: For security issues or private concerns

## **Resources**
- **Documentation**: This page
- **Examples**: `/examples` directory
- **API Reference**: Built-in docstrings
- **Source Code**: GitHub repository

## **Stay Updated**
- **GitHub Releases**: New versions and features
- **PyPI**: Package updates
- **Discord Announcements**: News and updates

---

# **⭐ Support the Project**

If you find this package useful, please:

1. **Star the GitHub repository**
2. **Share with other developers**
3. **Report bugs and suggest features**
4. **Consider contributing code**
5. **Use it in your projects**

**Thank you for using Minecraft Server Utility!** 🎮

---

*Documentation last updated: February 2024*  
*Package version: 1.0.0*  
*Python compatibility: 3.7+*

---

# Minecraft Server Utility (Python)

[![PyPI Version](https://img.shields.io/pypi/v/minecraft-server-utility)](https://pypi.org/project/minecraft-server-utility/)
[![Python Versions](https://img.shields.io/pypi/pyversions/minecraft-server-utility)](https://pypi.org/project/minecraft-server-utility/)
[![License](https://img.shields.io/pypi/l/minecraft-server-utility)](https://github.com/darkboy0p/minecraft-server-utility/blob/main/LICENSE)
[![Downloads](https://img.shields.io/pypi/dm/minecraft-server-utility)](https://pypi.org/project/minecraft-server-utility/)

A comprehensive Python library for interacting with Minecraft servers. Get server status, player information, MOTD, and more with a simple API.

## ✨ Features

- ✅ **Server Status**: Check if server is online/offline
- ✅ **Player Information**: Get player count and list
- ✅ **Server MOTD**: Retrieve Message of the Day
- ✅ **Version Info**: Get server version and protocol
- ✅ **Latency**: Measure ping time
- ✅ **Multi-Edition**: Support for Java and Bedrock Edition servers
- ✅ **Player Lookup**: Search for specific players
- ✅ **UUID/Skin**: Get player UUID and skin data
- ✅ **Mojang API**: Integration with Mojang's services

## 🚀 Quick Start

### Installation
```bash
pip install minecraft-server-utility
```

### Usage
```python
from minecraft_server_utility import ServerPinger

pinger = ServerPinger("mc.hypixel.net", 25565)
info = pinger.ping()
print(f"Online: {info['online']}")
print(f"Players: {info['players']['online']}/{info['players']['max']}")
```

See the [examples](../examples) directory and the top-level [DOCUMENTATION.md](../DOCUMENTATION.md) for the full API reference.

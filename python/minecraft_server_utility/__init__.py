"""
Minecraft Server Utility - A comprehensive library for interacting with Minecraft servers

Features:
- Check server online/offline status
- Get player count and list
- Retrieve server MOTD (Message of the Day)
- Get server version and protocol
- Ping latency measurement
- Support for Java and Bedrock Edition servers
- Search specific players
- Get UUID and skin
- Send messages (via RCON)
- Check server information

Example usage:
    >>> from minecraft_server_utility import ServerPinger
    >>> pinger = ServerPinger("mc.hypixel.net", 25565)
    >>> info = pinger.ping()
    >>> print(f"Online: {info['online']}")
    >>> print(f"Players: {info['players']['online']}/{info['players']['max']}")
"""

__version__ = "1.0.0"
__author__ = "darkboy0p"
__email__ = "wardengamerofficial@gmail.com"
__license__ = "MIT"
__url__ = "https://github.com/darkboy0p/minecraft-server-utility"

from .server_pinger import ServerPinger
from .bedrock_pinger import BedrockPinger
from .player_utils import PlayerUtils
from .mojang_api import MojangAPI
from .exceptions import (
    MinecraftServerException,
    ServerOfflineException,
    InvalidServerException,
    MojangAPIException,
    BedrockException,
)

__all__ = [
    'ServerPinger',
    'BedrockPinger',
    'PlayerUtils',
    'MojangAPI',
    'MinecraftServerException',
    'ServerOfflineException',
    'InvalidServerException',
    'MojangAPIException',
    'BedrockException',
]

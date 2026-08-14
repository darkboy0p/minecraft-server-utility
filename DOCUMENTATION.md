# 🎮 Minecraft Server Utility

A Python library for interacting with Minecraft servers, including server status checking, player lookups, Mojang API utilities, and Minecraft server monitoring.

[![PyPI](https://img.shields.io/pypi/v/minecraft-server-utility.svg)](https://pypi.org/project/minecraft-server-utility/)
[![Python](https://img.shields.io/pypi/pyversions/minecraft-server-utility.svg)](https://pypi.org/project/minecraft-server-utility/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 📋 Table of Contents

1. [Introduction](#-introduction)
2. [Features](#-features)
3. [Project Structure](#-project-structure)
4. [Installation](#-installation)
5. [Quick Start](#-quick-start)
6. [Java Server Pinger](#-java-server-pinger)
7. [Bedrock Server Pinger](#-bedrock-server-pinger)
8. [Mojang API](#-mojang-api)
9. [Player Utilities](#-player-utilities)
10. [Exception Handling](#-exception-handling)
11. [Advanced Usage](#-advanced-usage)
12. [Discord Bot Integration](#-discord-bot-integration)
13. [CLI Usage](#-cli-usage)
14. [Web API](#-web-api)
15. [Examples](#-examples)
16. [Testing](#-testing)
17. [Building the Package](#-building-the-package)
18. [Troubleshooting](#-troubleshooting)
19. [FAQ](#-faq)
20. [Changelog](#-changelog)
21. [Contributing](#-contributing)
22. [License](#-license)

---

# 📖 Introduction

**Minecraft Server Utility** is a Python library designed to make it easier to work with Minecraft servers and Minecraft player information.

The project provides utilities for:

* Minecraft Java Edition server status
* Minecraft Bedrock Edition server status
* Player UUID lookups
* Minecraft profile information
* Skin and cape URLs
* Player utilities
* Server monitoring
* Exception handling
* Optional Discord, web, and CLI integrations

## 📦 Package Information

**Package name:**

```text
minecraft-server-utility
```

**GitHub:**

https://github.com/darkboy0p/minecraft-server-utility

**PyPI:**

https://pypi.org/project/minecraft-server-utility/

**License:** MIT

---

# ✨ Features

## 🎯 Server Monitoring

* ✅ Java Edition server status
* ✅ Bedrock Edition server status
* ✅ Online/offline detection
* ✅ Player count
* ✅ Server version
* ✅ Protocol information
* ✅ MOTD
* ✅ Latency measurement
* ✅ Configurable timeout
* ✅ Server information utilities

## 👤 Player Utilities

* ✅ Minecraft username → UUID lookup
* ✅ UUID → username lookup
* ✅ Minecraft profile lookup
* ✅ Skin URL retrieval
* ✅ Cape URL retrieval
* ✅ Player name history
* ✅ Player search utilities

## 🔧 Developer Features

* ✅ Python type hints
* ✅ Custom exceptions
* ✅ Configurable requests
* ✅ Optional integrations
* ✅ Test support
* ✅ Package distribution through PyPI

---

# 📁 Project Structure

The project uses the following structure:

```text
minecraft-server-utility/
│
├── README.md
├── SECURITY.md
├── LICENSE
│
├── python/
│   ├── setup.py
│   │
│   └── minecraft_server_utility/
│       ├── __init__.py
│       ├── server_pinger.py
│       ├── bedrock_pinger.py
│       ├── mojang_api.py
│       ├── player_utils.py
│       ├── exceptions.py
│       ├── async_client.py
│       └── web_api.py
│
├── tests/
│   ├── __init__.py
│   ├── test_server_pinger.py
│   ├── test_bedrock_pinger.py
│   └── test_mojang_api.py
│
├── examples/
│   ├── server_status.py
│   ├── player_lookup.py
│   └── discord_bot.py
│
└── .github/
    └── workflows/
        ├── test.yml
        ├── ci.yml
        ├── security.yml
        └── publish-pypi.yml
```

> **Important:** `setup.py` is located inside the `python/` directory. The package build and installation commands should therefore be executed from `python/`.

---

# 📦 Installation

## From PyPI

```bash
pip install minecraft-server-utility
```

## From Source

Clone the repository:

```bash
git clone https://github.com/darkboy0p/minecraft-server-utility.git
cd minecraft-server-utility
```

Install the package:

```bash
cd python
pip install .
```

For development:

```bash
pip install -e .
```

---

# 🧩 Optional Dependencies

Optional dependencies can be installed using extras when they are defined by the package.

## Development

```bash
pip install -e ".[dev]"
```

## Discord

```bash
pip install -e ".[discord]"
```

## Web

```bash
pip install -e ".[web]"
```

## CLI

```bash
pip install -e ".[cli]"
```

---

# 🐍 Python Compatibility

The package currently targets:

| Python       | Support                    |
| ------------ | -------------------------- |
| Python 3.7   | ✅                          |
| Python 3.8   | ✅                          |
| Python 3.9   | ✅                          |
| Python 3.10  | ✅                          |
| Python 3.11  | ✅                          |
| Python 3.12+ | ⚠️ Depends on dependencies |

Python 2 is not supported.

---

# 🚀 Quick Start

## Import the Library

```python
from minecraft_server_utility import ServerPinger
```

## Check a Minecraft Server

```python
from minecraft_server_utility import ServerPinger

pinger = ServerPinger("mc.hypixel.net")

info = pinger.ping()

print("Online:", info["online"])
print("Players:", info["players"]["online"])
print("Maximum:", info["players"]["max"])
print("Version:", info["version"])
print("MOTD:", info["motd"])
print("Latency:", info["latency"], "ms")
```

---

# 🎮 Java Server Pinger

## Constructor

```python
ServerPinger(
    host: str,
    port: int = 25565,
    timeout: int = 5
)
```

### Parameters

| Parameter | Type  |  Default | Description           |
| --------- | ----- | -------: | --------------------- |
| `host`    | `str` | Required | Server hostname or IP |
| `port`    | `int` |  `25565` | Server port           |
| `timeout` | `int` |      `5` | Connection timeout    |

## Ping a Server

```python
from minecraft_server_utility import ServerPinger

pinger = ServerPinger("mc.hypixel.net")

info = pinger.ping()

print(info)
```

A typical response may contain:

```python
{
    "online": True,
    "host": "mc.hypixel.net",
    "port": 25565,
    "version": "Minecraft version",
    "protocol": 47,
    "players": {
        "online": 100,
        "max": 1000,
        "list": []
    },
    "motd": "Minecraft Server",
    "favicon": None,
    "latency": 50.0
}
```

The exact fields depend on the server response and implementation.

## Check Whether a Server Is Online

```python
from minecraft_server_utility import ServerPinger

pinger = ServerPinger("mc.hypixel.net")

if pinger.is_online():
    print("Server is online!")
else:
    print("Server is offline!")
```

## Get Player Count

```python
count = pinger.get_player_count()

print("Players online:", count)
```

## Get Player List

```python
players = pinger.get_player_list()

for player in players:
    print(player)
```

## Get MOTD

```python
motd = pinger.get_motd()

print(motd)
```

## Get Version

```python
version = pinger.get_version()

print(version)
```

---

# 🪨 Bedrock Server Pinger

## Constructor

```python
BedrockPinger(
    host: str,
    port: int = 19132,
    timeout: int = 5
)
```

## Basic Example

```python
from minecraft_server_utility import BedrockPinger

pinger = BedrockPinger(
    "play.example.com",
    19132
)

info = pinger.ping()

print("Online:", info["online"])
print("Edition:", info["edition"])
print("MOTD:", info["motd"])
print("Players:", info["online_players"])
print("Maximum:", info["max_players"])
print("Version:", info["version"])
print("Latency:", info["latency"])
```

A Bedrock response may contain:

```python
{
    "online": True,
    "host": "play.example.com",
    "port": 19132,
    "edition": "MCPE",
    "motd": "Minecraft Server",
    "version": "1.x.x",
    "protocol": 123,
    "max_players": 100,
    "online_players": 10,
    "server_id": "...",
    "gamemode": "Survival",
    "latency": 50.0
}
```

---

# 👤 Mojang API

The `MojangAPI` class provides utilities for retrieving Minecraft player information.

## Create a Client

```python
from minecraft_server_utility import MojangAPI

mojang = MojangAPI()
```

## Username → UUID

```python
uuid = mojang.get_uuid("PlayerName")

print(uuid)
```

## UUID → Username

```python
username = mojang.get_username(
    "00000000-0000-0000-0000-000000000000"
)

print(username)
```

## Get Player Profile

```python
profile = mojang.get_profile(uuid)

print(profile)
```

## Get Skin URL

```python
skin_url = mojang.get_skin_url(uuid)

print(skin_url)
```

## Get Cape URL

```python
cape_url = mojang.get_cape_url(uuid)

print(cape_url)
```

## Get Name History

```python
history = mojang.get_name_history(uuid)

for entry in history:
    print(entry)
```

## Search for a Player

```python
result = mojang.search_player("PlayerName")

print(result)
```

---

# 🧰 Player Utilities

```python
from minecraft_server_utility import PlayerUtils

utils = PlayerUtils()
```

## Get Player UUID

```python
uuid = utils.get_player_uuid("PlayerName")

print(uuid)
```

## Get Player Skin

Using a username:

```python
skin = utils.get_player_skin("PlayerName")

print(skin)
```

Using a UUID:

```python
skin = utils.get_player_skin(
    "00000000-0000-0000-0000-000000000000",
    is_uuid=True
)

print(skin)
```

## Search Player in Server

```python
player = utils.search_player_in_server(
    server_info,
    "PlayerName"
)

print(player)
```

## Format Player List

```python
formatted = utils.format_player_list(players)

print(formatted)
```

---

# ⚠️ Exception Handling

The library provides custom exceptions for common errors.

```python
from minecraft_server_utility import (
    MinecraftServerException,
    ServerOfflineException,
    InvalidServerException,
    MojangAPIException,
    BedrockException,
)
```

## Server Offline

```python
from minecraft_server_utility import (
    ServerPinger,
    ServerOfflineException,
)

try:
    pinger = ServerPinger("offline.example.com")
    info = pinger.ping()

except ServerOfflineException as error:
    print("Server is offline:", error)
```

## Invalid Server

```python
from minecraft_server_utility import (
    ServerPinger,
    InvalidServerException,
)

try:
    pinger = ServerPinger(
        "",
        port=0
    )

except InvalidServerException as error:
    print("Invalid server:", error)
```

## Mojang API Error

```python
from minecraft_server_utility import (
    MojangAPI,
    MojangAPIException,
)

try:
    mojang = MojangAPI()
    uuid = mojang.get_uuid("PlayerName")

except MojangAPIException as error:
    print("Mojang API error:", error)
```

## General Exception

```python
from minecraft_server_utility import ServerPinger

try:
    pinger = ServerPinger("example.com")
    info = pinger.ping()

except Exception as error:
    print("Unexpected error:", error)
```

---

# ⚡ Advanced Usage

## Custom Timeout

```python
from minecraft_server_utility import ServerPinger

pinger = ServerPinger(
    "example.com",
    timeout=10
)

info = pinger.ping()
```

---

# 🔄 Retry Logic

You can implement retry logic around the pinger:

```python
import time

from minecraft_server_utility import (
    ServerPinger,
    ServerOfflineException,
)


def ping_with_retry(
    host,
    port=25565,
    max_retries=3,
    delay=1,
):
    pinger = ServerPinger(
        host,
        port,
        timeout=5,
    )

    for attempt in range(max_retries):
        try:
            return pinger.ping()

        except ServerOfflineException:
            if attempt == max_retries - 1:
                raise

            time.sleep(delay)

    return None


info = ping_with_retry(
    "example.com",
    max_retries=3,
)

print(info)
```

---

# 📊 Multiple Server Monitoring

```python
import time

from minecraft_server_utility import ServerPinger


servers = {
    "Server 1": {
        "host": "example1.com",
        "port": 25565,
    },
    "Server 2": {
        "host": "example2.com",
        "port": 25565,
    },
}


while True:
    for name, server in servers.items():

        try:
            pinger = ServerPinger(
                server["host"],
                server["port"],
                timeout=5,
            )

            info = pinger.ping()

            print(
                f"{name}: "
                f"{info['players']['online']} players"
            )

        except Exception as error:
            print(f"{name}: ERROR - {error}")

    time.sleep(60)
```

---

# 🤖 Discord Bot Integration

Discord integration can be implemented using `discord.py`.

Install the optional dependency:

```bash
pip install -e ".[discord]"
```

Example:

```python
import os

import discord
from discord.ext import commands

from minecraft_server_utility import ServerPinger


intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def mc_ping(ctx, host, port=25565):

    try:
        port = int(port)

        pinger = ServerPinger(
            host,
            port,
            timeout=5,
        )

        info = pinger.ping()

        if info["online"]:
            await ctx.send(
                f"🎮 **{host}:{port}**\n"
                f"🟢 Online\n"
                f"👥 Players: "
                f"{info['players']['online']}/"
                f"{info['players']['max']}\n"
                f"🏷️ Version: {info['version']}\n"
                f"⚡ Latency: {info['latency']}ms"
            )
        else:
            await ctx.send(
                f"🔴 **{host}:{port}** is offline."
            )

    except Exception as error:
        await ctx.send(
            f"❌ Error: {error}"
        )


token = os.getenv("DISCORD_BOT_TOKEN")

if not token:
    raise RuntimeError(
        "DISCORD_BOT_TOKEN environment variable is not set."
    )

bot.run(token)
```

### 🔐 Security

Never put your Discord bot token directly into source code.

Use an environment variable:

```bash
DISCORD_BOT_TOKEN=your_token_here
```

---

# 💻 CLI

If the CLI extra is implemented by the package, install it with:

```bash
pip install -e ".[cli]"
```

Example commands:

```bash
minecraft-cli check example.com
```

Custom port:

```bash
minecraft-cli check example.com --port 25565
```

Player lookup:

```bash
minecraft-cli player PlayerName
```

Monitoring:

```bash
minecraft-cli monitor
```

> CLI commands depend on the CLI implementation included in the installed package.

---

# 🌐 Web API

If the web API module is included in the package, install the web dependencies:

```bash
pip install -e ".[web]"
```

Start the API:

```bash
python -m minecraft_server_utility.web_api
```

The local API may be available at:

```text
http://localhost:8000
```

Example:

```bash
curl http://localhost:8000/api/server/example.com/25565
```

Player lookup:

```bash
curl http://localhost:8000/api/player/PlayerName
```

> Web API endpoints depend on the implementation of `web_api.py`.

---

# 🧪 Testing

The project uses `pytest`.

From the repository root:

```bash
pip install -e "./python[dev]"
```

Run all tests:

```bash
pytest tests/ -v
```

Run a specific test:

```bash
pytest tests/test_server_pinger.py -v
```

Run with coverage:

```bash
pytest tests/ \
    --cov=python/minecraft_server_utility \
    --cov-report=term-missing
```

---

# 🔧 Development Installation

Clone the repository:

```bash
git clone https://github.com/darkboy0p/minecraft-server-utility.git
```

Enter the repository:

```bash
cd minecraft-server-utility
```

Install the package in editable mode:

```bash
pip install -e "./python"
```

Install development dependencies:

```bash
pip install -e "./python[dev]"
```

Run tests:

```bash
pytest tests/ -v
```

---

# 📦 Building the Package

Because `setup.py` is located inside `python/`, build commands should run from that directory.

```bash
cd python
```

Install build tools:

```bash
python -m pip install --upgrade build twine
```

Build the package:

```bash
python -m build
```

This creates:

```text
python/
└── dist/
    ├── minecraft_server_utility-*.tar.gz
    └── minecraft_server_utility-*.whl
```

Check the generated package:

```bash
twine check dist/*
```

---

# 🧪 TestPyPI

Upload to TestPyPI:

```bash
twine upload \
    --repository testpypi \
    dist/*
```

Install from TestPyPI:

```bash
pip install \
    --index-url https://test.pypi.org/simple/ \
    minecraft-server-utility
```

---

# 🚀 PyPI

Build the package:

```bash
cd python
python -m build
```

Check it:

```bash
twine check dist/*
```

Upload:

```bash
twine upload dist/*
```

> Do not publish API keys, passwords, tokens, or other credentials in the repository.

---

# 🔐 GitHub Actions

The repository contains workflows under:

```text
.github/workflows/
```

Expected workflows include:

```text
test.yml
ci.yml
security.yml
publish-pypi.yml
```

Because the Python package is located under `python/`, package-related commands should use the `python` directory.

For example:

```yaml
- name: Install package
  working-directory: python
  run: python -m pip install .
```

For editable development installation:

```yaml
- name: Install package
  working-directory: python
  run: python -m pip install -e .
```

Tests located at the repository root can be run with:

```yaml
- name: Run tests
  run: pytest tests/ -v
```

This keeps the repository structure consistent:

```text
repository root
        │
        ├── README.md
        ├── tests/
        │
        └── python/
             ├── setup.py
             └── minecraft_server_utility/
```

---

# 🛠️ Troubleshooting

## `README.md` Not Found

If you see:

```text
FileNotFoundError: README.md
```

make sure `setup.py` uses the repository root README.

The correct path is:

```python
README_PATH = ROOT / "README.md"
```

where:

```python
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
```

---

## Package Not Found

If installation reports that no packages were found, verify:

```text
python/
├── setup.py
└── minecraft_server_utility/
    └── __init__.py
```

The `__init__.py` file is important for the package structure.

---

## `pytest` Cannot Find Tests

Tests are located at the repository root:

```text
tests/
```

Run:

```bash
pytest tests/ -v
```

not:

```bash
cd python
pytest tests/
```

unless you specify the correct path:

```bash
pytest ../tests/ -v
```

---

## Build Fails

Upgrade packaging tools:

```bash
python -m pip install --upgrade pip setuptools wheel build
```

Then:

```bash
cd python
python -m build
```

---

## Python Version Problems

Check your Python version:

```bash
python --version
```

Check pip:

```bash
python -m pip --version
```

The package targets Python 3.7 or newer.

---

# ❓ FAQ

## Does this library support Java Edition?

Yes. The project provides Java Edition server pinging through `ServerPinger`.

## Does it support Bedrock Edition?

The project includes `BedrockPinger` for Bedrock server status queries.

## Can I look up Minecraft players?

Yes. `MojangAPI` provides player-related lookup functionality.

## Can I use the library in a Discord bot?

Yes. The core library can be used from Discord bots, and an optional Discord integration can be installed when supported by the package.

## Can I use it commercially?

The project is released under the MIT License. See the `LICENSE` file for the complete terms.

## Does the library store Minecraft player data?

The library itself should only store data when your own application explicitly chooses to persist it.

## Does it require a Minecraft server?

No. The library can query remote Minecraft servers using their network address.

---

# 🔒 Security

If you discover a security vulnerability, please do not publicly post sensitive exploit details in an issue.

See:

```text
SECURITY.md
```

for the project's security reporting instructions.

---

# 📋 Changelog

## 1.0.0

Initial release containing:

* Java Edition server utilities
* Bedrock server utilities
* Mojang API utilities
* Player utilities
* Custom exceptions
* Server monitoring functionality
* Package metadata
* Documentation

## Future Development

Potential future features include:

* RCON support
* Improved caching
* More Minecraft protocol support
* Additional server information
* Better asynchronous APIs
* Expanded CLI functionality
* Additional testing
* Improved documentation

---

# 🤝 Contributing

Contributions are welcome.

## 1. Fork the Repository

Fork the GitHub repository.

## 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/minecraft-server-utility.git
cd minecraft-server-utility
```

## 3. Create a Branch

```bash
git checkout -b feature/my-feature
```

## 4. Install Development Dependencies

```bash
pip install -e "./python[dev]"
```

## 5. Make Your Changes

Implement your feature or fix.

## 6. Run Tests

```bash
pytest tests/ -v
```

## 7. Check Code Style

```bash
flake8 python/
```

## 8. Commit

```bash
git add .
git commit -m "Add my feature"
```

## 9. Push

```bash
git push origin feature/my-feature
```

## 10. Open a Pull Request

Open a pull request on GitHub and describe your changes.

---

# 📐 Code Style

Please follow:

* PEP 8
* Type hints where appropriate
* Clear function and class names
* Useful docstrings
* Tests for new functionality
* Small, focused commits

Before submitting changes:

```bash
pytest tests/ -v
```

and:

```bash
flake8 python/
```

---

# 📞 Support

For bugs and feature requests, use GitHub Issues:

https://github.com/darkboy0p/minecraft-server-utility/issues

For documentation, see this README and the project's source code.

---

# ⭐ Support the Project

If you find Minecraft Server Utility useful:

* ⭐ Star the repository
* 🐛 Report bugs
* 💡 Suggest features
* 🔧 Contribute improvements
* 📦 Use the package in your projects

---

# 📜 License

Minecraft Server Utility is released under the **MIT License**.

See:

```text
LICENSE
```

for the complete license text.

---

# 🎮 Thank You

Thank you for using **Minecraft Server Utility**!

```text
Minecraft Server Utility
A Python toolkit for Minecraft server utilities.
```

---

*Last updated: August 2026*

*Package version: 1.0.0*

*Python compatibility: 3.7+*

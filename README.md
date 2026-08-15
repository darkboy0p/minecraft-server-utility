# 🎮 Minecraft Server Utility

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)
[![Java Version](https://img.shields.io/badge/java-8+-orange.svg)](https://www.java.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

# Releases
![PyPI Version](https://img.shields.io/pypi/v/minecraft-server-utility)
![PyPI Downloads](https://img.shields.io/pypi/dm/minecraft-server-utility)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/minecraft-server-utility)

A comprehensive, cross-language library for interacting with Minecraft servers. Supports both Python and Java with a unified API.

## ✨ Features

### Server Monitoring
- ✅ **Status Check** - Check if server is online/offline
- ✅ **Player Info** - Get player count and list
- ✅ **Server MOTD** - Retrieve Message of the Day
- ✅ **Version Info** - Get server version and protocol
- ✅ **Latency** - Measure ping time
- ✅ **Multi-Edition** - Support for Java and Bedrock Edition

### Player Management
- ✅ **Player Search** - Search for specific players
- ✅ **UUID Lookup** - Get player UUID from username
- ✅ **Skin Data** - Retrieve player skin URL
- ✅ **Profile Data** - Comprehensive player information

### Cross-Language Support
- ✅ **Python Package** - Full-featured Python implementation
- ✅ **Java Library** - Native Java implementation
- ✅ **Unified API** - Consistent interface across languages

## 🚀 Quick Start

### Python Installation

```bash
pip install minecraft-server-utility
```

See [python/README.md](python/README.md) for Python usage, and [DOCUMENTATION.md](DOCUMENTATION.md) for the full API reference. Java sources live under [java/](java/) and build with Maven.

## 📁 Project Structure

```
minecraft-server-utility/
├── python/       # Python package (pip install minecraft-server-utility)
├── java/         # Java library (Maven project, com.minecraftutility)
├── tests/        # Python test suite (pytest)
├── examples/     # Example scripts
└── .github/      # CI/CD workflows
```

"""Verify the built wheel installs and imports correctly in a clean venv."""
from minecraft_server_utility import ServerPinger, MojangAPI, __version__

print(f"✅ Package imported successfully")
print(f"✅ Version: {__version__}")

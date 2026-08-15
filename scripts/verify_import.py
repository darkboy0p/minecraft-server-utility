"""Verify the package can be imported after an editable install."""
import sys

try:
    from minecraft_server_utility import __version__, ServerPinger, MojangAPI
    print(f"✅ Package imported successfully")
    print(f"✅ Version: {__version__}")
except Exception as e:
    print(f"❌ Import failed: {e}")
    sys.exit(1)

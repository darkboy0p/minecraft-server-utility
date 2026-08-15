"""Verify version.py defines a non-empty __version__ (pre-build check)."""
import os
import sys

sys.path.insert(0, os.getcwd())

try:
    from minecraft_server_utility.version import __version__
    print(f"✅ Package version: {__version__}")
    if not __version__:
        raise SystemExit("❌ Package version is empty")
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

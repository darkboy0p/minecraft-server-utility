"""Smoke-test that core classes can be constructed without a network call."""
import sys

try:
    from minecraft_server_utility import ServerPinger, MojangAPI, PlayerUtils
    print("✅ All imports successful")
    pinger = ServerPinger("localhost", 25565, timeout=1)
    print(f"✅ ServerPinger created: {pinger.host}:{pinger.port}")
    api = MojangAPI(timeout=5)
    print("✅ MojangAPI created")
    utils = PlayerUtils()
    print("✅ PlayerUtils created")
    print("\n✅ All basic tests passed!")
except Exception as e:
    print(f"❌ Test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

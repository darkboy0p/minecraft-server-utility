#!/bin/bash
set -e

# Function to check server status
check_server() {
    local host=${1:-"localhost"}
    local port=${2:-"25565"}
    
    echo "Checking Minecraft server at $host:$port..."
    
    python -c "
import sys
from minecraft_server_utility import ServerPinger

try:
    pinger = ServerPinger('$host', $port, timeout=5)
    info = pinger.ping()
    print(f'✅ Server is online!')
    print(f'   Players: {info[\"players\"][\"online\"]}/{info[\"players\"][\"max\"]}')
    print(f'   Version: {info[\"version\"]}')
    print(f'   MOTD: {info[\"motd\"][:50]}...')
except Exception as e:
    print(f'❌ Server is offline or unreachable: {e}')
    sys.exit(1)
"
}

# Main entrypoint
if [ "$1" = "check" ]; then
    shift
    check_server "$@"
elif [ "$1" = "player" ]; then
    shift
    python -c "
from minecraft_server_utility import MojangAPI
mojang = MojangAPI()
uuid = mojang.get_uuid('$1')
if uuid:
    print(f'UUID for $1: {uuid}')
else:
    print(f'Player $1 not found')
"
elif [ "$1" = "example" ]; then
    shift
    cd /app/examples
    python "$@"
else
    exec "$@"
fi

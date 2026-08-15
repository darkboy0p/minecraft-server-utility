package com.minecraftutility;

import org.junit.Test;
import static org.junit.Assert.*;

public class TestServerPinger {

    @Test
    public void testInitialization() {
        ServerPinger pinger = new ServerPinger("example.com", 25565);
        assertNotNull(pinger);
    }

    @Test
    public void testToStringContainsHostAndPort() {
        ServerPinger pinger = new ServerPinger("mc.hypixel.net", 25565);
        String repr = pinger.toString();
        assertTrue(repr.contains("mc.hypixel.net"));
        assertTrue(repr.contains("25565"));
    }

    @Test
    public void testIsOnlineReturnsFalseForInvalid() {
        ServerPinger pinger = new ServerPinger("invalid.server.that.does.not.exist", 25565, 1000);
        // This should return false, not throw - ping() catches its own IOExceptions
        boolean online = pinger.isOnline();
        assertFalse(online);
    }

    @Test
    public void testServerInfoOfflineHandlesNullJson() {
        // ServerInfo constructor must not throw when there's no JSON payload
        ServerInfo info = new ServerInfo(false, "example.com", 25565, null);
        assertFalse(info.isOnline());
        assertEquals(0, info.getOnlinePlayers());
        assertEquals("", info.getVersion());
    }

    @Test
    public void testServerInfoHandlesMalformedJsonGracefully() {
        // Previously this would throw org.json.JSONException from the constructor
        ServerInfo info = new ServerInfo(true, "example.com", 25565, "{not valid json");
        assertFalse(info.isOnline());
    }
}

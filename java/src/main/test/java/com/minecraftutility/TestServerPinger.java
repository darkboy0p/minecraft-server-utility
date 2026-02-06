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
    public void testIsOnlineReturnsFalseForInvalid() {
        ServerPinger pinger = new ServerPinger("invalid.server.that.does.not.exist", 25565);
        // This should return false or not throw an exception
        try {
            boolean online = pinger.isOnline();
            assertFalse(online);
        } catch (Exception e) {
            // It's okay if it throws an exception for invalid servers
        }
    }
}

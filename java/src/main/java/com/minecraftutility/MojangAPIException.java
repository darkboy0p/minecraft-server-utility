package com.minecraftutility;

/** Raised when a Mojang API request fails or returns malformed data. */
public class MojangAPIException extends MinecraftUtilityException {
    public MojangAPIException(String message) {
        super(message);
    }

    public MojangAPIException(String message, Throwable cause) {
        super(message, cause);
    }
}

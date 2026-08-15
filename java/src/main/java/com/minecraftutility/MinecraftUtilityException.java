package com.minecraftutility;

/**
 * Base runtime exception for Minecraft Server Utility.
 * Mirrors the Python package's exceptions module so both language
 * implementations expose a comparable error-handling surface.
 */
public class MinecraftUtilityException extends RuntimeException {
    public MinecraftUtilityException(String message) {
        super(message);
    }

    public MinecraftUtilityException(String message, Throwable cause) {
        super(message, cause);
    }
}

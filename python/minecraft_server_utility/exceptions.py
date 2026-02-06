class MinecraftServerException(Exception):
    """Base exception for Minecraft Server Utility"""
    pass

class ServerOfflineException(MinecraftServerException):
    """Raised when server is offline or unreachable"""
    pass

class InvalidServerException(MinecraftServerException):
    """Raised when server address is invalid"""
    pass

class MojangAPIException(MinecraftServerException):
    """Raised when Mojang API requests fail"""
    pass

class BedrockException(MinecraftServerException):
    """Raised for Bedrock server errors"""
    pass

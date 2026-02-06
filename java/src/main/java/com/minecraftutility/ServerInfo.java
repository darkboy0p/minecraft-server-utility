package com.minecraftutility;

import org.json.JSONObject;
import org.json.JSONArray;

public class ServerInfo {
    private boolean online;
    private String host;
    private int port;
    private JSONObject data;
    
    public ServerInfo(boolean online, String host, int port, String jsonData) {
        this.online = online;
        this.host = host;
        this.port = port;
        
        if (jsonData != null && !jsonData.isEmpty()) {
            this.data = new JSONObject(jsonData);
        } else {
            this.data = new JSONObject();
        }
    }
    
    public boolean isOnline() {
        return online;
    }
    
    public String getHost() {
        return host;
    }
    
    public int getPort() {
        return port;
    }
    
    public String getMotd() {
        if (!online) return "";
        
        try {
            Object description = data.get("description");
            if (description instanceof JSONObject) {
                return ((JSONObject) description).getString("text");
            } else if (description instanceof String) {
                return (String) description;
            }
        } catch (Exception e) {
            // Fall through
        }
        
        return "";
    }
    
    public int getOnlinePlayers() {
        if (!online) return 0;
        
        try {
            JSONObject players = data.getJSONObject("players");
            return players.getInt("online");
        } catch (Exception e) {
            return 0;
        }
    }
    
    public int getMaxPlayers() {
        if (!online) return 0;
        
        try {
            JSONObject players = data.getJSONObject("players");
            return players.getInt("max");
        } catch (Exception e) {
            return 0;
        }
    }
    
    public String getVersion() {
        if (!online) return "";
        
        try {
            JSONObject version = data.getJSONObject("version");
            return version.getString("name");
        } catch (Exception e) {
            return "";
        }
    }
    
    public int getProtocol() {
        if (!online) return -1;
        
        try {
            JSONObject version = data.getJSONObject("version");
            return version.getInt("protocol");
        } catch (Exception e) {
            return -1;
        }
    }
    
    public String[] getPlayerList() {
        if (!online) return new String[0];
        
        try {
            JSONObject players = data.getJSONObject("players");
            JSONArray sample = players.getJSONArray("sample");
            String[] playerNames = new String[sample.length()];
            
            for (int i = 0; i < sample.length(); i++) {
                JSONObject player = sample.getJSONObject(i);
                playerNames[i] = player.getString("name");
            }
            
            return playerNames;
        } catch (Exception e) {
            return new String[0];
        }
    }
    
    public String getFavicon() {
        if (!online) return "";
        
        try {
            return data.getString("favicon");
        } catch (Exception e) {
            return "";
        }
    }
    
    public String getRawJson() {
        return data.toString();
    }
    
    @Override
    public String toString() {
        if (!online) {
            return String.format("Server %s:%d is offline", host, port);
        }
        
        return String.format(
            "Server: %s:%d\n" +
            "Version: %s\n" +
            "Players: %d/%d\n" +
            "MOTD: %s",
            host, port, getVersion(), getOnlinePlayers(), getMaxPlayers(), getMotd()
        );
    }
}

package com.minecraftutility;

import java.io.*;
import java.net.*;
import org.json.JSONObject;
import org.json.JSONArray;

public class PlayerLookup {
    
    public static PlayerData getPlayerData(String username) {
        try {
            // Get UUID from username
            String uuid = getUUID(username);
            if (uuid == null) return null;
            
            // Get profile data
            return getProfile(uuid);
            
        } catch (Exception e) {
            return null;
        }
    }
    
    public static String getUUID(String username) {
        try {
            URL url = new URL("https://api.mojang.com/users/profiles/minecraft/" + username);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setConnectTimeout(5000);
            conn.setReadTimeout(5000);
            
            if (conn.getResponseCode() == 200) {
                BufferedReader reader = new BufferedReader(
                    new InputStreamReader(conn.getInputStream())
                );
                
                StringBuilder response = new StringBuilder();
                String line;
                while ((line = reader.readLine()) != null) {
                    response.append(line);
                }
                reader.close();
                
                JSONObject json = new JSONObject(response.toString());
                return json.getString("id");
            }
        } catch (Exception e) {
            // Error occurred
        }
        
        return null;
    }
    
    public static PlayerData getProfile(String uuid) {
        try {
            URL url = new URL("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setConnectTimeout(5000);
            conn.setReadTimeout(5000);
            
            if (conn.getResponseCode() == 200) {
                BufferedReader reader = new BufferedReader(
                    new InputStreamReader(conn.getInputStream())
                );
                
                StringBuilder response = new StringBuilder();
                String line;
                while ((line = reader.readLine()) != null) {
                    response.append(line);
                }
                reader.close();
                
                JSONObject json = new JSONObject(response.toString());
                return new PlayerData(json);
            }
        } catch (Exception e) {
            // Error occurred
        }
        
        return null;
    }
    
    public static String getSkinUrl(String uuid) {
        PlayerData data = getProfile(uuid);
        if (data != null) {
            return data.getSkinUrl();
        }
        return null;
    }
}

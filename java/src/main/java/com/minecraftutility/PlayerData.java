package com.minecraftutility;

import org.json.JSONObject;
import org.json.JSONArray;
import java.util.Base64;

public class PlayerData {
    private JSONObject data;
    
    public PlayerData(JSONObject data) {
        this.data = data;
    }
    
    public String getUsername() {
        try {
            return data.getString("name");
        } catch (Exception e) {
            return null;
        }
    }
    
    public String getUUID() {
        try {
            return data.getString("id");
        } catch (Exception e) {
            return null;
        }
    }
    
    public String getSkinUrl() {
        try {
            JSONArray properties = data.getJSONArray("properties");
            
            for (int i = 0; i < properties.length(); i++) {
                JSONObject prop = properties.getJSONObject(i);
                if (prop.getString("name").equals("textures")) {
                    String encoded = prop.getString("value");
                    String decoded = new String(Base64.getDecoder().decode(encoded));
                    JSONObject textures = new JSONObject(decoded);
                    
                    JSONObject texturesObj = textures.getJSONObject("textures");
                    if (texturesObj.has("SKIN")) {
                        JSONObject skin = texturesObj.getJSONObject("SKIN");
                        return skin.getString("url");
                    }
                }
            }
        } catch (Exception e) {
            // Error parsing skin data
        }
        
        return null;
    }
    
    public String getCapeUrl() {
        try {
            JSONArray properties = data.getJSONArray("properties");
            
            for (int i = 0; i < properties.length(); i++) {
                JSONObject prop = properties.getJSONObject(i);
                if (prop.getString("name").equals("textures")) {
                    String encoded = prop.getString("value");
                    String decoded = new String(Base64.getDecoder().decode(encoded));
                    JSONObject textures = new JSONObject(decoded);
                    
                    JSONObject texturesObj = textures.getJSONObject("textures");
                    if (texturesObj.has("CAPE")) {
                        JSONObject cape = texturesObj.getJSONObject("CAPE");
                        return cape.getString("url");
                    }
                }
            }
        } catch (Exception e) {
            // Error parsing cape data
        }
        
        return null;
    }
    
    public JSONObject getRawData() {
        return data;
    }
    
    @Override
    public String toString() {
        return String.format("Player: %s (UUID: %s)", getUsername(), getUUID());
    }
}

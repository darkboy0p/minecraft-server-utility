package com.minecraftutility;

import java.io.*;
import java.net.*;
import org.json.JSONObject;

public class PlayerLookup {

    public static PlayerData getPlayerData(String username) {
        String uuid = getUUID(username);
        if (uuid == null) return null;

        return getProfile(uuid);
    }

    public static String getUUID(String username) {
        HttpURLConnection conn = null;
        try {
            URL url = new URL("https://api.mojang.com/users/profiles/minecraft/" + username);
            conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setConnectTimeout(5000);
            conn.setReadTimeout(5000);

            int status = conn.getResponseCode();
            if (status == 200) {
                String response = readBody(conn);
                JSONObject json = new JSONObject(response);
                return json.getString("id");
            }
            // 204/404: username not found - not an error, just no result
        } catch (IOException e) {
            // Network/timeout error - treat as "not found" to preserve the
            // original best-effort contract of this method.
        } finally {
            if (conn != null) conn.disconnect();
        }

        return null;
    }

    public static PlayerData getProfile(String uuid) {
        HttpURLConnection conn = null;
        try {
            URL url = new URL("https://sessionserver.mojang.com/session/minecraft/profile/" + uuid);
            conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setConnectTimeout(5000);
            conn.setReadTimeout(5000);

            int status = conn.getResponseCode();
            if (status == 200) {
                String response = readBody(conn);
                JSONObject json = new JSONObject(response);
                return new PlayerData(json);
            }
        } catch (IOException e) {
            // Network/timeout error - treat as "not found"
        } finally {
            if (conn != null) conn.disconnect();
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

    private static String readBody(HttpURLConnection conn) throws IOException {
        StringBuilder response = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(conn.getInputStream()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
        }
        return response.toString();
    }
}

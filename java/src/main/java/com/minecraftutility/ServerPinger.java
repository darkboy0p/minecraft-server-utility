package com.minecraftutility;

import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class ServerPinger {
    private String host;
    private int port;
    private int timeout;
    
    public ServerPinger(String host, int port) {
        this.host = host;
        this.port = port;
        this.timeout = 5000;
    }
    
    public ServerPinger(String host, int port, int timeout) {
        this.host = host;
        this.port = port;
        this.timeout = timeout;
    }
    
    public ServerInfo ping() {
        try (Socket socket = new Socket()) {
            socket.connect(new InetSocketAddress(host, port), timeout);
            DataInputStream in = new DataInputStream(socket.getInputStream());
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            
            // Send handshake
            ByteArrayOutputStream handshake = new ByteArrayOutputStream();
            DataOutputStream handshakeOut = new DataOutputStream(handshake);
            
            writeVarInt(handshakeOut, 0); // Packet ID
            writeVarInt(handshakeOut, 762); // Protocol version
            writeString(handshakeOut, host);
            handshakeOut.writeShort(port);
            writeVarInt(handshakeOut, 1); // Next state
            
            writeVarInt(out, handshake.size());
            out.write(handshake.toByteArray());
            
            // Send status request
            writeVarInt(out, 1);
            out.writeByte(0);
            
            // Read response
            readVarInt(in); // Packet length
            int packetId = readVarInt(in);
            
            if (packetId == 0) {
                int jsonLength = readVarInt(in);
                byte[] jsonBytes = new byte[jsonLength];
                in.readFully(jsonBytes);
                
                String jsonString = new String(jsonBytes, StandardCharsets.UTF_8);
                return new ServerInfo(true, host, port, jsonString);
            }
            
        } catch (Exception e) {
            // Server is offline or error occurred
        }
        
        return new ServerInfo(false, host, port, null);
    }
    
    private void writeVarInt(DataOutputStream out, int value) throws IOException {
        while (true) {
            if ((value & ~0x7F) == 0) {
                out.writeByte(value);
                return;
            }
            out.writeByte((value & 0x7F) | 0x80);
            value >>>= 7;
        }
    }
    
    private int readVarInt(DataInputStream in) throws IOException {
        int value = 0;
        int position = 0;
        byte currentByte;
        
        while (true) {
            currentByte = in.readByte();
            value |= (currentByte & 0x7F) << position;
            
            if ((currentByte & 0x80) == 0) break;
            
            position += 7;
            if (position >= 32) throw new IOException("VarInt too big");
        }
        
        return value;
    }
    
    private void writeString(DataOutputStream out, String string) throws IOException {
        byte[] bytes = string.getBytes(StandardCharsets.UTF_8);
        writeVarInt(out, bytes.length);
        out.write(bytes);
    }
    
    public boolean isOnline() {
        return ping().isOnline();
    }
    
    public int getPlayerCount() {
        return ping().getOnlinePlayers();
    }
    
    public String getMotd() {
        return ping().getMotd();
    }
    
    public String getVersion() {
        return ping().getVersion();
    }
}

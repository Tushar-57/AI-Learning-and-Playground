package com.example.demo.dto;

import dev.langchain4j.data.message.ChatMessage;
import dev.langchain4j.data.message.SystemMessage;
import dev.langchain4j.data.message.UserMessage;
import dev.langchain4j.data.message.AiMessage;

public class MessageDto {
    private String role;
    private String content;

    public MessageDto() {
    }

    public MessageDto(String role, String content) {
        this.role = role;
        this.content = content;
    }

    // Don't mind if you don't see Lombok.
    // Getters and setters 
    public String getRole() { return role; }
    public void setRole(String role) { this.role = role; }
    public String getContent() { return content; }
    public void setContent(String content) { this.content = content; }

    public ChatMessage toLangChainMessage() {
        if (role.equalsIgnoreCase("SYSTEM")) {
            return SystemMessage.from(content);
        } else if (role.equalsIgnoreCase("USER")) {
            return UserMessage.from(content);
        } else if (role.equalsIgnoreCase("ASSISTANT")) {
            return AiMessage.from(content);
        }
        throw new IllegalArgumentException("Invalid role: " + role);
    }
}
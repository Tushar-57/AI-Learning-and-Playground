package com.example.demo.service;

import java.util.List;

import dev.langchain4j.data.message.ChatMessage;
import dev.langchain4j.service.SystemMessage;
import dev.langchain4j.service.UserMessage;
import dev.langchain4j.service.spring.AiService;

@AiService
public interface Assistant {
    @SystemMessage("You are a polite assistant")
    String chat(String message);  // Existing method
    
//    / Proper chat with history implementation
//    @SystemMessage("You are a helpful assistant")
//    @UserMessage("""
//        Answer the question based on the conversation history:
//        {{messages}}
//        """)
    String chatWithHistory(List<ChatMessage> messages);
}

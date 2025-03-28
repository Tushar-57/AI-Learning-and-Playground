package com.example.demo.controller;

import dev.langchain4j.model.chat.ChatLanguageModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DemoController {

	private final ChatLanguageModel chatLanguageModel;
    
    @Autowired
    public DemoController(ChatLanguageModel chatLanguageModel) {
        this.chatLanguageModel = chatLanguageModel;
    }
    
    /*Example GET calls
     * 
     *(1) curl --location 'http://localhost:8080/chat2'
     *(2) http://localhost:8080/chat2?message="What is java"
     * */
//   Response1: I am an AI language model developed by OpenAI called GPT-3. I don't have a personal name as I am an artificial intelligence.
//   Response2: Java is a widely popular programming language that was created by Sun Microsystems (now owned by Oracle) and released in 1995. ....... It also has a vast library of pre-built classes and methods that developers can use to simplify their programming tasks.
    @GetMapping("/chat2")
    public String model(@RequestParam(value = "message", defaultValue = "What Is your name") String message) {
        return chatLanguageModel.chat(message);
    }
    /*Example GET calls
     * 
     *(1) curl --location 'http://localhost:8080/chat3'
     * */
//   Response: Hello! How can I assist you today?
    @GetMapping("/chat3")
    public ResponseEntity<String> model() {
        return ResponseEntity.ok(chatLanguageModel.chat("Hello"));
    }
}
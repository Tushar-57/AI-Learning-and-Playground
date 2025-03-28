package com.example.demo.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.dto.MessageDto;
import com.example.demo.service.Assistant;
import dev.langchain4j.data.message.ChatMessage;

@RestController
public class AssistantController {

	private final Assistant assistant;

	@Autowired
	public AssistantController(Assistant assistant) {
		this.assistant = assistant;
	}

	@GetMapping("/chat")
	public String chat(@RequestParam(value = "message", defaultValue = "Hello") String message) {
		return assistant.chat(message);
	}

/* ----------------------------------
 * Example Post Request for Reference
 * ----------------------------------	
 *  curl --location 'http://localhost:8080/postchat' \
	--header 'Content-Type: application/json' \
	--data '[{"role": "user", "content": "What is Capital of Canada ?"}]'
*/
	@PostMapping("/postchat")
	public ResponseEntity<List<MessageDto>> chat(@RequestBody List<MessageDto> messageDtos) {
		// Convert DTOs to LangChain messages
		List<ChatMessage> messages = new ArrayList<>();
		for (MessageDto dto : messageDtos) {
			messages.add(dto.toLangChainMessage());
		}

		// Get single response
		String responseContent = assistant.chatWithHistory(messages);

		// Convert response to DTO for User and Dev Friendly.
		MessageDto responseDto = new MessageDto("ASSISTANT", responseContent);

		// Return combined history + new response
		List<MessageDto> allMessages = new ArrayList<>(messageDtos);
		allMessages.add(responseDto);

		return ResponseEntity.ok(allMessages);
	}
}
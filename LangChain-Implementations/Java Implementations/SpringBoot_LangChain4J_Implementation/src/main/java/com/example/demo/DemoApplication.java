package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		System.out.println("APP_STARTED @ Tushar - No Environment Setup Found !\n");
		SpringApplication.run(DemoApplication.class, args);
		
	}

}

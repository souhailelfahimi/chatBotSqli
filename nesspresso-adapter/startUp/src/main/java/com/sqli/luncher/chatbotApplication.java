package com.sqli.luncher;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan(basePackages = {"com.sqli.*"})
@EntityScan(basePackages = {"com.sqli.*"})
public class chatbotApplication {
    public static void main(String[] args) {
        SpringApplication.run(chatbotApplication.class,args);
    }
}


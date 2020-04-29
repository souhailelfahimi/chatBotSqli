package com.example.controllers;

import com.example.Entities.Domain;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.http.HttpEntity;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

@RestController
@CrossOrigin
@RequestMapping("")
public class DomaineController {
    @PostMapping("/domains")
    private Object addNewDomain(@RequestBody Domain domain) throws IOException, InterruptedException {

        System.out.println(domain.getName() + "  " + domain.getPredefinedEntities().get(0).getName() + " " + domain.getPredefinedEntities().get(1).getName());
        if (domain.getName().equals("getCard")) {
            HttpClient client = HttpClient.newHttpClient();
            String loc = domain.getPredefinedEntities().get(0).getName();
            String type = domain.getPredefinedEntities().get(1).getName();
            String URL = "http://localhost:8081/country/" + loc + "/type/" + type;
            HttpRequest request = HttpRequest.newBuilder()
                    .GET()
                    .header("accept", "application/json")
                    .uri(URI.create(URL))
                    .build();
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            System.out.println(response.body());
            return response.body();
        }

        return ResponseEntity.ok("You have added successfully new domains");
    }
}

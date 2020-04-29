package com.example.Entities;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedList;
import java.util.List;

@Document
@Data @NoArgsConstructor @AllArgsConstructor
public class Domain  {
    @Id
    private String id;
    private String name;
    @DBRef
    private List<Entitie> predefinedEntities=new LinkedList<>();


}

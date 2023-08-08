package com.in28minutes.learnspringboot.controller;


import com.in28minutes.learnspringboot.courses.bean.Course;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;

@RestController
public class CourseController {

    // http://localhost:8080/courses
    @GetMapping("/courses")
    public List<Course> getAllCourses() {
        return Arrays.asList(new Course(1, "Learn Microservices", "in28minutes"),
        		new Course(2, "Learn Full Stack with Angular and React", "in28minutes"));
    }
    
    // http://localhost:8080/courses/1
    @GetMapping("/courses/1")
    public Course getCourseDetails() {
        return new Course(1, "Learn Microservices", "in28minutes");
    }
}

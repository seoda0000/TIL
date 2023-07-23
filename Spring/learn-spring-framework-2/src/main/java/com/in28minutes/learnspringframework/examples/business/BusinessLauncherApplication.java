package com.in28minutes.learnspringframework.examples.business;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan
public class BusinessLauncherApplication {

	public static void main(String[] args) {
		
		try(var context = new AnnotationConfigApplicationContext(BusinessLauncherApplication.class) ){
			
			System.out.println(context.getBean(BusinessCalculationService.class).findMax());
		}

	}

}

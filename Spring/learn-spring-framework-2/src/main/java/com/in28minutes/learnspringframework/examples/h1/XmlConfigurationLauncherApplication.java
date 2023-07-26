package com.in28minutes.learnspringframework.examples.h1;

import java.util.Arrays;

import org.springframework.context.support.ClassPathXmlApplicationContext;


public class XmlConfigurationLauncherApplication {
	
	public static void main(String[] args) {
		
		try (var context = new ClassPathXmlApplicationContext("contextConfiguration.xml")) {
			
			Arrays.stream(context.getBeanDefinitionNames()).forEach(System.out::println);
			System.out.println(context.getBean("name"));
			
//			context.getBean(GameRunner.class).run();

			

			
		}

	}

}

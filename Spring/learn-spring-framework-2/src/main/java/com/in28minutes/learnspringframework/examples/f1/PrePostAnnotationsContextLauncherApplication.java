package com.in28minutes.learnspringframework.examples.f1;

import java.util.Arrays;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.stereotype.Component;

import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;

@Component
class SomeClass {
	private SomeDependency someDependency;
	
	public SomeClass(SomeDependency someDependency) {
		super();
		this.someDependency = someDependency;
		System.out.println("All dependencies are ready!");
	}
	
	@PostConstruct // 의존성 주입이 완료되어 초기화가 수행된 후 실행되어야 하는 메서드에서 사용
	public void initialize() {
		someDependency.getReady();
	}
	
	@PreDestroy // 인스턴스가 컨테이너에 의해 제거되고 있다는 신호에 대한 콜백 알림으로서 메소드에서 쓰임. 일반적으로 보유하고 있던 리소스를 해제할 때 사용.
	public void cleanup() {
		System.out.println("Clean up");
	}
	
}

@Component
class SomeDependency {

	public void getReady() {
		System.out.println("Some logic using SomeDependency");
		
	}
	
}

@Configuration
@ComponentScan
public class PrePostAnnotationsContextLauncherApplication {
	
	public static void main(String[] args) {
		
		try (var context = new AnnotationConfigApplicationContext(PrePostAnnotationsContextLauncherApplication.class)) {
			
			Arrays.stream(context.getBeanDefinitionNames()).forEach(System.out::println);
			

			
		}

	}

}

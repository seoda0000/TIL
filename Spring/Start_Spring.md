https://start.spring.io/

# 스프링 컨테이너

스프링 빈 및 그의 수명주기를 관리하는 컨테이너
Spring Container, IOC Container

- Bean Factory
  - 기본 스프링 컨테이너
- Application Context
  - 특정 기능(웹 등)을 위해 고도화된 스프링 컨테이너

# POJO와 자바 빈, 스프링 빈

### POJO : Plain Old Java Object

```java
class Pojo {

    private String text;

    private int number;

    public String toString() {
        return text + ":" + number;
    }
}
```

### Java bean

```java

class JavaBean() implements Serializable {

    // 1. public no-arg constructor
    public JavaBean() {
    }

    private String text;

    private int number;

    // 2. getter and setter

    public String getText() {
        return text
    }

    public String setText(String text) {
        this.text = text
    }

    public String getNumber() {
        return number
    }

    public String setNumber(int number) {
        return this.number = number
    }






}
```

### 스프링 빈

```java
record Person(String name, int age, Address address) {
};

record Address(String firstLine, String city) {
};

@Configuration
public class HelloWorldConfiguration {

	@Bean
	public String name() {
		return "Ranga";
	}

	@Bean
	public int age() {
		return 15;
	}

	@Bean
	public Person person() {
		return new Person("Ravi", 20, new Address("Main Street", "Utrecht"));
	}

	@Bean
	public Person person2MethodCall() {
		return new Person(name(), age(), address());
	}

	@Bean
	public Person person3Parameters(String name, int age, Address address3) {
		return new Person(name, age, address3);
	}


	@Bean(name="address2")
	public Address address() {
		return new Address("Baker Street", "London");
	}


	@Bean(name="address3")
	public Address address3() {
		return new Address("Centraltown Street", "Suwon");
	}



}

```

- @Component 이용 : 자동 와이어링

```java
@Configuration
@ComponentScan("com.in28minutes.learnspringframework.game")
public class GamingAppLauncherApplication {

	public static void main(String[] args) {

		try (var context = new AnnotationConfigApplicationContext(GamingAppLauncherApplication.class)) {

			context.getBean(GamingConsole.class).up();

			context.getBean(GameRunner.class).run();

		}
	}
}

```

```java
@Component
public class PacmanGame implements GamingConsole {

	@Override
	public void up() {
		System.out.println("Eat Up");
	}

	@Override
	public void down() {
		System.out.println("Eat Down");
	}
}
```

- @Primary: 가장 먼저 참조
- @Qualifier: 이름을 붙여 참조

```java
@Component
public class GameRunner {
	private GamingConsole game;

	public GameRunner(@Qualifier("SuperContraGameQualifier")GamingConsole game) {
		this.game = game;
	}

	public void run() {

		System.out.println("Running game: " + game);
		game.up();
		game.down();
		game.left();
		game.right();

	}

}
```

```java
@Component
@Qualifier("SuperContraGameQualifier")
public class SuperContraGame implements GamingConsole {

	@Override
	public void up() {
		System.out.println("up");
	}

	@Override
	public void down() {
		System.out.println("Sit down");
	}
}
```

- @Autowired: 알아서 찾기. 클래스 정의에 Qualifier로 명시하지 않아도 됨

```java
@Component
class Algorithm
	@Autowired @Qualifier("radixSortQualifier")
	private TheAlgorithm wowwow;
```

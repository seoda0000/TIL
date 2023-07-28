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

스프링 프레임워크가 관리하는 모든 객체

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

---

- Dependency : 클래스를 구동하는데 필요한 다른 클래스
- @Component : 클래스에 @Component를 추가하면 클래스와 인스턴스는 스프링 프레임워크가 관리하게 된다.
- @ComponentScan : 특정 클래스에서 Component를 검색하여 스프링 빈 생성
- Dependency Injection : 빈과 의존성을 확인하고 이를 Wiring 한다
- IoC : 제어 반전
- IoC Container : 빈과 의존성의 생명 주기를 관리하는 스프링 프레임워크 컴포넌트
- Autowiring : 스프링 빈에 대한 의존성을 와이어링하는 과정 전체

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

## @Component vs @Bean

|                       | @Component                                    | @Bean                                                        |
| --------------------- | --------------------------------------------- | ------------------------------------------------------------ |
| 어디서                | 모든 Java Class                               | Spring Configuration Classes                                 |
| 사용하기 편한 정도    | 매우 쉬움. annotation 추가.                   | 모든 코드 작성 필요                                          |
| Autowiring            | Field, Setter, Constructor Injection에서 가능 | method call이나 method parameters에서 가능                   |
| beans를 누가 만드는지 | Spring Framework                              | 개발자                                                       |
| 추천 용도             | 어플리케이션 코드를 인스턴스화할 때           | 커스텀 비즈니스 로직 / 서드파티 라이브러리를 위한 인스턴스화 |

---

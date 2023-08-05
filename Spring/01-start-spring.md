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

# Spring Core

### Dependency

클래스를 구동하는데 필요한 다른 클래스

### Dependency Injection

빈과 의존성을 확인하고 이를 Wiring 하는 전반적인 과정. IoC라고도 한다.

### IoC

제어 반전

- 생성자 주입

생성자를 호출해서 의존성 주입

- 수정자 주입

수정자를 호출해서 의존성 주입

- 필드 주입

생성자와 수정자가 없는 경우 reflection을 사용해서 의존성을 주입한다.

### IoC Container

빈과 의존성의 생명 주기를 관리하는 스프링 프레임워크 컴포넌트

- Bean Factory : 기본 Spring IoC Container
- Application Context : 기업에 특화된 기능을 갖춘 고급 스프링 IoC 컨테이너

### Autowiring

스프링 빈에 대한 의존성을 와이어링하는 과정 전체

### @Component

- CDI : @Named

클래스에 @Component를 추가하면 클래스와 인스턴스는 스프링 프레임워크가 관리하게 된다.

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

### @ComponentScan

특정 클래스에서 Component를 검색하여 스프링 빈 생성

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

### @Primary: 가장 먼저 참조

### @Qualifier: 이름을 붙여 참조

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

### @Autowired

- CDI : @Inject

알아서 찾기. 클래스 정의에 Qualifier로 명시하지 않아도 됨

```java
@Component
class Algorithm
	@Autowired @Qualifier("radixSortQualifier")
	private TheAlgorithm wowwow;
```

---

## @Component vs @Bean

|                       | @Component                                    | @Bean                                                        |
| --------------------- | --------------------------------------------- | ------------------------------------------------------------ |
| 어디서                | 모든 Java Class                               | Spring Configuration Classes                                 |
| 사용하기 편한 정도    | 매우 쉬움. annotation 추가.                   | 모든 코드 작성 필요                                          |
| Autowiring            | Field, Setter, Constructor Injection에서 가능 | method call이나 method parameters에서 가능                   |
| beans를 누가 만드는지 | Spring Framework                              | 개발자                                                       |
| 추천 용도             | 어플리케이션 코드를 인스턴스화할 때           | 커스텀 비즈니스 로직 / 서드파티 라이브러리를 위한 인스턴스화 |

---

## 싱글톤 vs 프로토타입

```java
@Component

class NormalClass {
}

@Scope(value=ConfigurableBeanFactory.SCOPE_PROTOTYPE)
@Component
class PrototypeClass {

}
```

### 싱글톤(기본)

- 매번 특정 빈의 동일한 인스턴스 출력
- 무상태유지, 애플리케이션 전체

### 프로토타입

- 매번 특정 빈의 새로운 인스턴스 출력
- 상태유지가 되고 사용자 정보를 갖고 있는 빈을 생성하려는 경우

### 자바 싱글톤 vs 스프링 싱글톤

- 자바 싱글톤 : 설계 패턴 관점. 자바 가상머신당 1개의 객체 인스턴스
- 스프링 싱글톤 : 스프링 IoC 컨테이너당 1개의 객체 인스턴스가 주어지는 것
- 자바가 여러개의 IoC 컨테이너를 구동한다면 둘은 다른 개념이다. 보통 하나만 구동하긴 함.

## PostConstruct 및 PreDestroy

```java
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
```

### @PostConstruct

- 의존성 주입이 완료되어 초기화가 수행된 후 실행되어야 하는 메서드에서 사용

### @PreDestroy

- 인스턴스가 컨테이너에 의해 제거되고 있다는 신호에 대한 콜백 알림으로서 메소드에서 쓰임
- 일반적으로 보유하고 있던 리소스를 해제할 때 사용

---

## 스프링 annotation 정리

### @Component

모든 클래스에 추가 가능

제너릭 어노테이션

- @Service : 비즈니스 로직을 가진 클래스를 나타냄
- @Controller : 웹 애플리케이션 등 컨트롤러를 나타냄
- @Repository : DB에 데이터 저장, 조작, 검색 등을 요청하는 경우

### 가장 정확한 annotation을 사용하자.

- 의도에 대해 더 많은 정보를 줄 수 있다.
- 관점 지향 프로그래밍을 사용하여 어노테이션을 감지하고 추가 행동을 추가할 수 있다.

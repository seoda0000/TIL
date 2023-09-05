# 영속성 관리

### 🎯 목표

컨테이너 환경에서 웹 애플리케이션을 개발할 때 발생하는 다양한 문제점과 해결 방안 알아보기

# 트랜잭션 범위의 영속성 컨테스트

## 스프링 컨테이너의 기본 전략

스프링 : **트랜잭션 범위의 영속성 컨텍스트 전략**을 기본으로 사용.

<aside>
📌 **트랜잭션 범위의 영속성 컨텍스트 전략**

트랜잭션이 시작할 때 영속성 컨텍스트를 생성하고 트랜잭션이 끝날 때 영속성 컨텍스트를 종료한다. 같은 트랜잭션 안에서는 항상 **같은 영속성 컨텍스트**에 접근한다. 이때 트랜잭션의 범위에는 Service와 Repository가 포함된다.

</aside>

<aside>
📌 **@Transactional**

호출한 메서드가 실행하기 직전에 스프링의 **트랜잭션 AOP**가 먼저 동작하게 하는 어노테이션

</aside>

<aside>
📌 **AOP (Aspect Oriented Programming)**

관점 지향 프로그래밍. 여기서 관점이란 **흩어진 관심사들을 하나로 모듈화**한 것.

Spring AOP는 기본적으로 프록시 방식으로 동작한다.

</aside>

<aside>
📌 **프록시 패턴**

어떤 객체를 사용하고자 할 때, **객체를 직접적으로 참조하지 않고 해당 객체를 대행(proxy)하는 객체를 통해 대상 객체에 접근하는 방식**.

- **Spring AOP의 프록시**
  Target 클래스 혹은 그의 상위 인터페이스를 상속하는 프록시 클래스를 생성하고, 프록시 클래스에서 부가 기능에 관련된 처리를 한다.
  이를 통해 유지보수성을 높이고 Target에서는 순수한 비즈니스 로직에 집중할 수 있다. 만약 프록시를 이용하지 않는다면 여러 곳에서 부가기능을 반복적으로 호출해야 한다.

```java
// Target 클래스와 구현체
public interface TargetService{
    void logic();
}

@Service
public class TargetServiceImpl implements TargetService{
    @Override
		public void logic() {
        ...
}}
```

```java
// Target 클래스의 프록시
@Service
public class TargetServiceProxy implements TargetService{
		TargetService targetService = new TargetServiceImpl();

		@Override
		public void logic() {
        // Target 호출 이전에 처리해야하는 부가 기능

        // Target 호출
				targetService.logic();

        // Target 호출 이후에 처리해야하는 부가 기능
    }
}
```

```java
@Service
public class UseService{
		TargetService targetService = new TargetServiceProxy();

		public void useLogic() {
        // Target 호출하는 것처럼 부가 기능이 추가된 Proxy를 호출
				targetService.logic();
    }
}
```

</aside>

### 📜 AOP 동작 과정

1. 트랜잭션 시작
2. 해당 메서드 호출
   - 메서드 정상 종료
     1. JPA는 영속성 컨텍스트를 **플러시**해서 **변경 내용을 데이터베이스에 반영**
     2. 데이터베이스 **트랜잭션을 커밋** + 영속성 컨텍스트 종료
     3. 이후 조회한 엔티티는 준영속 상태가 된다
   - 예외 발생
     1. **트랜잭션을 롤백** (플러시 호출x)
     2. 영속성 컨텍스트 종료

### 🌟 트랜잭션이 같으면 같은 영속성 컨텍스트를 사용한다

다양한 위치에서 서로 다른 엔티티 매니저를 주입받아 사용해도 트랜잭션이 같으면 항상 같은 영속성 컨텍스트를 사용한다.

```java
// repository1과 repository2는 각각의 em이 있지만, 모두 한 트랜잭션 내에서 동작한다.
@Transactional
public void logic() {
	repository1.hello();
	Member member = repository2.findMember();
	return member;
}
```

### 🌟 트랜잭션이 다르면 다른 영속성 컨텍스트를 사용한다.

스프링 컨테이너는 스레드마다 각각 다른 트랜잭션을 할당한다.

같은 엔티티 매니저를 호출해도 접근하는 영속성 컨텍스트가 다르므로 멀티스레드 상황에서 안전하다. 즉 싱글 스레드 애플리케이션처럼 비즈니스 로직에 집중하여 단순하게 개발할 수 있다.

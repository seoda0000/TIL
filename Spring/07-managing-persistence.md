# 영속성 관리

### 🎯 목표

컨테이너 환경에서 웹 애플리케이션을 개발할 때 발생하는 다양한 문제점과 해결 방안 알아보기

# 트랜잭션 범위의 영속성 컨테스트

## 스프링 컨테이너의 기본 전략

스프링 : **트랜잭션 범위의 영속성 컨텍스트 전략**을 기본으로 사용.

<aside>
📌 트랜잭션 범위의 영속성 컨텍스트 전략

트랜잭션이 시작할 때 영속성 컨텍스트를 생성하고 트랜잭션이 끝날 때 영속성 컨텍스트를 종료한다. 같은 트랜잭션 안에서는 항상 **같은 영속성 컨텍스트**에 접근한다. 이때 트랜잭션의 범위에는 Service와 Repository가 포함된다.

</aside>

<aside>
📌 @Transactional

호출한 메서드가 실행하기 직전에 스프링의 **트랜잭션 AOP**가 먼저 동작하게 하는 어노테이션

</aside>

<aside>
📌 AOP (Aspect Oriented Programming)

관점 지향 프로그래밍. 여기서 관점이란 **흩어진 관심사들을 하나로 모듈화**한 것.

Spring AOP는 기본적으로 프록시 방식으로 동작한다.

</aside>

<aside>
📌 프록시 패턴

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

# 준영속 상태와 지연 로딩

트랜잭션 범위의 영속성 컨텍스트 전략을 사용하면 트랜잭션이 없는 프리젠테이션 계층(컨트롤러, 뷰)에서 엔티티는 준영속 상태다.

→ **변경 감지와 지연 로딩이 동작하지 않는다.**

<aside>
📌 준영속 상태

객체 지향 프로그래밍에서 영속성 상태 중 하나로, 객체의 상태를 데이터베이스에 저장하지 않으면서도 **일시적으로 변경된 상태를 유지**하는 것

</aside>

### 🌟 준영속 상태와 변경 감지

변경 감지 기능은 트랜잭션 범위인 서비스 계층까지만 동작한다.

프리젠테이션 계층에서는 단순히 데이터를 보여주기만 하기에 데이터를 수정할 일은 거의 없다.

### 🌟 준영속 상태와 지연 로딩

```java
@Entity
public class Order {
	@ID @GeneratedValue
	private Long id;

	@ManyToOne(getch = FetchType.LAZY) // 지연 로딩 전략
	private Member member;
}
```

```java
class OrderController {

	public String view(Long orderId) {

		Order order = orderService.findOne(orderId);
		Member member = order.getMember();
		member.getName(); // 지연 로딩 시 예외 발생

	}
}
```

연관된 렌티티를 지연 로딩으로 설정해서 프록시 객체를 조회했을 때, 아직 초기화하지 않은 프록시 객체를 사용하면 실제 데이터를 불러오려고 초기화를 시도한다. 그러나 준영속 상태는 영속성 컨텍스트가 없으므로 지연 로딩이 불가능하다. (LazyInitializationException)

### 💡 지연 로딩 문제 해결 방법

- **필요한 엔티티를 미리 로딩/초기화**

    <aside>
    💡 **글로벌 패치 전략 수정** (지연 로딩 → 즉시 로딩)
    
    `@ManyToOne(getch = FetchType.EAGER)`
    
    엔티티에서 설정하기 때문에 전체 애플리케이션에 적용된다.
    
    - 단점
        - 사용하지 않는 엔티티를 로딩한다.
        - N+1 문제가 발생한다.
    
    <aside>
    📌 **N+1 문제**
    
    처음 조회한 데이터 수만큼 다시 SQL을 사용해서 조회하는 문제.
    
    JPA가 JPQL을 분석해서 SQL을 생성할 때는 글로벌 패치 전략을 참고하지 않고 오직 JPQL 자체만 사용한다.
    
    ```sql
    JPQL:
    	select o from Order o
    
    SQL: 
    	select * from Order
    	select * from Member where id=?
    	select * from Member where id=?
    	select * from Member where id=?
    	...
    ```
    
    만약 전체 Order를 조회했을 때,
    
    1. 전체 Order를 조회한다
    2. 글로벌 패치 전략에 따라 연관된 Member도 조회해야 한다.
    3. 연관된 Member를 영속성 컨텍스트에서 찾는다.
    4. 만약 영속성 컨텍스트에 없으면 조회한 Order 엔티티 수 만큼 Member를 조회하는 쿼리를 날린다.
    
    **→ JPQL fetch join으로 해결 가능**
    
    </aside>
    
    </aside>
    
    <aside>
    💡 **JPQL fetch join**
    
    SQL JOIN을 사용해서 페치 조인 대상까지 함께 조회.
    
    JPQL을 호출하는 시점에 함께 로딩할 엔티티를 선택한다.
    
    ```sql
    JPQL:
    	select o
    	from Order o
    	join fetch o.member
    
    SQL:
    	select o.*, m.*
    	from Order o
    	join Member m on o.MEMBER_ID=m.MEMBER_ID
    ```
    
    - 단점
        - 화면에 맞춘 레포지토리 메소드가 증가 (프리젠테이션 계층이 데이터 접근 계층을 침범) → 무분별한 최적화 경계
    </aside>
    
    <aside>
    💡 강제로 초기화
    
    영속성 컨텍스트가 살아있을 때 프레젠테이션 계층이 필요한 엔티티를 강제로 초기화하여 반환
    
    </aside>


- OSIV를 사용해 엔티티를 항상 영속 상태로 유지

# 객체지향 프로그래밍 Object Oriented Programming

- 객체 : 사물과 같이 유형적인 것과 개념이나 논리와 같은 무형적인 것들
- 지향 : 작정하거나 지정한 방향으로 나아감
- 객체 모델링 : 현실세계의 객체를 SW 객체로 설계하는 것

### 특징 A PIE

- 추상화 Abstraction
- 다형성 Polymorphism
- 상속 Inheritance
- 캡슐화 Encapsulation

---

# 클래스

- 관련 있는 변수와 함수를 묶어서 만든 사용자정의 <자료형>
- 모든 객체들의 생산처. 객체를 생성하는 틀.
- 객체들 사이에서 메세지를 주고 받도록 만들어준다.

### 구성

- 속성 Attribute - 필드, 멤버 변수
- 동작 Behavior - 메소드
- 생성자 Constructor : 인스턴스를 생성할 때 호출하는 메소드
- (inner class)

### 선언

```java
[접근제한자] [활용제한자] class 클래스명 {
	속성 정의 (필드)
	기능 정의 (메소드)
	생성자
}
```

- 접근제한자 : `public` / `default`
- 활용제한자: `final` / `abstract`

`Ctrl + Shift + O` : 자동 import

- 클래스 예시

```java
public class Person {
	// 속성
	static int personCount; // 클래스 변수
	String name; // 인스턴스 변수
	int age;
	String hobby;
	
	// 동작
	public void info() {
		System.out.println("나의 이름은 " + name + "입니다.");
		System.out.println("나이는 " + age + "세, 취미는 " + hobby + " 입니다.");	
	}
}
```

- 함수 예시

```java
public class FunctionTest1 {
	public static void main(String[] args) {
		
		System.out.println("아침에 일어난다.");
		System.out.println("교육장으로 대중교통을 이용하여 이동한다.");
		System.out.println("오전 수업을 듣는다.");
		System.out.println("점식을 먹는다.");
		System.out.println("오후 수업을 듣는다.");
		System.out.println("집으로 대중교통을 이용하여 이동한다.");
		System.out.println("잔다.");
		
		System.out.println("============================");
		
		boolean homework;
		
		System.out.println("아침에 일어난다.");
		transfer("제주도", "비행기");
		homework = education();
		
		if(homework)
				System.out.println("과제를 해결한다.");
		
		transfer("집", "배");
		System.out.println("잔다.");
	}
	
	public static boolean education() {
		System.out.println("오전 수업을 듣는다.");
		System.out.println("점식을 먹는다.");
		System.out.println("오후 수업을 듣는다.");
		
		// 과제 랜덤 발생기.
		Random random = new Random();
		return random.nextBoolean();
		
		/* 이래도 됨
		Random random = ;
		return new Random().nextBoolean();
		*/
	}
	
	public static void transfer(String 장소, String 탈것) {
		System.out.println(장소+"(으)로 "+탈것+"(을)를 이용하여 이동한다.");
	}
}
```

---

# 변수

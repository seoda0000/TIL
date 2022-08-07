# Java 기본

### 컴퓨터의 자료표현

- 1 byte :  -128~127 표현
- 2의 보수법
    - 00001001 → 9
    - 10001001 → -119 : 왼쪽 첫번째 자리가 1이면 마이너스라는 뜻. 128에서 나머지 1에 해당하는 숫자를 뺀다.

<br>

### 자바 가상머신 (JVM, Java virtual machine)

- **자바 바이트코드**를 실행할 수 있는 주체
    - 자바 바이트코드 : **OS에 독립적**.
    - JVM : OS마다 있음
    - JRE : 실행 시 필요한 것
    - JDK : JRE + 개발에 필요한 것
- Java 원시 프로그램 `.java` → 컴파일 → 자바 바이트 코드 `.class`
- 모든 JVM은 자바 가상 머신 규격에 정의된대로 자바 바이트코드를 실행

cf) `.`:참조 연산자 “가지고 있는”

<br>

### main method

- 실행 명령인 java를 실행 시 **가장 먼저 호출**되는 부분
- Application 시작 → 특정 클래스의 main() 실행
    - 만약, Application에서 main() 메소드가 없다면 절대로 실행 XXX
- `public static void matin(String [] args){ }`

<br>

### 주석 Coment

- `//내용` : 해당 줄을 주석처리 (Ctrl + /)
- `/*내용*/` : 해당 범위의 내용 주석처리
- `/**내용*/` : Documentation API를 위한 주석처리

<br>

### 출력문

- `print` 출력
- `println` 뒤에 자동 줄 바꿈
- `printf("%d", 10)` 포맷 설정
    - %d 정수
    - %f 실수
    - %c 문자
    - %s 문자열

```java
public class intro01_Hello {
	public static void main(String[] args) {
		System.out.println("Hello SSAFY!!!");
		System.out.print("Hello SSAFY!!!\n");
		
		System.out.printf("%4d\n", 10); //4칸을 확보한 뒤 오른쪽부터 차지 '  10'
		System.out.printf("%-4d\n", 10); //4칸을 확보한 뒤 왼쪽부터 차지 '10  '
		System.out.printf("%04d\n", 10); //4칸을 확보한 뒤 오른쪽부터 차지 (빈칸 0으로) '0010'
		
		System.out.printf("%f\n", 10.1); //10.100000
		System.out.printf("%.2f\n", 10.1); //10.10
		
		System.out.printf("%s\n", "와우우우"); //문자열은 쌍따옴표 사용
		System.out.printf("%c\n", '와'); //문자는 따옴표 사용
		
		System.out.printf("안녕하세요. 저는 %s입니다. 혈액형은 %c일 걸요?\n", "리자", 'A');
	}
}
```

---

# 변수와 자료형

### 변수

- 데이터를 저장할 메모리의 위치를 나타내는 이름
- 메모리 상에 데이터를 보관할 수 있는 공간을 확보
- 클래스 이름 : PascalCase
- 합성어 : camelCase
- Python&상수 : SNAKE_CASE
- HTML&CSS : kebab-case

<br>

### 메모리의 단위

- 0과 1을 표현하는 bit
- 8bit = 1byte

<br>

### Data Type-기본 자료형

| 타입 | 세부타입 | 데이터형 | 크기 | 범위 |
| --- | --- | --- | --- | --- |
| 논리형 |  | boolean |  | true/flase |
| 문자형 |  | char | 2byte | 0~65,535 |
| 숫자형 | 정수형 | byte | 1byte | -128~127 |
|  |  | short | 2byte | -32,768~32,767 |
|  |  | int | 4byte | -2,147,483,648~2,147,483,647 |
|  |  | long | 8byte | -9,223,372,036,854,775,808~9,223,372,036,854,775,807 |
|  | 실수형 | float | 4byte |  |
|  |  | double | 8byte |  |

<br>

### 선언

- {자료명} {변수명}
- ex) `int age;` `String name;`

### 저장

- {변수명} = {저장할 값}
- ex) `age = 30;`, `name = “철수”`
- 기본 자료형은 값을 저장, 참조 자료형은 값이 있는 주소가 저장
- `b = age;` 기초 자료형에서는 값을 복사해서 저장

### 초기화

- {자료형} {변수명} = {저장할 값}
- ex) `int age = 30`

<br>


### 자료형의 크기 비교

- 단순 크기가 아닌 표현 범위 기준!
- byte < short, char < int < long < float < double

<br>

### 데이터 형변환

- 묵시적 Implicit Casting
    - **범위가 넓은 데이터 형**에 좁은 데이터 형을 대입
    - ex) `byte b = 100; int i = b;`
- 명시적 Explicit Casting
    - **범위가 좁은 데이터 형**에 넓은 데이터 형을 대입
    - 형 변환 연산자 사용 `(타입) 값;`
    - 데이터 손실 위험
    - ex) `int i = 100; byte b = (byte) i;`

---

# 연산자

| 종류 | 연산기호 | 결합 방향 | 우선순위 |
| --- | --- | --- | --- |
| 최우선 연산자 | () . [] |  |  |
| 단항 연산자 | ++ — + - ~ ! (type) : 형변환 * / % | ← | 높음 |
| 산술 연산자 | + - << >> >>> | → |  |
| 비교 연산자 | < > <= >= instanceof == != | → |  |
| 논리 연산자 | & ^ | && || | → |  |
| 삼항 연산자 | ? : | → |  |
| 대입 연산자 | = *= /= %= += -= <≤ >>= >>>= &= ^= ≠ | ← |  |
- 만약 우선순위가 동급이면 작성된 순서로 실행.

<br>

### 단항 연산자

- 증감 연산자 ++, —
    - 피연산자의 값을 1 증가, 감소
    - 전위형prefix ++i : 하고 연산
    - 후위형postfix i-- : 연산 후 함
- 부호 연산자 +-
- 논리 부정 연산자 !
- 비트 부정 연산자 ~
- 형 변환 연산자 (type)

### 산술 연산자

- * / % + -
- 정수와 실수의 연산 → 실수

### 비교 연산자

- 대소 비교 연산 : < > <= >= → boolean
- 동등 비교 연산 : == != → boolean
    - **string 변수 비교 : equals() 사용**
- 객체 타입 비교 연산 : instanceof

### 논리 연산자

- && : 논리 곱 (AND)
- || : 논리 합 (OR)
- ! : 논리 부정 (NOT)
- 효율적인 연산 가능 short circuit evaluation

### 삼항 연산자

- 조건식 ? 식1 : 식2
- 조건식이 참일 경우 식1 수행
- 조건식이 거짓일 경우 식2 수행

### 복합 대입 연산자

- +=, -=, *=, /=…

---

# 제어문 (조건문 & 반복문)

## 조건문 Conditional Statement

### if문

```java
if(조건식) {
		실행할 문장1;
		실행할 문장2;
		…
}

if(조건식)
		실행할 문장1; // 실행할 문장이 하나라면 중괄호 생략 가능
		실행할 문장2; // if문과 별개로 무조건 실행됨. 중괄호 되도록 생략하지 말기!
```

### if-else문

```java
if(조건식) {
		실행할 문장1;
		실행할 문장2;
		…
}else {
		실행할 문장a;
		…
}

if(조건식)
		실행할 문장1; // 실행할 문장이 하나라면 중괄호 생략 가능
else 
		실행할 문장a; // 실행할 문장이 하나라면 중괄호 생략 가능
```

### 중첩 if문

```java
if(조건식A) {
		if(조건식B) {
				조건식 A, B 모두 참일 경우 수행할 문장;
		}else {
				조건식 A는 참, B는 거짓일 경우 수행할 문장;
		}
}else {
		조건식 A가 거짓일 경우 수행할 문장;
}

// 중첩의 횟수에는 제한이 없음
```

### if - else if - else문

```java
if(조건식) {
		실행할 문장1;
		...
}else if (조건식) {
		실행할 문장a;
		...
}...{
}else {
		실행할 문장A;
		...
}
```

<br>

### switch문

- 인자로 선택변수를 받아 변수의 값에 따라서 실행문이 결정.

```java
switch(수식) {  // 수식에 올 수 있는 것 : byte, short, char, int, enum, String
		case 값1:
				실행문 A;
				break;  
		case 값2:
				실행문 B;
				break;
		default:  // else의 역할과 동일
				실행문 C;
}
```

```java
// break문 없이도 사용 가능

int month = 12;

switch(month) {
case 1:
case 3:
case 5:
case 7:
case 8:
case 10:
case 12:
		System.out.pintln("31일");
		break;
case 4:
case 6:
case 9:
case 11:
		System.out.pintln("30일");
		break;
case 2:
		System.out.pintln("28일");
		break;
default:
		System.out.pintln("그러한 달은 없다.");
}
```

---
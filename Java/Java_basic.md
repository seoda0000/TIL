- [**Java 기본**](#Java-기본)
  - [컴퓨터의 자료표현](#컴퓨터의-자료표현)
  - [자바 가상머신 (JVM, Java virtual machine)](<#자바-가상머신-(JVM,-Java-virtual-machine)>)
  - [main method](#main-method)
  - [주석 Coment](#주석-Coment)
  - [출력문](#출력문)
- [**변수와 자료형**](#변수와-자료형)
  - [변수](#변수)
  - [메모리의 단위](#메모리의-단위)
  - [Data Type-기본 자료형](#Data-Type-기본-자료형)
  - [선언](#선언)
  - [저장](#저장)
  - [초기화](#초기화)
  - [자료형의 크기 비교](#자료형의-크기-비교)
  - [데이터 형변환](#데이터-형변환)
- [**연산자**](#연산자)
  - [단항 연산자](#단항-연산자)
  - [산술 연산자](#산술-연산자)
  - [비교 연산자](#비교-연산자)
  - [논리 연산자](#논리-연산자)
  - [삼항 연산자](#삼항-연산자)
  - [복합 대입 연산자](#복합-대입-연산자)
- [**제어문 (조건문 & 반복문)**](<#제어문-(조건문-&-반복문)>)
  - [조건문 Conditional Statement](#조건문-Conditional-Statement)
    - [if문](#if문)
    - [if-else문](#if-else문)
    - [중첩 if문](#중첩-if문)
    - [if - else if - else문](#if---else-if---else문)
    - [do ~ while문](#do-~-while문)

---

# Java 기본

- Java 간단히 사용하기

`jshell`
`/exit`

### 컴퓨터의 자료표현

- 1 byte : -128~127 표현
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
- main + Ctrl + Space + Enter

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

| 타입   | 세부타입 | 데이터형 | 크기  | 범위                                                 |
| ------ | -------- | -------- | ----- | ---------------------------------------------------- |
| 논리형 |          | boolean  |       | true/flase                                           |
| 문자형 |          | char     | 2byte | 0~65,535                                             |
| 숫자형 | 정수형   | byte     | 1byte | -128~127                                             |
|        |          | short    | 2byte | -32,768~32,767                                       |
|        |          | int      | 4byte | -2,147,483,648~2,147,483,647                         |
|        |          | long     | 8byte | -9,223,372,036,854,775,808~9,223,372,036,854,775,807 |
|        | 실수형   | float    | 4byte |                                                      |
|        |          | double   | 8byte |                                                      |

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

| 종류          | 연산기호                              | 결합 방향 | 우선순위 |
| ------------- | ------------------------------------- | --------- | -------- | --- | --- | --- |
| 최우선 연산자 | () . []                               |           |          |
| 단항 연산자   | ++ — + - ~ ! (type) : 형변환 \* / %   | ←         | 높음     |
| 산술 연산자   | + - << >> >>>                         | →         |          |
| 비교 연산자   | < > <= >= instanceof == !=            | →         |          |
| 논리 연산자   | & ^                                   | &&        |          |     | →   |     |
| 삼항 연산자   | ? :                                   | →         |          |
| 대입 연산자   | = \*= /= %= += -= <≤ >>= >>>= &= ^= ≠ | ←         |          |

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

- - / % + -
- 정수와 정수의 연산 → 정수 `(ex 5/2 → 2)`
- 정수와 실수의 연산 → 실수

### 비교 연산자

- 대소 비교 연산 : < > <= >= → boolean
- 동등 비교 연산 : == != → boolean

  - **string 변수 비교 : equals() 사용**

  ```python
  String c = "Hi";
  String d = "Hi";
  String e = new String("Hi"); # 다른 메모리 공간에 생성

  System.out.println(c == d); # true
  System.out.println(c == e); # false
  System.out.println(c.equals(e)); # true
  ```

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

- +=, -=, \*=, /=…

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

## 반복문 Loop

### for문

```java
for(1초기화식; 2조건식; 4증감식){
		3반복 수행할 문장
}

for(int i = 0; i<10; i++){
		System.out.println(i);
}
```

- 초기화는 반복문이 시작될 때 한번 실행됨
- 조건식이 false이면, 반복문 종료
- 증감식은 반복문의 반복이 끝나면 실행
- 초기화식, 증감식은 (,)를 이용하여 둘 이상을 작성할 수 있음. `int i=0, j=0;`
- 필요하지 않은 부분은 생략할 수 있음. `for(;;)` 조건식을 비우면 무한루프
- 반복횟수를 알고 있을 때 유용

### 중첩 for문

```java
for(초기화식; 조건식; 증감식){
		for(초기화식; 조건식; 증감식){
				반복 수행할 문장
		}
}

// 구구단
for(int i = 2; i <= 9; i++){
		System.out.printf("%d단\n", i)
		for(int j = 1; j <= 9; j++){
				System.out.printf("%d * %d = %d\n", i, j, i * j)
		}
}
```

### while문

```java
while(1조건식) {
		2반복 수행할 문장;
}
```

- 조건식 생략 불가능

### do ~ while문

```java
do{
		1반복 수행할 문장;
}while(2조건식);
```

- 블록 내용을 먼저 수행 후 조건식 판단 (최소 한번은 수행)
- 조건식이 true인 경우 계속 반복
- 조건식 생략 불가능

### break

### continue

---

# 배열 Array

- 같은 종류의 데이터를 저장하기 위한 자료구조
- 크기가 고정되어 있음 (한번 생성된 후 크기 변경 불가)
- 배열을 객체로 취급
- 배열의 요소를 참조하려면 배열 이름과 색인을 조합하여 사용
- `[stack 영역]` array 이름 → 주소로 참조 → `[heap 영역]` array 내용 : String 주소 → 주소로 참조 → String 내용

<br>

### 배열의 선언

- 타입[] 변수 `int[] arr` ⭐
- 타입 변수[] `int arr[]`
  | 타입 | 배열이름 | 선언 |
  | ------- | -------- | ---------------- |
  | int | iArr | int[] iArr; |
  | char | cArr | char[] cArr; |
  | boolean | bArr | boolean[] bArr; |
  | String | strArr | String[] strArr; |
  | Date | dateArr | Date[] dateArr; |

<br>

### 배열의 생성과 초기화

- `자료형[] 배열이름 = {값1, 값2, 값3, 값4};` // 선언과 동시에 초기화
- `배열이름 = new 자료형[] {값1, 값2, 값3, 값4};` // 배열 생성 및 값 초기화
- `배열이름 = new 자료형[길이];` // 배열 생성
  | 자료형 | 기본값 | 비고 |
  | --------------------------- | -------- | ---------------------- |
  | boolean | false | |
  | char | ‘\u0000’ | 공백문자 |
  | byte, short, int | 0 | |
  | long | 0L | |
  | float | 0.0f | |
  | double | 0.0 | |
  | 참조형 변수 (String, Date…) | null | 아무것도 참조하지 않음 |
- 배열의 사용
- index는 0부터
- `배열이름.length` : 배열 길이 조회
- 배열의 길이는 임의로 변경 불가
- 길이 변경 필요시 새로운 배열 생성 후 내용을 옮긴다

<br>

### for-each

- 가독성이 개선된 반복문. 배열 및 Collections에서 사용
- index 대신 직접 요소 (elements)에 접근하는 변수 제공
- natually ready only (copied value)

```java
int[] arr = {77, 50, 10, 12, 64, 15};

for(int i = 0 ; i<arr.length; i++) {
		arr[i] *= 2;
}

System.out.println(Arrays.toString(arr)); // 빠르게 배열 내용 확인
```

<br>

### 배열의 복사

- `System.arraycopy(Object src, int srcPos, Object dest, int destPos, int length)`
- `src` : 원본 배열
- `srcPos` : 원본 배열 복사 시작 위치
- `dest` : 복사할 배열
- `destPos` : 복사 받을 시작 위치
- `length` : 복사할 크기

```java
package array00;

import java.util.Arrays;

public class arrayfirst {
	public static void main(String[] args) {

		int[] arr = {77, 50, 10, 12, 64, 15};

		int[] tmp = new int[arr.length*2]; // 반복문을 이용하여 복사
		for(int i = 0; i < arr.length; i++) {
			tmp[i] = arr[i];
		}
		System.out.println(Arrays.toString(tmp)); // [77, 50, 10, 12, 64, 15, 0, 0, 0, 0, 0, 0]

		int[] tmp2 = new int[arr.length*2];

		System.arraycopy(arr, 0, tmp2, 0, arr.length);

		System.out.println(Arrays.toString(tmp2)); // [77, 50, 10, 12, 64, 15, 0, 0, 0, 0, 0, 0]
	}
}
```

```java
// 최대값, 최소값 찾기

int[] intArray = {3, 27, 13, 8, 235, 7, 22, 9, 435, 31, 54};

int min = 1000;
int max = 0;
for(int num: intArray) {
		if(num>max) {
				max = num;
		}
		if(num<min) {
				min = num;
		}
}
System.out.printf("min: %d, max: %d\n", min, max);
// 빈도수 구하기

int[] intArray = {3, 7, 2, 5, 7, 7, 9, 2, 8, 1, 1, 5, 3}

int[] used = new int[10];

for(int num:intArray) {
		used[num]++;
}

System.out.println(Arrays.toString(used));
```

---

# 다차원 배열 Multidimensional Array

- 2차원 이상의 배열
- 배열 요소로 또 다른 배열을 가지는 배열

<br>

### 2차원 배열 선언

- `int[][] iArr`
- `int iArr[][]`
- `int[] iArr[]`

<br>

### 2차원 배열 생성

- `배열의 이름 = new 배열유형[1차원 배열개수][1차원 배열의 크기];` 1차원 크기 고정
- `배열의 이름 = new 배열유형[1차원 배열개수][];` 1차원 크기 고정 x 기본값 null
- 2차원 배열의 요소인 **1차원 배열의 크기가 모두 같을 필요는 없다.**

<br>

### 2차원 배열 탐색

- 모든 2차원 배열의 원소 중 3의 배수의 개수와 그들의 합을 출력

```java
public static void main(String[] args) {
		int[][] grid = {
				{2, 3, 1, 4, 7}, {8, 13, 3, 33, 1},
				{7, 4, 5, 80, 12}, {17, 9, 11, 5, 4},
				{4, 5, 91, 27, 7}
		};
		int count = 0;
		int sum = 0;
		for(int[] row: grid) {
				for(int num: row) {
						if(num%3==0) {
								count++;
								sum+=num;
						}
				}
		}
		System.out.printf("개수: %d, 총합: %d%n", count, sum);
}
```

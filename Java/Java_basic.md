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
```
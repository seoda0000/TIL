- [JavaScript](#javascript)
		- [JavaScript 실행하기](#javascript-실행하기)
- [JavaScript 기초 문법](#javascript-기초-문법)
- [변수와 식별자](#변수와-식별자)
		- [식별자 정의와 특징](#식별자-정의와-특징)
	- [변수 선언 키워드](#변수-선언-키워드)
			- [💡 선언, 할당, 초기화](#-선언-할당-초기화)
			- [💡 호이스팅 hoisting](#-호이스팅-hoisting)
	- [데이터 타입](#데이터-타입)
- [원시 타입 데이터](#원시-타입-데이터)
		- [Number](#number)
		- [String](#string)
		- [Empty Value](#empty-value)
		- [Boolean](#boolean)
- [연산자](#연산자)
		- [할당 연산자](#할당-연산자)
		- [비교 연산자](#비교-연산자)
		- [동등 연산자 `==`](#동등-연산자-)
		- [일치 연산자 `===`](#일치-연산자-)
		- [논리 연산자](#논리-연산자)
		- [삼항 연산자](#삼항-연산자)
- [조건문](#조건문)
		- [`if`, `else if`, `else`](#if-else-if-else)
		- [`switch`](#switch)
- [반복문](#반복문)
		- [`while`](#while)
		- [`for`](#for)
		- [`for...in`](#forin)
		- [`for...of`](#forof)
		- [`for...in` 과 `for...of` 의 차이](#forin-과-forof-의-차이)
- [함수](#함수)
		- [함수 선언식](#함수-선언식)
		- [함수 표현식 ⭐](#함수-표현식-)
		- [기본 인자 Default arguments](#기본-인자-default-arguments)
		- [매개변수와 인자의 개수 불일치 허용](#매개변수와-인자의-개수-불일치-허용)
		- [전개 구문 Spread syntax `...`](#전개-구문-spread-syntax-)
	- [화살표 함수 Arrow Function](#화살표-함수-arrow-function)
		- [즉시 실행 함수(Immediately Invoked Function Expression)](#즉시-실행-함수immediately-invoked-function-expression)
- [참조 타입 데이터](#참조-타입-데이터)
- [배열 Array](#배열-array)
		- [배열 메서드](#배열-메서드)
		- [`forEach`](#foreach)
		- [배열 순회 비교](#배열-순회-비교)
		- [`map`](#map)
		- [`filter`](#filter)
		- [`reduce`](#reduce)
		- [`find`](#find)
		- [`some`](#some)
		- [`every`](#every)
- [객체 Object](#객체-object)
		- [key](#key)
		- [value](#value)
		- [객체 요소 접근](#객체-요소-접근)
	- [객제 관련 ES6 문법](#객제-관련-es6-문법)
		- [1. 속성명 축약](#1-속성명-축약)
		- [2. 메서드명 축약](#2-메서드명-축약)
		- [3. 계산된 속성](#3-계산된-속성)
		- [4. 구조 분해 할당](#4-구조-분해-할당)
		- [5. Spread syntax](#5-spread-syntax)
		- [6. Export \& Import](#6-export--import)
	- [JSON](#json)
		- [Object → JSON](#object--json)
		- [JSON → Object](#json--object)
			- [💡 배열은 객체다](#-배열은-객체다)

<br>

---




# JavaScript

- HTML 문서의 콘텐츠를 동적으로 변경할 수 있는 언어
- Web이라는 공간에서 채팅, 게임 등 다양한 동작의 기반
- 웹 브라우저에는 JavaScript를 해석하는 엔진이 있음
- 다른 개발에서도 다양히 활용

<aside>
🍦 Vanilla JavaScript

웹 브라우저에서 바로 실행할 수 있는 JavaScript 문법들

</aside>

### JavaScript 실행하기

1. 웹 브라우저로 실행 `개발자 도구 (F12)` → Console
2. Node.js 이용 `node file.js`
    - 설치 확인
        
        `node -v`
        
        `npm -v`
        

---

# JavaScript 기초 문법

- 세미콜론 생략 가능
- 들여쓰기 2칸
- 블럭 : `{ }`
- 주석
    
    ```jsx
    // 한줄 주석
    /*
    여러줄
    주석
    */
    ```
    
- Airbnb Style Guide
    
    [GitHub - airbnb/javascript: JavaScript Style Guide](https://github.com/airbnb/javascript)
    

<br>

---

# 변수와 식별자

- 식별자 : 변수를 구분할 수 있는 변수명
    - 문자, $, _로 시작
    - 대소문자 구분

<br>

### 식별자 정의와 특징

- 카멜 케이스 `camelCase`
    - 변수, 객체, 함수
- 파스칼 케이스 `PascalCase`
    - 클래스, 생성자
- 대문자 스네이크 케이스 `SNAKE_CASE`
    - 상수

<br>


## 변수 선언 키워드

| 키워드 | 선언 |  | 재할당 | 재선언 |
| --- | --- | --- | --- | --- |
| let | 블록 스코프 지역 변수를 선언 | 동시에 값을 초기화 | O | X |
| const | 블록 스코프 읽기 전용 상수를 선언 | 동시에 값을 초기화 | X | X |
| var | (함수 스코프) 변수를 선언 | 동시에 값을 초기화 | O | O |


<br>


#### 💡 선언, 할당, 초기화

<aside>


- **선언 Declaration** : 변수를 생성하는 행위 또는 시점
- **할당 Assignment** : 선언된 변수에 값을 저장하는 행위 또는 시점
- **초기화 Initialization** : 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

```jsx
let foo            // 선언
console.log(foo)   // undefined

foo = 11           // 할당
console.log(foo)   // 11

let bar = 0        // 선언 + 할당
console.log(bar)   // 0
```

<br>


</aside>

#### 💡 호이스팅 hoisting

<aside>


변수를 선언 이전에 참조할 수 있는 현상.

var 에 나타나므로 사용 권장 XXX

</aside>

---

<br>

## 데이터 타입

| 원시 타입 Primitive | 참조 타입 Reference |
| --- | --- |

![Untitled](./images/basic1.png)

---

<br>

# 원시 타입 데이터

### Number

- 정수 또는 실수형 숫자를 표현하는 자료형

```jsx
const c = 3.14        // float - 숫자 표현
const d = 2.998e8     // 2.998 * 10^8
const e = Infinity 
const g = NaN         // Not a Number

Number.isNaN(NaN)     // true : 값이 NaN일 때만 true
Number.isNaN(0 / 0)   // true
Number.isNaN('NaN')   // false

```

- NaN을 반환하는 경우
    1. 숫자로서 읽을 수 없음 `parseInt(”어찌구”)`, `Number(undefined)`
    2. 결과가 허수인 수학 계산식 `Math.sqrt(-1)`
    3. 피연산자가 NaN `7 ** NaN`
    4. 정의할 수 없는 계산식 `0 * Infinity`
    5. 문자열을 포함하면서 덧셈이 아닌 계산식 `"가" / 3`

<br>


### String

- 문자열을 표현하는 자료형
- 덧셈 가능
- 줄바꿈 시 \n 사용

```jsx
const firstName = "Ned"
const lastName = "Stark"
const fullName = firstName + lastName

const word = "Game \nof Throne"
```

- Template Literal : 줄바꿈, 변수 삽입 가능

```jsx
const age = 29
const message = `소개하겠습니다.
신해량은 ${age}세입니다.`
```

```jsx
for (let j = 0; j < 5; j++) {
  let a = (2*j+1)
  let next = ''
  let middle = ''
  for (i = 0; i < 4 - a/2 ; i++) {
    next += ' '
  }
  for (i = 0; i < a; i++) {
    middle += '*'
  }
  console.log(`${next}${middle}`)
}

for (let i=1; i <= 9; i+=2) {
  console.log(' '.repeat((9-i)/2) + '*'.repeat(i))
}

    *
   ***
  *****
 *******
*********
```

<br>


### Empty Value

- `null`
    - null 값 :변수의 값이 없음을 의도적으로 표현
- `undefined`
    - 값이 정의되어 있지 않음 : 자동으로 할당

```jsx
let Name
console.log(Name)  // undefined

typeof null        // "object"
typeof undefined   // "undefined"
```

<br>


### Boolean

- `true`/ `false`
- 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 `true` 또는 `false`로 변환됨

| 데이터 타입 | false | true |
| --- | --- | --- |
| undefined | 항상 false | X |
| null | 항상 false | X |
| Number | 0, -0, NaN | 나머지 모든 경우 |
| String | 빈 문자열 | 나머지 모든 경우 |
| Object | X | 항상 true |

<br>


---

# 연산자

### 할당 연산자

- Increment (++) : 1 증가
- Decrement (—) : 1 감소
- +=, -= 등 더 분명한 표현 권장

<br>


### 비교 연산자

- <, >
- 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
    - 알파벳 후순위가 더 크다
    - 소문자가 대문자보다 더 크다

<br>


### 동등 연산자 `==`

- 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- 권장 X

<br>


### 일치 연산자 `===`

- 두 피연산자가 같은 객체를 가리키거나, 값과 타입이 모두 같을 경우 true 반환
- 암묵적 타입 변환이 발생 X 엄격한 비교

<br>


### 논리 연산자

- 단축 평가 지원

| and | && |
| --- | --- |
| or | || |
| not  | ! |

<br>


### 삼항 연산자

- 3개의 피연산자를 사용하여 첫번째 조건에 따라 앞이나 뒤의 값을 반환하는 연산자

```jsx
true ? 1 : 2   // 1
false ? 1 : 2  // 2

const result = Math.PI > 4 ? 'Yep' : 'Nope'
console.log(result)  // Nope
```

<br>


---

# 조건문

### `if`, `else if`, `else`

- 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단

```jsx
const name = 'manager'

if (name === 'admin') {
	console.log('관리자님 환영합니다.')
} else if (name === 'manager') {
	console.log('매니저님 환영합니다.')
} else {
	console.log(`${name}님 환영합니다.`)
}
```

<br>


### `switch`

- 조건 표현식의 결과값이 어느 값에 해당하는지 판별
- break 및 default문은 선택적으로 사용 가능
- break문이 없는 경우 break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행

```jsx
switch (expression) {
	case 'first value': {
		// do something
		[break]
	}
	case 'second value': {
		// do something
		[break]
	}
	[default: {
		// do something
	}]
}
```

```jsx
// block문이 없는 경우

const name = '신해량'

switch (name) {
	case '신해량': {
		console.log('관리자님 환영합니다.')
	}
	case 'manager': {
		console.log('매니저님 환영합니다.')
	}
	default: {
		console.log(`${name}님 환영합니다.`)
	}
}

// 출력 결과
관리자님 환영합니다.
매니저님 환영합니다.
신해량님 환영합니다.
```

```jsx
// block문이 있는 경우

const name = '신해량'

switch (name) {
	case '신해량': {
		console.log('관리자님 환영합니다.')
		break
	}
	case 'manager': {
		console.log('매니저님 환영합니다.')
		break
	}
	default: {
		console.log(`${name}님 환영합니다.`)
	}
}

// 출력 결과
관리자님 환영합니다.
```

<br>


---

# 반복문

### `while`

- 조건문이 참이기만 하면 문장을 계속해서 수행

```jsx
while (조건문) {
	// do something
}

// ex
let i = 0

while (i < 6) {
	console.log(i)
	i += 1
}

// 0, 1, 2, 3, 4, 5
```

<br>


### `for`

- 특정한 조건이 거짓으로 판별될 때까지 반복
- `const` 사용 시 에러 발생

```jsx
for ([초기문]; [조건문]; [증감문]) {
	// do something
}

// ex
for (let i = 0; i < 6; i++) {
	console.log(i)
}

// 0, 1, 2, 3, 4, 5
```

1. 반복문 진입 및 변수 i 선언
2. 조건문 평가 후 코드 블럭 실행
3. 코드 블럭 실행 후 i 값 증가

<br>


### `for...in`

- 객체(Object)의 속성을 순회할 때 사용
- `const` 사용 시 에러가 발생하지 않음

```jsx
for (variable in object) {
	statements
}

// ex
const fruits = {a: 'apple', b: 'banana'}

for (const key in fruits) {
	console.log(key) // a, b
	console.log(fruits[key]) // apple, banana
}
```

<br>


### `for...of`

- 반복 가능한 객체를 순회할 때 사용
- 반복 가능한(iterable) 객체의 종류: Array, Set, String 등
- `const` 사용 시 에러가 발생하지 않음

```jsx
for (variable of object) {
	statements
}

// ex
const numbers = [0, 1, 2, 3]

for (const number of numbers) {
	console.log(number)  // 0, 1, 2, 3
}
```

<br>


### `for...in` 과 `for...of` 의 차이

- `for...in` : 속성 이름을 통해 반복 → 객체 순회 적합
- `for...of` : 속성 값을 통해 반복 → iterable 순회 적합

```jsx
const arr = [3, 5, 7]

for (const i in arr) {
	console.log(i)  // 0 1 2
}

for (const i of arr) {
	console.log(i)  // 3 5 7
}
```

---

<br>


# 함수

- 참조 타입 중 하나로써 function 타입에 속함
- 함수를 정의하는 방법
    - 함수 선언식 (function declaration)
    - 함수 표현식 (function expression)

<br>


### 함수 선언식

- 일반적인 프로그래밍 언어의 함수 정의 방식
- 익명함수 불가능
- 호이스팅 발생 : 함수 호출 이후에 선언해도 동작

```jsx
function 함수명() {
	// do something
}

function add(num1, num2) {
	return num1 + num2
}

add(2, 7) // 9
```

<br>


### 함수 표현식 ⭐

- 표현식 내에서 함수를 정의하는 방식
- 함수 표현식은 함수의 이름을 생략한 익명 함수로 정의 가능
- 호이스팅 발생 X

```jsx
변수키워드 함수명 = function () {
	// do something
}

// 익명 함수
const sub = function (num1, num2) {
	return num1 - num2
}

sub(7, 2) // 5

// 함수 이름 명시
const mySub = function namedSub(num1, num2) {
	return num1 - num2
}

mySub(7, 2) // 5
namedSub(7, 2)  // ReferenceError: nameSub is not defined
```

<br>


### 기본 인자 Default arguments

- 인자 작성 시 = 뒤 기본 인자 선언 가능

```jsx
const greeting = function (name = 'Anonymous') {
	return `Hi ${name}`
}

greeting()  // Hi Anonymous
```

<br>


### 매개변수와 인자의 개수 불일치 허용

- 매개변수보다 인자의 개수가 많을 경우

```jsx
const twoArgs = function (arg1, arg2) {
	return [arg1, arg2]
}

twoArgs(1, 2, 3)  // [1, 2]
```

- 매개변수보다 인자의 개수가 적을 경우

```jsx
const threeArgs = function (arg1, arg2, arg3) {
	return [arg1, arg2, arg3]
}

threeArgs(1, 2)  // [1, 2, undefined]
```

<br>


### 전개 구문 Spread syntax `...`

- 전개 구문을 사용하면 배열이나 문자열과 같이 반복 가능한 객체를 배열의 경우는 요소, 함수의 경우는 인자로 확장할 수 있음
1. 배열과의 사용 (배열 복사)
    
    ```jsx
    let parts = ['shoulders', 'knees']
    let lyrics = ['head', ...parts, 'and', 'toes']
    // ['head, 'shoulders', 'knees', 'and', 'toes']
    ```
    
2. 함수와의 사용 Rest parameters
    - 정해지지 않은 수의 매개변수를 배열로 받을 수 있음
    
    ```jsx
    const restOpr = function (arg1, arg2, ...restArgs) {
    	return [arg1, arg2, restArgs]
    }
    restArgs(1, 2, 3, 4, 5)  // [1, 2, [3, 4, 5]]
    restArgs(1, 2)  // [1, 2, []]
    ```
    

<br>


## 화살표 함수 Arrow Function

- 함수를 비교적 간결하게 정의할 수 있는 문법
1. `function` 키워드 생략 가능
2. 함수의 매개 변수가 하나 뿐이라면 매개변수의 `()` 생략 가능
3. 함수의 내용이 한 줄이라면 `{}` 와 `return` 도 생략 가능
- 화살표 함수는 항상 익명 함수 (표현식에서만 사용 가능)

```jsx
const arrow1 = function (name) {
	return `hello, ${name}`
}

// 1. `function` 키워드 생략 가능
const arrow2 = (name) => { return `hello, ${name}`}

// 2. 함수의 매개 변수가 하나 뿐이라면 매개변수의 `()` 생략 가능
const arrow3 = name => { return `hello, ${name}`}

// 3. 함수의 내용이 한 줄이라면 `{}` 와 `return` 도 생략 가능
const arrow4 = name => `hello, ${name}`
```

```jsx
// 1. 인자가 없다면? () or _로 표시 가능
let noArgs = () => 'No args'
noArgs = _ => 'No args'

// 2-1. object를 return 한다면
let returnObject = () => { return { key: 'value'} } // return을 명시적으로 적어준다.

// 2-2. return을 적지 않으려면 괄호를 붙여야 함
returnObject = () => ({ key: 'value' })
```

<br>


### 즉시 실행 함수(Immediately Invoked Function Expression)

- 선언과 동시에 실행되는 함수
- 함수의 선언 끝에 ‘()’를 추가하여 선언되자 마자 실행하는 형태
- ‘()’ 에 값을 넣어 인자로 넘겨줄 수 있음
- 즉시 실행 함수는 선언과 동시에 실행되기 때문에 같은 함수를 다시 호출할 수 없음
- 이러한 특징을 살려 초기화 부분에 많이 사용
- 일회성 함수이므로 익명함수로 사용하는 것이 일반적

```jsx
(function(num)) { return num ** 3 })(2) // 8

(num => num ** 3)(2) // 8

```

<br>


---

# 참조 타입 데이터

- 객체라고도 말함.
- 객체는 속성들의 모음(collection)
    - Array
    - Object

<br>


---

# 배열 Array

- 키와 속성들을 담고 있는 참조 타입의 객체
- 순서를 보장
- 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이 : `array.length`

```jsx
const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])       // 1
console.log(numbers[-1])      // undefined
console.log(numbers.length)   // 5
```

<br>


### 배열 메서드

| 메서드 |  설명 | 비고 |
| --- | --- | --- |
| reverse | 원본 배열의 요소들의 순서를 반대로 정렬 |  |
| push & pop | 배열의 가장 뒤에 요소를 추가 또는 제거 |  |
| unshift & shift | 배열의 가장 뒤에 요소를 추가 또는 제거 |  |
| includes | 배열에 특정 값이 존재하는지 판별 후 참/거짓 반환 |  |
| indexOf | 배열에 특정 값이 존재하는지 판별 후 인덱스 반환 | 요소가 없을 경우 -1 반환 |
| join | 배열의 모든 요소를 구분자를 이용하여 연결 | 구분자 생략 시 쉼표 기준 |

```jsx
const numbers = [1, 2, 3, 4, 5]
numbers.reverse()
console.log(numbers)  // [5, 4, 3, 2, 1]

const numbers = [1, 2, 3, 4, 5]
numbers.push(100)
console.log(numbers)  // [1, 2, 3, 4, 5, 100]
numbers.pop()
console.log(numbers)  // [1, 2, 3, 4, 5]

console.log(numbers.includes(1))  // true
console.log(numbers.includes(100))  // false

result = numbers.indexOf(3)
console.log(result)  // 2

result = numbers.indexOf(100)
console.log(result)  // -1

result = numbers.join()  
console.log(result)  // 1,2,3,4,5

result = numbers.join('')  
console.log(result)  // 12345

result = numbers.join(' ')  
console.log(result)  // 1 2 3 4 5

result = numbers.join('-')  
console.log(result)  // 1-2-3-4-5

```

<br>


| 메서드 |  설명 | 비고 |
| --- | --- | --- |
| forEach | 배열의 각 요소에 대해 콜백 함수를 한번씩 실행 | 반환값 없음 |
| map | 콜백 함수의 반환값을 요소로 하는 새로운 배열 반환 |  |
| filter | 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환 |  |
| reduce | 콜백 함수의 반환 값들을 하나의 값acc에 누적 후 반환 |  |
| find | 콜백 함수의 반환 값이 참이면 해당 요소를 반환 |  |
| some | 배열의 요소 중 하나라도 판별 함수를 통과한다면 참을 반환 |  |
| every | 배열의 모든 요소가 판별 함수를 통과하면 참을 반환 |  |

<br>


### `forEach`

```jsx
array.forEach((element, index, array) => {
	// do something
})

const colors = ['red', 'blue', 'greem']
colors.forEach((color) => {
	console.log(color)
})

// red
// blue
// green
```

<br>


### 배열 순회 비교

| 방식 | 특징 | break, continue | 비고 |
| --- | --- | --- | --- |
| for loop | 인덱스를 활용하여 배열의 요소에 접근 | 사용 가능 |  |
| for … of | 인덱스 없이 배열의 요소에 바로 접근 | 사용가능 |  |
| forEach |  | 사용 불가능 | Airbnb Style Guide 권장 방식 |


<br>


### `map`

```jsx
array.map((element, index, array) => {
	// do something
})

const numbers = [1, 2, 3]
const doubleNumbers = numbers.map((number) => {
	return number * 2
})
console.log(doubleNumbers) // [2, 4, 6]
```

<br>


### `filter`

```jsx
array.filter((element, index, array) => {
	// do something
})

const products = [
	{ name: 'cucumber', type: 'vegetable' },
	{ name: 'banana', type: 'fruit' },
	{ name: 'carrot', type: 'vegetable' },
	{ name: 'apple', type: 'fruit' },
]

const fruits = products.filter((product) => {
	return product.type === 'fruit'
})
```

<br>


### `reduce`

- `initialValue` (optional)
    - 최소 callback 함수 호출 시 acc에 할당되는 값
    - default : 배열의 첫번째 값
    - 빈 배열일 경우 필수적으로 써야함

```jsx
array.reduce((acc, element, index, array) => {
	// do something
}, initialValue)

const tests = [90, 90, 80, 77]

const sum = tests.reduce(function (total, x) {
	return total + x
}, 0) // 0 생략 가능

const sum = tests.reduce((total, x) => total + x, 0)
const sum = tests.reduce((total, x) => total + x, 0) / test.length  // 평균
```

<br>


### `find`

- 조건을 만족하는 첫번째 요소 반환
- 찾는 값이 배열에 없으면 undefined 반환

```jsx
array.find((element, index, array)) {
	// do something
}

const avengers = [
	{ name: 'Tony Stark', age: 45 },
	{ name: 'Steve Rogers', age: 32 },
	{ name: 'Thor', age: 40 },
]

const avenger = find((avenger) => {
	return avenger.name === 'Thor' 
})
```

<br>


### `some`

- 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 true 반환
- 모든 요소가 통과하지 못하면 false 반환
- 빈 배열은 항상 false 반환

```jsx
array.some((element, index, array) => {
	// do something
})

const arr = [1, 2, 3, 4, 5]

const result = arr.some((elem) => {
	result elem % 2 === 0
})
// true
```

<br>


### `every`

- 배열의 모든 요소가 주어진 판별 함수를 통과하면 true 반환
- 하나의 요소라도 통과하지 못하면 false 반환
- 빈 배열은 항상 true 반환

```jsx
array.every((element, index, array) => {
	// do something
})

const arr = [1, 2, 3, 4, 5]

const result = arr.every((elem) => {
	result elem % 2 === 0
})
// false
```

<br>




---

# 객체 Object

- 속성property의 집합
- 중괄호 내부에 key와 value의 쌍으로 표현

### key

- 문자열 타입만 가능
- key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현

### value

- 함수 포함 모든 타입 가능

<br>


### 객체 요소 접근

- 점(.) 또는 대괄호([])로 가능
- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

---

<br>


## 객제 관련 ES6 문법

### 1. 속성명 축약

- 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 축약 가능

```jsx
const books = ['Learning Java', 'Learning Python']
const megazines = ['Vogue', 'Science']

const bookShop = {
	books,
	megazines,
}
console.log(bookShop)
/*
{
	books: ['Learning Java', 'Learning Python'],
	megazines: ['Vogue', 'Science']
}
*/
```

<br>


### 2. 메서드명 축약

- 메서드 선언 시 function 키워드 생략 가능

```jsx
const obj = {
	greeting() {
		console.log('Hi!')
	}
}

obj.greeting() // Hi!
```

<br>


### 3. 계산된 속성

- 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능

```jsx
const key = 'country'
const value = ['한국', '미국', '일본', '중국']

const myObj = {
	[key]: value
}

console.log(myObj) // {country: ['한국', '미국', '일본', '중국']}
console.log(myObj.country) // ['한국', '미국', '일본', '중국']
```

<br>


### 4. 구조 분해 할당

- 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

```jsx
const userInformation = {
	name: 'ssafy kim',
	useId: 'ssafyStudent1234',
	phoneNumber: '010-1234-1234',
	email: 'ssafy@ssafy.com'
}

const { name } = userInformation
const { userId } = userInformation
const { phoneNumber } = userInformation
const { email } = userInformation

// 여러개도 가능
const { name, userId } = userInformation
```

<br>


### 5. Spread syntax

- 배열과 마찬가지로 전개구문을 사용해 객체 내부에서 객체 전개 가능
- 얕은 복사에 활용 가능

```jsx
const obj = {b: 2, c: 3, d: 4}
const newObj = {a: 1, ...obj, e: 5}

console.log(newObj)  // {a: 1, b: 2, c: 3, d: 4, e: 5}
```


### 6. Export & Import

```jsx
// person.js
const person = {
	name:'Max'
}

export default person
```

```jsx
utility.js

export const clean = () => {}
export const baseData = 10;
```

```jsx
// app.js
import person from './person.js'
import prs from './person.js

import { baseData } from './utility.js'
import { clean as cl } from './utility.js'
import * as bundled from '.utility.js'
```

- Export : 파일 내 항목을 다른 파일로 보낼 수 있다.
    - default export (보통) : default를 사용하면 이 파일에서 export 될 기본 객체를 선언한다. import하는 파일에서 자유롭게 이름을 선언할 수 있다.
    - named export : default를 사용하지 않으면 특정 객체의 이름을 중괄호 안에 담아야 한다. as 를 활용해 자유롭게 이름을 선언할 수 있다.


<br>


## JSON

- JavaScript Object Notation
- Key-Value 형태로 이루어진 자료 표기법
- JS의 Object와 유사한 구조를 가지고 있지만 Object는 그 자체로 타입이고, JSON은 형식이 있는 “문자열”
- 즉 JSON을 Object로 사용하기 위해서는 변환 작업이 필요

```jsx
const jsObject = {
	coffee: 'Americano',
	iceCream: 'Cookie and cream',
}
```

### Object → JSON

```jsx
const objToJson = JSON.stringify(jsObject)

console.log(objToJson) // {"coffee":"Americano","iceCream":"Cookie and cream"}
console.log(typeof objToJson) // string
```

### JSON → Object

```jsx
const jsonToObj = JSON.parse(objToJson)

console.log(jsonToObj) // {coffee: 'Americano', iceCream: 'Cookie and cream'}
console.log(typeof jsonToObj) // object
```

<br>

#### 💡 배열은 객체다

<aside>


- 배열은 키와 속성들을 담고 있는 참조 타입의 객체
- 배열은 인덱스를 키로 가지며 length 프로퍼티를 갖는 특수한 객체
    
    ```jsx
    Object.getOwnPropertyDescriptors([1, 2, 3])
    
    /*
    {
    	'0': { value: 1, writable: true, enumerable: true, configurable: true },
    	'1': { value: 2, writable: true, enumerable: true, configurable: true },
    	'2': { value: 3, writable: true, enumerable: true, configurable: true },
    	length: { value: 3, writable: true, enumerable: false, configurable: false },
    }
    */
    ```
    
</aside>
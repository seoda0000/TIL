“브라우저에서의 JavaScript”

- 웹 페이지에서 다양한 기능을 구현하는 스크립트 언어
- 정적인 정보만 보여주던 웹 페이지를 데이터가 주기적으로 갱신되거나, 사용자와 상호 작용을 하거나, 애니메이션 등이 동작하게 하는 것이 가능

### Browser APIs

- 웹 브라우저에 내장된 API, 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터를 제공하거나 오디오를 재생하는 등 복잡한 일을 수행할 수 있게 함
- JavaScript로 Browser API들을 사용해서 여러가지 기능을 사용할 수 있음
- 종류
    - DOM
    - Geolocation API (지리 정보)
    - WebGL (그래픽)

# DOM

- “문서 객체 모델 Document Object Model”
- 문서의 구조화된 표현을 제공
- 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
    - 문서 구조, 스타일, 내용등을 쉽게 변경할 수 있게 도움
    - HTML 콘텐츠를 추가, 제거, 변경, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작 가능
- HTML 문서를 구조화하여 **각 요소를 객체로 취급**
- 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어
- 문서를 논리 트리로 표현
- 메서드를 사용하면 프로그래밍적 트리에 접근 → 문서의 구조, 스타일, 컨텐츠를 변경 가능
- 동일한 문서를 표현, 저장, 조작하는 방법을 제공
- DOM은 웹 페이지의 객체 지향 표현
- JavaScript와 같은 스크립트 언어를 이용해 DOM을 수정 가능

## `window` object

- DOM을 표현하는 창
- 가장 최상위 객체 (생략 가능)
- 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄

### window 메서드 예시

- 새 탭 열기 `window.open()`
- 경고 대화 상자 표시 `window.print()`
- 인쇄 대화 상자 표시 `window.alert()`

## `document` object

- 브라우저가 불러온 웹 페이지
- 페이지 컨텐츠의 진입점의 역할
- <body> 등과 같은 수많은 요소 포함

- 현재 문서의 제목 바꾸기 `document.title = 'ssafy’`

<aside>
💡 파싱 Parsing

- 구문 분석, 해석
- 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
</aside>

- DOM 조작 순서
1. 선택
2. 조작

### 선택 관련 메서드

`document.querySelector(selector)`

- 제공한 선택자와 일치하는 element 한 개 선택
- 제공한 CSS selector를 만족하는 첫번째 element 객체를 반환 (없다면 null 반환)

`document.querySelectorAll(selector)`

- 제공한 선택자와 일치하는 여러 element를 선택
- 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
- 제공한 CSS selector를 만족하는 NodeList를 반환

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a6e8f62c-d73a-45e2-83b3-c2c56f79289c/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a1af2385-7053-4ae8-adf2-ba60a29fc0c6/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d1426fe6-e108-4e64-9f3d-0ae5e6344d1b/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/90bbd965-7431-4423-a2af-ea2ec1992473/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3f0f1030-9790-4057-9c75-85e763cfa7a1/Untitled.png)

# Event

1. DOM 요소가 Event를 수신
2. 받은 Event를 처리
3. 다양한 html요소에 부착

# Event 취소

---

# `this`

- 함수가 어떻게 호출되었는지에 따라 동적으로 결정

# `this` INDEX

## 전역 문맥에서의 `this`

- 브라우저 실행 → `window`

## 함수 문맥에서의 `this`

⭐ 함수를 호출한 방법에 의해 결정됨

### 1. 단순 호출

- 전역 객체

### 2. Method

- **객체의 메서드**이므로 **해당 객체가 바인딩**

```jsx
const myObj
```

### 3. Nested (Function 키워드)

```jsx
const myObj = {
	numbers: [1],
	myFunc() {
		console.log(this)  //myObj
		this.numbers.forEach(function (number) {
			console.log(number) // 1
			console.log(this) // window
		})
	}
}
```

- forEach의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴

→ 단순 호출방식으로 사용되었기 때문

→ 해결 방법 : **화살표 함수**

```jsx
const myObj = {
	numbers: [1],
	myFunc() {
		console.log(this)  //myObj
		this.numbers.forEach((number) => {
			console.log(number) // 1
			console.log(this) // myObj
		})
	}
}

myObj.myFunc()
```

- 이전에 일반 function 키워드와 달리 메서드의 객체를 잘 가리킴
- 화살표 함수에서 this는 자신을 감싼 정적 범위
- 자동으로 한 단계 상위의 scope의 context를 바인딩

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f228d633-b8e5-4a30-b283-1c8166eedafd/Untitled.png)
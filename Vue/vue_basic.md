# Vue intro

## Front-end Framework

- Front-end 개발이란?
    - 사용자에게 보여주는 화면 만들기
- Web APP(SPA)을 만들 때 사용하는 도구
    - SPA - Single Page Application : 웹페이지가 디바이스에 설치된 App처럼 보이는 것

### SPA

- 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식을 의미
    - CSR(Client Side Rendering) 방식으로 요청을 처리
    
    <aside>
    💡 SSR (Server Side Rendering)
    
    - 서버가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식
    - 전달 받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행
    </aside>
    

## CSR (Client Side Rendering)

- 서버로부터 최초로 받아오는 문서는 빈 html 문서
- 각 요청에 대한 대응을 JS를 사용하여 필요한 부분만 다시 렌더링
1. 새로운 페이지를 서버에 AJAX로 요청
2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
3. JSON 데이터를 JS로 처리, DOM 트리에 반영(렌더링)

### Why CSR?

1. 클라이언트 - 서버간 통신, 즉 트래픽이 감소 → 빠른 응답 속도
2. 새로고침 없이 필요한 부분만 고쳐나가므로 각 요청이 끊김없이 진행
3. BE와 FE의 작업을 명확히 분리 → 협업 용이

### 단점

1. 첫 구동 시 필요한 데이터가 많으면 최초 작동 시간까지 오랜 시간 소요
2. 검색 엔진 최적화 및 노출이 어려움

<aside>
💡 SEO(Search Engine Optimization)

- 검색 엔진 등에 서비스나 제품 등이 효율적으로 노출되도록 개선하는 과정
</aside>

---

# Vue로 코드 작성하기

- template
- script
- style

[Introduction - Vue.js](https://v2.vuejs.org/v2/guide/)

```html
<body>
	<div id="app">
		<p id="name">name : {{ message }} </p>
		<input type="text" v-model="message">
	</div>
	<!-- development version, includes helpful console warnings -->
	<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
	<script>
		const app = new Vue({
			el: '#app',
			data: {
				message: '',
			},
		})
	</script>
</body>
```

1. Vue CDN 가져오기
2. Vue instance 생성
    - Vue instance - 1개의 Object
    - 정해진 속성명을 가진 Object
3. el, data 설정
    - data에 관리할 속성 정의
4. 선언적 렌더링 `{{ }}`
    - Vue data를 화면에 렌더링
5. input tag에 v-model 작성
    - input에 값 입력 → Vue data 반영
    - Vue data → DOM 반영

<aside>
💡 Dev Tools 확인

- Vue devtools에서 data변경 → DOM 반영
- 눈에 보이는 화면을 조작하는 것이 아닌 Vue가 가진 data를 조작
</aside>

---

# MVVM Pattern

- 소프트 아키텍쳐 패턴의 일종
- 마크업 언어로 구현하는 그래픽 사용자 인터페이스(view)의 개발을 Back-end(model)로부터 분리시켜 view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함

### View

- 우리 눈에 보이는 부분 = DOM

### Model

- 실제 데이터 = JSON

### View Model (Vue)

- View를 위한 Model
- View와 연결binding되어 Action을 주고 받음
- Nodel이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
- View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨

### 독립성 증가, 적은 의존성

- View는 Model을 모름. Model도 View를 모름.
- DOM은 Data를 모름. Data도 DOM 모름.

---

# Vue instance

- Vue instance === 1개의 객체
- 아주 많은 속성과 메서드를 이미 가지고 있음

```html
<body>
	<!-- development version, includes helpful console warnings -->
	<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
	<script>
		const vm = new Vue()
		console.log(vm)
	</script>
</body>
```

<aside>
💡 생성자 함수

- new 연산자로 사용하는 함수
- 함수 이름은 반드시 대문자로 시작

```jsx
function Member(name, age, sId) {
	this.name = name
	this.age = age
	this.sId = sId
}

const member3 = new Member('isaac', 21, 2022654321)
```

</aside>

## `el` (element)

- Vue instance와 DOM을 연결mount하는 옵션
    - View와 Model을 연결하는 역할
    - HTML id, class와 마운트 가능
- Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음
    - Vue 속성 및 메서드 사용 불가

## `data`

- Vue instance의 데이터 객체 혹은 인스턴스 속성
- 데이터 객체는 반드시 기본 객체 `{ }` (Object)여야 함
- 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음
- 정의된 속성은 interpolation `{{}}`을 통해 view에 렌더링 가능
- 추가된 객체의 각 값들은 `this.message` 형태로 접근 가능

```html
<div id="app">
	{{ message }}
</div>
...
<script>
	const app = new Vue({
		el: '#app',
		data: {
			message: 'Hello, Vue!'
		}
	})
	console.log(app)
</script>
```

## `methods`

- Vue instance의 method들을 정의하는 곳
- 콘솔창에서 실행 가능 ex) `app.print()`
- DOM에 바로 반영 → Vue의 강력한 반응성

🚧 메서드를 **정의**할 때, Arrow Function을 사용하면 안됨

- `this`가 상위 객체 `window`를 가리킨다.
- 내부에서는 사용 가능

```jsx
...
    const app = new Vue({
      el: '#app',
      // 3. data
      data: {
        message: 'Hello, Vue!'
      },

      // 4. methods
      methods: {
        print: function () {
          console.log(this.message) // this.$data.message
        },

        bye: function () {
          this.message = 'Bye, Vue!'
        },

        // 4-1. arrow function
        arrowBye: () => {
          this.message = 'Arrow Function?'
          console.log(this)
        }
      }
    })
    console.log(app)
  </script>
```

---

# Basic of syntax

## Template Syntax

[Template Syntax - Vue.js](https://v2.vuejs.org/v2/guide/syntax.html)

- **렌더링 된 DOM**을 기본 Vue instance의 data에 **선언적으로 바인딩**할 수 있는 **HTML 기반 template syntax**
    - 렌더링 된 DOM : 브라우저에 의해 보기 좋게 그려질 HTML 코드
    - 선언적으로 바인딩 : Vue instance와 DOM을 연결
    - HTML 기반 template syntax : HTML 코드에 직접 작성할 수 있는 문법 제공

## Template Interpolation

- RAW HTML, JS 표현식 등 가능

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/92d92cf6-45fb-46ae-ace5-9de81569082b/Untitled.png)

```jsx
<body>
  <!-- 1. Text interpolation -->
  <div id="app">
    <p>메시지: {{ msg }}</p>   
    <p>HTML 메시지 : {{ rawHTML }}</p>
    <p>HTML 메시지 : <span v-html="rawHTML"></span></p>
    <p>{{ msg.split('').reverse().join('') }}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    // 1. Text interpolation
    const app = new Vue({
      el: '#app',
      data: {
        msg: 'Text interpolation',
        rawHTML: '<span style="color:red"> 빨간 글씨</span>'
      }
    })
  </script>
</body>
```

---

# Directives

## 기본 구성

- v-접두사가 있는 특수 속성에는 값을 할당할 수 있음
    - 값에는 JS 표현식을 작성할 수 있음
- 역할 : 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것

## `v-on:submit.prevent="onSubmit"`

- `v-on` : Name
- `submit` : Argument
- `prevent` : Modifiers
- `onSubmit` : Value
- `:` 을 통해 전달인자를 받을 수 있음
- `.` 로 표현되는 특수 접미사 -directive를 특별한 방법으로 바인딩 해야 함

## `v-text`

- {{ }} 와 동일한 역할

## `v-html`

- RAW HTML을 표현할 수 있는 방법

🚧 사용자가 입력, 제공하는 컨텐츠에는 절대 사용 금지 (XSS 공격 참고)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7861870-a40e-4e4e-bc9e-90539de17043/Untitled.png)

```jsx
<body>
	<!-- 2. v-text & v-html -->
  <div id="app2">
    <!-- 2-1. v-text & {{}} -->
    <p v-text="message"></p>
    <!-- 같음 -->
    <p>{{ message }}</p>

    <!-- 2-2. v-html -->
    <p v-html="html"></p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
		// 2. v-text && v-html
    const app2 = new Vue({
      el: '#app2',
      data: {
        message: 'Hello!',
        html: '<a href="https://www.google.com">GOOGLE</a>'
      }
    })
  </script>
</body>
```

## `v-show`

- 표현식에 작성된 값에 따라 element를 보여 줄 것인지 결정
    - boolean 값이 변경될 때마다 반응
- 대상 element의 display 속성을 기본 속성과 none으로 toggle
- **요소 자체는 항상 DOM에 렌더링 됨**

## `v-if`

- `v-show`와 사용방법 동일
- **단, 값이 false인 경우 DOM에서 사라짐**
- `v-if` `v-else-if` `v-else` 형태

```jsx
<div id="app3">
    <p v-show="isActive">보이니? 안보이니?</p>
    <p v-if="isActive">안보이니? 보이니?</p>
</div>
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    // 3. v-show && v-if
    const app3 = new Vue({
      el: '#app3',
      data: {
        isActive: false // true면 보임
      }
    })
</script>
```

### v-show VS v-if

- v-show
    - Expensive initial load, cheap toggle
- v-if
    - Cheap initial load, expensive toggle

## v-for

- `for .. in ..` 형식
- 반복한 데이터 타입에 모두 사용 가능
- (char, index) : index를 함께 출력
- 각 요소가 객체라면 dot notation으로 접근 가능

```jsx
<body>
  <!-- 3. v-for -->
  <div id="app">
    <h2>String</h2>
    <div v-for="char in myStr">
      {{ char }}
    </div>
    <div v-for="(char, index) in myStr" :key="index">
      <p>{{ index }}번째 문자열 {{ char }}</p>
    </div>

    <h2>Array</h2>
    <div v-for="(item, index) in myArr" :key="index">
      <p>{{ index }}번째 아이템 {{ item }}</p>
    </div>

    <div v-for="(item, index) in myArr2" :key="`arry-${index}`">
      <p>{{ index }}번째 아이템</p>
		  <p>{{ item.name }}</p>
    </div>

    <h2>Object</h2>
    <div v-for="value in myObj">
      <p>{{ value }}</p>
    </div>

    <div v-for="(value, key) in myObj"  :key="key">
      <p>{{ key }} : {{ value }}</p>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        // 1. String
        myStr: 'Hello, World!',

        // 2-1. Array
        myArr: ['python', 'django', 'vue.js'],

        // 2-2. Array with Object
        myArr2: [
          { id: 1, name: 'python', completed: true},
          { id: 2, name: 'django', completed: true},
          { id: 3, name: 'vue.js', completed: false},
			  ],
        
        // 3. Object
        myObj: {
          name: 'harry',
          age: 27
        },
      }
    })
  </script>
</body>
```

### 특수속성 key

🚧 **v-for 사용 시 반드시 key 속성을 각 요소에 작성**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c3917488-7be1-4459-b8f9-12f2686a72bd/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4b693562-e651-4dc4-81ca-50cf375bbb18/Untitled.png)

## v-on

축약어 : `@`

## v-bind

축약어 : `:`

```jsx

<div id="app2">
    <a v-bind:href="url">Go To GOOGLE</a>  // url <- 문자열 아님!! JS의 공간

    <p v-bind:class="redTextClass">빨간 글씨</p>
    <p v-bind:class="{ 'red-text': true }">빨간 글씨</p>
    <p v-bind:class="[redTextClass, borderBlack]">빨간 글씨, 검은 테두리</p>

    <p :class="theme">상황에 따른 활성화</p>
    <button @click="darkModeToggle">dark Mode {{ isActive }}</button>
  </div>
...
<script>
	const app2 = new Vue({
      el: '#app2',
      data: {
        url: 'https://www.google.com/',
        redTextClass: 'red-text',
        borderBlack: 'border-black',
        isActive: true,
        theme: 'dark-mode'
      },
	})
</script>
```

## v-model

- 양방향 바인딩
- 한중일은 조합형 문자라 한박자 늦음

```jsx
<body>
  <div id="app">
    <h2>1. Input -> Data</h2>
    <h3>{{ myMessage }}</h3>
    <input @input="onInputChange" type="text">
    <hr>

    <h2>2. Input <-> Data</h2>
    <h3>{{ myMessage2 }}</h3>
    <input v-model="myMessage2" type="text">
    <hr>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        myMessage: '',
        myMessage2: '',
      },
      methods: {
        onInputChange: function (event) {
          this.myMessage = event.target.value
        },
      }
    })
  </script>
</body>
```
# 리액트와 뷰의 비교

|  | 리액트 | 뷰 |
| --- | --- | --- |
| 정의 | 자바스크립트 UI 라이브러리 | 자바스크립트 프레임워크 |
| 부분 사용 | 필요한 라이브러리만 사용 | 부분적인 사용이 불가능 |
| 자유도 | 개발자가 자유롭게 개발 | 프레임 워크가 지원해주는 문법에 따라 작성 |
| 디폴트 제공 | 리액트 자체만으로는 전역 상태 관리, 라우팅, 빌드 시스템 등을 지원하지 않음 (별도의 라이브러리 필요) | 라이브러리와 달리 더 많은 기능을 디폴트로 제공 |
| 문법 | JSX(JavaScript XML) 형태로 코드를 작성 | HTML, JS, CSS 코드 영역을 분리해서 작성 |
| 구조 | JavaScript만으로 UI 로직과 DOM을 구현 | <template>에 HTML 작성 영역, <script> 안에는 JS, <style> 안에 CSS를 작성 |
| 컴포넌트 및 재사용 | 컴포넌트의 생성 및 재사용. 파일별로 컴포넌트를 분리 가능, 새로운 함수형 컴포넌트를 생산에 용이 | 새로운 컴포넌트를 위해 새로운 파일(template, script, style 구성)을 하나 필요.  |
| props | props 형태로 전달 / 다른 곳에서 재사용 용이 | props 전달 시 해당 컴포넌트를 사용하는 모든 파일에 작성 |
| 장점 | 타입 스크립트 사용 용이 | 리액트보다 살짝 빠름 |

---

# 리액트 시작하기

```jsx
npx create-react-app { app 이름 }
cd { app 이름 } 
npm start
```

---

# 리액트 기본 구조

## index.js

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App'; // 자바 스크립트 파일의 경우 확장자 생략 가능

ReactDOM.render(<App />, document.getElementById('root')); 
```


### `render(jsx 구문, 어느 부분에 랜더링 해야 하는지)`

- JS 내의 HTML 구문은 빌드 단계에서만 가능하다. (jsx구문)
- 브라우저는 App을 보여주지 않는다. App이 return하는 HTML Tag를 보여준다.
- root : index에서 ID로 찾을 수 있다.

## App.js

### 리액트 컴포넌트

- 자바스크립트 함수 형식
- jsx코드(HTML처럼 보인다)를 return

```jsx
function App() {
  return <div>Hello!</div>;
}

export default App;
```

# 스타일 적용하기

### CSS 파일 import

`import './index.css';`

### class 선언

`<div className="card"> // HTML의 class`

---

# 컴포넌트

## App.js

### `<Componet key="value"/>`

- 컴포넌트로 데이터 넘겨주기 : props 객체

```jsx
import Todo from "./components/Todo";
function App() {
  return <div>
    <h1>My Todos</h1>
    <Todo text="Learn React"/> 
    <Todo text="Master React"/>
    <Todo text="Explore React"/>
  </div>; 
} 

export default App;
```

## Todo.js

### `{props.key}`

- props : 자바스크립트 객체. 함수의 변수로 받음.
- {} 안은 리액트가 자바스크립트로 인식

```jsx

function Todo(props) { 

  return (
    <div className="card">
      <h2>{ props.text }</h2>
      <div className="actions">
        <button className="btn">Delete</button>
      </div>
    </div>
  )
}

export default Todo;
```

---

# 이벤트 적용

## 패키지 import

### `import { useState } from 'react';`

## 리액트 훅 선언

- 리액트 훅. 컴포넌트 함수나 커스텀 훅 안에서 바로 호출되어야 한다.
- 항상 두가지 요소를 가진 배열로 표현된다.

### `const [ 현재 상태의 스냅샷, state값을 변경할 수 있는 함수 ] = useState(초기값);`

- 첫번째 값 : 현재 상태의 스냅샷
- 두번째 값 : state값을 변경할 수 있는 함수. 이 함수가 호출될 때마다 해당 컴포넌트 함수가 재실행된다.

## 함수 정의

- 컴포넌트 내부에서 함수 정의
- 리액트 훅의 두번째 값 (함수)를 활용

```jsx
import { useState } from 'react';

import Modal from './Modal';
import Backdrop from './Backdrop';

function Todo(props) { 
  const [ modalIsOpen, setModalIsOpen ] = useState(false);

  function deleteHandler() {
    setModalIsOpen(true);
  }

  function closeModalHandler() {
    setModalIsOpen(false);
  }

  return (
    <div className="card">
      <h2>{ props.text }</h2>
      <div className="actions">
        <button className="btn" onClick={deleteHandler}>Delete</button>
      </div>
      { modalIsOpen && (
        <Modal onCancel={closeModalHandler} onConfirm={closeModalHandler} />
      )}
      { modalIsOpen && <Backdrop onCancel={closeModalHandler} /> }
    </div>
  )
}

export default Todo;
```

## 함수 및 변수 활용

### `<컴포넌트 이벤트={함수} />`

- 컴포넌트 내부에 함수를 쓸 때는 ( ) 생략. ( )를 붙이면 코드를 검증되는 순간에 실행된다. 생략해야 특정 조건에 실행될 수 있다.

### `{ modalIsOpen ? <Modal /> : null }`
`{ modalIsOpen && <Modal /> }`

- 변수 값에 따라 컴포넌트 띄우고 없애기

## 사용자 정의 컴포넌트에서의 활용

### `<컴포넌트 이벤트={함수} />`

- 이벤트와 함수를 정의해주어야 한다.
- 이벤트도 props로 넘긴다고 생각하면 된다.

### `function 컴포넌트내부함수() { props.함수() };`

```jsx
function Modal(props) {

    function cancelHandler() {
        props.onCancel();
    };
    function confirmHandler() {
        props.onConfirm();
    };
    return (
    <div className="modal">
        <p>Are you sure?</p>
        <button className="btn btn--alt" onClick={cancelHandler}>Cancel</button>
        <button className="btn" onClick={confirmHandler}>Confirm</button>
    </div>
    );
}

export default Modal;
```

- 함수 정의 후 요소에 이벤트로 적용해준다.


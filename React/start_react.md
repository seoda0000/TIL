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

### `render(HTML 구문, 어느 부분에 랜더링 해야 하는지)`

- JS 내의 HTML 구문은 빌드 단계에서만 가능하다. (jsx구문)
- 브라우저는 App을 보여주지 않는다. App이 return하는 HTML Tag를 보여준다.
- root : index에서 ID로 찾을 수 있다.

## App.js

### 리액트 컴포넌트

- 자바스크립트 함수 형식
- jsx코드(HTML)를 return

```jsx
function App() {
  return <div>Hello!</div>;
}

export default App;
```

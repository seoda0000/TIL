import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App'; // 자바 스크립트 파일의 경우 확장자 생략 가능


ReactDOM.render(<App />, document.getElementById('root')); 
// JS 내의 HTML 구문은 빌드 단계에서만 가능하다. (jsx구문)
// render(HTML 구문, 어느 부분에 랜더링 해야 하는지)
// 브라우저는 App을 보여주지 않는다. App이 return하는 HTML Tag를 보여준다.

// root : index에서 ID로 찾을 수 있다.


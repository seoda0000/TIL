import { useState } from 'react';

import Modal from './Modal';
import Backdrop from './Backdrop';

function Todo(props) { // props는 객체
  const [ modalIsOpen, setModalIsOpen ] = useState(false); // 초기값 설정
  // 리액트 훅. 컴포넌트 함수나 커스텀 훅 안에서 바로 호출되어야 한다.
  // 항상 두가지 요소를 가진 배열로 표현된다.
  // 첫번째 값 : 현재 상태의 스냅샷
  // 두번째 값 : state값을 변경할 수 있는 함수. 이 함수가 호출될 때마다 해당 컴포넌틓 함수가 재실행된다.

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
// HTML처럼 보이지만 리액트 객체. 속성을 정의할 수 있다.
// ()를 붙이면 코드를 검증되는 순간에 실행된다.
// { modalIsOpen ? <Modal /> : null }
// { modalIsOpen && <Modal /> }
export default Todo;
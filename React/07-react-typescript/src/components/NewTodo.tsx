import React, { useRef } from "react";

const NewTodo: React.FC<{ onAddTodo: (text: string) => void }> = (props) => {
  const todoTextInputRef = useRef<HTMLInputElement>(null);

  const submitHandler = (event: React.FormEvent) => {
    // 제출 시 발생하는 이벤트
    event.preventDefault();

    const enteredText = todoTextInputRef.current!.value;
    // 물음표 : 값이 정의되지 않은 시점까지 고려
    // 느낌표 : null이 아니라는 걸 확신

    if (enteredText?.trim().length === 0) {
      // throw an error
      return;
    }

    props.onAddTodo(enteredText);
  };

  return (
    <form onSubmit={submitHandler}>
      <label htmlFor="text">Todo text</label>
      <input type="text" id="text" ref={todoTextInputRef} />
      <button>Add Todo</button>
    </form>
  );
};

export default NewTodo;

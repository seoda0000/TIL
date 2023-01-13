import React from "react";
import Todo from "../models/todo";
import TodoItem from "./TodoItem";

const Todos: React.FC<{ items: Todo[] }> = (props) => {
  // {}를 이용해 FC의 기능을 밖으로 꺼냄. 어떤 객체 타입을 입력하든 기본 객체 타입인 children과 합쳐줌
  return (
    <ul>
      {props.items.map((item) => (
        <TodoItem item={item} />
      ))}
    </ul>
  );
};

export default Todos;

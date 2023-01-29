import React from "react";
import Todo from "../models/todo";

const TodoItem: React.FC<{
  item: Todo;
  onRemoveTodo: () => void;
}> = (props) => {
  return <li onClick={props.onRemoveTodo}>{props.item.text}</li>;
};

export default TodoItem;

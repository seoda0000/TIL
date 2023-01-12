import React from "react";

const Todos: React.FC<{}> = (props) => {
  return <ul>{props.children}</ul>;
};

export default Todos;

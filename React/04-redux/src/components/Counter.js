import { useSelector, useDispatch } from "react-redux";
// useSelector : 저장소가 관리하는 상태 부분을 자동으로 선택/구독

import classes from "./Counter.module.css";

const Counter = () => {
  // 컴포넌트 삭제 시 자동으로 구독 취소

  const dispatch = useDispatch();
  const counter = useSelector((state) => state.counter); // 저장소에서 추출하려는 데이터 선택
  const show = useSelector((state) => state.showCounter);

  const incrementHandler = () => {
    dispatch({ type: "increment" });
  };
  const increaseHandler = () => {
    dispatch({ type: "increase", amount: 5 }); // action payload 추가 가능
  };
  const decrementHandler = () => {
    dispatch({ type: "decrement" });
  };

  const toggleCounterHandler = () => {
    dispatch({ type: "toggle" });
  };

  return (
    <main className={classes.counter}>
      <h1>Redux Counter</h1>
      {show && <div className={classes.value}>{counter}</div>}
      <div>
        <button onClick={incrementHandler}>Increment</button>
        <button onClick={increaseHandler}>Increase by 5</button>
        <button onClick={decrementHandler}>Decrement</button>
      </div>
      <button onClick={toggleCounterHandler}>Toggle Counter</button>
    </main>
  );
};

export default Counter;

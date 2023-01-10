const redux = require("redux");

// Reducer 함수. [예전 상태, 상태를 dispatch하는 함수] -> 새로운 상태 객체를 반환.
const counterReducer = (state = { counter: 0 }, action) => {
  // 처음으로 호출될 때 한번 실행됨
  if (action.type === "increment") {
    return {
      counter: state.counter + 1,
    };
  }

  if (action.type === "decrement") {
    return {
      counter: state.counter - 1,
    };
  }

  return state;
};

const store = redux.createStore(counterReducer); // createStore가 대체됨
// 어떤 Reducer 함수가 어떤 저장소를 변화하는지 넣어줌

// store을 구독하는 컴포넌트 생성
const counterSubscriber = () => {
  const latestState = store.getState(); // store가 변화할 때마다 store의 최신상태 스냅샷 제공
  console.log(latestState);
};

store.subscribe(counterSubscriber); // 리덕스에게 함수의 존재를 알려줌. 상태가 변경될 때마다 이 함수가 실행되도록 함.

store.dispatch({ type: "increment" }); // 고유한 문자열로 타입을 지정해야 함.dispatch를 해서 데이터 변화.
store.dispatch({ type: "decrement" });

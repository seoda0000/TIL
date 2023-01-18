import { configureStore } from "@reduxjs/toolkit";
import authReducer from "./auth";
import counterReducer from "./counter";

const store = configureStore({
  reducer: { counter: counterReducer, auth: authReducer },
}); // 여러 리듀서 통합

export default store;

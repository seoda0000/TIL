import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: []
  },
  getters: {
    todosCount(state) {
      return state.todos.length
    },
    completedCount(state) {
      return state.todos.filter((todo)=>{
        return todo.isCompleted === true
      }).length
    }
  },
  mutations: {
    CREATE_TODO (state, newTodo) {
      state.todos.push(newTodo)
    },
    CHECK_TODO (state, todo) {
      const idx = state.todos.indexOf(todo)
      state.todos[idx].isCompleted = !state.todos[idx].isCompleted
    },
    DELETE_TODO (state, todo) {
      const idx = state.todos.indexOf(todo)
      state.todos.splice(idx, 1)
    },
  },
  actions: {
    createTodo(context, newTodo) {
      context.commit('CREATE_TODO', newTodo)
    },
    checkTodo(context, todo) {
      context.commit('CHECK_TODO', todo)
    },
    deleteTodo(context, todo) {
      context.commit('DELETE_TODO', todo)
    },
    saveTodosToLocalStorage(context) {
      const jsonTodos = JSON.stringify(context.state.todos)
      localStorage.setItem('todos', jsonTodos)
    }
  },
  modules: {
  }
})

<template>
  <div id="app" style="margin: auto;">
    <div
    style="
      width: 260px;
      border: 3px solid black;
      padding: 25px;
      align-items: center;
      margin: auto;"
    >
    <h1 class="title">Todo List</h1>
    <h4 class="title2">All Todos : {{ todosCount }}</h4>
    <h5 class="title3">completed : {{ completedCount }}    |     uncompleted : {{ todosCount-completedCount }}</h5>
    <br>
    <TodoList/>
    <br>
    <TodoForm/>
  </div>
</div>
</template>

<script>
import TodoForm from './components/TodoForm.vue';
import TodoList from './components/TodoList.vue';


export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList
  },
  computed: {
    todosCount() {
      return this.$store.getters.todosCount
    },
    completedCount() {
      return this.$store.getters.completedCount
    }
  },
  created() {
    
  }
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');
  #app {
    font-family: 'Nanum Gothic', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  .title {
    font-family: 'Montserrat', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    font-weight: bold;
    text-align: center;
    color: #2c3e50;
    margin-top: 40px;

  }

  .title2 {
    font-family: 'Montserrat', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    font-weight: bold;
    text-align: center;
    color: #2c3e50;
  }

  .title3 {
    font-family: 'Montserrat', sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  
</style>

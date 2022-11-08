<template>
  <div>
    <div v-for="(todo, index) in todos" :key="index" align="left" class="box">
      <TodoListItem :todo="todo"/>
      <br>
    </div>
  </div>
</template>

<script>
import TodoListItem from './TodoListItem.vue';

export default {
  name: 'TodoList',
  components: {
    TodoListItem
  },
  computed: {
    todos() {
      return this.$store.state.todos
    }
  }

}
</script>

<style>
  .box {
    border-color:black;
    border-width: 3px;
  }

</style>
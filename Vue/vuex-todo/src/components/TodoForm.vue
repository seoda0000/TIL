<template>
  <div>
    <input 
      type="text"
      v-model="inputData"
      @keyup.enter="createTodo"
      style="margin-right:10px; width: 215px;"
    >
    <button @click="createTodo" class="plus">
      +
    </button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    createTodo() {
      if (this.inputData.trim()) {
        const newTodo = {
          'title': this.inputData.trim(),
          'isCompleted': false
        }
        this.$store.dispatch('createTodo', newTodo)
        this.inputData = null
      }
    }

  }
}
</script>

<style>
.plus {
    background-color: white;
    border-color: black;
    border-radius: 4px;
    cursor: pointer;
    color: black;
    border-width: 1px;
}

</style>
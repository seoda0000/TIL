<script src="https://kit.fontawesome.com/3120ef72b0.js" crossorigin="anonymous"></script>
<template>
  <div>
    <font-awesome-icon v-if="!todo.isCompleted" icon="fa-regular fa-kiss" style="margin-right:10px"/>
    <font-awesome-icon v-if="todo.isCompleted" icon="fa-regular fa-thumbs-up" style="margin-right:10px"/>
    <span
      :class="{ 'is-completed': todo.isCompleted }"
      style="
        margin-right:10px;
        width: 205px;
        display:inline-block;
        "
      @click="checkTodo"
      id="font-face"
    >
    {{ todo.title }}
    </span>
    <button
      class="xxx"
      style="align-self=center;"
      @click="deleteTodo"
    >
    x
    </button>
    <hr>
  </div>
</template>

<script>
import Vue from 'vue'
/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faKiss } from '@fortawesome/free-regular-svg-icons'
import { faThumbsUp } from '@fortawesome/free-regular-svg-icons'

/* add icons to the library */
library.add(faKiss)
library.add(faThumbsUp)

/* add font awesome icon component */
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false



export default {
  name: 'TodoListItem',
  props: {
    todo: Object
  },
  methods: {
    checkTodo() {
      this.$store.dispatch('checkTodo', this.todo)
    },
    deleteTodo() {
      this.$store.dispatch('deleteTodo', this.todo)
    }
  }

}
</script>

<style>
  .xxx {
    background-color: black;
    border-color: white;
    border-radius: 4px;
    cursor: pointer;
    color: white;
    border-width: 1px;
  }

  .is-completed {
    text-decoration: line-through;
  }

</style>
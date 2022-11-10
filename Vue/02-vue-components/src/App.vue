<template>
  <div id="app">
    <TheLunch @choose-lunch="chooseLunch"/>
    <h1>{{ lunch }}</h1>
    <hr>
    <TheLotto :lunch="lunch"/>
  </div>
</template>

<script>
import TheLunch from './components/TheLunch.vue';
import TheLotto from './components/TheLotto.vue';
export default {
  name: 'App',
  components: {
    TheLunch,
    TheLotto,
  },
  data: function() {
    return {
      lunch: ''

    }
  },
  props: {

  },
  methods: {
    chooseLunch: function(menu) {
      this.lunch = menu
    }
  }
}
</script>

<style>

</style>

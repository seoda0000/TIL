<template>
  <div>
    <h1>점심 메뉴</h1>
    <button @click="chooseLunch">Pick One</button>
  </div>
  
</template>

<script>
export default {
  name: 'TheLunch',
  data: function() {
    return {
      lunch: ['국밥' , '짜장면' , '햄버거'],

    }
  },
  methods: {
    chooseLunch: function () {
      let random_index = Math.floor(Math.random() * 3);
      let menu = this.lunch[random_index]
      this.$emit('choose-lunch', menu)

    }
  }

}
</script>

<style>

</style>
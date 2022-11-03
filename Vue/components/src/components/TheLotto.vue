<template>
  <div>
    <h1>{{ lunch }} 먹고 로또</h1>
    <button @click="lotto">Get Lucky Numbers</button>
    {{ lotto_number }}
  </div>
  
</template>

<script>
export default {
  name: 'TheLotto',
  props: {
    lunch: String
  },
  data: function() {
    return {
      lotto_number: ''
    }
  },
  methods: {
    lotto: function () {
      this.lotto_number = _.sampleSize(_.range(1, 46), 6)
    }
  }
}
</script>

<style>

</style>
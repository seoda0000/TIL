<template>
  <li @click="clickVideo">
    <img :src="video.snippet.thumbnails.default.url" alt="">
    {{ video.snippet.title }}
  </li>
</template>

<script>

export default {
  name: 'VideoListItem',
  data: function() {
    return {
    }
  },
  props: {
    video: Object,
  },
  methods: {
    clickVideo: function() {
      this.$emit('click-video', this.video)
    }
  }

}
</script>

<style>

</style>
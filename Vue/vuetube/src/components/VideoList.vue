<template>
  <div>
    <ul v-for="(video, idx) in videos" :key="idx">
      <VideoListItem
        :video="video"
        @click-video="clickVideo"
      />
    </ul>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem
  },
  props: {
    videos: Array
  },
  methods: {
    clickVideo: function(videoNow) {
      this.$emit('click-video', videoNow)
    }
  }

}
</script>

<style>

</style>
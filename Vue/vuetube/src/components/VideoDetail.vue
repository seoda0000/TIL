<template>
  <div>
    <br>
    <iframe width="560" height="315" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
    :src="'https://www.youtube.com/embed/' + videoNow.id.videoId"></iframe>
    <h3>{{ videoNow.snippet.title }}</h3>
    <p>{{ videoNow.snippet.description }}</p>
    
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    videoNow: Object
  }
}
</script>

<style>

</style>
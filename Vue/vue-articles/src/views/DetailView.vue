<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>글 제목 : {{ article?.title }}</p>
    <p>글 내용 : {{ article?.content }}</p>
    <p>글 작성시간 : {{ articleCreatedAt }}</p>
    <button @click="deleteArticle">삭제</button>
    <router-link :to="{ name: 'index'}">뒤로 가기</router-link>
  </div>
</template>

<script>
export default {
  name: 'DetailView',
  data() {
    return {
      article: null,
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
    articleCreatedAt() {
      const article = this.article
      const createdAt = new Date(article?.createdAt).toLocaleString()
      return createdAt
    }
  },
  methods: {
    getArticleById(id) {
      // console.log(this.articles)
      // const id = this.$route.params.id
      for (const article of this.articles) {
        if (article.id === Number(id)) {
          this.article = article
          break
        }
      }
      if (this.article === null) {
        this.$router.push({ name: 'NotFound404' })
        
      }
    },
    deleteArticle() {
      this.$store.commit('DELETE_ARTICLE', this.article.id)
      this.$router.push({ name: 'index' })
    }
  },
  created() {
    this.getArticleById(this.$route.params.id)
  }

}
</script>

<style>

</style>
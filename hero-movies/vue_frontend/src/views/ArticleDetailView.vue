<template>
  <div>
    <h1>{{ article.title }}</h1>
    <!-- 일단 최신목록, 나중에 보던 페이지 목록으로 가는거 해보자 -->
    <router-link :to="{ name: 'community' }">최신목록</router-link>
    <p>
      {{ article.content }}
    </p>
    <!-- Article Edit/Delete UI -->
    <div v-if="isAuthor">
    <!-- <div> -->
      <router-link :to="{ name: 'articleEdit', params: { articleId } }">
        수정
      </router-link>
      |
      <button @click="deleteArticle(articleId)">삭제</button>
    </div>

    <!-- Article Like UI -->
    <!-- <div>
      Likeit:
      <button
        @click="likeArticle(articleId)"
      >
      {{ likeCount }}
      </button>
    </div> -->

    <hr />
    <!-- Comment UI -->
    <comment-list :comments="article.comments"></comment-list>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'

  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articleId: this.$route.params.articleId,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
      // ...mapGetters(['article']),
      // likeCount() {
      //   return this.article.like_users?.length
      // }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articleId)
    },
  }
</script>

<style></style>

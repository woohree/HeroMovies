<template>
  <div>
    <div class="d-flex flex-column align-items-center">
      <div>
        <h1>자유게시판</h1>
      </div>
      <div>
        <router-link :to="{ name: 'reviewList' }" class="community-next-title">리뷰게시판</router-link>
      </div>
    </div>

    <!-- 
      게시글 10개씩 출력 + 페이지네이터 
      글 번호 / 제목 / 작성자 / 작성시간 / 추천 수
      -->
    <div class="container">
      <div class="mb-3 d-flex article-create-btn">
        <router-link class="text-decoration-none" :to="{ name: 'articleNew' }"><v-btn>글쓰기</v-btn></router-link>
      </div>
      <div class="row" v-for="article in articles" :key="article.id">
        <div class="col-1">
          {{ article.id }}
        </div>
        <div class="col">
          <router-link 
            class="article-title"
            :to="{ name: 'articleDetail', params: {articleId: article.id} }">
            {{ article.title }}
          </router-link>
        </div>
        <div class="col-2">
          <router-link class="article-title" :to="{ name: 'profile', params: { userId: article.user.id} }">
            {{ article.user.username }}

          </router-link>
        </div>
        <div class="col-2 ms-auto">
          {{ article.created_at | dateFormat("MM-DD HH:mm") }}
           <!-- | dateFormat("YY-MM-DD HH:mm") -->
        </div>
      </div>
    </div>

    <div class="text-center">
      <v-pagination
        v-model="page"
        color="#033"
        :length="parseInt((len-1)/10)+1"
        :total-visible="7"
        prev-icon="mdi-menu-left"
        next-icon="mdi-menu-right"
        @click.native="fetchArticles(page)"
      ></v-pagination>
    </div>
   
  </div>
</template>

<script>
  import moment from "moment"
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'CommunityView',
    data() {
      return {
        page: 1,
      }
    },
    computed: {
      ...mapGetters(['articles', 'len'])
    },
    methods: {
      ...mapActions(['fetchArticles', 'fetchArticlesLength'])
    },
    filters: {
      dateFormat: function(val, format) {
        return moment(val).format(format);
      }
    },
    created() {
      this.fetchArticles(this.page),
      this.fetchArticlesLength()
    },

  }
</script>

<style>
  .community-next-title {
    color: black;
    text-decoration-line: none;
  }
  .community-next-title:hover {
    text-decoration-line: underline;
    color: rgb(26, 87, 84);
  }
  .article-create-btn {
    margin-left: 90%;
  }
  .article-title:hover {
    text-decoration-line: underline;
    color: rgb(26, 87, 84);
  }
  .article-title {
    text-decoration-line: none;
    color: black;
  }
</style>

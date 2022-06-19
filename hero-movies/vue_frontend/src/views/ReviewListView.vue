<template>
  <div>
    <div class="d-flex flex-column align-items-center">
      <div>
        <h1>리뷰게시판</h1>
      </div>
      <div>
        <router-link :to="{ name: 'community' }" class="review-next-title">자유게시판</router-link>
      </div>
    </div>

    <div class="container">
      <!-- <div class="mb-3 d-flex review-create-btn">
        <router-link class="text-decoration-none" :to="{ name: 'reviewNew' }"><v-btn>리뷰쓰기</v-btn></router-link>
      </div> -->
      <div class="row" v-for="review in reviews" :key="review.id">
        <div class="col-1">
          {{ review.id }}
        </div>
        <div class="col-3">
          {{ review.reviewed_movie.title }}
        </div>
        <div class="col">
          <router-link 
            class="review-title"
            :to="{ name: 'reviewDetail', params: {reviewId: review.id} }">
            {{ review.title }}
          </router-link>
        </div>
        <div class="col-2">
          <router-link class="article-title" :to="{ name: 'profile', params: { userId: review.user.id} }">
            {{ review.user.username }}

          </router-link>
        </div>
        <div class="col-2 ms-auto">
          {{ review.created_at | dateFormat("MM-DD HH:mm") }}
           <!-- | dateFormat("YY-MM-DD HH:mm") -->
        </div>
      </div>
    </div>

    <div class="text-center">
      <v-pagination
        v-model="page"
        color="#033"
        :length="parseInt((lenReviews-1)/10)+1"
        :total-visible="7"
        prev-icon="mdi-menu-left"
        next-icon="mdi-menu-right"
        @click.native="fetchReviews(page)"
      ></v-pagination>
    </div>
   
  </div>
</template>

<script>
  import moment from "moment"
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ReviewListView',
    data() {
      return {
        page: 1,
      }
    },
    computed: {
      ...mapGetters(['reviews', 'lenReviews'])
    },
    methods: {
      ...mapActions(['fetchReviews', 'fetchReviewsLength'])
    },
    filters: {
      dateFormat: function(val, format) {
        return moment(val).format(format);
      }
    },
    created() {
      this.fetchReviews(this.page)
      this.fetchReviewsLength()
    },

  }
</script>

<style>
  .review-next-title {
    color: black;
    text-decoration-line: none;
  }
  .review-next-title:hover {
    text-decoration-line: underline;
    color: rgb(26, 87, 84);
  }
  .review-create-btn {
    margin-left: 90%;
  }
  .review-title:hover {
    text-decoration-line: underline;
    color: rgb(26, 87, 84);
  }
  .review-title {
    text-decoration-line: none;
    color: black;
  }
</style>

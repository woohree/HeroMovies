<template>
  <div>
    <h1>{{ review.title }}</h1>
    <!-- 일단 최신목록, 나중에 보던 페이지 목록으로 가는거 해보자 -->
    <router-link :to="{ name: 'reviewList' }">최신목록</router-link>
    <p>
      {{ review.content }}
    </p>
    <!-- review Edit/Delete UI -->
    <div v-if="isAuthorReview">
    <!-- <div> -->
      <!-- <router-link :to="{ name: 'reviewEdit', params: { reviewId } }">
        수정
      </router-link>
      | -->
      <button @click="deleteReview(reviewId)">삭제</button>
    </div>

    <hr />
    <!-- Comment UI -->
    <review-comment-list :comments="review.comments"></review-comment-list>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import ReviewCommentList from '@/components/ReviewCommentList.vue'

  export default {
    name: 'ReviewDetail',
    components: { ReviewCommentList },
    data() {
      return {
        reviewId: this.$route.params.reviewId,
      }
    },
    computed: {
      ...mapGetters(['isAuthorReview', 'review']),
      // ...mapGetters(['review']),
      // likeCount() {
      //   return this.review.like_users?.length
      // }
    },
    methods: {
      ...mapActions([
        'fetchReview',
        'likeReview',
        'deleteReview',
      ])
    },
    created() {
      this.fetchReview(this.reviewId)
    },
  }
</script>

<style></style>

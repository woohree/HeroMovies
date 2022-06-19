<template>
  <div>
    <h1>리뷰 수정</h1>
    <review-form v-if="isReview" :review="review" action="update">

    </review-form>
  </div>

</template>

<script>
import ReviewForm from '@/components/ReviewForm.vue'
import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'AritcleEditView',
    components: { ReviewForm },
    computed: {
      ...mapGetters(['review', 'isReview',])
    },
    methods: {
      ...mapActions(['fetchReview'])
    },
    created() {
      this.fetchReview(this.$route.params.reviewId)
    },
  }
</script>

<style></style>

<template>
  <div>
    <h1>새로운 리뷰</h1>
    <review-form :movie="movie" action="create" :rating="0"></review-form>
  </div>
</template>

<script>
import ReviewForm from '@/components/ReviewForm.vue'

export default {
  name: 'ReviewNewView',
  components: {
    ReviewForm,
  },
  data() {
    return {
      movie: {
        pk: null,
        reviewTitle: '',
        review: '',
      }
    }
  }
}
</script>

<style>

</style>
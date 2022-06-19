<template>
  <form @submit.prevent="onSubmit" class="comment-list-form">
    <label for="comment">내용: </label>
    <input type="text" id="comment" v-model="content" required>
    <button>작성</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewCommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['review']),
  },
  methods: {
    ...mapActions(['createReviewComment']),
    onSubmit() {
      this.createReviewComment({ reviewId: this.review.id, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>
.comment-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}
</style>
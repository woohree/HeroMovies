<template>
  <div class="comment-list">
    <ul>
      <review-comment-list-item 
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.id">
      </review-comment-list-item>        
    </ul>

    <review-comment-list-form></review-comment-list-form>
  </div>
</template>

<script>
import ReviewCommentListItem from '@/components/ReviewCommentListItem.vue'
import ReviewCommentListForm from '@/components/ReviewCommentListForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ReviewCommentList',
  components: { ReviewCommentListForm, ReviewCommentListItem },
  props: { comments: Array },
}
</script>

<style>
.comment-list {
  border: 1px solid blue;
}
</style>
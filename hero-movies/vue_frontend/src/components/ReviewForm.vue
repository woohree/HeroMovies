<template>
  <div class="m-3">
    <h1>{{ movie.title }}</h1>

    <!-- 필요한거 
         1. 영화 제목
         2. 평점
         3. 리뷰 제목
         4. 리뷰 내용 

         => 영화객체, 리뷰객체, 수정or새글 필요 -->

    <v-card>
      <v-form
        ref="form"
        @submit.prevent="submit()"
      >
        <v-container fluid>
          <v-row>
            <v-col col="12">
              <v-text-field
                v-model="form.score"
                label="평점"
                required>
              </v-text-field>
            </v-col>

            <v-col
              cols="12"
            >
              <v-text-field
                v-model="form.title"
                :rules="rules.title"
                label="제목"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-textarea
                v-model="form.content"
                :rules="rules.content"
              >
                <template v-slot:label>
                  <div>
                    내용
                  </div>
                </template>
              </v-textarea>
            </v-col>
          </v-row>
        </v-container>
        <v-card-actions>
          <v-btn
            text
            @click="resetForm"
          >
            초기화
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            :disabled="!formIsValid"
            text
            color="primary"
            type="submit"
          >
            작성
          </v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ReviewForm',
    props: {
      movie: Object,
      rating: Number,
      action: String,
      review: Object,
    },
    data() {
      const defaultForm = Object.freeze({
        title: this.review.title,
        content: this.review.content,
        score: this.rating,
        reviewed_movie: this.movie.id
      })

      return {
        // dataRating: this.rating,
        form: Object.assign({}, defaultForm),
        rules: {
          title: [val => (val || '').length > 0 || '제목을 입력해주세요.'],
          content: [val => (val || '').length > 0 || '내용을 입력해주세요.'],
        },
        defaultForm,
      }
    },

    computed: {
      formIsValid () {
        return (
          this.form.title &&
          this.form.content
        )
      },
    },

    methods: {
      ...mapActions(['createReview', 'updateReview', 'votingMovie']),

      resetForm () {
        this.form = Object.assign({}, this.defaultForm)
        this.$refs.form.reset()
      },

      submit () {
        // console.log(score)
        if (this.action === 'create') {
          this.createReview(this.form)
          this.votingMovie(this.form)
        } else if (this.action === 'update') {
          const payload = {
            id: this.review.id,
            ...this.form,
          }
          this.updateReview(payload)
        }
        this.resetForm()
        this.$modal.hideAll()
      },
    },
}
</script>

<style>

</style>
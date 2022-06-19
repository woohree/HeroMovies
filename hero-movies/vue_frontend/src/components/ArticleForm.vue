<template>
  <v-card flat>
    <v-form
      ref="form"
      @submit.prevent="submit"
    >
      <v-container fluid>
        <v-row>
          <v-col cols="12">
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
          취소
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn
          :disabled="!formIsValid"
          text
          type="submit"
        >
          작성
        </v-btn>
      </v-card-actions>
    </v-form>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      const defaultForm = Object.freeze({
        title: this.article.title,
        content: this.article.content,
      })

      return {
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
      ...mapActions(['createArticle', 'updateArticle']),

      resetForm () {
        this.form = Object.assign({}, this.defaultForm)
        this.$refs.form.reset()
      },

      submit () {
        if (this.action === 'create') {
          this.createArticle(this.form)
        } else if (this.action === 'update') {
          const payload = {
            id: this.article.id,
            ...this.form,
          }
          this.updateArticle(payload)
        }
        this.resetForm()
      },
    },
  }
</script>

<style></style>

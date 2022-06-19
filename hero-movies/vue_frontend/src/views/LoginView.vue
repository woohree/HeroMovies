<template>
  <div>
    <h1>로그인</h1>

    <account-error-list v-if="authError"></account-error-list>

    <!-- <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">username: </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div>

      <div>
        <label for="password">password: </label>
        <input v-model="credentials.password" type="password" id="password" required />
      </div>

      <button>Login</button>
    </form> -->
    <v-form
      ref="form"
      v-model="valid"
      lazy-validation
      @submit.prevent="login({ username, password })"
    >
      <v-text-field
        v-model="username"
        :rules="idRules"
        label="아이디"
      ></v-text-field>

      <v-text-field
        v-model="password"
        :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="pwRules"
        :type="show ? 'text' : 'password'"
        label="비밀번호"
        @click:append="show = !show"
      ></v-text-field>

      <v-btn
      color="black"
      class="mr-4"
      type="submit"
      :disabled="!isLoginValid"
      >
      로그인
      </v-btn>

      <!-- <v-btn
        color="black"
        class="mr-4"
        @click="reset"
      >
        취소
      </v-btn> -->

    </v-form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },

    data() {
      return {
        // credentials: {
        //   username: '',
        //   password: '',
        // },

        show: false,
        password: '',
        pwRules: [value => !!value || '비밀번호를 입력해주세요.',],
          // required: 
          // min: v => v.length >= 8 || 'Min 8 characters',


        valid: true,
        username: '',
        idRules: [v => !!v || '아이디를 입력해주세요.',],
          // v => (v && v.length <= 10) || 'ID must be less than 10 characters',
      }
    },

    computed: {
      ...mapGetters(['authError']),
      isLoginValid() {
        return this.username && this.password
      },
    },

    methods: {
      ...mapActions(['login']),

      reset () {
        this.$refs.form.reset()
      },
    },
  }
</script>

<style></style>

<template>
  <div>
    <h1>회원가입</h1>
    <account-error-list v-if="authError"></account-error-list>

    <v-form
      @submit.prevent="signup(credentials)">

      <v-card
        class="mx-auto"
      >
        <v-card-title class="text-h6 font-weight-regular justify-space-between">
          <v-avatar
            class="subheading signup-step"
            color="#2962FF"
            size="24"
            v-text="step"
          ></v-avatar>
          <span>{{ currentTitle }}</span>
        </v-card-title>

        <v-window v-model="step">

          <v-window-item :value="1">
            <v-card-text>
              <v-text-field
                label="아이디"
                v-model="credentials.username">
              </v-text-field>
              <v-text-field
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show ? 'text' : 'password'"
                @click:append="show = !show"
                label="비밀번호"
                v-model="credentials.password1"
              ></v-text-field>
              <v-text-field
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show ? 'text' : 'password'"
                @click:append="show = !show"
                label="비밀번호 확인"
                v-model="credentials.password2"
              ></v-text-field>
            </v-card-text>
          </v-window-item>

          <v-window-item :value="2">
            <v-card-text>
              <v-text-field
                label="이메일"
              ></v-text-field>
            </v-card-text>
          </v-window-item>

          <v-window-item :value="3">
            <v-card-text>
              <v-textarea>              
                <template v-slot:label>
                  <div>내용</div>
                </template>
              </v-textarea>
            </v-card-text>
          </v-window-item>

          <!-- <v-window-item :value="4">
            파일 업로드
            <v-file-input v-model="credentials.profile_image">

            </v-file-input>
          </v-window-item> -->

          <v-window-item :value="5">
            <div class="pa-4 text-center">
              <v-img
                class="mb-4"
                contain
                height="128"
                src="https://cdn.vuetifyjs.com/images/logos/v.svg"
              ></v-img>
              <h3>
                영웅, 영화들에 오신 것을 환영합니다.
              </h3>
              <v-btn>
                <router-link class="text-decoration-none signup-home-btn" style="display: block;" :to="{ name: 'main' }">홈으로</router-link>
              </v-btn>
            </div>
          </v-window-item>

        </v-window> 

        <v-divider></v-divider>

        <v-card-actions>
          <v-btn
            :disabled="step === 1 || step === 4"
            text
            @click="step--"
          >
            이전
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            :disabled="step >= 3"
            text
            @click="step++"
          >
            다음
          </v-btn>
          <v-btn
            v-if="step === 3"
            type="submit"
          >완료
          </v-btn>
          <!-- 이거 클릭 이벤트 거니까 서브밋이 안먹네,,,ㅜㅜ 
          라우터로 페이지 하나 해서 완료화면 보여줄까 -->
            <!-- @click="[step++, onUp(), submit()]" -->
        </v-card-actions>
      </v-card>

    </v-form>
  </div>
</template>

<script>
import AccountErrorList from '@/components/AccountErrorList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SignupView',
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: '',
        password1: '',
        password2: '',
        // email: '',
        // profile_image: null,
        // introduction: ''
      },
      step: 1,
      show: false,
    }
  },
  computed: {
    ...mapGetters(['authError']),

    currentTitle () {
      switch (this.step) {
        case 1: return '아이디, 비밀번호(필수)'
        case 2: return '이메일(필수)'
        case 3: return '소개글(필수)'
        case 4: return '프로필 사진(필수)'
        default: return '회원가입 완료'
      }
    },
  },
  methods: {
    ...mapActions(['signup']),
    onUp() {
      window.scrollTo(0, 0)
    }
  },
}
</script>

<style>
  .signup-step {
    color: white;
    margin-right: 8px;
  }
  .signup-home-btn {
    color: black;
  }
</style>

          <!-- <v-window-item :value="3">
            <v-card-text>

                <v-row>
                  <v-col
                    v-for="n in 9"
                    :key="n"
                    class="d-flex child-flex"
                    cols="4"
                  >

                    <v-img
                      :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
                      :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
                      aspect-ratio="1"
                      class="grey lighten-2"
                    >
                      <template v-slot:placeholder>
                        <v-row
                          class="fill-height ma-0"
                          align="center"
                          justify="center"
                        >
                          <v-progress-circular
                            indeterminate
                            color="grey lighten-5"
                          ></v-progress-circular>
                        </v-row>
                      </template>
                    </v-img>
                  </v-col>
                </v-row>

            </v-card-text>
          </v-window-item> -->
<template>
  <div v-if="movie">
    <v-hover>
      <template v-slot:default="{ hover }">
        <v-card>
          <!-- 포스터 이미지 -->
          <v-img class="poster" style="height:300px" :src="`https://image.tmdb.org/t/p/original` + movie.poster_path"></v-img>
          <v-fade-transition>
            <v-overlay
              class="poster-overlay"
              v-if="hover"
              absolute
              color="rgb(0, 0, 0)">
              <div class="movie-item-btns d-flex flex-column">
                <p class="text-center">{{ movie.title }}</p>
                <v-card-actions class="pa-4">
                  <v-rating
                    @click.native="showReviewFormModal"
                    v-model="rating"
                    background-color="light"
                    color="#FFB300"
                    dense
                    half-increments
                    hover
                    size="20">
                  </v-rating>
                  <!-- <span>
                    ({{ rating*2 }})
                  </span> -->
                </v-card-actions>
                <v-btn
                  v-b-modal="`${idx}${category}`"
                  class="movie-info-btn" 
                  color="#78909C"
                  @click="fetchMovie(movie.id)"
                >상세정보
                </v-btn>
              </div>
            </v-overlay>
          </v-fade-transition>
        </v-card>  
      </template>
    </v-hover>


      <b-modal
        :id="`${idx}${category}`"
        hide-header
        hide-footer
        size="lg"
        class="movie-modal"
        >
        <v-card 
          class="modal-card p-3"
          :style="{ 'background-image': `linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.6)), url(https://image.tmdb.org/t/p/original` + selectMovie.backdrop_path }"
        >
        <div class="d-flex">
          <img :src="`https://image.tmdb.org/t/p/original` + selectMovie.poster_path" :alt="selectMovie.title" width="300px">
          <div class="mx-4 movie-modal-detail">
            <h3>{{ selectMovie.title }}</h3>
            <p style="font-size: 0.7rem; font-style: italic">{{ selectMovie.tagline }}</p>
            <h6>개봉일: {{ selectMovie.release_date }}</h6>
            <h6 v-if="selectMovie.runtime !== 0">상영 시간: {{ selectMovie.runtime }}분</h6>
            <div>
              <div v-if="selectMovie.vote_average !== 0">
                <v-rating
                  v-model="selectMovie.vote_average"
                  background-color="rgb(233, 233, 233)"
                  color="#FFB300"
                  :length="10"
                  readonly	
                  size="20">
                </v-rating>
                <p style="font-size: 0.8rem">({{ selectMovie.vote_average }}점 / {{ selectMovie.vote_count }}명)</p>
              </div>
              <v-btn
                v-if="!isWished"
                class="mb-3 p-0"
                text>
                <v-icon
                  :style="isWished ? {color: '#FF5722'} : {color: 'rgb(233, 233, 233)'} "
                  @click="wishingMovie(movie.id)">
                  mdi-heart-settings-outline
                </v-icon>
              </v-btn>
              <v-btn
                v-if="isWished"
                class="mb-3 p-0"
                text>
                <v-icon
                  :style="isWished ? {color: '#FF5722'} : {color: 'rgb(233, 233, 233)'} "
                  @click="wishingMovie(movie.id)">
                  mdi-heart-settings
                </v-icon>

              </v-btn>
            </div>
            <p style="font-size: 0.9rem">{{ selectMovie.overview }}</p>
          </div>
        </div>
        </v-card>
      </b-modal>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
// import MovieModalInfo from '@/components/MovieModalInfo.vue'
import ReviewForm from '@/components/ReviewForm.vue'
// import StarRating from 'vue-star-rating'
// import moment from "moment"

export default {
  name: 'MovieGlideItem',
  components: {
    // StarRating,
    // MovieModalInfo,
  },
  data() {
    return {
      rating: 0,
    }
  },
  props: {
    movie: Object,
    idx: Number,
    category: String,
  },
  methods: {
    ...mapActions(['fetchMovie', 'wishingMovie']), 
    // 리뷰했던거면 액션 edit으로 보낼 수 있게... 시간이... 부족해...
    showReviewFormModal() {
      this.$modal.show(ReviewForm, {
        rating: this.rating*2,
        movie: this.movie,
        action: 'create',
        review: {
          pk: null,
          title: '',
          content: '',
        }
      }, {
        draggable: true,
        scrollable: true,
        adaptive: true,
        height: 'auto',
      })
    },
  },
  computed: {
    ...mapGetters(['selectMovie', 'isWished']),
  }
}
</script>

<style>
  .movie-item-btns * {
    margin: auto;
  }
  .movie-modal-detail {
    color: rgb(233, 233, 233);
  }
  .modal-body {
    padding: 0 !important;
  }

</style>
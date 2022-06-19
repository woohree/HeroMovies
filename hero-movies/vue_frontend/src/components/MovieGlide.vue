<template>
  <div v-if="movies.length">
    <h2>{{ kCategory }}</h2>
    <!-- <h2>{{movies[1]}}</h2> -->
    <!-- 글라이드 -->
    <!-- 카테고리 별 영화 리스트 -->
    <vue-glide
    :perView="6"
    :gap="20"
    :keyboard="false"
    :bound="true"
    >

      <vue-glide-slide
      v-for="(movie, idx) in movies"
      :key="idx"
      >

        <movie-glide-item 
        :movie="movie"
        :idx="idx"
        :category="category">
        </movie-glide-item>

      </vue-glide-slide>

      <template slot="control">
        <v-icon class="glide-margin glide-btns" data-glide-dir="<">mdi-chevron-left</v-icon>
        <v-icon class="glide-btns" data-glide-dir=">">mdi-chevron-right</v-icon>
      </template>

    </vue-glide>
  <hr>
  </div>
</template>

<script>
import { Glide, GlideSlide } from 'vue-glide-js'
import MovieGlideItem from '@/components/MovieGlideItem.vue'

// 여기서 카테고리에 맞추어서 서버에 요청해서 movies 받아다가 출력
export default {
  name: 'MovieItem',
  components: {
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide,
    MovieGlideItem,
  },
  props: {
    movies: Array,
    category: String,
  },
  computed: {
    kCategory() {
      const categoryInKorean = {
        Recommendation: '추천 영화',
        MCU: '마블 시네마틱 유니버스',
        DCU: '디씨 시네마틱 유니버스',
        SSU: '소니 스파이더맨 유니버스',
      }
      return categoryInKorean[this.category]
    }
  }
}
</script>

<style>
  .glide-margin {
    margin-left: 47.5%;
  }
  .glide-btns:hover {
    cursor: pointer;
  }
</style>

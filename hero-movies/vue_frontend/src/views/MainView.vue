<template>
  <div>
    <h1 class="text-center">영화</h1>
    <div v-if="movies.length">
      <movie-glide 
      v-for="(movies, key) in filteredMovies" 
      :key="key"
      :movies="movies"
      :category="key">
      </movie-glide>
      <!-- v-for="(category, idx) in categories" 
      :key="idx" 
      :category="category" -->

    </div>
  </div>
</template>

<script>
import MovieGlide from '@/components/MovieGlide.vue'
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'MainView',
  components: {
    MovieGlide,
  },
  data() {
    return {
      categories: ['Recommendation', 'MCU', 'DCU', 'SSU',],
    }
  },
  computed: {
    ...mapGetters(['filteredMovies', 'movies', 'recomMovies'])
  },
  
  methods: {
    ...mapActions(['fetchMovies', 'fetchRecomMovies'])
  },

  created() {
    this.fetchRecomMovies()
    this.fetchMovies()
  }
  
}
</script>

<style>

</style>
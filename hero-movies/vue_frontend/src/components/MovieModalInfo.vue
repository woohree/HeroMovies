<template>
  <v-card class="modal-movie-info m-4"
  :style="{ 'background-image': `url(https://image.tmdb.org/t/p/original` + movie.backdrop_path}"
  >
    <h1>{{ movie.title }}</h1>


  </v-card>


</template>

<script>
import { mapActions, mapGetters } from 'vuex'


export default {
  name: 'MovieModalInfo',
  props: {
    movieId: Number,
  },
  methods: {
    ...mapActions(['fetchMovie']),
  },
  computed: {
    ...mapGetters(['movie'])
  },
  created() {
    this.fetchMovie(this.movieId)
  }
}
</script>

<style>
  .modal-movie-info {
    color: rgb(156, 156, 61);
    /* width: 0%; */
    /* margin: 5%; */
  }
</style>
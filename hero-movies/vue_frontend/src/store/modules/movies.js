import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'
// import _ from 'lodash'

export default {
  state: {
    recomMovies: [],
    movies: [],
    selectMovie: {},
    // isWished: false,
  },
  
  getters: {
    // movies에 객체 형식으로 카테고리에 따른 영화목록을 따로 불러올 수 있으면 좋겠음 => 그래야 모달에서 컨트롤하기 편함
    // recomMovies: state => state.recomMovies,
    movies: state => state.movies,
    selectMovie: state => state.selectMovie,
    // isWished: state => state.isWished,
    isWished: (state, getters) => {return state.selectMovie.wishing_users?.includes(getters.currentUser.pk)},
    isVoted: (state, getters) => {return state.selectMovie.voted_users?.includes(getters.currentUser.pk)},    
    filteredMovies: state => {
      const movieObj = {
        Recommendation: state.recomMovies.filter(movie => movie.poster_path && movie.status === 'Released'),
        MCU: state.movies.filter(movie => movie.keywords.filter(keyword => keyword.id === 180547).length && movie.poster_path && movie.status === 'Released'),
        DCU: state.movies.filter(movie => movie.keywords.filter(keyword => keyword.id === 229266).length && movie.poster_path && movie.status === 'Released'),
        SSU: state.movies.filter(movie => movie.keywords.filter(keyword => keyword.id === 296915).length && movie.poster_path && movie.status === 'Released'),
      }
      return movieObj
    },
  },

  mutations: {
    SET_RECOM_MOVIES(state, movies) { state.recomMovies = movies },
    // SET_IS_WISHED(state) { state.isWished = false },
    // FETCH_IS_WISHED(state, flag) { state.isWished = flag },
    SET_MOVIES(state, movies) { state.movies = movies },
    SET_MOVIE(state, movie) { state.selectMovie = movie },
    // SET_KEYWORDS(state, keywords) { state.keywords = keywords },
  },

  actions: {
    fetchRecomMovies({ commit, getters }) {
      axios({
        url: drf.movies.recomMovies(),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => {
        console.log(res.data)
        commit('SET_RECOM_MOVIES', res.data)
      })
    },
      
    votingMovie({ commit, getters }, vote) {
      // console.log(vote)
      axios({
        url: drf.movies.voteMovie(vote.reviewed_movie),
        method: 'post',
        data: vote,
        headers: getters.authHeader,
      })
        .then(res => {
          // console.log(res.data)
          commit('SET_MOVIE', res.data)
        })
        .catch(err => console.error(err))
    },

    wishingMovie({ commit, getters }, movieId) {
      // console.log(state.selectMovie.wishing_users.includes(getters.currentUser.pk))
      axios({
        url: drf.movies.wishMovie(movieId),
        method: 'put',
        headers: getters.authHeader,
      })
        .then(res => {
          // console.log(res.data)
          commit('SET_MOVIE', res.data)
          // dispatch('fetchIsWished')
        })
    },
    fetchMovies({ commit, getters }) {
      // console.log('무비즈 요청')
      // console.log(getters.authHeader)
      // console.log(drf.movies.movies())
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          // console.log(res.data)
          commit('SET_MOVIES', res.data)
        })
        .catch(err => console.error(err.response))
    },

    fetchMovie({ commit, getters }, movieId) {
      axios({
        url: drf.movies.movie(movieId),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.state === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    // fetchKeywords({ commit, getters }, movieId) {
    //   axios({
    //     url: drf.movies.keywords(movieId),
    //     method: 'get',
    //     headers: getters.authHeader,
    //   })
    //     .then(res => commit('SET_KEYWORDS', res.data))
    //     .catch(err => console.error(err))
    // }
  },
}
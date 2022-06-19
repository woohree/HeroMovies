const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const ARTICLES = 'articles/'
const COMMENTS = 'comments/'
const MOVIES = 'movies/'
const REVIEWS = 'reviews/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + `${username}/` + 'profile/',
  },

  articles: {
    articles: () => HOST + ARTICLES,
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) => HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
    // comment: commentPk => HOST + ARTICLES + COMMENTS + `${commentPk}/`
  },

  // 일단 일단임
  movies: {
    recomMovies: () => HOST + MOVIES + 'recommended/',
    movies: () => HOST + MOVIES,
    movie: movieId => HOST + MOVIES + `${movieId}/`,
    // keyword: movieId => HOST + MOVIES + 'keyword/' + `${movieId}/`,
    seenMovie: movieId => HOST + MOVIES + `${movieId}/` + 'seen/',
    wishMovie: movieId => HOST + MOVIES + `${movieId}/` + 'wishing/',
    voteMovie: movieId => HOST + MOVIES + `${movieId}/` + 'voting/'
  },

  reviews: {
    reviews: () => HOST + REVIEWS,
    review: reviewPk => HOST + REVIEWS + `${reviewPk}/`,
    comments: reviewPk => HOST + REVIEWS + `${reviewPk}/` + COMMENTS,
    comment: (commentPk) => HOST + REVIEWS + COMMENTS + `${commentPk}/`
  }
}

import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'
// import accounts from './accounts'

export default {
  state: {
    reviews: [],
    review: {},
    lengthReviews: 0,
  },

  getters: {
    reviews: state => state.reviews,
    review: state => state.review,
    isAuthorReview: (state, getters) => {
      return state.review.user?.username === getters.currentUser.username
    },
    isReview: state => !_.isEmpty(state.review),
    lenReviews: state => state.lengthReviews,
  },

  mutations: {
    SET_REVIEWS: (state, reviews) => state.reviews = reviews,
    SET_REVIEW: (state, review) => state.review = review,
    SET_REVIEW_COMMENTS: (state, comments) => (state.review.comments = comments),
    SET_REVIEWS_LENGTH: (state, length) => state.lengthReviews = length
  },

  actions: {
    fetchReviewsLength({ commit, getters }) {
      axios({
        url: drf.reviews.reviews(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          // console.log(res.data)
          commit('SET_REVIEWS_LENGTH', res.data.length)
        })
        .catch(err => console.error(err.response))

    },

    fetchReviews({ commit, getters }, page) {
    // fetchArticles({ commit }) {
      /* 게시글 목록 받아오기
      GET: articles URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.reviews.reviews(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          // console.log(res.data)
          commit('SET_REVIEWS', res.data.slice((page-1)*10, (page-1)*10+10))
        })
        .catch(err => console.error(err.response))
    },

    fetchReview({ commit, getters }, reviewId) {
    // fetchArticle({ commit }, articleId) {
      /* 단일 게시글 받아오기
      GET: article URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          단순 에러일 때는
            에러 메시지 표시
          404 에러일 때는
            NotFound404 로 이동
      */
      axios({
        url: drf.reviews.review(reviewId),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_REVIEW', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },

    createReview({ commit, getters }, review) {
      /* 게시글 생성
      POST: articles URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      
      axios({
        url: drf.reviews.reviews(),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          // console.log(res.data)
          commit('SET_REVIEW', res.data)
          router.push({
            name: 'reviewDetail',
            params: { reviewId: getters.review.id }
          })
        })
    },

    updateReview({ commit, getters }, { id, title, content}) {
      /* 게시글 수정
      PUT: article URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.reviews.review(id),
        method: 'put',
        data: { title, content },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.push({
            name: 'reviewDetail',
            params: { reviewId: getters.review.id }
          })
        })
    },

    deleteReview({ commit, getters }, reviewId) {
    // deleteArticle({ commit }, articleId) {
      /* 게시글 삭제
      사용자가 확인을 받고
        DELETE: article URL (token)
          성공하면
            state.article 비우기
            AritcleListView로 이동
          실패하면
            에러 메시지 표시
      */
      
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.reviews.review(reviewId),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_REVIEW', {})
            router.push({ name: 'reviewList' })
          })
          .catch(err => {
            console.log('실패')
            console.error(err.response)
          })
      }
    },

    likeReview({ commit, getters }, reviewId) {
      /* 좋아요
      POST: likeArticle URL(token)
        성공하면
          state.article 갱신
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.reviews.likeReview(reviewId),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_REVIEW', res.data))
        .catch(err => console.error(err.response))
    },

		createReviewComment({ commit, getters }, { reviewId, content }) {
      /* 댓글 생성
      POST: comments URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const comment = { content }

      axios({
        url: drf.reviews.comments(reviewId),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    updateReviewComment({ commit, getters }, { reviewId, commentId, content }) {
      /* 댓글 수정
      PUT: comment URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */
      const comment = { content }

      axios({
        url: drf.reviews.comment(reviewId, commentId),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteReviewComment({ commit, getters }, { reviewId, commentId }) {
      /* 댓글 삭제
      사용자가 확인을 받고
        DELETE: comment URL (token)
          성공하면
            응답으로 state.article의 comments 갱신
          실패하면
            에러 메시지 표시
      */
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.reviews.comment(reviewId, commentId),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_REVIEW_COMMENTS', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },
  },
}

import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'


// 메인 페이지, 영화 리스트
import MainView from '@/views/MainView.vue'

// 커뮤니티 페이지, 자유 게시판
import CommunityView from '@/views/CommunityView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleEditView from '@/views/ArticleEditView.vue'
import ArticleNewView from '@/views/ArticleNewView.vue'
// 리뷰 게시판
import ReviewDetailView from '@/views/ReviewDetailView.vue'
import ReviewEditView from '@/views/ReviewEditView.vue'
import ReviewListView from '@/views/ReviewListView.vue'
import ReviewNewView from '@/views/ReviewNewView.vue'

// 유저 
import ProfileView from '@/views/ProfileView.vue'
import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'

// 404
import NotFound404 from '@/views/NotFound404.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainView
  },
  {
    path: '/community/articles',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/community/articles/:articleId',
    name: 'articleDetail',
    component: ArticleDetailView
  },
  {
    path: '/community/articles/:articleId/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },
  {
    path: '/community/articles/new',
    name: 'articleNew',
    component: ArticleNewView
  },
  {
    path: '/community/reviews',
    name: 'reviewList',
    component: ReviewListView
  },
  {
    path: '/community/reviews/:reviewId',
    name: 'reviewDetail',
    component: ReviewDetailView
  },
  {
    path: '/community/reviews/:reviewId/edit',
    name: 'reviewEdit',
    component: ReviewEditView
  },
  {
    path: '/community/reviews/new',
    name: 'reviewNew',
    component: ReviewNewView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile/:userId',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  // 이전 페이지에서 발생한 에러메시지 삭제
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login', 'signup']

  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('로그인을 해야 합니다.')
    next({ name: 'login' })
  } else {
    next()
  }

  if (!isAuthRequired && isLoggedIn) {
    next({ name: 'articles' })
  }
})

export default router


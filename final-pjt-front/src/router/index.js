import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup.vue'
import Login from '@/views/accounts/Login.vue'
import Community from '@/views/communities/Community.vue'
import Create from '@/views/communities/Create.vue'
import Detail from '@/views/communities/Detail.vue'
import Update from '@/views/communities/Update.vue'
import Profile from '@/views/accounts/Profile.vue'
import MovieList from '@/views/movies/MovieList.vue'
import MovieDetail from '@/views/movies/MovieDetail.vue'
import UserUpdate from '@/views/accounts/UserUpdate.vue'
import MovieRecommend from '@/views/MovieRecommend.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/', 
    redirect: '/movies/',
  },
  {
    path: '/accounts/signup/',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/:user_name/update/',
    name: 'UserUpdate',
    component: UserUpdate,
  },
  {
    path: '/accounts/:user_name/',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/accounts/login/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/community/',
    name: 'Community',
    component: Community,
  },
  {
    path: '/community/create/',
    name: 'Create',
    component: Create,
  },
  {
    path: '/community/:article_pk/Update/',
    name: 'Update',
    component: Update,
  },
  {
    path: '/community/:article_pk/',
    name: 'Detail',
    component: Detail,
  },
  {
    path: '/movies/',
    name: 'MovieList',
    component: MovieList,
  },
  {
    path: '/movies/:movie_pk/',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path: '/MovieRecommend/',
    name: 'MovieRecommend',
    component: MovieRecommend,
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

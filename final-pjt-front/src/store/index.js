import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
import axios from 'axios'
export default new Vuex.Store({
  state: {
    posts: null,
    post: null,
    comments: null,
    comment: null,
    username: null,
    //userdata 나누기
    userLikeMovie: null,
    userWatchedMovie: null,
    userLikePost: null,
    userPost: null,
    //////
    movieList: null,
    movie: null,
    reviews: null,
    likes_count: null,
    islogincheck: null,
    movielikeval: null,
    movielikes: null,
    movielikescount: null,
    moviewatchval: null,
    moviewatchcount: null,
    searchedMovie: null,
    communityLikeval: null,
    firstMovie: null,
  },
  


  mutations: {
    GET_FIRST_MOVIES: function(state, data){
      state.firstMovie = data
    },
    GET_ARTICLES: function(state, articles){
      state.posts=articles
    },
    GET_ARTICLE: function(state, article){
      state.post=article
    },
    GET_COMMENTS: function(state, comments){
      state.comments=comments
    },
    CREATE_NEW_COMMENT: function(state, comment){
      state.comment=comment
    },
    GET_USERNAME: function(state, username){
      state.username=username
    },
    GET_PROFILE: function(state, userdata){
      state.userLikeMovie= userdata.like_movies
      state.userWatchedMovie= userdata.watched_movies
      state.userLikePost= userdata.like_posts
      state.userPost= userdata.posts_user

    },
    GET_MOVIES: function(state, movies){
      state.movieList = movies 
    },
    GET_MOVIE: function(state, movie){
      state.movie = movie
      
    },
    GET_REVIEWS: function(state, reviews){
      state.reviews = reviews
    },
    GET_LIKES: function(state, data){
      state.likes_count = data.likes_count
      state.communityLikeval = data.value

    },
    GET_MOVIE_LIKE: function(state, movielikes){
      state.movielikescount = movielikes.count
      state.movielikeval = movielikes.data
    },
    GET_MOVIE_WATCHED: function(state, res){
      state.moviewatchcount = res.count
      state.moviewatchval = res.watched
    },
    SEARCH_MOVIE: function(state, res){
      state.searchedMovie = res
    },
    RESET_SEARCH_MOVIE: function(state){
      state.searchedMovie = ''
    }
    






  },
  actions: {
    //게시글 처음 조회
    firstData: function({commit}){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/movies/`,
      })
      .then((res) =>{
        commit('GET_FIRST_MOVIES', res.data)
      })
    },


    //게시글 목록조회
    getPosts: function({commit}){
      axios({
        method:'get',
        url: 'http://127.0.0.1:8000/community/',
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then((res)=>{
        commit('GET_ARTICLES',res.data)
      })
      },
    //게시글 상세조회
    getPost: function({commit}, page){
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/community/${page}/`,
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then((res)=>{
        commit('GET_ARTICLE', res.data)
      })
    },
    getPostD: function({commit}, url){
      var page =url.split('/')
      axios({
        method:'GET',
        url: `http://127.0.0.1:8000/community/${page[2]}/`,
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then((res)=>{
        commit('GET_ARTICLE', res.data)
      })
    },
    getCommunityList: function({commit}, url){
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000${url}/comment/`,
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then((res)=>{
        commit('GET_COMMENTS', res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    getUsername: function({commit}){
      const token = localStorage.getItem('jwt')
      const TpayLoad = token.split('.')[1]
      const payLoad = Buffer.from(TpayLoad, 'base64');
      const result = JSON.parse(payLoad.toString())
      commit('GET_USERNAME', result.username)  
      },
    getUserProfile: function({commit}, username){
      
      axios({
        method:'get',
        url: `http://127.0.0.1:8000${username}/`,
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then((res)=>{
        commit('GET_PROFILE', res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
      
    },
    getMovies: function({commit}){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/movies/`,
      })
      .then((res)=> {
        commit('GET_MOVIES', res.data)
      })
    },
    getMovie:function({commit}, url){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000${url}`,
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then((res)=>{
        commit('GET_MOVIE', res.data)
      })
      .catch((err)=> {
        console.log(err)
        
      })
    },
    getMovie2:function({commit}, url){
        axios({
        method:'get',
        url: `http://127.0.0.1:8000/movies/${url}/`,
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then((res)=>{
        commit('GET_MOVIE', res.data)
      })
      .catch((err)=> {
        console.log(err)
        
      })
    },
    getReviews: function({commit}, url){
      axios({
        method:'GET',
        url: `http://127.0.0.1:8000${url}/review/`,
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then((res)=>{
        commit('GET_REVIEWS', res.data)
      })
    },
    getLikes: function({commit}, url){
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000${url}/likes/`,
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then((res)=>{
        commit('GET_LIKES', res.data)
      })
    },
    
    getMovieLike: function({commit}, url){
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000${url}/likes/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}` 
        }
      })
      .then((res)=>{
        commit('GET_MOVIE_LIKE', res.data)
      })
    },
    getMovieWatched: function({commit}, url){
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000${url}/watched/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}` 
        }
      })
      .then((res)=>{
        commit('GET_MOVIE_WATCHED', res.data)
      })
    },
    searchMovie: function({commit}, movieName){
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/movies/search/${movieName}/`, 
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}` 
        }
      })
      .then((res)=>{
        commit('SEARCH_MOVIE', res.data)
      })
      .catch(()=>{
        commit('RESET_SEARCH_MOVIE')
      })
    }
    
    
    
    
  },
  modules: {
  }
})

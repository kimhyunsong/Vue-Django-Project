<template>
  <div class="b-row container">
    
    <span style="font:italic bold 3em Georgia, serif">
      Movie List
    </span>

    <b-row>
    <b-card
      id="b-card" 
      bg-variant="light"
      v-for="movie in showMovies" :key="movie.id"
      :title="movie.title"
      :img-src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`"
      text-variant="dark"
      @click="getDetail(movie.id)"
      img-alt="Image"
      img-top
      tag="article"
      style="max-width: 18rem; border-style: solid; border-width: 4px 4px 4px 4px"
      class="mb-5 mt-5 mx-auto card border-dark"
    >


    
      
      <b-button @click='getDetail(movie.id)' variant="warning"><i class="fas fa-search"></i></b-button>
    </b-card>
    </b-row>

  <!--로딩 스피너-->
  <div class="text-center" v-if="isLoading">
    <br>
    <br>
    <br>
    <br>
    <label for="spinner"><h1>영화를 가져오는중.....</h1></label>
    <div><b-spinner id="spinner">     
    </b-spinner>
    <br><br><br><br><br><br><br><br><br><br><br><br><br><br></div></div>
 
    
    
    
    



  </div>




  
</template>

<script>
import axios from 'axios'
export default {
  name:'MovieList',
  data: function() {
    return {
      isLoading: true,
      showMovies: [],
      cnt : 12,

    }
  },
  methods:{
    ScrollBottom: function(){
      const {scrollHeight, scrollTop, clientHeight} = document.documentElement
      if (scrollHeight - Math.round(scrollTop) <= 2*clientHeight){
        this.showMovies.push(...this.movies.splice(0, this.cnt))
      }
    },
    getMovies(){
      this.$store.dispatch('getMovies')
    },
    getDetail: function(idx){
      
      if (localStorage.getItem('jwt')){
        this.$store.dispatch('getMovie', idx)
        this.$router.push({name:'MovieDetail', params:{ movie_pk:idx }}) 
      } else {
        this.$router.push({name:'Login'})
      }
    }
  },
  watch:{
    showMovies: function(){
      if (this.showMovies.length) {
        return this.isLoading=false
      }
    },
    
  },
  computed:{
    movies: function(){
      return this.$store.state.firstMovie
    }
  },
  created: function(){
    if (this.movies === null) {
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/movies/`,
      })
      .then((res) =>{
        this.movies = res.data
        this.showMovies.push(...this.movies.splice(0, this.cnt))
        window.addEventListener('scroll', this.ScrollBottom)
      
      })
    } else {
      this.showMovies.push(...this.movies.splice(0, this.cnt))
      window.addEventListener('scroll', this.ScrollBottom)
    }
  },
  destroyed(){
    window.removeEventListener('scroll', this.ScrollBottom)
  }
    
   
}
</script>

<style>
 #b-card:hover{
   
    -webkit-transform:scale(1.1);
    -moz-transform:scale(1.1);
    -ms-transform:scale(1.1);   
    -o-transform:scale(1.1);
    transform:scale(1.1);

 }
</style>
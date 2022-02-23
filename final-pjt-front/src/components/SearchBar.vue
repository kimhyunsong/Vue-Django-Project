<template>
  <div>
    <input
    
    placeholder="이곳에 영화를 검색해보세요!"
    style="width:300px"
    :input="movieName" 
    @keyup="search"
    type="text">
    
  <div style="width:500px" v-if=" isLoading && isText"><label for="spinner"><h1>영화를 가져오는중.....</h1></label>
    <div><b-spinner id="spinner">     
    </b-spinner></div></div>
  <b-list-group
    class="container" 
    style="width:305px; margin-left:10px"
    v-for="movie in searchedMovie" :key="movie.id">
    
    <b-list-group-item @click="getDetail(movie.id)">
    
    <img align='left' width="30" :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="">
    <div align="left">{{movie.title}}</div>
    <div align="right"><b-button variant="success"  @click="getDetail(movie.id)">검색</b-button></div>
    
    
    </b-list-group-item>
  
  </b-list-group>

  </div>
</template>

<script>
export default {
  name:'SearchBar',
  data: function(){
    return {
      movieName: '',
      isText: false,
      isLoading: true,
      // items :{
      //   Title : this.searchedMovie.title
      // }
      
    }
  },
  methods:{
    search: function(event){
      this.movieName = event.target.value
      this.$store.dispatch('searchMovie', this.movieName)
      
    },
    getDetail: function(idx){
      
      if (localStorage.getItem('jwt')){
        this.$store.dispatch('getMovie2', idx)
        this.$router.push({name:'MovieDetail', params:{ movie_pk:idx }}).catch(()=>{}); 
      } else {
        this.$router.push({name:'Login'})
      }
    }
  },
  watch:{
    isText: function(){
      if (this.movieName.length) {
        return this.isText= true
      }
    },
    isLoading: function(){
      if (this.$store.state.searchedMovie.length) {
        return this.isLoading=false
      }
    }
  },
  computed:{
    searchedMovie: function(){
      return this.$store.state.searchedMovie
    }
  }
}
</script>

<style>

</style>
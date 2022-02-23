<template>
  <div>
    <md-content v-if="movie" class="container" align="left" style="border-radius:0.8em; border-style: inset; background-color:#000000">
      <div style="padding-top:5px; color:white"><h1>{{movie.movies.title}}</h1> <b
      
      v-for="genre in movie.genres" :key=genre.id
      > &nbsp;[{{genre.name}}]&nbsp; </b></div>

      <div class="d-flex">
      <img 
      :src="`https://image.tmdb.org/t/p/w200/${movie.movies.poster_path}`" alt="">
      <div style="background-color:#000000; margin-left:5px">
        
        <span v-if="movie.movies.overview">
        <b class="movie_overview">
        
        
         {{movie.movies.overview}} </b>
         </span>
         <span v-else>
         <b class="movie_overview"> 영화 정보가 없습니다.</b>
         
         </span>
         
         </div>
      


      </div>
      <span v-if="TeaserId">
      <div class="video-container">
      <iframe 
      id="ytplayer" type="text/html"
      width="640" height="390"
      :src="`https://www.youtube.com/embed/${TeaserId}?autoplay=1`" frameborder="0"></iframe>
      </div>
      </span>
      
      <button class="btn" @click="getVideo(movie.movies.id)"><span style="color:red"><i class="fab fa-youtube"></i></span></button>
   
      
     

  



    
    <div class="inline" align="right" style="margin-bottom:10px">
      <span v-if="likeval"
      style="font-size: 15px; color: Dodgerblue"
      >
      <label for="md-icon-button md-accent" style="font-style:italic ;color:white">찜 목록에 담겼습니다.</label>
      <md-button 
    @click.native="movieLikes"
    class="md-icon-button md-accent">
        <md-icon>thumb_up</md-icon>
    </md-button>       
      </span>
      <span v-else
      style="font-size: 15px"
      >
      <label for="md-icon-button md-accent" style="color:white">찜 목록에 담으시겠습니까?</label>
       <md-button 
     @click.native="movieLikes"
     class="md-icon-button md-raised md-accent">
        <md-icon>thumb_up</md-icon>
      </md-button>
        </span>


      
      





     
      <span v-if="watchval">
        <label for="md-icon-button md-primary" style="color:white">시청 목록에 담겼습니다.</label>
      <md-button 
      @click.native="haveSeen"
      class="md-icon-button md-primary">
        <i name="checked" class="fas fa-video" style="font-size:28px; color: Mediumslateblue;"></i>
      </md-button>
      </span>
      <span v-else>
        <label for="md-icon-button md-primary" style="color:white">시청 목록에 담으시겠습니까?</label>
       <md-button
      @click.native="haveSeen" 
      class="md-icon-button md-primary">
        <i name="checked" class="fas fa-video" style="font-size:28px; color: #ffffff;"></i>
      </md-button>
      </span>
      </div>
    
      </md-content>
      <movie-comment-detail></movie-comment-detail>
  </div>
</template>

<script>
import axios from 'axios'
import MovieCommentDetail from '@/components/movies/MovieCommentDetail'

export default {
  name: 'MovieDetail',
  data: function(){
    return {
      searchKeyword: null,
      video: null,
      TeaserId: null,
    }
  },
  components:{
    MovieCommentDetail
  },
  created: function(){
    this.$store.dispatch('getMovie', document.location.pathname)
    this.$store.dispatch('getMovieLike', document.location.pathname)
    this.$store.dispatch('getMovieWatched', document.location.pathname)
    
  },
  methods:{
    getVideo: function(videoId) {
      axios({
        method: 'GET',
        url : `https://api.themoviedb.org/3/movie/${videoId}/videos?api_key=a86920ed23507e1eea21c293aa45a948&language=ko-KR`

      })
      .then((res)=>{
        if (res.data.results.length === 0){
          alert('티저 영상이 없네요 :(')
        }else {
        this.TeaserId = res.data.results[0].key
        }
      })
    },
    haveSeen:function(){
      axios({
        method:'POST',
        url: `https://djmovie.net${document.location.pathname}/watched/`,
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then((res)=>{
        console.log(res)
        this.$store.dispatch('getMovieWatched', document.location.pathname)

      })
    },
    movieLikes: function(){
      axios({
        method: 'POST',
        url: `https://djmovie.net${document.location.pathname}/likes/`,
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then(()=>{
        this.$store.dispatch('getMovieLike', document.location.pathname)
      })
    },
    
  },
  computed: {
    movie: function(){
      return this.$store.state.movie
    },
    likeval: function(){
      return this.$store.state.movielikeval
    },
    likecount: function(){
      return this.$store.state.movielikescount
    },
    watchval:{
      get() {
        return this.$store.state.moviewatchval
      },
      set(){
        this.$store.dispatch('getMovieLike', document.location.pathname)

      }

    },

   
    watchcount: function(){
      return this.$store.state.moviewatchcount
    }

    
  },
}
</script>

<style>
  .video-container {
    float: inline-start;
    position: relative;
    padding-top: 56.25%;
    height: 0;
  }
  .video-container iframe{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
  .movie_overview {
    font-family: Times, "Times New Roman", Georgia, serif;
    color:white;
  }
</style>
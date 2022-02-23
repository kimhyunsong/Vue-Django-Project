<template>
  <div class="b-row container">
      <div class="md-layout-item" style="width:300px">
        <md-field>
          <md-select v-model="selected1" name="country" id="country" placeholder="찜목록 기반 추천">
            <md-option value="1">1개 추천!</md-option>
            <md-option value="2">2개 추천!</md-option>
            <md-option value="3">3개 추천!</md-option>
            <md-option value="4">4개 추천!</md-option>
            <md-option value="5">5개 추천!</md-option>
            
          </md-select>
        </md-field>
      </div>
    
    <label v-if="select_like_movies" for="b-card1"><h1> 좋아요 기반 알고리즘 영화 추천 </h1></label>
    <carousel>
      <slide v-for="movie in select_like_movies" :key="movie.id">
    <b-card
      v-b-tooltip.hover.top="'영화 상세정보를 보려면 돋보기를 누르세요!'"
      id="b-card1" 
      bg-variant="light"
      :title="movie.title"
      :img-src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`"
      text-variant="dark"
      img-alt="Image"
      img-top
      tag="article"
      style="height: 570px; max-width: 300px; border-style: solid; border-width: 4px 4px 4px 4px"
      class="mb-5 mt-5 mx-auto card border-dark"
      
    >
    <b-card-text>
      <b-button @click='getDetail(movie.id)' variant="warning"><i class="fas fa-search"></i></b-button>
    </b-card-text>
    </b-card>
    </slide>
    </carousel>




  <div class="md-layout-item" style="width:300px">
        <md-field>
          <md-select v-model="selected2" name="country" id="country" placeholder="시청한 영화 기반 추천">
            <md-option value="1">1개 추천!</md-option>
            <md-option value="2">2개 추천!</md-option>
            <md-option value="3">3개 추천!</md-option>
            <md-option value="4">4개 추천!</md-option>
            <md-option value="5">5개 추천!</md-option>
            
          </md-select>
        </md-field>
      </div>











    <label v-if="select_watched_movies" for="b-card2"><h1> 시청 경험 기반 알고리즘 영화 추천 </h1></label>
    <carousel>
    <slide v-for="movie in select_watched_movies" :key="movie.id">
    <b-card
      v-b-tooltip.hover.top="'영화 상세정보를 보려면 돋보기를 누르세요!'"
      id="b-card2" 
      bg-variant="light"
      :title="movie.title"
      :img-src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`"
      text-variant="dark"
      
      img-alt="Image"
      img-top
      tag="article"
      style="height: 570px; max-width: 300px; border-style: solid; border-width: 4px 4px 4px 4px"
      class="mb-5 mt-5 card border-dark"
    >
    <b-card-text>
      <b-button @click='getDetail(movie.id)' variant="warning"><i class="fas fa-search"></i></b-button>
      </b-card-text>
    </b-card>
    </slide>
    </carousel>







  </div>
</template>

<script>
import _ from 'lodash'
import axios from 'axios'
import { Carousel, Slide } from 'vue-carousel';

export default {
  name:'MovieRecommend',
  data: function(){
    return {
      like_movies: null,      //좋아하는 영화 중 장르가 같은 영화 리스트(사용자가 이미 좋아하는 것도 포함)
      select_like_movies: null,
      watched_movies: null, // 본 영화 중 장르가 같은 영화 리스트(사용자가 이미 본 영화도 포함.)
      select_watched_movies: null,
      selected1: null,
      userWatchedMovie: null,
      userLikeMovie: null,
      selected2: null,

    }
  },
  components:{
    Carousel,
    Slide
  },
  methods:{
    getDetail: function(idx){
      this.$store.dispatch('getMovie', idx)
      this.$router.push({name:'MovieDetail', params:{ movie_pk:idx }}) 
    }
  },
  watch: {
    selected1: function(){
      if (this.selected1) {
        if (this.userLikeMovie.length >= 2){
            const temp1 = []
            while (temp1.length < this.selected1) {
              const value = _.sample(this.watched_movies)
              if (!(value in this.userLikeMovie) && !(value in temp1)) {
                temp1.push(value)
              }
            this.select_like_movies = temp1
            }
      
        } else {
          this.$fire({
            title: "저장된 데이터가 부족하여 영화 목록으로 이동합니다.",
            text: `(찜 목록 2개 이상) 현재 : ${this.userWatchedMovie.length}개`,
            type: "error",
            timer: 3000
          }).then(()=> {
           this.$router.push({name:'MovieList'})
          })        
          
        }
      } else {
      alert('저장된 데이터가 부족합니다. 영화목록에서 좋아요와 시청한 영화 기능을 이용해주세요')
    }
    },
    selected2: function(){
      if (this.selected2) {
        if (this.userWatchedMovie.length >= 2){

          const temp2 = []
          while (temp2.length < this.selected2) {
            const value = _.sample(this.like_movies)

            if (!(value in this.userWatchedMovie) && !(value in temp2)) {
              temp2.push(value)
            }
          this.select_watched_movies = temp2
        }
      } else {
        this.$fire({
            title: "저장된 데이터가 부족하여 영화 목록으로 이동합니다.",
            text: `(시청 목록 2개 이상) 현재 : ${this.userWatchedMovie.length}개`,
            type: "error",
            timer: 3000
          }).then(() => {
           this.$router.push({name:'MovieList'})
          })         
      }
      } else {
      alert('저장된 데이터가 부족합니다. 영화목록에서 좋아요와 시청한 영화 기능을 이용해주세요')
    }
     
    },

  },
  created: function(){
    if (localStorage.getItem('jwt')){
    const token = localStorage.getItem('jwt')
    const TpayLoad = token.split('.')[1]
    const payLoad = Buffer.from(TpayLoad, 'base64');
    const result = JSON.parse(payLoad.toString())
    axios({
        method:'get',
        url: `http://127.0.0.1:8000/accounts/${result.username}/`,
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then((res)=>{
        this.userLikeMovie = res.data.like_movies
        this.userWatchedMovie = res.data.watched_movies
      })
    axios({
      method: 'GET',
      url: `http://127.0.0.1:8000/movies/recommend/${this.$store.state.username}`,
      headers: {
        Authorization: `JWT ${localStorage.getItem('jwt')}` 
      }
    })
    .then((res)=>{
      if (res.data.watched_movies.length && res.data.like_movies.length){
        this.watched_movies = res.data.watched_movies
        this.like_movies = res.data.like_movies         
      } else {
        this.$fire({
            title: "찜 목록과 시청기록을 두 개 이상 설정해주세요.",
            type: "warning",
            timer: 3000
          }).then((r) => {
           console.log(r.value)
          }) 
      }
    })
    .catch((err)=>{
      console.log(err)
    })
    } else {
      this.$fire({
        title:'로그인이 필요합니다.',
        text: `로그인 페이지로 이동합니다.`,
        type: "warning",
        timer: 3000
      }).then((r)=> {
        console.log(r.value)
        this.$router.push({name:"Login"})
    }
    )} 
  }
}
</script>

<style>

</style>
<template>
  <div class="container" align="left">

    <h1>{{profileUser}}님의 프로필</h1>
    <br>
    <label for="b-card2"><h2>찜 목록</h2></label>
    
  <carousel>
  <slide v-for="movie in userLikeMovie" :key="movie.id">
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
      style="height: 540px; max-width: 300px; border-style: solid; border-width: 4px 4px 4px 4px"
      class="mb-5 mt-5 card border-dark"
    > 
      <b-card-text><div align="right"><b-button @click='getDetail(movie.id)' variant="warning"><i class="fas fa-search"></i></b-button></div></b-card-text>
    </b-card>
  </slide>
  </carousel>








<label for="b-card2"><h2>시청 목록</h2></label>
  <carousel>
  <slide v-for="movie in userWatchedMovie" :key="movie.id">
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
      style="height: 540px; max-width: 300px; border-style: solid; border-width: 4px 4px 4px 4px"
      class="mb-5 mt-5 card border-dark"
    >   
      <b-card-text>      <div align="right"><b-button @click='getDetail(movie.id)' variant="warning"><i class="fas fa-search"></i></b-button></div>
</b-card-text>

    </b-card>
  </slide>
  </carousel>
















  <md-content class="container"
  style="border-radius:0.8em; border-style: inset; background-color:#F9DDDD"
  v-if="userLikePost"><br><h5> '좋아요'한 게시글 :</h5> <b v-for="post in userLikePost" :key="post.id">{{post.title}}</b></md-content>
  <br>  
  <md-content class="container" style="border-radius:0.8em; border-style: inset; background-color:#F9DDDD" v-if="userPost">
    <br>
    <h5>{{profileUser}}님이 작성한 게시글 :
    </h5><b v-for="post in userPost" :key="post.id">
      {{post.title}} <hr> </b>
      
      </md-content>
 
      
      

  <div class="inline" align="right">
  <span v-if="username===profileUser">
  <md-chip 
  @click="Update"
  class="md-primary" md-clickable>회원정보 수정</md-chip>
  </span>
  <span v-if="username===profileUser">
  <md-chip 
  @click="deleteUser"
  class="md-accent" md-clickable>회원 탈퇴</md-chip>
  </span>
  </div>




  </div>
</template>

<script>
import axios from 'axios'
import { Carousel, Slide } from 'vue-carousel';
export default {
  name: 'Profile',
  components: {
    Carousel,
    Slide
  },
  
  data: function(){
    return {
      key: false,
      profileUser: decodeURIComponent(`${document.location.pathname}`).split('/')[2],
    }
  },
  methods:{
    
    Update: function(){
      if (this.$store.state.username === this.profileUser){
      this.$router.push({name:'UserUpdate', params:{ user_name: this.username }})
      } else {
        alert('남의 계정에 손대지 마세요')
      }
    },
    getDetail: function(idx){  
      if (localStorage.getItem('jwt')){
        this.$store.dispatch('getMovie', idx)
        this.$router.push({name:'MovieDetail', params:{ movie_pk:idx }}) 
      } else {
        this.$router.push({name:'Login'})
      }
    },
    deleteUser: function(){
      if (this.$store.state.username === this.profileUser){
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/accounts/${this.username}/update/`,
        headers: {
          Authorization : `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then(()=>{
        localStorage.removeItem('jwt')
        this.$emit('logout')
        this.$router.push({name:'Login'})
      })
      } else {
        alert('남의 계정에 손대지 마세요')
      }
    }
  },
  computed:{
    username: function(){
      return this.$store.state.username
    },
    userLikeMovie: function(){
      return this.$store.state.userLikeMovie
    },
    userWatchedMovie: function(){
      return this.$store.state.userWatchedMovie
    },
    userLikePost: function(){
      return this.$store.state.userLikePost
    },
    userPost: function(){
      return this.$store.state.userPost
    },



  },
  created: function(){
    if (localStorage.getItem('jwt')) {
    this.$store.dispatch('getUsername')
    } else{
      this.$router.push({name:'MovieList'})

    }
      //프로필 내용 불러오기
    if (decodeURIComponent(`${document.location.pathname}`).split('/')[2] !='login'){
    this.$store.dispatch('getUserProfile', document.location.pathname)
    } else {
      this.$router.push({name:'MovieList'})
    }

  },


}
</script>

<style>
.row{
  margin-top:100px;
}

</style>
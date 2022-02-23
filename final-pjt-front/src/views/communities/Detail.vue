<template>
  <div class="container" v-if="article">

    <md-content class="container" align="left" style="border-radius:0.8em; border-style: inset; background-color:#000000;">  
      <br>
      <h1 style="color:white">제목 : {{article.title}}</h1>     
      <div align="right">
        <span v-if="likestatus"><span @click="likes" style="color: Dodgerblue"><i class="fas fa-thumbs-up"></i></span></span>
        <span v-else><span @click="likes"><i class="fas fa-thumbs-up" style="color:white"></i></span></span>
        <span style="color:white"> &nbsp; {{likes_count}}</span>
      </div>
      <hr style="color:white">
      <div style="text-align:right color:white">
        <p style="color:white"> 글쓴이 :{{article.username}} / 수정 시간 : {{convertDate(article.updated_at)}}</p>
      </div>
      <div style="color:white">{{article.content}}</div>
      <p @click="getProfile"> </p>
      <div class="container" align="right">
      <span v-if="username===article.username">
        <div style="margin-top:20px;">
          <md-chip class="md-primary md-raised md-default" @click='update(article.id)' md-clickable>업데이트</md-chip>&nbsp;  
          <md-chip class="md-accent md-raised md-default" @click="delArticle" md-clickable>삭제</md-chip>&nbsp;  
          <!-- <span @click="delArticle"><i class="fas fa-trash-alt"></i></span> -->
        </div>
      </span>
    </div>
    <br>
    </md-content>
    
    <hr>
    <community-comment-list class="container"></community-comment-list>

  </div>
</template>

<script>
import CommunityCommentList from '@/components/communities/CommunityCommentList'
import axios from 'axios'
export default {
  name:'Detail',
  components:{
    CommunityCommentList
  },
  

  computed:{
    article: function() {
      return this.$store.state.post
    },
    config: function(){
      return this.$store.state.config
    },
    likes_count: function(){
      return this.$store.state.likes_count
    },
    username: function(){
      return this.$store.state.username
    },
    likestatus: function(){
      return this.$store.state.communityLikeval
    }
    
    
  },
  methods:{
    convertDate: function(dateTime){
      let dateComponents = dateTime.split('T');
      let date = dateComponents[0].split("-");
      let time = dateComponents[1].substring(0,8).split(":");
      return `${date[0]}/${date[1]}/${date[2]} ${time[0]}:${time[1]}:${time[2]}`
    },



    likes: function(){
      axios({
        method:'POST',
        url: `http://127.0.0.1:8000${document.location.pathname}/likes/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then(()=>{
        this.$store.dispatch('getLikes', document.location.pathname)
         
      })
    },
    update: function(idx){
      this.$router.push({name:'Update', params:{article_pk:idx}})
    },
    delArticle: function(){
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000/community/${this.article.id}/`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
        data: this.article,

      })
      .then(()=>{
        this.$router.push({name:'Community'})
      })
      .catch(()=>{
        alert('접근권한이 없습니다.')
      })
    },
    getProfile: function(){
      this.$router.push({name:'Profile', params:{ user_name:this.article.username }})
    },

 
    
   
  },
  created: function(){
    this.$store.dispatch('getUsername')
    // 게시글 하나 조회
    this.$store.dispatch('getPostD', document.location.pathname)
    //게시글에 달린 좋아요 조회
    this.$store.dispatch('getLikes', document.location.pathname) 

   
  },

  
    
  
  
  
    
   
  
  
 

  
}
</script>

<style>

</style>
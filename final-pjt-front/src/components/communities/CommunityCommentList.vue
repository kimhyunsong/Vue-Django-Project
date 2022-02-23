<template>
  <div class="container" align="left">
    <div v-for="comment in comments" :key="comment.id">
    <span v-if="username===comment.username">
      <md-content class="container border: 4px" style="border-radius:0.8em; border-style: inset; background-color: #000000">
        <div style="font-style:italic; color:white" align="left">{{comment.username}} : {{comment.content}} {{comment}} <span align="right"> <md-chip @click="deleteComment(comment.id)" class="md-accent" md-clickable>삭제하기</md-chip></span></div>&nbsp;
        
      </md-content>
        
        </span>
      <br>
    </div>

    <md-field>
      <label>Textarea</label>
      <md-textarea v-model="newComment"
      @keyup.enter="createComment"
      ></md-textarea>
    </md-field>
    <div class="container" align="right" style="margin-top:20px;">
      <md-chip class="md-dense md-raised md-default" @click="createComment" md-clickable>작성</md-chip>
    </div>
    <br>




   


  </div>
</template>

<script>

import axios from 'axios'
export default {
  name:'CommunityCommentList',
  created: function(){
    this.$store.dispatch('getCommunityList', document.location.pathname)
    this.$store.dispatch('getUsername')
  },
  data: function(){
    return{
      newComment: null,
    }
  },
  
  methods:{
   
    createComment: function(){
      if (this.newComment) {
        axios({
          method: 'POST',
          url: `http://127.0.0.1:8000${document.location.pathname}/comment/`, 
          headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          },
          data: {content : this.newComment},
        })
        .then(()=>{
          this.$store.dispatch('getCommunityList', document.location.pathname)
          this.newComment=null
        })
        .catch((err)=>{
          console.log(err)
        })
    
      }
      
    },
    deleteComment: function(idx){
        axios({
          method:'DELETE',
          url: `http://127.0.0.1:8000${document.location.pathname}/comment/${idx}`,
          headers:{
            Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
        })
        .then(()=>{
          this.$store.dispatch('getCommunityList', document.location.pathname)
        })
        .catch(()=>{
          alert('접근 권한이 없습니다.')
        })
      }
    },
    computed: {
    comments: function(){
      return this.$store.state.comments
    },
    config: function(){
      return this.$store.state.config
    },
    username: function(){
      return this.$store.state.username
    }
    

}
}
</script>

<style>

</style>
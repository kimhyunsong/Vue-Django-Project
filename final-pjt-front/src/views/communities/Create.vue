<template>
  <div>
    
    <h1>Community Article</h1>
    <md-field class="container">
      <label>제목을 입력하세요</label>
      <md-input v-model="article.title" autofocus></md-input>
    </md-field>
    <md-field class="container">
      <label>Textarea</label>
      <md-textarea v-model="article.content" @keyup.enter="post"></md-textarea>
    </md-field>
    <div class="container" align="right">
      <md-chip class="md-dense md-raised md-default" @click="post" md-clickable>작성</md-chip>
    </div>
    <br>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'Create',
  data: function (){
    return {
      article:{
      title: null,
      content: null,
      }
      
    }
  },
  methods:{
    post: function () {
      const article = {
        title : this.article.title,
        content : this.article.content
      }
      if (article.title && article.content){
      axios ({
        method: 'POST',
        url: 'http://127.0.0.1:8000/community/',
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
        data: article,

      })
      .then((res)=>{
        article.title=null,
        article.content=null,
        //생성후 상세 페이지로 가기전 로드
        this.$store.dispatch('getPost',res.data.id)
        this.$router.push({name:'Detail', params:{article_pk:res.data.id}})
        })
      .catch((err)=> {
        console.log(err)
      })
      }
      
    }
  },
  created: function(){
  }
  
  }

  
</script>

<style>

</style>
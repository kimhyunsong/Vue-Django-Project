<template>
  <div class="container">

    <h1>Community Article Update</h1>
    <md-field class="container">
      <label>제목을 입력하세요</label>
      <md-input v-model="article.title" autofocus></md-input>
    </md-field>
    <md-field class="container">
      <label>Textarea</label>
      <md-textarea v-model="article.content" @keyup.enter="Updatearticle"></md-textarea>
    </md-field>
    <div>
      <md-chip class="md-dense md-raised md-default" @click="Updatearticle" md-clickable>글 수정</md-chip>
    </div>
  
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'Update',

  methods:{    
    Updatearticle: function () {
      if (this.article.title && this.article.content){
      axios ({
        method: 'PUT',
        url: `http://127.0.0.1:8000/community/${this.article.id}/`,
        headers: {
          Authorization : `JWT ${localStorage.getItem('jwt')}`
        },
        data: this.article,
      })
      .then((res)=>{    
        this.$router.push({name:'Detail', params:{article_pk:res.data.id}})
      })
      .catch(()=> {
        alert('접근권한이 없습니다.')
      })
      }
    }
  },
  computed:{
    article: function() {
      return this.$store.state.post
    },

  },
  created: function(){
    this.$store.dispatch('getPostD', document.location.pathname)



  }
  }
 

</script>

<style>

</style>
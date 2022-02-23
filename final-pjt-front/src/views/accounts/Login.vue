<template>
  <div class="container" style="width:300px">

    <md-field>
      <label>아이디를 입력하세요</label>
      <md-input v-model="credentials.username" autofocus></md-input>
    </md-field>
    <md-field>
      <label>비밀번호</label>
      <md-input @keyup.enter="login" v-model="credentials.password" type="password"></md-input>
    </md-field>
    <div>
      <md-chip class="md-dense md-raised md-default" @click="login" md-clickable>login</md-chip>
    </div>
    <br>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Login',
  data: function (){
    return {
      credentials:{
        username: null,
        password: null,
      }
    }
  },
  methods: {
   login: function(){
     axios({
       method:'post',
       url:'http://127.0.0.1:8000/accounts/login/',
       data: this.credentials
     })
     .then(res=>{
      //토큰 설정하고
       localStorage.setItem('jwt', res.data.token)
       //로그인 확인을 emit한다.
       this.$emit('login')
       // 로그인 이후 필요한 커뮤니티 로드
       this.$store.dispatch('getPosts')
       this.$store.dispatch('getUsername')
       this.$router.push({name:'MovieList'})
     
     })
     .catch(()=>{
       this.$fire({
        title: '알수 없는 회원 정보',
        text: `아이디나 비밀번호가 일치하지 않습니다.`,
        type: "error",
        timer: 3000
      }).then((r)=> {
        console.log(r.value)
     })
    })
   } 
  }

}
</script>

<style>

</style>
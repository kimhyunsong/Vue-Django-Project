<template>
  <div class="container" style="width:300px">
    <h1>Signup</h1>

    <md-field>
      <label>사용자 아이디</label>
      <md-input v-model="credentials.username"></md-input>
    </md-field>


    <md-field>
      <label>비밀번호</label>
      <md-input v-model="credentials.password" type="password"></md-input>
      
    </md-field>


    <md-field>
      <label>비밀번호 확인</label>
      <md-input
      @keyup.enter='signup'
      v-model="credentials.passwordConfirmation" type="password"></md-input>
      
    </md-field>
    <div><md-chip class="md-dense md-raised md-default" @click="signup" md-clickable>회원가입</md-chip></div>
   
   <br>

   

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Signup',
  data (){
    return {
      credentials:{
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function(){
      axios({
        method:'POST',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
      .then(()=>{
        axios({
        method: 'POST',
        url:'http://127.0.0.1:8000/accounts/login/',
        data: this.credentials
        })
                .then(res=>{
                  localStorage.setItem('jwt', res.data.token)
                  this.$emit('login')
                  //프로필 로드전에 필요한 사용자 이름생성
                  this.$store.dispatch('getUsername')
                  this.$fire({
                    title: "성공적으로 가입되었습니다.",
                    type: "success",
                    timer: 3000
                  }).then(r => {
                  console.log(r.value);
                  });
                  this.$router.push({name:'Community'})
                })
                .catch((err)=>{
                    console.log(err)
                })
      })
      .catch(() =>{
        if (this.credentials.password === this.credentials.passwordConfirmation){
            this.$fire({
                text: `이미 가입한 사용자가 있습니다.`,
                type: "error",
                timer: 3000
              }).then((r)=> {
                console.log(r.value)
          })
          } else {
            this.$fire({
                text: `비밀번호가 일치하지 않습니다.`,
                type: "error",
                timer: 3000
              }).then((r)=> {
                console.log(r.value)
          }) 
        }
    })
    }
    }
  }
</script>

<style>

</style>

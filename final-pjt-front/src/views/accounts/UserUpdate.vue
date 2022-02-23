<template>
  <div class="container" style="width:300px">
    <h1>Update</h1>

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
      @keyup.enter='update'
      v-model="credentials.passwordConfirmation" type="password"></md-input>
      
    </md-field>
   <div> <button @click="update">회원정보 수정</button></div>
   <br>

   

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'UserUpdate',
  data (){
    return {
      credentials:{
        username: null,
        password: null,
        passwordConfirmation: null,
      },
      isLogin: false,

    }
  },
  computed:{
    username: function(){
      return this.$store.state.username
    }
  },
  methods: {
    update: function(){
      axios({
        method:'PUT',
        url: `http://127.0.0.1:8000/accounts/${this.username}/update/`,
        data: this.credentials,
        headers: {
          Authorization : `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then(()=>{
        axios({
        method: 'POST',
        url:'http://127.0.0.1:8000/accounts/login/',
        data: this.credentials
        })
          .then(()=>{
            localStorage.removeItem('jwt')  
            this.$emit('logout')
            alert('정보가 수정되었습니다. 다시 로그인해 주세요')
            this.$router.push({name:'Login'})
          })
          .catch(err=>{
            console.log(err)
          })
      })
      .catch(err =>{
        console.log(err)
      })
    }
  },
  created: function(){
    //유저 정보를 미리 가져옴.
    this.$store.dispatch('getUsername')
},
  
}
</script>

<style>

</style>
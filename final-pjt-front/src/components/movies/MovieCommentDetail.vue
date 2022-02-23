<template>
  <div>
    <br>
   <div class="container" align="left"  
    v-for="review in reviews" :key="review.id">
      <md-content class="container border: 4px"
      style="border-radius:0.8em; border-style: inset; background-color:#000000"
      >
      <star-rating
        :rating=review.vote
        :read-only=true
        :star-size="20"
        style="margin-bottom:1.2em"
        ></star-rating> 
      <div>
        <b style="font-style:italic; color:white">{{review.username}} : {{review.content}} <p> 작성시간 : </p>
         <span v-if="username === review.username"> 
        <md-chip @click.native="deleteReview(review.id)" class="md-accent" md-clickable>삭제하기</md-chip>
          </span></b> 
          
      </div> &nbsp;
      
      <br>
      </md-content>
      <br>

   </div>

    

    <div>
      <md-field class="container">
      <label>Textarea</label>
      <md-textarea v-model="reviewInput"
      @keyup.enter="createReview"
      ></md-textarea>
      </md-field>    
      <div class="container" align="right" style="margin-bottm:20px">
        
        
        
        <star-rating
          inline
          @rating-selected ="setRating"
          
          :max-rating="5"
          inactive-color="#000"
          active-color="#ffd055"
          :star-size="20"
          v-model="rating">
        </star-rating>
        <div style="margin-top:20px;">
        <md-chip class="md-dense md-raised md-default" @click="createReview" md-clickable>작성</md-chip>
        </div>
      </div>
  
    </div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import axios from 'axios'
export default {
  name:'MovieCommentDetail',
  components:{
    StarRating
  },
  data: function(){
    return {
      reviewInput: null,
      rating: 0,
    }
  },
  created: function(){
    this.$store.dispatch('getReviews', document.location.pathname)
    this.$store.dispatch('getUsername')
  },
  methods:{

    convertDate: function(responseDate) {
      let dateComponents = responseDate.split('T');
      let date = dateComponents[0].split("-");
      let time = dateComponents[1].substring(0,8).split(":");
      return `${date[0]}/${date[1]}/${date[2]} ${time[0]}:${time[1]}:${time[2]}`
    },



    deleteReview: function(idx){   
      console.log(idx)
      if (idx.username !== this.username) {
      axios({
        method: 'DELETE',
        url: `http://127.0.0.1:8000${document.location.pathname}/review/${idx}`,
        headers: {
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
      })
      .then(()=>{
        this.$store.dispatch('getReviews',document.location.pathname)
      })
      } else {
        alert('접근 권한이 없습니다.') //수정 필요
      }
    },
    setRating: function(rating){
      this.rating=rating
    },
    createReview: function(){
      if (this.reviewInput){
      axios({
        method: 'POST',
        url: `http://127.0.0.1:8000${document.location.pathname}/review/`,
        data: {
          content:this.reviewInput,
          vote: this.rating
          },
        headers: {
            Authorization: `JWT ${localStorage.getItem('jwt')}`
          },
      })
      .then(()=>{
        this.$store.dispatch('getReviews',document.location.pathname)
        this.reviewInput= null
        this.rating=0
      })
    } else {
      alert('게시글을 작성하세요')
    }
    }
  },
  computed:{
    reviews: function(){
      return this.$store.state.reviews
    },
    username: function(){
      return this.$store.state.username
    }
  }
}
</script>

<style>

</style>
<template>
  <div class="overflow-auto container">

  <b-table bordered outlined dark :fields="fields" :items="items">
    <!--actions를 필드에 추가 -->
    <template #cell(actions)="row">  
      
      <b-button size="sm" @click="detailPage(row.item.id)" >
        Detail
      </b-button>
    </template>
  </b-table>
  
  </div>
</template>



<script>
import axios from 'axios'
export default {
  name:'Community',
  data(){
    return {
      items: [],
       fields: [
        {
          label: '작성자',
          key: 'username',
        },
        {
          label: '제목',
          key: 'title',
          
        },
        {
          label: '작성 시간',
          key: 'created_at',
        },
        {
          label: '상세 정보',
          key: 'actions'
        },
      
      ],
      headVariant: 'dark',
    
    }
  },


  methods:{
    
    // 게시글 상세조회(인자 = 게시글 id)
     detailPage (page){
      //로그인 여부 분기
      if (localStorage.getItem('jwt')){ 
        this.$store.dispatch('getPost', page)
        this.$router.push({name:'Detail', params:{ article_pk:page}})
      } else {
        this.$router.push({name:'Login'})
      }
    },
  },
  


  created: function() {
    axios({
      method:'get',
      url: 'http://127.0.0.1:8000/community/',
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        }
    })
    .then((res) =>{
      //차후 게시글 30번째 이상일때 수정필요시 수정
      for (var i = 0; i < res.data.length; i++) {
        res.data[i].created_at = this.convertDate(res.data[i].created_at)
        this.items.push(res.data[i])
      }
    })
    
  },
  

}
</script>

<style>

</style>
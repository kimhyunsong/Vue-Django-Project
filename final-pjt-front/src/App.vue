<template>
  <div id="app" class="b-container">

    <b-navbar class="" id="navbar" type="dark" variant="dark">
      <b-navbar-nav>
        <b-nav-item>
          <router-link :to="{ name:'MovieList'}" style="color:white; text-decoration:none; margin-left: 30px">
            Movie
          </router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link :to="{ name:'MovieRecommend'}" style="color:white; text-decoration:none; margin-left: 30px">
            MovieRecommend
          </router-link>
        </b-nav-item>
        <!-- Navbar dropdowns -->
        <b-nav-item-dropdown v-if="isLogin" text="Community" right>
          <b-dropdown-item href="#">
            <router-link :to="{ name:'Community' }" style="color:black; text-decoration:none;">
              Community
            </router-link>
          </b-dropdown-item>
          <b-dropdown-item href="#">
            <router-link :to="{ name:'Create' }" style="color:black; text-decoration:none;">
              Create
            </router-link>
          </b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item>
        <search-bar v-if="isLogin"></search-bar>
        </b-nav-item>

        
        <b-nav-item-dropdown text="User" right>
          <span v-if="isLogin">
            <b-dropdown-item>
              <router-link :to="{ name:'Profile', params:{user_name:username} }" style="color:black; text-decoration:none;">
                Profile
              </router-link>
            </b-dropdown-item>
            <b-dropdown-item>
              <router-link @click.native="logout" to='#' style="color:black; text-decoration:none;">
                logout
              </router-link>
            </b-dropdown-item>
          </span>
          <span v-else>
            <b-dropdown-item>
              <router-link :to="{ name:'Signup'}" style="color:black; text-decoration:none;">
                Signup
              </router-link>
            </b-dropdown-item>
            <b-dropdown-item>
              <router-link :to="{ name:'Login' }" style="color:black; text-decoration:none;">
                Login
              </router-link>
            </b-dropdown-item>
          </span>
        </b-nav-item-dropdown>
      </b-navbar-nav>
      
    </b-navbar>
    <router-view @login="confirm" @logout="unconfirm"/>

  </div>
</template>



<script>
import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import VueGoodTablePlugin from 'vue-good-table';
import SearchBar from '@/components/SearchBar.vue'



// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-good-table/dist/vue-good-table.css'
import VueCarousel from 'vue-carousel'


// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
Vue.use(VueMaterial)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
Vue.use(VueGoodTablePlugin);
Vue.use(VueCarousel)

import axios from 'axios'
export default{
  name: 'App',
  components:{
    SearchBar,
  },
  data: function(){
    return {
      isLogin : false,
      
    }
  },
  computed: {
    username: function(){
      return this.$store.state.username
    }
  },
  
  methods:{
    confirm: function(){
      this.isLogin = true
    },
    unconfirm: function(){
      this.isLogin = false
    },
    logout: function(){
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({name:'Login'})
    }
  },


  created: function(){
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/movies/`,
      })
      .then((res) =>{
        this.$store.state.firstMovie= res.data
      })
    


    this.$store.dispatch('firstData')
    if (localStorage.getItem('jwt')) {
      this.isLogin = true
      this.$store.dispatch('getPosts')
      this.$store.dispatch('getUsername')
    } else {
      this.isLogin = false
    }
      
    
  }, 
}
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
}

#navbar {
  margin-bottom: 30px;
}



</style>

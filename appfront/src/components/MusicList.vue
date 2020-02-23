<template>
    <div class = "MusicList">
        <el-button type="primary" @click="searchSongs()" style="float:left; margin: 2px;">新增</el-button>
        <aplayer autoplay
         :music = musicList
        />
    </div>

</template>

<script>
  import Vue from "vue";
  import axios from 'axios';
  import Aplayer from 'vue-aplayer'
  Vue.prototype.$http = axios
  export default {
      name: 'MusicList',
      data () {
        return {
          input:"",
          musicList:[],
          title:"你是我的眼",
          artist:"林宥嘉",
          "pic":"https://moeplayer.b0.upaiyun.com/aplayer/secretbase.jpg",
          "src":"https://moeplayer.b0.upaiyun.com/aplayer/secretbase.mp3"
        }
      },
      methods:{
        searchSongs(){
          this.$http.get('http://127.0.0.1:8000/index')
          .then((response) =>{
            var response = response.data
            
            var hotSong = response["hotsong_json"].data
            console.log(hotSong)
            for(var song in hotSong){
              console.log(hotSong[song])
              let waitsong = {}
              waitsong.artist = hotSong[song].searchWord,
              waitsong.title = hotSong[song].searchWord,
              waitsong.pic = "https://moeplayer.b0.upaiyun.com/aplayer/secretbase.jpg",
              waitsong.src = "https://moeplayer.b0.upaiyun.com/aplayer/secretbase.mp3"
              this.musicList.push(waitsong)
            }
            console.log(this.musicList)
          })
        }
      },
      components:{
        Aplayer
      }
    }

</script>
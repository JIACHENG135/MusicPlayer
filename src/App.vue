<template>
  <div id="app">
    <div class="container">
      <h1 align="center">Vue-APlayer</h1>


      <el-input
        placeholder="请输入内容"
        v-model="input4">
        <i @click="searchSong();jumpOver()" ref="bubble" slot="prefix" class="el-input__icon el-icon-search bubble-wrapper"></i>
      </el-input>

      <aplayer
        float
        showLrc
        :music="{
            title: list3[0].title,
            artist: list3[0].artist,
            src: list3[0].src,
            pic: list3[0].pic,
            lrc: list3[0].lrc,
          }"
        :list='list3'
        :lrcType="3"
      />
  <el-carousel :interval="4000" type="card" height="200px">
    <el-carousel-item v-for="item in albumList" :key="item.id" >

      <el-card :body-style="{ padding: '0px' }">
        <el-image :src="item.picUrl" @click="updateListByAlbum(item.id)"></el-image>
        <div style="padding: 14px;">
          <span>好吃的汉堡</span>
        </div>
      </el-card>
    </el-carousel-item>
  </el-carousel>
  <!-- <animator></animator> -->
  <!-- <iconrotor ref="foo"></iconrotor> -->
    </div>
  </div>
</template>
<script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.15.2/axios.js"></script>
<script>
  function SearchRotate(){
   this.refs.foo.jumoOver();
  }
</script>>
<script>
  import Aplayer from 'vue-aplayer'
  import MusicList from "./components/MusicList"
  import Animator from "./components/Animator"
  import IconRotor from "./components/IconRotor"
  import axios from 'axios';
  import Vue from "vue";
  import { TimelineLite, Back, Elastic, Expo } from "gsap"

  Vue.prototype.$http = axios
  export default {
    name: 'App',
    components: {
      Aplayer,"animator":Animator,'iconrotor':IconRotor,
    },
    data () {
      return {
        muted: false,
        music3: null,
        albumList: [],
        input4:"周杰伦",
        list3: [
          {
            title: '前前前世',
            artist: 'RADWIMPS',
            src: "http://m8.music.126.net/20200221141856/e9e282cb745e4134da9089ca48a2af4a/ymusic/0fd6/4f65/43ed/a8772889f38dfcb91c04da915b301617.mp3",
            pic: 'https://p1.music.126.net/uIFI3Zx-3aiMNsFlAMBxBQ==/109951163142162226.jpg',
            lrc: 'https://cn-east-17-aplayer-35525609.oss.dogecdn.com/yourname.lrc',
          },
        ],
      }
    },
    mounted:function(){
      this.addHQAlbum();
      this.searchSong();
    },
    methods:{
      // Add top soongs
      addhotSongs(){
        this.$http.get('http://127.0.0.1:8000/index')
          .then((response) => {
            // console.log(response.error_num)
            // var res = JSON.parse(response.data)
            var songs= response.data
            this.list3 = []
            for(var i=0;i<songs.length;i++){
              this.list3.push({
                src:songs[i].src,
                lrc:songs[i].lrc,
                title:songs[i].title,
                artist:songs[i].artist,
                pic:songs[i].pic,
              })
            }
            })
          },
      // Create high qualified album
      addHQAlbum(){
        console.log("Try to add album")
        this.$http.get('http://127.0.0.1:8000/index/addAlbum')
        .then((response) => {
          var res = response.data.albums
          console.log(res)
          for(var i = 0;i<6;i++){
            this.albumList.push(res[i]);
          }
        })
      },

      searchSong(){
        // this.$refs.foo.jumpOver()
        this.$http.get('http://127.0.0.1:8000/index/searchSong/' + this.input4)
          .then((response) => {
            var songs= response.data
            this.list3 = []
            for(var i=0;i<songs.length;i++){
              if(songs[i].src!=0){
                this.list3.push({
                  src:songs[i].src,
                  lrc:songs[i].lrc,
                  title:songs[i].title,
                  artist:songs[i].artist,
                  pic:songs[i].pic,
                })
              }

            }
            })
      },

      updateListByAlbum(albumID){
        this.$http.get('http://127.0.0.1:8000/index/updateList/' + albumID)
          .then((response) => {
            var songs= response.data


            var i = 0
            while (this.list3.length>1){
              this.list3.pop()
            }
            while(i<5){
              this.list3.push({
                src:songs[i].src,
                lrc:songs[i].lrc,
                title:songs[i].title,
                artist:songs[i].artist,
                pic:songs[i].pic,
              })
              i += 1;
            }
            })
      },




          jumpOver(){
            const { bubble, bubblePulse } = this.$refs
            const timeline = new TimelineLite()
            timeline.to(bubble, 0.4, {
            scale: 0.5,
            rotation: 16,
            ease: Back.easeOut.config(1.7),
            })   

            
            timeline.to(bubble, 1.0, {
            scale: 1,
            rotation: '-=16',
            ease: Elastic.easeOut.config(2.5, 0.5),
            })

            }



      },

  
  }


</script>
<style>
  html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;
  }
  body {
    font-family: Source Sans Pro, 'PingFang SC', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    background: linear-gradient(135deg, rgb(65, 184, 131), rgb(74, 156, 238));
    color: #fff;
    overflow-y: auto;
  }
  #app {
    text-align: center;
  }
  .container {
    max-width: 32rem;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 50px;
    padding: 0 15px;
  }
  h1 {
    font-size: 48px;
    margin: 30px 0 10px;
  }
  h3 {
    font-size: 24px;
  }
  input {
    background-color: transparent;
    outline: none;
    border: none;
    color: inherit;
    font-size: inherit;
    text-align: center;
    border-bottom: 1px solid rgba(255, 255, 255, .5);
  }
  a {
    color: #35495e;
    text-decoration: none;
  }
  p {
    font-size: 18px;
  }
  /* for carousel from ElementUI */
    .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }


  .bubble {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid white;
  background: #272727;
  border-radius: 50%;
  height: 100px;
  width: 100px;
}
.bubble-pulse {
  position: absolute;
  z-index: 1;
  height: 120px;
  width: 120px;
  top: 50%;
  left: 50%;
  margin-top: -60px;
  margin-left: -60px;
  background: #272727;
  border-radius: 50%;
  opacity: 0;
  transform: scale(0);
}
.bubble-image {
  height: 50%;
}
</style>
import Vue from 'vue'
import Router from 'vue-router'
import MusicList from '@/components/MusicList'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MusicList',
      component: MusicList
    }
  ]
})

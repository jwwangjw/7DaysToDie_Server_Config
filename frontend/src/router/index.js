/*
 * @Descripttion: 
 * @version: 
 * @Author: wjw
 * @Date: 2022-02-08 12:06:25
 * @LastEditors: wjw
 * @LastEditTime: 2022-02-08 15:10:06
 */
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path:'/setting',
    name:'setting',
    component: () => import('../components/setting.vue')
  },
  {
    path:'/more',
    name:'more',
    component:()=>import('../components/more.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

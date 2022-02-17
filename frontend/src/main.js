/*
 * @Descripttion: 
 * @version: 
 * @Author: wjw
 * @Date: 2022-02-08 12:06:25
 * @LastEditors: wjw
 * @LastEditTime: 2022-02-08 13:58:21
 */
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

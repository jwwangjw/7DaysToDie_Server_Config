<!--
 * @Descripttion: 
 * @version: 
 * @Author: wjw
 * @Date: 2022-02-08 12:06:25
 * @LastEditors: wjw
 * @LastEditTime: 2022-02-09 17:29:13
-->
<template>
  <div id="app">
     <el-container>
    <el-header>
    <div id="nav">
      <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      router
      @select="handleSelect"
    >
      <!-- 自定义logo组件 -->
      <el-menu-item index="0"> <svg t="1644300543118" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1422" width="200" height="50"><path d="M85.333333 170.666667a128 128 0 0 1 128-128h597.333334a128 128 0 0 1 128 128v128a42.666667 42.666667 0 1 1-85.333334 0V170.666667a42.666667 42.666667 0 0 0-42.666666-42.666667H213.333333a42.666667 42.666667 0 0 0-42.666666 42.666667v723.669333l324.010666-144a42.666667 42.666667 0 0 1 34.645334 0L853.333333 894.336V469.333333a42.666667 42.666667 0 1 1 85.333334 0v425.002667a85.333333 85.333333 0 0 1-119.978667 77.994667L512 836.010667 205.312 972.373333A85.333333 85.333333 0 0 1 85.333333 894.293333V170.666667z" fill="#75C82B" p-id="1423"></path><path d="M341.333333 298.666667a42.666667 42.666667 0 0 1 42.666667-42.666667h256a42.666667 42.666667 0 0 1 38.613333 60.842667l-170.666666 362.666666a42.666667 42.666667 0 1 1-77.226667-36.352L572.8 341.333333H384a42.666667 42.666667 0 0 1-42.666667-42.666666z" fill="#75C82B" p-id="1424"></path></svg></el-menu-item>

      <el-menu-item v-for="(item, i) in navList" :key="i" :index="item.name">
          <template slot="title">
            <span> {{ item.navItem }}</span>
          </template>
        </el-menu-item>

      <el-menu-item index="50">
        <i class="el-icon-search" />
        <el-input v-model="keyWord" size="mini" placeholder="搜索" />
      </el-menu-item>
      
      </el-menu>
    </div>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
  </div>
</template>
<script>
export default {
  data() {
    return {
      navList: [
        { name: "/setting", navItem: "七日杀配置文件生成" },
        { name: "/more", navItem: "待实现功能与使用说明" },
      ],
    };
  },
  components: {
  },
  methods:{
    handleSelect(key, keyPath) {
        console.log(keyPath)
      }
  }
}
</script>>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 0px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>

<!--
 * @Descripttion: 
 * @version: 
 * @Author: wjw
 * @Date: 2022-02-08 12:06:25
 * @LastEditors: wjw
 * @LastEditTime: 2022-02-09 17:47:36
-->
<template>
  <div class="hello" style="width:95%;margin-left:auto">
    <div class="demo-image__lazy" style="width:50%;height:400px;float:left">
      <el-image v-for="url in urls" :key="url" :src="url" lazy></el-image>
    </div>
    <div class="para" style="width:45%;float:right;background-color:	#C0C0C0">
      <p align=left style="padding:10px">关于作者：<br>一个爱好七日杀的萌新玩家<br>使用说明：<br>首先点击对应的生成按钮<br>填写并上传成功后下载<br>替换对应文件即可<br>问题反馈：1508417398@qq.com<br>本来想做一个服主管理器的，无奈没有相关的文档（大哭）</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'more',
  data() {
      return {
        urls: [
          'https://gitee.com/jiawei__wang/image/raw/master/img/20220209171346.jpg',
          'https://gitee.com/jiawei__wang/image/raw/master/img/20220209172932.jpg',
          'https://gitee.com/jiawei__wang/image/raw/master/img/20220209173026.jpg',
        ]
      }
  },
  props: {
    msg: String
  },
  methods:{
    getData(){ 
      let url='http://127.0.0.1:8000/';
      axios.get(url  + 'result/')
        .then(res => {
            console.log(res)
        }).catch(error => {
            console.log(error)
        })
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>

<template>
  <el-menu :default-active="route.path" router mode="horizontal">
    <el-menu-item index="/">GEP应用</el-menu-item>
    <el-menu-item index="/financing">融资信贷</el-menu-item>
    <el-menu-item index="/compensation">生态补偿</el-menu-item>
    <el-menu-item index="/trading">市场交易</el-menu-item>
    <el-menu-item index="/damage">损害赔偿</el-menu-item>
    <el-menu-item index="/others">其它</el-menu-item>
  </el-menu>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'
const route = useRoute()
</script>
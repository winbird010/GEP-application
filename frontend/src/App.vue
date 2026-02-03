<template>
  <el-container class="layout-container">
    <!-- 顶部 Header -->
    <el-header class="app-header" height="60px">
      <div class="header-content">
        <h1 class="header-title">GEP应用平台</h1>
      </div>
    </el-header>

    <el-container class="main-container">
      <!-- 左侧边栏菜单 -->
      <el-aside width="200px" class="sidebar">
        <el-menu
          :default-active="$route.path"
          router
          class="sidebar-menu"
          background-color="#304156"
          text-color="#bfcbd9"
          active-text-color="#409EFF"
        >
          <el-menu-item index="/">
            <el-icon><HomeFilled /></el-icon>
            <span>首页</span>
          </el-menu-item>

          <el-menu-item index="/financing">
            <el-icon><Money /></el-icon>
            <span>融资信贷</span>
          </el-menu-item>

          <el-menu-item index="/compensation">
            <el-icon><ScaleToOriginal /></el-icon>
            <span>生态补偿</span>
          </el-menu-item>

          <el-menu-item index="/trading">
            <el-icon><ShoppingCart /></el-icon>
            <span>市场交易</span>
          </el-menu-item>

          <el-menu-item index="/damage">
            <el-icon><Warning /></el-icon>
            <span>损害赔偿</span>
          </el-menu-item>

          <el-menu-item index="/others">
            <el-icon><More /></el-icon>
            <span>其它</span>
          </el-menu-item>
        </el-menu>
      </el-aside>

      <!-- 主内容区 -->
      <el-main class="main-content">
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'
import { HomeFilled, Money, ScaleToOriginal, ShoppingCart, Warning, More } from '@element-plus/icons-vue'

const $route = useRoute()
</script>

<style scoped>
.layout-container {
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}

.app-header {
  background-color: #fff;
  border-bottom: 2px solid #e4e7ed;  /* 横线分隔 */
  padding: 0 20px;
  display: flex;
  align-items: center;
  box-shadow: 0 1px 4px rgba(0,21,41,.08);
}

.header-content {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

.header-title {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
  color: #303133;
  text-align: left;  /* 左对齐 */
  line-height: 60px;
}

.main-container {
  height: calc(100vh - 60px);
  overflow: hidden;
}

.sidebar {
  background-color: #304156;
  box-shadow: 2px 0 6px rgba(0,21,41,.35);
  overflow-y: auto;
}

.sidebar-menu {
  border-right: none;
  height: 100%;
}

.sidebar-menu .el-menu-item {
  height: 50px;
  line-height: 50px;
  padding-left: 20px !important;
}

.sidebar-menu .el-menu-item:hover {
  background-color: #263445 !important;
}

.sidebar-menu .el-menu-item.is-active {
  background-color: #263445 !important;
  border-right: 3px solid #409EFF;
}

.main-content {
  background-color: #f0f2f5;
  padding: 20px;
  overflow-y: auto;
  height: 100%;
}

/* 响应式：移动端侧边栏隐藏 */
@media (max-width: 768px) {
  .el-aside {
    width: 64px !important;
  }

  .sidebar-menu span {
    display: none;
  }

  .sidebar-menu .el-menu-item {
    padding-left: 20px !important;
    justify-content: center;
  }
}
</style>

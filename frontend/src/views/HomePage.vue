<template>
  <div>
    <h1>GEP 应用</h1>
    <div class="card-grid">
      <router-link v-for="item in modules" :key="item.slug" :to="`/${item.slug}`" class="card">
        <el-icon :size="48"><component :is="item.icon" /></el-icon>
        <h3>{{ item.title }}</h3>
        <p>{{ item.subtitle }}</p>
      </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
// import * as Icons from '@element-plus/icons-vue' // 暂无全局注册需求

const modules = ref([
  { slug: 'financing', title: '融资信贷', subtitle: '基于GEP核算的绿色金融支持', icon: 'Money' },
  { slug: 'compensation', title: '生态补偿', subtitle: '跨区域生态补偿机制', icon: 'Crop' },
  { slug: 'trading', title: '市场交易', subtitle: '生态产品市场化交易', icon: 'Shop' },
  { slug: 'damage', title: '损害赔偿', subtitle: '生态损害赔偿量化', icon: 'Warning' },
  { slug: 'others', title: '其它应用', subtitle: '考核评价与规划决策', icon: 'More' }
])
</script>

<style scoped>
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-top: 20px;
}
.card {
  display: block;
  padding: 20px;
  border: 1px solid #e4e7ed;
  border-radius: 8px;
  text-align: center;
  text-decoration: none;
  color: #303133;
  transition: box-shadow 0.3s;
}
.card:hover {
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
</style>
<template>
  <div class="home-container">
    <!-- Hero 区域：展示 home.py 的平台介绍 -->
    <div class="hero-section" v-if="homeData">
      <h1 class="main-title">{{ homeData.title }}</h1>
      <h2 class="sub-title">{{ homeData.subtitle }}</h2>
      <el-divider />
      <p class="hero-text">{{ homeData.hero }}</p>

      <!-- 统计数据：5+应用领域、100+案例等 -->
      <el-row :gutter="20" class="stats-row">
        <el-col :xs="24" :sm="8" v-for="stat in homeData.stats" :key="stat.label">
          <el-card class="stat-card" shadow="hover">
            <el-icon :size="40" color="#67C23A">
              <component :is="stat.icon" />
            </el-icon>
            <div class="stat-value">{{ stat.value }}</div>
            <div class="stat-label">{{ stat.label }}</div>
          </el-card>
        </el-col>
      </el-row>
    </div>

    <!-- 加载状态 -->
    <el-skeleton v-else :rows="10" animated />

    <!-- 5个应用领域入口（保留现有功能） -->
    <div class="modules-section">
      <h3 class="section-title">应用领域</h3>
      <el-row :gutter="20">
        <el-col :xs="24" :sm="12" :md="8" v-for="module in modules" :key="module.slug">
          <el-card
            class="module-card"
            shadow="hover"
            @click="$router.push(`/${module.slug}`)"
          >
            <div class="module-icon">
              <el-icon :size="32" color="#409EFF">
                <component :is="module.icon" />
              </el-icon>
            </div>
            <h4 class="module-name">{{ module.name }}</h4>
            <p class="module-desc">{{ module.desc }}</p>
          </el-card>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

// 与 ContentCard 相同的 API 调用方式
const homeData = ref<any>(null)

// 5个模块配置（与现有入口一致）
const modules = [
  {
    slug: 'financing',
    name: '融资信贷',
    desc: '基于GEP核算的绿色金融支持',
    icon: 'Money'
  },
  {
    slug: 'compensation',
    name: '生态补偿',
    desc: '跨区域生态补偿机制',
    icon: 'ScaleToOriginal'
  },
  {
    slug: 'trading',
    name: '市场交易',
    desc: '生态产品市场化交易',
    icon: 'ShoppingCart'
  },
  {
    slug: 'damage',
    name: '损害赔偿',
    desc: '环境损害量化赔偿',
    icon: 'Warning'
  },
  {
    slug: 'others',
    name: '其它应用',
    desc: '考核评价、规划决策等',
    icon: 'More'
  }
]

// 获取首页数据（调用 home.py 接口）
onMounted(async () => {
  try {
    const response = await axios.get('/api/home/')
    homeData.value = response.data
  } catch (error) {
    console.error('获取首页数据失败:', error)
    // 失败时显示默认数据（可选）
    homeData.value = {
      title: 'GEP应用平台',
      subtitle: '生态系统生产总值核算成果应用',
      hero: 'GEP核算已从理论走向实践...',
      stats: [
        { label: '应用领域', value: '5+', icon: 'Grid' },
        { label: '成功案例', value: '100+', icon: 'TrendCharts' },
        { label: '覆盖省份', value: '20+', icon: 'MapLocation' }
      ]
    }
  }
})
</script>

<style scoped>
.home-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

/* Hero 区域样式 */
.hero-section {
  text-align: center;
  margin-bottom: 60px;
  padding: 40px 20px;
  background: linear-gradient(135deg, #f0f9eb 0%, #ffffff 100%);
  border-radius: 12px;
}

.main-title {
  font-size: 36px;
  color: #303133;
  margin-bottom: 10px;
  font-weight: bold;
}

.sub-title {
  font-size: 20px;
  color: #67C23A;
  margin-bottom: 30px;
  font-weight: 500;
}

.hero-text {
  font-size: 16px;
  line-height: 2;
  color: #606266;
  text-align: justify;
  text-indent: 2em;
  margin: 20px 0 40px;
  white-space: pre-line;  /* 保留 home.py 中的换行符 */
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

/* 统计卡片样式 */
.stats-row {
  margin-top: 40px;
}

.stat-card {
  text-align: center;
  padding: 30px 20px;
  margin-bottom: 20px;
  transition: transform 0.3s;
}

.stat-card:hover {
  transform: translateY(-5px);
}

.stat-value {
  font-size: 36px;
  font-weight: bold;
  color: #67C23A;
  margin: 15px 0 5px;
}

.stat-label {
  font-size: 14px;
  color: #909399;
}

/* 应用领域区域 */
.modules-section {
  margin-top: 60px;
}

.section-title {
  font-size: 24px;
  color: #303133;
  text-align: center;
  margin-bottom: 30px;
  position: relative;
}

.section-title::after {
  content: '';
  display: block;
  width: 60px;
  height: 3px;
  background: #67C23A;
  margin: 10px auto 0;
  border-radius: 2px;
}

.module-card {
  cursor: pointer;
  text-align: center;
  padding: 30px 20px;
  margin-bottom: 20px;
  transition: all 0.3s;
  border: 1px solid #ebeef5;
}

.module-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.1);
  border-color: #67C23A;
}

.module-icon {
  margin-bottom: 15px;
}

.module-name {
  font-size: 18px;
  color: #303133;
  margin-bottom: 10px;
  font-weight: 600;
}

.module-desc {
  font-size: 14px;
  color: #909399;
  line-height: 1.5;
}

/* 响应式适配 */
@media (max-width: 768px) {
  .main-title {
    font-size: 28px;
  }

  .hero-text {
    font-size: 14px;
    text-indent: 1.5em;
  }

  .stat-value {
    font-size: 28px;
  }
}
</style>

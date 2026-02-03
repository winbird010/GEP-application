<template>
  <div class="home-container">
    <!-- 只保留 Hero 文本（平台介绍长文本） -->
    <div class="hero-section" v-if="homeData">
      <p class="hero-text">{{ homeData.hero }}</p>

      <!-- 统计数据 -->
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
    <el-skeleton v-else :rows="6" animated />

    <!-- 应用领域入口卡片 -->
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
import { Money, ScaleToOriginal, ShoppingCart, Warning, More } from '@element-plus/icons-vue'

const homeData = ref<any>(null)

const modules = [
  { slug: 'financing', name: '融资信贷', desc: '基于GEP核算的绿色金融支持', icon: 'Money' },
  { slug: 'compensation', name: '生态补偿', desc: '跨区域生态补偿机制', icon: 'ScaleToOriginal' },
  { slug: 'trading', name: '市场交易', desc: '生态产品市场化交易', icon: 'ShoppingCart' },
  { slug: 'damage', name: '损害赔偿', desc: '环境损害量化赔偿', icon: 'Warning' },
  { slug: 'others', name: '其它应用', desc: '考核评价、规划决策等', icon: 'More' }
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
      hero: 'GEP核算已从理论走向实践，生态价值正在变为"真金白银"。从四川巴州的GEP质押贷款，到湖北神农架-襄阳的' +
        '"水质对赌"补偿，再到重庆开州-宣汉的跨省生态指标交易，全国各地已涌现出融资信贷、生态补偿、市场交易、损害赔偿' +
        '等多个领域的成功案例，证明了GEP核算能带来实实在在的收益。当前，虽然国家层面统一的制度设计尚在完善，地方实践' +
        '也因支持力度不同而进展不一，但"绿水青山就是金山银山"的理念已深入人心。随着国家生态文明建设的深化，更多标准化、' +
        '市场化的政策工具必将出台，GEP核算的应用前景广阔。率先探索的地方，不仅将获得生态与经济的双重回报，更将在未来的' +
        '绿色发展格局中占据先机。',
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
  max-width: 100%;
  margin: 0 auto;
}

/* Hero 区域：只保留文本 */
.hero-section {
  background: #fff;
  padding: 30px;
  border-radius: 8px;
  margin-bottom: 20px;
  box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
}

.hero-text {
  font-size: 16px;
  line-height: 2;
  color: #606266;
  text-align: justify;
  text-indent: 2em;
  margin: 0 0 30px 0;  /* 移除上方 margin，因为去掉了标题 */
  white-space: pre-line;
}

/* 统计卡片 */
.stats-row {
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid #ebeef5;
}

.stat-card {
  text-align: center;
  padding: 20px;
  transition: transform 0.3s;
}

.stat-card:hover {
  transform: translateY(-3px);
}

.stat-value {
  font-size: 32px;
  font-weight: bold;
  color: #67C23A;
  margin: 10px 0 5px;
}

.stat-label {
  font-size: 14px;
  color: #909399;
}

/* 应用领域 */
.modules-section {
  margin-top: 30px;
}

.section-title {
  font-size: 20px;
  color: #303133;
  margin-bottom: 20px;
  padding-left: 10px;
  border-left: 4px solid #67C23A;
}

.module-card {
  cursor: pointer;
  text-align: center;
  padding: 25px 20px;
  margin-bottom: 20px;
  transition: all 0.3s;
  background: #fff;
}

.module-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0,0,0,.1);
  border-color: #67C23A;
}

.module-icon {
  margin-bottom: 15px;
}

.module-name {
  font-size: 16px;
  color: #303133;
  margin-bottom: 8px;
  font-weight: 600;
}

.module-desc {
  font-size: 13px;
  color: #909399;
  line-height: 1.5;
}
</style>

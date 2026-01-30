<template>
  <div class="content-card" v-if="content">
    <el-icon :size="48" color="#67C23A">
      <component :is="content.icon" />
    </el-icon>
    <h1>{{ content.title }}</h1>
    <h2>{{ content.subtitle }}</h2>
    <p class="content-text">{{ content.content }}</p>
  </div>
  <el-skeleton v-else :rows="5" animated />
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useContentStore } from '@/stores/content'

const props = defineProps<{ slug: string }>()
const store = useContentStore()

const content = computed(() => store.currentContent)

// 自动加载
import { onMounted } from 'vue'
onMounted(() => store.fetchContent(props.slug))
</script>

<style scoped>
.content-card {
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 20px;
  text-align: center;
}
.content-text {
  font-size: 16px;
  line-height: 1.8;
  color: #333;
  margin-top: 20px;
}
</style>
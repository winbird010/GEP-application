<template>
  <ContentCard :slug="slug" />
</template>

<script setup lang="ts">
import ContentCard from '@/components/ContentCard.vue'
const slug = 'others'   // 每个文件改这里即可
</script>
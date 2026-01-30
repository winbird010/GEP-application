import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

export interface Content {
  id: number
  slug: string
  title: string
  subtitle: string
  content: string
  icon: string
}

export const useContentStore = defineStore('content', () => {
  const currentContent = ref<Content | null>(null)
  const loading = ref(false)
  const error = ref('')

  const fetchContent = async (slug: string) => {
    loading.value = true
    error.value = ''
    try {
      const response = await axios.get(`/api/contents/${slug}`)
      currentContent.value = response.data
    } catch (e) {
      error.value = '加载失败'
      console.error('[store] fetchContent failed:', e)   // ← 现在用了一次
    } finally {
      loading.value = false
    }
  }

  return { currentContent, loading, error, fetchContent }
})

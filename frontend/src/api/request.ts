import axios from 'axios'

// Render 会自动注入 VITE_API_BASE_URL，本地开发默认 localhost
const baseURL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

const instance = axios.create({
  baseURL,
  timeout: 10000,
})

export default instance

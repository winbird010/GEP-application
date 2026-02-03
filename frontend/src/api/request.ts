import axios from 'axios'

// 开发环境用相对路径 /api（走 Vite 代理），生产用绝对 URL
const baseURL = import.meta.env.VITE_API_BASE_URL || '/api'
// console.log('Request config loaded, timestamp:', Date.now())
// const baseURL = '/api'
console.log('Current baseURL:', baseURL) // 调试用，看控制台输出
const instance = axios.create({
  baseURL,
  timeout: 10000,
})

export default instance

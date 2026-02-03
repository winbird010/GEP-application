import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/financing', component: () => import('@/views/FinancingPage.vue') },
  { path: '/compensation', component: () => import('@/views/CompensationPage.vue') },
  { path: '/trading', component: () => import('@/views/TradingPage.vue') },
  { path: '/damage', component: () => import('@/views/DamagePage.vue') },
  { path: '/others', component: () => import('@/views/OthersPage.vue') },
]

export default createRouter({
  history: createWebHistory(),
  routes
})

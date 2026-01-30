import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],

  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  },

  // ---------- 开发服务器 ----------
  server: {
    port: 5173,
    proxy: {
      '/api': 'http://localhost:8000'
    },
    // 本地也带压缩 & 长缓存（调试无影响）
    headers: {
      'Cache-Control': 'public, max-age=31536000, immutable'
    }
  },

  // ---------- 生产构建 ----------
  build: {
    target: 'esnext',
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true
      }
    },
    chunkSizeWarningLimit: 1200,
    rollupOptions: {
      output: {
        // 手动拆包 + 内容哈希（长期缓存友好）
        manualChunks: {
          vue: ['vue', 'vue-router', 'pinia'],
          element: ['element-plus']
        },
        entryFileNames: 'assets/[name]-[hash].js',
        chunkFileNames: 'assets/[name]-[hash].js',
        assetFileNames: 'assets/[name]-[hash].[ext]'
      }
    },
    // 输出 gzip 大小报告（Vite 4+ 自动生成 .gz）
    reportCompressedSize: true,
    write: true
  }
})

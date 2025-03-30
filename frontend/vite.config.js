import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    proxy: {
      '/data': 'http://localhost:8000' // 👈 Redirige /data al backend real solo en desarrollo
    }
  }
})

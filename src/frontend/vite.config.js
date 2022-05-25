import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import ViteFonts from 'vite-plugin-fonts'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // Font Settings
    ViteFonts({
      google: {
        families: [
          'Open Sans',
          'Noto Sans Japanese',
        ],
      },
    }),
  ],
  // devServer Settings
  server: {
    host: true,
    watch: {
      usePolling: true,
    },
  },
})

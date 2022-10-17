const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: '../connect_telegram_ext/static',
  publicPath: '/static',
  pages: {
    setting: {
      entry: 'src/main.js',
      template: 'public/settings.html',
      filename: 'settings.html',
    },
  },
})

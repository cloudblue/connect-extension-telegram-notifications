<template>
  <TelegramSettings />
</template>

<script>
import createApp from '@cloudblueconnect/connect-ui-toolkit'
import TelegramSettings from './components/TelegramSettings.vue'

export default {
  name: 'App',
  components: {
    TelegramSettings
  },
  created(){
    createApp({});
  }
}
</script>

<style>
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
}
</style>

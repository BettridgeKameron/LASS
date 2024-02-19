<template>
  <div id="content">
    <AppHeader></AppHeader>
    <router-view />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import AppHeader from './components/AppHeader.vue'
export default defineComponent({
  name: 'App',
  components: {
    AppHeader
  }
})
</script>

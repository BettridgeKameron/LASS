<template>
  <div id="app" class="bg-gray-900">
    <StringInput />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import StringInput from './components/StringInput.vue'

export default defineComponent({
  name: 'App',
  components: {
    StringInput
  }
})
</script>

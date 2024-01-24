// This is just some random generated boilerplate code to have something initial
<template>
  <div class="container mx-auto p-4 max-w-2xl">
    <div class="flex flex-col space-y-4">
      <input
        v-model="userInput"
        type="text"
        class="w-full border-2 border-gray-300 p-2 rounded-md"
        placeholder="Enter a string"
      />
      <button
        @click="sendString"
        class="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Send
      </button>
      <div v-if="reversedString" class="text-green-500">Reversed String: {{ reversedString }}</div>
      <div v-if="errorMessage" class="text-red-500">Error: {{ errorMessage }}</div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import axios from 'axios'

export default defineComponent({
  name: 'StringInput',
  setup() {
    const userInput = ref('')
    const reversedString = ref('')
    const errorMessage = ref('')

    const sendString = async () => {
      errorMessage.value = '' // Reset error message
      try {
        const response = await axios.post('http://localhost:5000/reverse_string', {
          string: userInput.value
        })
        reversedString.value = response.data.reversed_string
      } catch (error) {
        errorMessage.value = 'Could not connect to the server.'
        console.error('Error:', error)
      }
    }

    return { userInput, reversedString, sendString, errorMessage }
  }
})
</script>

// This is just some random generated boilerplate code to have something initial
<template>
  <div class="container mx-auto p-4 max-w-2xl">
    <div class="mb-12">
      <h2 class="text-3xl font-bold mb-4">Compare Prints</h2>
      <div class="flex items-start justify-between">
        <p class="text-lg py-4">
          {{ currentPrompt }}
        </p>
        <button class="btn btn-neutral hover:bg-blue-700 ml-2" @click="nextPrompt">
          Next Prompt
        </button>
      </div>
    </div>
    <div class="flex flex-col space-y-4">
      <textarea
        v-model="userInput"
        type="text"
        style="height: 500px"
        class="w-full h-12 border-2 border-gray-300 p-2 py-2 rounded-md"
        placeholder="Enter a string"
      ></textarea>
      <button
        @click="sendString"
        class="btn btn-neutral w-full hover:bg-blue-700 font-bold py-2 px-4 rounded"
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
  },
  data() {
    return {
      prompts: [
        'What is your favorite color?',
        'What did you do today?',
        'Describe a memorable moment in your life'
      ],
      currentPromptIndex: 0
    }
  },
  computed: {
    currentPrompt() {
      return this.prompts[this.currentPromptIndex]
    }
  },
  methods: {
    nextPrompt() {
      //Increments the current prompt index or at least to 0 if at end
      this.currentPromptIndex = (this.currentPromptIndex + 1) % this.prompts.length
    }
  }
})
</script>

<template>
  <div class="container mx-auto p-4">
    <h1 class="text-4xl font-bold mb-2 py-10">Text Rephrasal Tool</h1>
    <div class="flex flex-col space-y-4">
      <div class="flex space-x-3">

        <textarea
          v-model="textToAnalyze"
          type="text"
          style="width: 800px; height: 500px;  resize: none;"
          class="border-2 border-gray-300 p-2 rounded-md"
          placeholder="Input: Enter a string"
        ></textarea>

        <textarea
          readonly
          style="width: 800px; height: 500px; resize: none;"
          class="w-1/2 border-2 border-gray-300 p-2 rounded-md self-end"
        >
        {{ rephrasedResult }}
        </textarea>
    </div>
      <button
          @click="rephraseText"
          class="w-1/3 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Rephrase
        </button>
      <div v-if="errorMessage" class="text-red-500">Error: {{ errorMessage }}</div>
    </div>
  </div>
</template>
  
  <script lang="ts">
  import { defineComponent, ref } from 'vue'
  import axios from 'axios'
  
  export default defineComponent({
    name: 'TextRephrase',
    setup() {
      const textToAnalyze = ref('')
      const errorMessage = ref('')
      const rephrasedResult = ref('')
  
      async function rephraseText() {
        errorMessage.value = '' // Reset error message
        try {
          const response = await axios.post('http://localhost:5000/api/v1/text/rephrase', {
            text: textToAnalyze.value 
          })
          rephrasedResult.value = response.data.rephrased_result;
          console.log('Response: ', response.data);
        } catch (error) {
          errorMessage.value = 'Could not connect to the server.'
          console.error('Error:', error)
        }
      }
  
      return {
        textToAnalyze, 
        rephrasedResult, 
        rephraseText, 
        errorMessage 
      }
    }
  })
  </script>
  
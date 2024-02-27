<template>
  <div class="container mx-auto p-4 max-w-2xl">
    <div class="mb-12">
      <h2 class="text-3xl font-bold mb-4">Sentiment Analysis</h2>
    </div>
    <div class="flex flex-col space-y-5">
      <textarea
        v-model="userInput"
        type="text"
        style="height: 500px"
        class="w-full h-12 border-2 border-gray-300 p-2 py-2 rounded-md bg-base-300"
        placeholder="Enter some words!"
      ></textarea>
      <button
        @click="sendString"
        class="btn btn-neutral w-full hover:bg-blue-700 font-bold py-2 px-4 rounded"
      >
        Send
      </button>
        <div class="box-content h-full p-2 border-2 border-gray-300 bg-base-300 rounded-md" v-if="markedResult != ''">
          <div v-if="markedResult" v-html="markedResult"></div>
          <br>
          <span class="text-red-500">Sentiment Score: </span>
          <div v-if="score !== undefined" class="text-red-500" v-html="score"></div>
          <div v-else class="text-red-500" v-html="0" style="display: none;"></div>
          <div v-if="errorMessage" class="text-red-500">Error: {{ errorMessage }}</div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import axios from 'axios'

export default defineComponent({
  name: 'SentAnalysis',
  setup() {
    const userInput = ref('');
    const reversedString = ref('');
    const errorMessage = ref('');
    const markedWords = ref<string[]>([]);
    const highlightedResult = ref<string>('');
    const markedResult = ref('');
    const score = ref('');

    const sendString = async () => {
      errorMessage.value = ''; // Reset error message
      try {
        console.log('Sending string:', userInput.value);
        const response = await axios.post<{ marked_string: string }>('http://localhost:5000/api/v1/text/sentiment-analysis', {
        string: userInput.value
      });
        //reversedString.value = response.data.reversed_string

        console.log('Received response:', response);

        markedResult.value = response.data.words;
        score.value = response.data.score;

        console.log('Marked result:', markedResult.value); // Log the marked result

        //highlightedResult.value = highlightPrompt(markedWords.value);
        //console.log('Marked Words:', response.data.marked_words);

      } catch (error) {
        errorMessage.value = 'Could not connect to the server.'
        console.error('Error:', error)
      }
    };

    /*
    const highlightPrompt = (words: string[]): string => {
      let result = userInput.value;

      words.forEach(word => {
        result = result.replace(new RegExp(`\\b(${word})(?![a-zA-Z])\\b`, 'gi'), '<span class="highlight">$1</span>');
      });
      return result;
    };
    */
    return { userInput, markedResult, score, sendString, errorMessage, isHighlighted: true}
  },

  data() {
    return {
      prompts: [
        'What is your favorite color?',
        'What did you do today?',
        'Describe a memorable moment in your life'
      ],
      currentPromptIndex: 0,
      highlightedResult: '',
    };
  },
  /*
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
  */
})
</script>
<template>
  <div class="container mx-auto p-4 max-w-2xl">
    <div class="flex flex-col space-y-4">
      <textarea
        v-model="textToAnalyze"
        class="w-full border-2 border-gray-300 p-3 rounded-md"
        placeholder="Type something..."
        rows="4"
      ></textarea>

      <button
        @click="analyzeSentiment"
        class="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Send
      </button>
      <div v-html="styledText" class="p-6 rounded shadow bg-neutral-content"></div>
      <div v-if="errorMessage" class="text-center font-semibold text-red-500">
        {{ errorMessage }}
      </div>
      <div v-if="sentimentScore" class="text-xl text-center font-semibold">
        Overall Sentiment Score: {{ sentimentScore }}
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue'
import axios from 'axios'
interface SentimentWord {
  [key: string]: number
}

interface SentimentResults {
  score: string
  words: SentimentWord[]
}

export default defineComponent({
  name: 'SentimentAnalysis',
  setup() {
    const textToAnalyze = ref('')
    const sentimentScore = ref('')
    const sentimentResults = ref<SentimentResults>({ score: '', words: [] })
    const errorMessage = ref('')

    const styledText = computed(() => {
      return sentimentResults.value.words
        .map((wordObj: SentimentWord) => {
          const word = Object.keys(wordObj)[0]
          const score = wordObj[word]
          const colorStyle = getColorStyle(score)
          return `<span style="${colorStyle}">${word}</span>`
        })
        .join(' ')
    })

    function getColorStyle(score: number): string {
      const minScore = -1;
      const maxScore = 1;
      
      //Calculate if word is emotionally connected
      if(score == 0){
        return 'color: black;'
      }

      // Map the score to a value between 0 and 1
      const normalizedScore = (score - minScore) / (maxScore - minScore);

      // Calculate RGB values 
      const red = Math.round(255 * (1 - normalizedScore));
      const green = Math.round(255 * normalizedScore);

      const color = `color: rgb(${red}, ${green}, 0);`;

      return color;
    }

    async function analyzeSentiment() {
      errorMessage.value = ''
      try {
        const response = await axios.post('http://127.0.0.1:5000/api/v1/text/sentiment-analysis', {
          text: textToAnalyze.value
        })
        sentimentResults.value = response.data.sentimentResults
        sentimentScore.value = response.data.sentimentResults.score
      } catch (error) {
        errorMessage.value = 'There was an error analyzing the sentiment. Please try again.'
        console.error('Error:', error)
      }
    }

    return {
      textToAnalyze,
      analyzeSentiment,
      sentimentScore,
      styledText,
      errorMessage
    }
  }
})
</script>

<style scoped></style>

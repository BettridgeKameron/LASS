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
          const colorClass = getColorClass(score)
          return `<span class="${colorClass}">${word}</span>`
        })
        .join(' ')
    })

    function getColorClass(score: number): string {
      const threshold = 0.3
      // This will by dynamic eventually (i.e. different shades of red/green instead of 1 shade of red/green). Only have to edit this function.

      if (score >= threshold) {
        return 'text-green-600'
      } else if (score <= -threshold) {
        return 'text-red-600'
      } else {
        return 'text-black'
      }
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

import { createRouter, createWebHistory } from 'vue-router'
import StringInput from '@/components/StringInput.vue'
import HomePage from '@/views/HomePage.vue'
import SentimentAnalysis from '@/views/SentimentAnalysis.vue'
import TextRephrase  from '@/views/TextRephrase.vue'
import FingerprintCreation from '@/views/FingerprintCreation.vue'

const routes = [
  {
    path: '/',
    name: 'home-page',
    component: HomePage,
    meta: {
      title: 'LASS-Home Page'
    },
  },
  {
    path: '/sentiment-analysis',
    name: 'sentiment-analysis',
    component: SentimentAnalysis,
    meta: {
      title: 'LASS-Sentiment Analysis'
    },
  },
  {
    path: '/string-input',
    name: 'string-input',
    component: StringInput,
    meta: {
      title: 'LASS-String Input'
    }
  },
  {
    path: '/text-rephrase',
    name: 'text-rephrase',
    component: TextRephrase,
    meta: {
      title: 'LASS-Text Rephrase'
    }
  },
  {
    path: '/fingerprint-creation',
    name: 'finger-print-creation',
    component: FingerprintCreation,
    meta: {
      title: 'LASS-Fingerprint Creation'
    }
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

router.beforeEach((to) => {
  document.title = (to.meta?.title as string) ?? 'Default Title'
})
export default router

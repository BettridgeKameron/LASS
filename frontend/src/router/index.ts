import { createRouter, createWebHistory } from 'vue-router'
import StringInput from '@/components/StringInput.vue'
import HomePage from '@/views/HomePage.vue'

const routes = [
  {
    path: '/',
    name: 'home-page',
    component: HomePage
  },
  {
    path: '/string-input',
    name: 'string-input',
    component: StringInput
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router

import { createRouter, createWebHistory } from 'vue-router'
import StringInput from '../components/StringInput.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: StringInput
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router

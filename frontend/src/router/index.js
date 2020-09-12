import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home.vue'
import Start from '@/components/Start.vue'
import DailyMenu from '@/components/DailyMenu.vue'
import Register from '@/components/Register.vue'
import Login from '@/components/Login.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Start',
    component: Start
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/details',
    name: 'DailyMenu',
    component: DailyMenu
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

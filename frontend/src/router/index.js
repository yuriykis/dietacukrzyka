import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home.vue'
import Start from '@/components/Start.vue'
import DailyMenu from '@/components/DailyMenu.vue'
import Register from '@/components/Register.vue'
import Login from '@/components/Login.vue'
import FeaturedRecipes from '@/components/FeaturedRecipes.vue'
import Profile from '@/components/Profile.vue'
import MealDetails from '@/components/MealDetails.vue'
import { isValidAccessToken } from '@/services/auth'

Vue.use(VueRouter)


  const routes = [
  {
    path: '/',
    name: 'Start',
    component: Start,
    meta: {
      allowAnonymous: true
    }
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/details/:date/:day/',
    name: 'DailyMenu',
    component: DailyMenu
  },
  {
    path: '/meal_details/:date/:meal_id',
    name: 'MealDetails',
    component: MealDetails
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    meta: {
      allowAnonymous: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: {
      allowAnonymous: true
    }
  },
  {
    path: '/featured_recipes',
    name: 'FeaturedRecipes',
    component: FeaturedRecipes
  },
  {
    path: '/recipes_details',
    name: 'FeaturedRecipes',
    component: FeaturedRecipes
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  }
]
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.allowAnonymous)) {
    return next()
  }
  if (!isValidAccessToken()) {
    next({
      path: '/login',
      query: { redirect: to.fullPath }
    })
    location.reload()
  } else {
    next()
  }
})


export default router

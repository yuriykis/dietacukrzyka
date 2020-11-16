import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home.vue'
import Start from '@/components/Start.vue'
import DailyMenu from '@/components/DailyMenu.vue'
import DailyMenuCurrent from '@/components/DailyMenuCurrent.vue'
import Register from '@/components/Register.vue'
import Login from '@/components/Login.vue'
import FeaturedRecipes from '@/components/FeaturedRecipes.vue'
import Profile from '@/components/Profile.vue'
import MealDetails from '@/components/MealDetails.vue'
import About from '@/components/About.vue'
import { isValidAccessToken } from '@/services/auth'

Vue.use(VueRouter)


  const routes = [
  {
    path: '/',
    name: 'Start',
    component: Start,
    meta: {
      hideForAuth: true
    }
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/details/:date/:day/',
    name: 'DailyMenu',
    component: DailyMenu,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/details/current/:date/:day/',
    name: 'DailyMenuCurrent',
    component: DailyMenuCurrent,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/meal_details/:date/:meal_id',
    name: 'MealDetails',
    component: MealDetails,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    meta: {
      hideForAuth: true
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: {
      hideForAuth: true
    }
  },
  {
    path: '/featured_recipes',
    name: 'FeaturedRecipes',
    component: FeaturedRecipes,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/recipes_details',
    name: 'FeaturedRecipes',
    component: FeaturedRecipes,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/about',
    name: 'About',
    component: About,
    meta: {
      requiresAuth: true
    }
  }
]
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {

  if(!isValidAccessToken()){
    if (to.matched.some(record => record.meta.hideForAuth)) {
      next()
    } 
    if (to.matched.some(record => record.meta.requiresAuth)) {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    }
  } else {
    if (to.matched.some(record => record.meta.hideForAuth)) {
      next({
        path: '/home',
        query: { redirect: to.fullPath }
      })
    } 
    if (to.matched.some(record => record.meta.requiresAuth)) {
      next()
    }
  }

})


export default router

<template>
   <v-container>         
          <FoodMenu/>      
      </v-container>
</template>

<script>
import FoodMenu from '@/components/FoodMenu';
import { getUser } from '@/services/api'
export default {
  name: 'Home',

  components: {
    FoodMenu,
  },

  data: () => ({
    user: {}
  }),
  created () {
    this.getUserData()
  },
  methods: {
    getUserData () {
      this.user = getUser()
      console.log(this.user)
    }
  }
};
</script>

<style>

</style>
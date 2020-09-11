<template>
   <v-container>         
               
      </v-container>
</template>

<script>
import { getUser } from '@/services/api'
export default {
  name: 'Home',

  components: {
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
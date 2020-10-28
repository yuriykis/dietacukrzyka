<template>
  <v-container>
    <FoodMenu />
  </v-container>
</template>

<script>
import FoodMenu from '@/components/FoodMenu'
export default {
  name: 'Home',

  components: {
    FoodMenu,
  },

  data: () => ({
    user: {},
  }),
  created() {},
  methods: {},
}
</script>

<style></style>

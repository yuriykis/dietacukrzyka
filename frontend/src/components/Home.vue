<template>
  <v-container>
    <v-row justify="center" align="center" v-if="loading">
      <Loader />
    </v-row>
    <FoodMenu v-else />
  </v-container>
</template>

<script>
import FoodMenu from '@/components/FoodMenu'
import Loader from '@/components/Loader'
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'Home',

  components: {
    FoodMenu,
    Loader,
  },
  computed: mapGetters(['getClientInfo']),
  data: () => ({
    user: {},
    loading: true,
  }),
  created() {},
  methods: {
    ...mapActions(['fetchData', 'fetchAllImages', 'getRecipesFromServer']),
  },
  async mounted() {
    await this.fetchData()
    await this.fetchAllImages()
    await this.getRecipesFromServer()
    this.loading = false
  },
}
</script>

<style></style>

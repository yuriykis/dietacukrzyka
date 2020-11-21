<template>
  <v-container>
    <v-container>
      <v-row class="mb-2 no-gutters">
        <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="100%"
          max-height="80"
          color="rgba(116,34,60,0.8)"
        >
          <v-row>
            <v-col cols="8">
              <h2 class="ma-4">Polecane Przepisy</h2>
            </v-col>
            <v-col v-if="is_dietician">
              <v-btn
                @click="goToRecipeCreating"
                color="#98AF4F"
                class="ma-3 white--text"
                >{{ 'Dodaj nowy przepis' }}</v-btn
              >
            </v-col>
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
    <v-container v-for="(recipe, i) in getRecipes" :key="i">
      <v-row class="mb-8 no-gutters">
        <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="100%"
          @click="seeDetails(i)"
          color="rgba(28,29,30,0.8)"
        >
          <v-row>
            <v-col>
              <h3 class="ml-5">{{ recipe.name }}</h3>
            </v-col>
            <v-col>
              <h5 class="mt-4"></h5>
            </v-col>
          </v-row>
          <v-row justify="center">
            <v-card class="ma-4" height="300" width="700">
              <v-img
                :style="{ cursor: 'pointer' }"
                :src="
                  getRecipeImageByName(
                    recipe.name.replaceAll(' ', '_').replaceAll(',', '')
                  )
                "
                max-width="100%"
                max-height="100%"
              />
            </v-card>
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'FeaturedRecipes',
  data: () => ({
    loading: true,
    is_dietician: false,
  }),
  computed: mapGetters([
    'getRecipes',
    'getRecipeImageByName',
    'getClientInfoFromStore',
  ]),
  methods: {
    ...mapActions(['getClientInfoFromServer']),
    seeDetails(i) {
      this.$router.push({
        path: `/recipes_details/${i}`,
      })
    },
    goToRecipeCreating() {
      this.$router.push({
        path: '/recipes/new/',
      })
    },
  },
  async mounted() {
    await this.getClientInfoFromServer()
    this.is_dietician = this.getClientInfoFromStore.is_dietician
  },
}
</script>

<style scoped>
.rounded-corner {
  border-radius: 20px;
}
h3,
h5 {
  color: white;
}
h2,
h4 {
  color: white;
}
</style>

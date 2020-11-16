<template>
  <v-container>
    <v-container>
      <v-row class="mb-2 no-gutters">
        <v-col class="mt-10" cols="12" align="center" justify="center">
          <h1 style="font-size: 60px;">Polecane Przepisy</h1>
        </v-col>
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
import { mapGetters } from 'vuex'
export default {
  name: 'FeaturedRecipes',
  data: () => ({
    loading: true,
  }),
  computed: mapGetters(['getRecipes', 'getRecipeImageByName']),
  methods: {
    seeDetails(i) {
      this.$router.push({
        path: `/recipes_details/${i}`,
      })
    },
  },
  async mounted() {},
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
</style>

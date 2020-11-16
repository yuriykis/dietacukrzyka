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
            <v-col cols="7">
              <h2 class="ma-4">{{ getRecipes[current_recipe].name }}</h2>
            </v-col>
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
    <v-container>
      <v-row class="mb-1 no-gutters">
        <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="100%"
          color="rgba(28,29,30,0.8)"
        >
          <v-row>
            <v-col cols="6">
              <v-sheet
                class="mt-4 ml-5"
                color="#A8C256"
                width="95%"
                height="300"
              >
                <h3 class="ma-1">Składniki:</h3>
                <div
                  v-for="ingredient in getRecipes[current_recipe].ingredients"
                  :key="ingredient"
                >
                  <h3 class="ma-1">* {{ ingredient }}</h3>
                </div>
              </v-sheet>
            </v-col>
            <v-col cols="6">
              <v-sheet class="mt-4" width="95%" height="300">
                <v-img
                  :src="
                    getRecipeImageByName(
                      getRecipes[current_recipe].name
                        .replaceAll(' ', '_')
                        .replaceAll(',', '')
                    )
                  "
                  max-height="100%"
                >
                </v-img>
              </v-sheet>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <v-sheet class="mx-4" color="rgba(116,34,60,0.8)" height="300">
                <h4 class="ma-1">Przygotowanie:</h4>
                <h4 class="ma-1">{{ getRecipes[current_recipe].method }}</h4>
              </v-sheet>
            </v-col>
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'RecipeDetails',
  data: () => ({
    current_recipe: 0,
  }),
  computed: mapGetters(['getRecipes', 'getRecipeImageByName']),
  methods: {},
  mounted() {
    this.current_recipe = this.$route.params.recipe_id
  },
}
</script>

<style scoped>
.rounded-corner {
  border-radius: 20px;
}
h2,
h4 {
  color: white;
}
h3 {
  background-color: #a8c256;
  color: white;
}
</style>

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
              <h2 class="ma-4">{{ recipe.name }}</h2>
            </v-col>
            <v-col>
              <h4 class="ma-6">
                {{ (Math.round(recipe.weights_info[2]) * 1) / 1 }} kcal
              </h4>
            </v-col>
            <v-col>
              <h4 class="ma-6">
                {{ (Math.round(recipe.weights_info[0]) * 1) / 1 }} g
              </h4>
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
                  v-for="(ingredient, i) in recipe.ingredients"
                  :key="ingredient"
                >
                  <h3 class="ma-1">
                    * {{ ingredient }}
                    <span style="color: red;"
                      >{{
                        (Math.round(recipe.weights_info[1][i]) * 1) / 1
                      }}
                      g</span
                    >
                  </h3>
                </div>
              </v-sheet>
            </v-col>
            <v-col cols="6">
              <v-sheet class="mt-4" width="95%" height="300">
                <v-img
                  :src="
                    getRecipeImageByName(
                      recipe.name.replaceAll(' ', '_').replaceAll(',', '')
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
                <h4 class="ma-1">{{ recipe.method }}</h4>
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
  name: 'Menu',
  data: () => ({
    recipe: {},
    date: '',
    dates: {
      '2020-11-16': 0,
      '2020-11-17': 1,
      '2020-11-18': 2,
      '2020-11-19': 3,
      '2020-11-20': 4,
      '2020-11-21': 5,
      '2020-11-22': 6,
    },
    meal_types_data: [
      'sniadanie',
      'II sniadanie',
      'obiad',
      'podwieczorek',
      'kolacja',
    ],
    ingredients: [],
    ingredients_weight: {},
    meal_mass: 0,
    calorific_value: 0,
  }),
  computed: mapGetters(['getClientMealByDayId', 'getRecipeImageByName']),
  methods: {},
  mounted() {
    this.date = this.$route.params.date
    this.recipe = this.getClientMealByDayId(
      this.dates[this.date],
      this.meal_types_data[this.$route.params.meal_id]
    )
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

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
              <h2 class="ma-4">{{ recipes[0].name }}</h2>
            </v-col>
            <v-col>
              <h4 class="ma-6">{{ recipes[0].calories }} kcal</h4>
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
                <div v-for="ingredient in ingredients" :key="ingredient">
                  <h3 class="ma-1">* {{ ingredient }}</h3>
                </div>
              </v-sheet>
            </v-col>
            <v-col cols="6">
              <v-sheet class="mt-4" width="95%" height="300">
                <v-img
                  :src="
                    require(`../assets/Dania/${recipes[0].name
                      .replaceAll(' ', '_')
                      .replaceAll(',', '')}.jpg`)
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
                <h4 class="ma-1">{{ recipes[0].method }}</h4>
              </v-sheet>
            </v-col>
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import {
  getClientMenu,
  getClientMenuIngredients,
  generateClientIngredientsWeight,
} from '@/services/api'
export default {
  name: 'Menu',
  data: () => ({
    recipes: [],
    ingredients: [],
    ingredients_weight: {},
  }),
  methods: {
    fetchData(i, date) {
      getClientMenu(i, date).then((response) => {
        this.recipes.push(response.data)
        if (i < 4) {
          this.fetchData(++i, date)
        } else {
          this.calcTotalDayilyCalories()
        }
      })
    },
    fetchIngredients(i, date) {
      getClientMenuIngredients(i, date).then((response) => {
        this.ingredients = [...JSON.parse(response.data)]
      })
    },
    getIngredietsWeight() {
      generateClientIngredientsWeight(
        this.$route.params.meal_id,
        this.$route.params.date
      ).then((response) => {
        this.ingredients_weight = JSON.parse(JSON.stringify(response.data))
        console.log(this.ingredients_weight)
      })
    },
  },
  mounted() {
    this.fetchData(this.$route.params.meal_id, this.$route.params.date)
    this.fetchIngredients(this.$route.params.meal_id, this.$route.params.date)
    this.getIngredietsWeight()
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

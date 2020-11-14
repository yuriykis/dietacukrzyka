<template>
  <v-container>
    <v-container>
      <v-row class="mb-1 no-gutters">
        <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="100%"
          color="rgba(116,34,60,0.8)"
        >
          <v-row>
            <v-col>
              <h2 class="ma-4">{{ day }}</h2>
            </v-col>
            <v-col>
              <h2 class="ma-4">
                {{
                  date
                    .split('-')
                    .reverse()
                    .toString()
                    .replaceAll(',', '.')
                }}
              </h2>
            </v-col>
            <v-col>
              <h2 class="ma-6">
                {{ (Math.round(total_calories) * 1) / 1 }} kcal
              </h2>
            </v-col>
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
    <v-container v-for="(meal, i) in meals" :key="i">
      <v-row class="mb-1 no-gutters">
        <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="100%"
          color="rgba(28,29,30,0.8)"
        >
          <v-col cols="12">
            <v-row>
              <v-col cols="10">
                <h2 class="ml-5">{{ meal }}</h2>
              </v-col>
              <v-col>
                <h2 class="ml-5">
                  {{
                    (Math.round(recipes[meal_types_data[i]].weights_info[2]) *
                      1) /
                      1
                  }}
                  kcal
                </h2>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <h3 class="ma-3">
                  {{ recipes[meal_types_data[i]].name }}
                </h3>
                <h4 class="ma-3">
                  {{ recipes[meal_types_data[i]].method }}
                </h4>
              </v-col>
              <v-col>
                <v-card class="rounded-corner" max-width="300">
                  <v-tooltip v-model="show[i]" top>
                    <template v-slot:activator="{ on, attrs }">
                      <v-img
                        v-bind="attrs"
                        v-on="on"
                        @click="goToMealDetails(i)"
                        :style="{ cursor: 'pointer' }"
                        :src="
                          getRecipeImageByName(
                            recipes[meal_types_data[i]].name
                              .replaceAll(' ', '_')
                              .replaceAll(',', '')
                          )
                        "
                        max-height="300"
                        max-width="300"
                      >
                      </v-img>
                    </template>
                    <span>Zobacz szczegóły</span>
                  </v-tooltip>
                </v-card>
              </v-col>
            </v-row>
          </v-col>
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
    show: [],
    meals: ['Śniadanie', 'II śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja'],
    meal_types_data: [
      'sniadanie',
      'II sniadanie',
      'obiad',
      'podwieczorek',
      'kolacja',
    ],
    recipes: [],
    date: '',
    day: '',
    days: {
      Poniedziałek: 0,
      Wtorek: 1,
      Środa: 2,
      Czwartek: 3,
      Piątek: 4,
      Sobota: 5,
      Niedziela: 6,
    },
    calorific_values: [],
    total_calories: 0,
    images: [],
  }),
  computed: mapGetters(['getClientInfoByDay', 'getRecipeImageByName']),
  methods: {
    goToMealDetails(i) {
      this.$router.push({
        path: `/meal_details/${this.date}/${i}/`,
      })
    },
    calculateTotalCalories() {
      for (let i = 0; i < 5; i++) {
        this.total_calories += this.recipes[
          this.meal_types_data[i]
        ].weights_info[2]
      }
    },
  },
  mounted() {
    this.date = this.$route.params.date
    this.day = this.$route.params.day
    this.recipes = this.getClientInfoByDay(this.days[this.day])
    this.calculateTotalCalories()
  },
}
</script>

<style scoped>
.rounded-corner {
  border-radius: 20px;
}
h2 {
  color: white;
}
h3 {
  background-color: #a8c256;
  color: white;
}
h4 {
  background-color: rgba(116, 34, 60, 0.8);
  color: white;
}
</style>

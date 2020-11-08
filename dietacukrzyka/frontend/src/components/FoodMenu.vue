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
            <v-col>
              <h2 class="ma-4">Dieta na ten tydzień</h2>
            </v-col>
            <v-col>
              <h4 class="ma-6">16.11.2020 - 22.11.2020</h4>
            </v-col>
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
    <v-container v-for="(day, i) in days" :key="i">
      <v-row class="mb-1 no-gutters">
        <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="100%"
          color="rgba(28,29,30,0.8)"
        >
          <v-row class="mb-2">
            <v-col cols="3">
              <h2 class="ml-5">{{ day }}</h2>
            </v-col>
            <v-col>
              <h4 class="mt-5">{{ recipes[i]['sniadanie'].date }}</h4>
            </v-col>
            <v-col>
              <h4 class="mt-5">
                {{ (Math.round(total_calories[i]) * 1) / 1 }} kcal
              </h4>
            </v-col>
          </v-row>
          <v-slide-group
            v-model="model"
            class="mb-4"
            :prev-icon="prevIcon ? 'mdi-minus' : undefined"
            :next-icon="nextIcon ? 'mdi-plus' : undefined"
            :multiple="multiple"
            :mandatory="mandatory"
            :show-arrows="showArrows"
            :center-active="centerActive"
          >
            <v-slide-item v-for="j in 5" :key="j">
              <v-card class="ma-4" height="200" width="300">
                <v-img
                  @click="
                    seeDetails(recipes[i][meal_types_data[j - 1]].date, days[i])
                  "
                  :src="
                    images[
                      recipes[i][meal_types_data[j - 1]].name
                        .replaceAll(' ', '_')
                        .replaceAll(',', '')
                    ]
                  "
                >
                  <h3 class="ma-3">
                    <span>{{ meal_types[j - 1] }}</span>
                  </h3>
                  <h3 class="ml-3">
                    <span>{{ recipes[i][meal_types_data[j - 1]].name }}</span>
                  </h3>
                </v-img>
              </v-card>
            </v-slide-item>
          </v-slide-group>
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
    days: [
      'Poniedziałek',
      'Wtorek',
      'Środa',
      'Czwartek',
      'Piątek',
      'Sobota',
      'Niedziela',
    ],
    meal_types: [
      'Śniadanie',
      'II śniadanie',
      'Obiad',
      'Podwieczorek',
      'Kolacja',
    ],
    meal_types_data: [
      'sniadanie',
      'II sniadanie',
      'obiad',
      'podwieczorek',
      'kolacja',
    ],
    recipes: [],
    total_calories: [0, 0, 0, 0, 0, 0, 0],
    images_array: [],
    images: {},
  }),
  computed: mapGetters(['getClientInfo', 'getRecipeImages']),
  methods: {
    seeDetails(date, day) {
      this.$router.push({
        path: `/details/${date}/${day}`,
      })
    },
    calculateTotalCalories() {
      for (let i = 0; i < 7; i++) {
        for (let j = 0; j < 5; j++) {
          this.total_calories[i] += this.recipes[i][
            this.meal_types_data[j]
          ].weights_info[2]
        }
      }
    },
    imageArrayToImageObject() {
      this.images_array.forEach((image) => {
        this.images[Object.keys(image)[0]] = Object.values(image)[0]
      })
    },
  },
  mounted() {
    this.recipes = Object.assign(this.getClientInfo)
    this.images_array = Object.assign(this.getRecipeImages)
    this.imageArrayToImageObject()
    this.calculateTotalCalories()
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
h3 span {
  background-color: rgba(116, 34, 60, 0.8);
  color: white;
}
h3 {
  color: white;
}
</style>

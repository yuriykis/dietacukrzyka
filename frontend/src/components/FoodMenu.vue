<template>
  <v-container>
  <v-container>
      <v-row class="mb-2 no-gutters">
          <v-sheet
            class="mx-auto rounded-corner"
            elevation="8"
            width="100%"
            max-height="80"
            color= "rgba(116,34,60,0.8)"
            >
                <v-row>
                    <v-col>
                        <h2 class="ma-4">Dieta na ten tydzień</h2>
                    </v-col>
                    <v-col>
                        <h3 class="ma-6">{{ total_calories }} kcal</h3>
                    </v-col>
                    <v-col>
                        <h4 class="ma-6">10.08.2020 - 16.08.2020</h4>
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
          color= "rgba(28,29,30,0.8)"
        >
        <v-row class="mb-2">
            <v-col cols=3>
                <h2 class="ml-5">{{ day }}</h2>
            </v-col>
            <v-col>
              <h4 class="mt-2">{{i + 10}}.08.2020</h4>
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
                  <v-slide-item
                    v-for="i in 5"
                    :key="i"
                  >
                    <v-card
                      class="ma-4"
                      height="200"
                      width="300"
                    >
                    <v-img @click="seeDetails(day)" :src="require(`../assets/image${i%3+1}.jpg`)">
                      <h3 class="ma-3">
                        <span>{{ meal_types[i - 1] }}</span>
                      </h3>
                      <h3 class="ml-3">
                        <span>{{ recipes[i - 1].name }}</span>
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
import { getClientMenu } from '@/services/api'
  export default {
    name: 'Menu',
    data: () => ({
      days: ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela'],
      meal_types: ['Śniadanie', 'II śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja'],
      recipes: [],
      total_calories: 0
    }),
    methods: {
      seeDetails (day) {
        this.$router.push({
          path: `/details/${day}`
        })
      },
      fetchData (i) {
         getClientMenu(i).then((response) => {
             this.recipes.push(response.data)
             if (i < 4) {
                 this.fetchData(++i)
             } else {
               this.calcTotalDayilyCalories()
             }
         })
      },
      calcTotalDayilyCalories () {
        this.recipes.forEach((meal) => {
          this.total_calories += meal.calories
        })
        this.total_calories *= 7
      }
    },
    mounted () {
        this.fetchData(0)
    }
  }
</script>

<style scoped>
.rounded-corner{
    border-radius:20px;
}
h2, h4 {
  color: white;
}
h3 span {
  background-color: rgba(116,34,60,0.8);
  color: white;
}
h3 {
  color: white;
}
</style>
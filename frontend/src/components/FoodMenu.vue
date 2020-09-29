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
                        <h4 class="ma-6">12.10.2020 - 19.10.2020</h4>
                    </v-col>
                </v-row>
          </v-sheet>
      </v-row>
  </v-container>
  <v-container v-if="loading">
    <v-row align="center" justify="center" v-if="loading">
              <Loader />
            </v-row>
  </v-container>
      <v-container v-else v-for="(day, i) in days" :key="i">
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
              <h4 class="mt-2">{{i + 12}}.10.2020</h4>
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
                    v-for="j in 5"
                    :key="j"
                  >
                    <v-card
                      class="ma-4"
                      height="200"
                      width="300"
                    >
                    <v-img @click="seeDetails(day, i)" :src="require(`../assets/image${j%3+1}.jpg`)">
                      <h3 class="ma-3">
                        <span>{{ meal_types[j - 1] }}</span>
                      </h3>
                      <h3 class="ml-3">
                        <span>{{ recipes[5 * (i%2) + j - 1].name }}</span>
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
import Loader from "@/components/Loader"
  export default {
    name: 'Menu',
    data: () => ({
      days: ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela'],
      meal_types: ['Śniadanie', 'II śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja'],
      recipes: [],
      total_calories: 0,
      dates: ['2020-10-12', '2020-10-13'],
      loading: true
    }),
    components: {
      Loader
    },
    methods: {
      seeDetails (day, i) {
        this.$router.push({
          path: `/details/${day}/${i}`
        })
      },
      fetchData (i, dates, j) {
         getClientMenu(i, dates[j]).then((response) => {
             this.recipes.push(response.data)
             if (i < 4) {
                 this.fetchData(++i, dates, j)
             } else {
               if (j === 0) {
                 i = 0
                 j++
                 this.fetchData(i, dates, j)
              } else {
                this.calcTotalDayilyCalories()
                this.loading = false
              }
             }
         })
      },
      calcTotalDayilyCalories () {
        this.recipes.forEach((meal) => {
          this.total_calories += meal.calories
        })
        this.total_calories *= 3
      }
    },
    mounted () {
        this.fetchData(0, this.dates, 0)
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
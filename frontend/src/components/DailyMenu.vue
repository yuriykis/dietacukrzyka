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
              <h2 class="ma-4">{{ date }}</h2>
            </v-col>
            <v-col>
              <h2 class="ma-6">{{ total_calories }} kcal</h2>
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
    <v-container v-else v-for="(meal, i) in meals" :key="i">
      <v-row class="mb-1 no-gutters">
        <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="100%"
          color="rgba(28,29,30,0.8)"
          @click="goToMealDetails(i)"
        >
          <v-col cols="12">
            <v-row>
              <v-col cols="10">
                <h2 class="ml-5">{{ meal }}</h2>
              </v-col>
              <v-col>
                <h2 class="ml-5">{{ calorific_values[i] }} kcal</h2>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <h3 class="ma-3">
                  {{ mealData[i].name }}
                </h3>
                <h4 class="ma-3">
                  {{ mealData[i].method }}
                </h4>
              </v-col>
              <v-col>
                <v-card class="rounded-corner" max-width="300">
                  <v-img
                    @click="seeDetails(date, days[i])"
                    :src="images[i]"
                    max-height="300"
                    max-width="300"
                  >
                  </v-img>
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
import {
  getClientMenu,
  generateClientIngredientsWeight,
  getFile,
} from '@/services/api'
import Loader from '@/components/Loader'
export default {
  name: 'Menu',
  data: () => ({
    meals: ['Śniadanie', 'II śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja'],
    mealData: [],
    date: '',
    day: '',
    loading: true,
    calorific_values: [],
    total_calories: 0,
    images: [],
  }),
  components: {
    Loader,
  },
  methods: {
    fetchData(i, date) {
      getClientMenu(i, date).then((response) => {
        this.mealData.push(response.data)

        generateClientIngredientsWeight(i, date).then((response) => {
          this.ingredients_weight = response.data
          this.ingredients_weight = this.ingredients_weight
            .replaceAll(' ', '')
            .replaceAll('[', '')
            .replaceAll(']', '')
            .split(',')
          this.meal_mass = this.ingredients_weight[0]
          let calorific_value = this.ingredients_weight[
            this.ingredients_weight.length - 1
          ]
          calorific_value = Math.round(parseFloat(calorific_value) * 1) / 1
          this.calorific_values.push(calorific_value)
          this.total_calories += calorific_value

          if (i < 4) {
            this.fetchData(++i, date)
          } else {
            this.fetchAllImages(0)
          }
        })
      })
    },
    goToMealDetails(i) {
      this.$router.push({
        path: `/meal_details/${this.date}/${i}/`,
      })
    },
    fetchFile(fileName) {
      return getFile(fileName).then(async (response) => {
        const image = Buffer.from(response.data, 'binary').toString('base64')
        const data = `data:${response.headers[
          'content-type'
        ].toLowerCase()};base64,${image}`
        return data
      })
    },
    fetchAllImages(index) {
      const fileName = this.mealData[index].name
        .replaceAll(' ', '_')
        .replaceAll(',', '')
      this.fetchFile(fileName + '.jpg')
        .then((data) => {
          this.images.push(data)
          this.fetchAllImages(++index)
        })
        .catch((e) => {
          console.log(e)
          this.loading = false
        })
    },
  },
  mounted() {
    this.fetchData(0, this.$route.params.date)
    this.date = this.$route.params.date
    this.day = this.$route.params.day
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

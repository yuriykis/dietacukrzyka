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
              <h4 class="ma-6">12.10.2020 - 18.10.2020</h4>
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
    <v-container v-else v-for="(date, i) in dates" :key="i">
      <v-row class="mb-1 no-gutters">
        <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="100%"
          color="rgba(28,29,30,0.8)"
        >
          <v-row class="mb-2">
            <v-col cols="3">
              <h2 class="ml-5">{{ days[i] }}</h2>
            </v-col>
            <v-col>
              <h4 class="mt-2">{{ date }}</h4>
            </v-col>
            <v-col>
              <h4 class="mt-2">{{ total_calories[i] }} kcal</h4>
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
                  @click="seeDetails(date, days[i])"
                  :src="images[5 * i + j - 1]"
                >
                  <h3 class="ma-3">
                    <span>{{ meal_types[j - 1] }}</span>
                  </h3>
                  <h3 class="ml-3">
                    <span>{{ recipes[5 * i + j - 1].name }}</span>
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
import {
  getClientMenu,
  generateClientIngredientsWeight,
  getFile,
} from '@/services/api'
import Loader from '@/components/Loader'
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
    recipes: [],
    dates: [
      '2020-10-12',
      '2020-10-13',
      '2020-10-14',
      '2020-10-15',
      '2020-10-16',
      '2020-10-17',
      '2020-10-18',
    ],
    loading: true,
    total_calories: [0, 0, 0, 0, 0, 0, 0],
    images: [],
    image: {},
  }),
  components: {
    Loader,
  },
  methods: {
    seeDetails(date, day) {
      this.$router.push({
        path: `/details/${date}/${day}`,
      })
    },
    fetchData(i, dates, j) {
      getClientMenu(i, dates[j]).then((response) => {
        this.recipes.push(response.data)

        generateClientIngredientsWeight(i, dates[j]).then((response) => {
          this.ingredients_weight = response.data
          this.ingredients_weight = this.ingredients_weight
            .replaceAll(' ', '')
            .replaceAll('[', '')
            .replaceAll(']', '')
            .split(',')
          let calorific_value = this.ingredients_weight[
            this.ingredients_weight.length - 1
          ]
          calorific_value = Math.round(parseFloat(calorific_value) * 1) / 1
          this.total_calories[j] += calorific_value

          if (i < 4) {
            this.fetchData(++i, dates, j)
          } else {
            if (j < 6) {
              i = 0
              this.fetchData(i, dates, ++j)
            } else {
              this.fetchAllImages(0)
            }
          }
        })
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
      const fileName = this.recipes[index].name
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
    this.fetchData(0, this.dates, 0)
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

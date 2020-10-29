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
    <v-container v-else v-for="(day, i) in days" :key="i">
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
              <h4 class="mt-2">{{ recipes[i][0].date }}</h4>
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
                    <span>{{ recipes[i][j - 1].name }}</span>
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
import { getFile } from '@/services/api'
import Loader from '@/components/Loader'
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
    recipes: [],
    loading: false,
    total_calories: [0, 0, 0, 0, 0, 0, 0],
    images: [],
    recipe_names: [],
  }),
  components: {
    Loader,
  },
  computed: mapGetters(['getClientInfo']),
  methods: {
    seeDetails(date, day) {
      this.$router.push({
        path: `/details/${date}/${day}`,
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
      const fileName = this.recipe_names[index]
        .replaceAll(' ', '_')
        .replaceAll(',', '')
      this.fetchFile(fileName + '.jpg')
        .then((data) => {
          this.images.push(data)
          this.fetchAllImages(++index)
        })
        .catch((e) => {
          console.log(e)
        })
    },
    calculateTotalCalories() {
      for (let i = 0; i < 7; i++) {
        for (let j = 0; j < 5; j++) {
          this.total_calories[i] += this.recipes[i][j].weights_info[2]
          this.recipe_names.push(this.recipes[i][j].name)
        }
      }
    },
  },
  mounted() {
    this.recipes = Object.assign(this.getClientInfo.data)
    this.calculateTotalCalories()
    this.fetchAllImages(0)
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

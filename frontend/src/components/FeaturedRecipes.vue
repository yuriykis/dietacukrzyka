<template>
  <v-container>
    <v-container>
      <v-row class="mb-2 no-gutters">
        <v-col class="mt-10" cols="12" align="center" justify="center">
          <h1 style="font-size: 60px;">Polecane Przepisy</h1>
        </v-col>
      </v-row>
    </v-container>
    <v-container v-for="(recipe, i) in recipes" :key="i">
      <v-row class="mb-8 no-gutters">
        <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="100%"
          @click="seeDetails()"
          color="rgba(28,29,30,0.8)"
        >
          <v-row>
            <v-col>
              <h3 class="ml-5">{{ recipe.name }}</h3>
            </v-col>
            <v-col>
              <h5 class="mt-4"></h5>
            </v-col>
          </v-row>
          <v-row justify="center">
            <v-card class="ma-4" height="300" width="700">
              <v-img
                @click="seeDetails(date, days[i])"
                :src="images[i]"
                max-width="100%"
                max-height="100%"
              />
            </v-card>
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import { getClientMenu, getFile } from '@/services/api'
// <v-img :src="require(`../assets/image${i%3+1}.jpg`)"/>
export default {
  name: 'Menu',
  data: () => ({
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
    images: [],
  }),
  methods: {
    seeDetails() {
      this.$router.push({
        path: '/recipes_details',
      })
    },
    fetchData(i, dates, j) {
      getClientMenu(i, dates[j]).then((response) => {
        this.recipes.push(response.data)
        if (i < 4) {
          this.fetchData(++i, dates, j)
        } else {
          if (j < 6) {
            i = 0
            j++
            this.fetchData(i, dates, j)
          } else {
            this.fetchAllImages(0)
          }
        }
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
h3,
h5 {
  color: white;
}
</style>

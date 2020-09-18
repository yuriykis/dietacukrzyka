<template>
  <v-container>
  <v-container>
      <v-row class="mb-2 no-gutters">
          <v-col class="mt-10" cols=12  align="center" justify="center">
                <h1>Polecane Przepisy</h1>
          </v-col>
      </v-row>
  </v-container>
      <v-container>
          <v-row class="mb-8 no-gutters">
          <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          max-width="800"
          @click="seeDetails()"
          color= "rgba(28,29,30,0.8)"
        >
        <v-row>
            <v-col>
                <h3 class="ml-5">{{ recipes[0].name }}</h3>
            </v-col>
            <v-col>
              <h5 class="mt-4"></h5>
            </v-col>
        </v-row>
                    <v-card
                      class="ma-4"
                      height=300
                      width="700"
                    >
                    <v-img height=300 :src="require(`../assets/image1.jpg`)"/>
                    </v-card>
            </v-sheet>
          </v-row>
          <v-row class="mb-8 no-gutters">
          <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          max-width="800"
          @click="seeDetails()"
          color= "rgba(28,29,30,0.8)"
        >
        <v-row>
            <v-col>
                <h3 class="ml-5">{{ recipes[1].name }}</h3>
            </v-col>
            <v-col>
              <h5 class="mt-4"></h5>
            </v-col>
        </v-row>
                    <v-card
                      class="ma-4"
                      height=300
                      width="700"
                    >
                    <v-img height=300 :src="require(`../assets/image2.jpg`)"/>
                    </v-card>
            </v-sheet>
          </v-row>
          <v-row class="mb-8 no-gutters">
          <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          max-width="800"
          @click="seeDetails()"
          color= "rgba(28,29,30,0.8)"
        >
        <v-row>
            <v-col>
                <h3 class="ml-5">{{ recipes[2].name }}</h3>
            </v-col>
            <v-col>
              <h5 class="mt-4"></h5>
            </v-col>
        </v-row>
                    <v-card
                      class="ma-4"
                      height=300
                      width="700"
                    >
                    <v-img height=300 :src="require(`../assets/image3.jpg`)"/>
                    </v-card>
            </v-sheet>
          </v-row>
    </v-container>
  </v-container>
</template>

<script>
import { getClientMenu } from '@/services/api'
// <v-img :src="require(`../assets/image${i%3+1}.jpg`)"/>
  export default {
    name: 'Menu',
    data: () => ({
      recipes: []
    }),
    methods: {
      seeDetails () {
        this.$router.push({
          path: '/recipes_details'
        })
      },
      fetchData (i) {
         getClientMenu(i).then((response) => {
             this.recipes.push(response.data)
             if (i < 3) {
                 this.fetchData(++i)
             }
         })
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
h3, h5 {
  color: white;
}
</style>
<template>
  <v-container>
    <v-container>
      <v-row class="mb-1 no-gutters">
        <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="800"
          color= "rgba(116,34,60,0.8)"
        >
          <v-row>
              <v-col>
                  <h2 class="ma-4">Poniedziałek </h2>
              </v-col>
              <v-col>
                <h5 class="mt-4"></h5>
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
        width="800"
        color= "rgba(28,29,30,0.8)"
        >
          <v-col cols="12">
            <v-row>
              <h2 class="ml-5">{{ meal }}</h2>
            </v-row>
            <v-row>
              <v-col>
                <h3 class="mr- ma-3" >
                  {{ mealData[i].name }}
                </h3>
                <!-- <h4 class="ml-3">
                  {{ mealData[i].ingedients }}
                </h4> -->
                <h4 class="ma-3">
                  {{ mealData[i].method }}
                </h4>
              </v-col>
              <v-card
              class="mr-n12 mx-auto mr-xs-2 rounded-corner"
              max-width="450">

                <v-img
                  :src="require(`../assets/image${i%3+1}.jpg`)"
                  max-height="300"
                >
                </v-img>
              </v-card>
            </v-row>
          </v-col>
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
      meals: ['Śniadanie', 'II śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja'],
      mealData: [],
      backgroundUrl: ["../assets/image1.jpg", "../assets/image2.jpg", "../assets/image3.jpg"]
    }),
    methods: {
      fetchData (i) {
        
        getClientMenu(i).then((response) => {
          this.mealData.push(response.data)
             if (i < 5) {
                 this.fetchData(++i)
             }
          });

      }
    },
    mounted () {
        this.fetchData(0)
        console.log(this.mealData)
    }
  }
</script>

<style scoped>
.rounded-corner{
    border-radius:20px;
}
h2{
  color: white;
}
h3 {
  background-color:#A8C256;
  color: white;
}
h4 {
  background-color: rgba(116,34,60,0.8);
  color: white;
}
</style>
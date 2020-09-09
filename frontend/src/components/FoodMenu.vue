<template>
  <v-container>
  <v-container>
      <v-row class="mb-2 no-gutters">
          <v-sheet
            class="mx-auto rounded-corner"
            elevation="8"
            width="800"
            max-height="80"
            >
                <v-row>
                    <v-col>
                        <h3 class="ma-4">Dieta na ten tydzień</h3>
                    </v-col>
                    <v-col>
                        <h5 class="ma-6">1500 kcal</h5>
                    </v-col>
                    <v-col>
                        <h5 class="ma-6">10.08.2020 - 16.08.2020</h5>
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
          max-width="800"
          @click="seeDetails(day)"
        >
        <v-row>
            <v-col>
                <h3 class="ml-5">{{ day }}</h3>
            </v-col>
            <v-col>
              <h5 class="mt-4">{{i + 10}}.08.2020</h5>
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
                    v-for="i in 9"
                    :key="i"
                  >
                    <v-card
                      class="ma-4"
                      height="100"
                      width="200"
                    >
                    <v-img :src="require(`../assets/image${i%3+1}.jpg`)"/>
                    </v-card>
                  </v-slide-item>
               </v-slide-group>
            </v-sheet>
          </v-row>
    </v-container>
  </v-container>
</template>

<script>
  export default {
    name: 'Menu',
    data: () => ({
      days: ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
    }),
    methods: {
      seeDetails (day) {
        this.$router.push({
          path: '/details', 
          query : {
            day
          }
        })
      }
    }
  }
</script>

<style scoped>
.rounded-corner{
    border-radius:20px;
}
</style>
<template>
  <v-container>
       <v-container>
          <v-row class="mb-1 no-gutters">
          <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="800"
        >
        <v-row>
            <v-col>
                <h3 class="ml-5">{{ day }}</h3>
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
        >
        <v-row>
            <v-col>
                <h3 class="ml-5">{{ meal }}</h3>
            </v-col>
            <v-col>
                <h5 class="mt-4">{{ date }}</h5>
            </v-col>
        </v-row>
            </v-sheet>
          </v-row>
    </v-container>
  </v-container>
</template>

<script>
  export default {
    name: 'Menu',
    data: () => ({
      meals: ['Śniadanie', 'II śniadanie', 'Obiad', 'Podwieczorek', 'Kolacja'],
      day: ''
    }),
    created () {
        this.getDay()
    },
    methods: {
        getDay(){
            this.day = this.$route.query.day
        }
    }
  }
</script>

<style scoped>
.rounded-corner{
    border-radius:20px;
}
</style>
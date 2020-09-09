<template>
  <v-container>
      <v-container v-for="(day, i) in days" :key="i">
          <v-row class="mb-1 no-gutters">
          <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          max-width="800"
        >
        <v-row>
            <v-col>
                <h3 class="ml-5">{{ day }}</h3>
            </v-col>
            <v-col>
              <h5 class="mt-4">{{i + 10}}.08.2020</h5>
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
    props: [
        'day',
        'date'
    ],
    data: () => ({
      days: ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
    })
  }
</script>

<style scoped>
.rounded-corner{
    border-radius:20px;
}
</style>
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
              <h2 class="ml-5">O Aplikacji</h2>
            </v-col>
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
    <v-container>
      <v-row class="mb-1 no-gutters">
        <v-sheet
          dark
          class="mx-auto rounded-corner"
          elevation="8"
          width="100%"
          color="rgba(28,29,30,0.8)"
        >
          <v-row>
            <v-col cols="10">
              <h3 class="ma-5">Aplikacja wspierająca zdrowe odżywianie</h3>
              <p class="ma-5">
                Aplikacja utworzona w ramach projektu inżynierskiego. Głównym
                celem jest budowanie zdrowych nawyków żywieniowych oraz wiedzy
                związanej ze zdrowym odżywianiem u użytkowników systemu.
                Aplikacja pozwala na wygenerowanie tygodniowej diety, z
                uwzględnieniem preferencji zywieniowych, danych fizycznych
                użytkownika oraz alergenów. Umożliwia również kontrolowanie
                spożytych dziennie kalorii.
                <br /><br />
                Gorąco zachęcamy do testowania funkcjonalności aplikacji oraz
                bardzo prosimy o wypełnienie ankiety:
              </p>
              <v-btn
                class="ml-5"
                href="https://docs.google.com/forms/d/e/1FAIpQLSf-asMzOrwYfGN3bCJCGsnS1N9qnlodIPUg8OgCapkkBfOpug/viewform"
                target="_blank"
                color="#98AF4F"
              >
                Przejdź do ankiety
              </v-btn>
              <h3 class="ma-5">Smacznego!</h3>
            </v-col>
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
export default {
  name: 'About',
  data: () => ({}),
  components: {},
  methods: {},
  async mounted() {},
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
h3 {
  color: white;
}
.transparent-body {
  background: transparent;
}
.theme--light.v-list {
  background: #c2f588;
}
</style>

<template>
  <v-app>
    <v-app-bar
      app
      color="#BBD274"
      dark
    >
    <v-row>
      <v-col lg="1">
        <AppIcon class="ma-3"/>
      </v-col>
      <v-col lg="9">
        <h1 class="ma-4">Zdrowa Dieta</h1>
      </v-col>
      <v-col lg="1">
        <PersonIcon class="ma-3"/>
      </v-col>
    </v-row>
    </v-app-bar>

    <v-main>
      <v-row>
        <v-col lg="2">
           <Menu/>
        </v-col>
         <v-col>
           <FoodMenu/>
        </v-col>
         <v-col lg="2">
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
import AppIcon from './assets/logo.svg';
import PersonIcon from './assets/person-circle.svg';
import Menu from './components/Menu';
import FoodMenu from './components/FoodMenu';

export default {
  name: 'App',

  components: {
    Menu,
    AppIcon,
    FoodMenu,
    PersonIcon
  },

  data: () => ({
    //
  }),
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap');

h1 {
  font-family: 'Dancing Script', cursive;
  color: #c51162;
}


.theme--dark.v-application {
  background-color: var(--v-background-base, #121212) !important;
}
.theme--light.v-application {
  background-color: var(--v-background-base, white) !important;
}
</style>
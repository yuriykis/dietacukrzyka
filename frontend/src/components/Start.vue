<template>
  <v-container class="test">
     <v-container>
        <v-row class="mb-2 no-gutters mh-100 mw-75" >
          <!-- <v-sheet
            class="mx-auto rounded-corner"
            elevation="8"
            width="100%"
            height="70%"
            @click="seeDetails()"
            color="rgba(28,29,30,0.8)"
          > -->

            <v-col class="mh-100 frame ml-0  rounded-corner">
              <v-row class="mx-auto">
                <h1>
                  Witaj 
                </h1>
              </v-row>
              <v-row class="mx-auto">
                <h3  class="mx-auto">
                  Zaloguj się aby zacząć.
                </h3>
              </v-row>
              <!-- <img src="@/assets/Welcome.jpg" alt="Image alt" height="80%"/> -->
            </v-col>
            
          <!-- </v-sheet> -->
        </v-row>
     </v-container>
  </v-container>
</template>

<script>
export default {
  name: 'Start',

  components: {},

  data: () => ({
    user: {},
  }),
  created() {},
  methods: {},
}
</script>

<style scoped>
.rounded-corner {
  border-radius: 20px;
}

h1 {
  color: white;
  font-size: 266px;
}
h3 {
  background-color: #a8c256;
  color: white;
  font-size: 26px;
} 
.frame{
  height: 800px;
  background-image: url('../assets/Welcome.jpg');
  background-size: cover;
}
.test{
  /* background-color: red; */
  /* margin-left: -8.5%; */
}
::v-deep .v-icon.notranslate.mdi.mdi-chevron-right.theme--light{
  color: white;
  background-color: #a8c256;
}

@media screen and (max-width: 600px) {
  h1 {
  font-size: 66px;
  }
  h3 {
    font-size: 22px; 
  } 
}
</style>

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
                <h2 class="ml-5">Twoje Konto</h2>
            </v-col>
        </v-row>
            </v-sheet>
          </v-row>
    </v-container>
      <v-container>
          <v-row class="mb-1 no-gutters">
          <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="800"
          color= "rgba(28,29,30,0.8)"
        >
              <v-row>
                  <v-col>
                   <v-tabs
                   background-color= "rgba(28,29,30,0)"
                   color="#98AF4F"
                   centered
                   v-model="tabs">
                  <v-tab><h4>Ustawienia Konta</h4></v-tab>
                  <v-tab><h4>Dane fizyczne</h4></v-tab>
                  <v-tab><h4>Preferencje żywieniowe</h4></v-tab>
                  <v-tab><h4>Dokumenty</h4></v-tab>
                  </v-tabs>
                  <v-tabs-items v-model="tabs">
                   <v-tab-item>
                     <v-card
                     color= "rgba(116,34,60)">
                     <v-row>
                       <v-col class="ml-3">
                        <v-text-field
                      background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Imię"
                        v-model="data.name"
                        >
                      </v-text-field>
                      <v-text-field
                      background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Numer telefonu"
                        >
                      </v-text-field>
                      <v-text-field
                      background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Miasto"
                        >
                      </v-text-field>
                      <v-text-field
                      background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Kod Pocztowy"
                        >
                      </v-text-field>
                      </v-col>
                      <v-col class="mr-3">
                       <v-text-field
                      background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Nazwisko"
                        v-model="data.last_name"
                        >
                      </v-text-field>
                      <v-text-field
                      background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Adres Email"
                        v-model="data.email"
                        >
                      </v-text-field>
                      <v-text-field
                      background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Region"
                        >
                      </v-text-field>
                      <v-text-field
                      background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Kraj"
                        >
                      </v-text-field>
                      </v-col>
                     </v-row>
                     </v-card>
                   </v-tab-item>
                    <v-tab-item>
                     <v-card
                     color= "rgba(116,34,60)">
                     <v-row>
                       <v-col class="mx-10">
                        <v-text-field
                      background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Masa ciała"
                        v-model="data.weight"
                        >
                      </v-text-field>
                      <v-text-field
                      background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Wzrost"
                        v-model="data.height"
                        >
                      </v-text-field>
                      <v-text-field
                      background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Poziom cukru"
                        >
                      </v-text-field>
                      <v-text-field
                      background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "BMI"
                        >
                      </v-text-field>
                      </v-col>
                     </v-row>
                     </v-card>
                   </v-tab-item>
                    <v-tab-item>
                     <v-card
                     color= "rgba(116,34,60)">
                     <v-row>
                       <v-col>                      
                      </v-col>
                      <v-col>                
                      </v-col>
                     </v-row>
                     </v-card>
                   </v-tab-item>
                    <v-tab-item>
                     <v-card
                     color= "rgba(116,34,60)">
                     <v-row>
                       <v-col>                  
                      </v-col>
                      <v-col>                  
                      </v-col>
                     </v-row>
                     </v-card>
                   </v-tab-item>
                   </v-tabs-items>
                   <v-row lign="center" justify="center">                   
                       <v-btn color="#98AF4F" class="ma-3 white--text" @click="saveNewDetails">{{ 'Zapisz' }}</v-btn>
                     </v-row>
                  </v-col>
              </v-row>
            </v-sheet>
          </v-row>
    </v-container>
  </v-container>
</template>

<script>
import { getClientData, saveClientData } from "@/services/api"
  export default {
    name: 'Menu',
    data: () => ({
      tabs: null,
      data: {}
    }),
    methods: {
      saveNewDetails () {
        saveClientData(this.data)
      },
      fetchData () {
        getClientData().then((response) => {
          this.data = response.data
        })
      }
    },
    mounted () {
      this.fetchData()
    }
  }
</script>

<style scoped>
.rounded-corner{
    border-radius:20px;
}
h2, h4 {
  color: white;
}
h3 {

  color: white;
}
.transparent-body {
  background: transparent
}
</style>
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
              <h2 class="ml-5">Twoje Konto</h2>
            </v-col>
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
    <v-container v-if="loadingData"> </v-container>
    <v-container v-else>
      <v-row class="mb-1 no-gutters">
        <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="100%"
          color="rgba(28,29,30,0.8)"
        >
          <v-row>
            <v-col>
              <v-tabs
                background-color="rgba(28,29,30,0)"
                color="#98AF4F"
                centered
                v-model="tabs"
              >
                <v-tab><h4>Ustawienia Konta</h4></v-tab>
                <v-tab><h4>Dane fizyczne</h4></v-tab>
                <v-tab><h4>Preferencje żywieniowe</h4></v-tab>
                <v-tab><h4>Dokumenty</h4></v-tab>
              </v-tabs>
              <v-tabs-items v-model="tabs">
                <v-tab-item>
                  <v-card color="rgba(116,34,60)">
                    <v-row>
                      <v-col class="ml-3">
                        <v-text-field
                          background-color="light-green lighten-1"
                          color="light-green darken-4"
                          :height="field_height"
                          filled
                          rounded
                          label="Imię"
                          v-model="data.name"
                        >
                        </v-text-field>
                        <v-text-field
                          background-color="light-green lighten-1"
                          color="light-green darken-4"
                          :height="field_height"
                          filled
                          rounded
                          label="Wiek"
                          v-model="data.age"
                        >
                        </v-text-field>
                        <v-text-field
                          background-color="light-green lighten-1"
                          color="light-green darken-4"
                          :height="field_height"
                          filled
                          rounded
                          label="Adres Email"
                          v-model="data.email"
                        >
                        </v-text-field>
                      </v-col>
                      <v-col class="mr-3">
                        <v-text-field
                          background-color="light-green lighten-1"
                          color="light-green darken-4"
                          :height="field_height"
                          filled
                          rounded
                          label="Nazwisko"
                          v-model="data.last_name"
                        >
                        </v-text-field>
                        <v-select
                          :items="gender"
                          background-color="light-green lighten-1"
                          color="light-green darken-4"
                          :height="field_height"
                          filled
                          rounded
                          label="Płeć"
                          v-model="selected_gender"
                        ></v-select>
                        <v-text-field
                          background-color="light-green lighten-1"
                          color="light-green darken-4"
                          :height="field_height"
                          filled
                          rounded
                          label="Kraj zamieszkania"
                        >
                        </v-text-field>
                      </v-col>
                    </v-row>
                  </v-card>
                </v-tab-item>
                <v-tab-item>
                  <v-card color="rgba(116,34,60)">
                    <v-row>
                      <v-col class="mx-10">
                        <v-text-field
                          background-color="light-green lighten-1"
                          color="light-green darken-4"
                          :height="field_height"
                          filled
                          rounded
                          type="number"
                          label="Masa ciała"
                          @change="calculateBmi"
                          v-model="data.weight"
                        >
                        </v-text-field>
                        <v-text-field
                          background-color="light-green lighten-1"
                          color="light-green darken-4"
                          :height="field_height"
                          filled
                          rounded
                          type="number"
                          label="Wzrost"
                          @change="calculateBmi"
                          v-model="data.height"
                        >
                        </v-text-field>
                        <v-text-field
                          background-color="light-green lighten-1"
                          color="light-green darken-4"
                          :height="field_height"
                          filled
                          readonly
                          rounded
                          label="BMI"
                          v-model="bmi"
                        >
                        </v-text-field>
                      </v-col>
                    </v-row>
                  </v-card>
                </v-tab-item>
                <v-tab-item>
                  <v-card color="rgba(116,34,60)">
                    <v-row>
                      <v-col class="mx-10">
                        <v-select
                          :items="getIngredients"
                          background-color="light-green lighten-1"
                          color="light-green darken-4"
                          :height="ingredients_field_height[0]"
                          filled
                          rounded
                          chips
                          multiple
                          label="Ulubione składniki"
                          v-model="preferred_ingredients"
                          @change="changeFieldHeight(0, preferred_ingredients)"
                        ></v-select>
                        <v-select
                          :items="getIngredients"
                          background-color="light-green lighten-1"
                          color="light-green darken-4"
                          :height="ingredients_field_height[1]"
                          filled
                          rounded
                          chips
                          multiple
                          label="Standardowe składniki"
                          v-model="standard_ingredients"
                          @change="changeFieldHeight(1, standard_ingredients)"
                        ></v-select>
                        <v-select
                          :items="getIngredients"
                          background-color="light-green lighten-1"
                          color="light-green darken-4"
                          :height="ingredients_field_height[2]"
                          filled
                          rounded
                          chips
                          multiple
                          label="Alergeny"
                          v-model="allergens"
                          @change="changeFieldHeight(2, allergens)"
                        ></v-select>
                      </v-col>
                    </v-row>
                  </v-card>
                </v-tab-item>
                <v-tab-item>
                  <v-card color="rgba(116,34,60)">
                    <v-row>
                      <v-col> </v-col>
                      <v-col> </v-col>
                    </v-row>
                  </v-card>
                </v-tab-item>
              </v-tabs-items>
              <v-row>
                <v-col>
                  <v-row align="center" justify="center" v-if="loading">
                    <Loader />
                  </v-row>
                  <v-row align="center" justify="center" v-else>
                    <v-btn
                      color="#98AF4F"
                      class="ma-3 white--text"
                      @click="saveNewDetails"
                      >{{ 'Zapisz' }}</v-btn
                    >
                  </v-row>
                  <v-row align="center" justify="center">
                    <h5 v-if="complete_ok" style="color: green;">
                      <span>Dane zostały pomyślnie zaktualizowane</span>
                    </h5>
                    <h5 v-if="fail_mail" style="color: red;">
                      <span>Adres email nie jest dostępny</span>
                    </h5>
                  </v-row>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from 'vuex'
import Loader from '@/components/Loader'
export default {
  name: 'Menu',
  data: () => ({
    tabs: null,
    data: {},
    loading: false,
    loadingData: false,
    complete_ok: false,
    fail_mail: false,
    gender: ['Kobieta', 'Mężczyzna', 'Inna'],
    selected_gender: '',
    bmi: 0,
    preferred_ingredients: [],
    standard_ingredients: [],
    allergens: [],
    field_height: 60,
    ingredients_field_height: [60, 60, 60],
    filed_row: [1, 1, 1],
  }),
  components: {
    Loader,
  },
  computed: mapGetters(['getClientInfoFromStore', 'getIngredients']),
  methods: {
    ...mapActions([
      'saveClientInfoOnServer',
      'getClientInfoFromServer',
      'getAllIngredientsFromServer',
    ]),
    ...mapMutations(['saveClientInfoInStore']),
    changeFieldHeight(item_number, ingredients) {
      var ingredients_string = ''
      ingredients.forEach((ingredient) => {
        ingredients_string += ingredient
      })
      if (ingredients_string.length > 100 * this.filed_row[item_number]) {
        this.ingredients_field_height[item_number] += 60
        this.filed_row[item_number]++
      }
    },
    async saveNewDetails() {
      this.data['preferred_ingredients'] = this.preferred_ingredients
      this.data['standard_ingredients'] = this.standard_ingredients
      this.data['allergens'] = this.allergens
      this.saveClientInfoInStore(this.data)
      this.loading = true
      this.complete_ok = false
      this.fail_mail = false
      this.genderTranslator(this.selected_gender)
      try {
        await this.saveClientInfoOnServer(this.data)
        this.loading = false
        this.complete_ok = true
        this.fail_mail = false
      } catch (e) {
        this.loading = false
        this.complete_ok = false
        this.fail_mail = true
      }
    },
    calculateBmi() {
      this.bmi =
        Math.round(
          (this.data.weight / Math.pow(this.data.height / 100, 2)) * 100
        ) / 100
    },
    genderTranslator(gender) {
      switch (gender) {
        case 'male':
          this.selected_gender = 'Mężczyzna'
          break
        case 'female':
          this.selected_gender = 'Kobieta'
          break
        case 'other':
          this.selected_gender = 'Inna'
          break
        case 'Mężczyzna':
          this.data.gender = 'male'
          break
        case 'Kobieta':
          this.data.gender = 'female'
          break
        case 'Inna':
          this.data.gender = 'other'
          break
        default:
          break
      }
    },
    async fetchData() {
      await this.getClientInfoFromServer()
      this.data = this.getClientInfoFromStore
      console.log(this.data)
      this.genderTranslator(this.data.gender)
      this.calculateBmi()
    },
  },
  async mounted() {
    this.fetchData()
    await this.getAllIngredientsFromServer()
  },
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

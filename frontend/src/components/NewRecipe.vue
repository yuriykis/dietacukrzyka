<template>
  <v-container>
    <v-dialog v-model="dialog" persistent max-width="520">
      <v-card dark color="#a8c256">
        <v-card-title class="headline">
          Proszę wprowadzić procent wagi składnika
        </v-card-title>
        <v-card-actions>
          <v-col>
            <v-text-field
              background-color="light-green lighten-1"
              color="light-green darken-4"
              type="number"
              filled
              rounded
              label="Procent wagi"
              v-model="mass_fraction_actual"
              :rules="[
                checkMassFraction(mass_fraction_actual, mass_whole_meal),
              ]"
            >
            </v-text-field>
            <v-row justify="center">
              <v-btn color="green darken-1" text @click="saveMassFraction"
                >OK</v-btn
              >
            </v-row>
          </v-col>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-snackbar
      v-model="snackbar"
      :multi-line="multiLine"
      :top="y === 'top'"
      timeout="4000"
      :color="color"
    >
      {{ text }}

      <template v-slot:action="{ attrs }">
        <v-btn color="blue" text v-bind="attrs" @click="snackbar = false">
          <v-icon color="blue">{{ 'mdi-close-circle-outline ' }}</v-icon>
        </v-btn>
      </template>
    </v-snackbar>
    <v-container>
      <v-row class="mb-2 no-gutters">
        <v-sheet
          class="mx-auto rounded-corner"
          elevation="8"
          width="100%"
          max-height="80"
          color="rgba(116,34,60,0.8)"
        >
          <v-row>
            <v-col cols="7">
              <h2 class="ma-4">Tworzenie nowego przepisu</h2>
            </v-col>
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
    <v-container>
      <v-row class="mb-1 no-gutters">
        <v-sheet
          class="rounded-corner"
          width="100%"
          color="rgba(28,29,30,0.8)"
          style="position: relative;"
        >
          <v-overlay :absolute="true" :value="loading">
            <Loader />
          </v-overlay>
          <v-row justify="center" align="center">
            <v-card color="rgba(116,34,60)" width="100%" class="ma-3 mt-5">
              <v-col>
                <v-text-field
                  background-color="light-green lighten-1"
                  color="light-green darken-4"
                  :height="field_height"
                  filled
                  rounded
                  label="Nazwa przepisu"
                  v-model="name"
                >
                </v-text-field>
                <v-select
                  :items="getIngredients"
                  background-color="light-green lighten-1"
                  color="light-green darken-4"
                  :height="field_height"
                  filled
                  rounded
                  chips
                  multiple
                  label="Składniki"
                  v-model="ingredients"
                  @change="dialog = true"
                ></v-select>
                <v-select
                  :items="recipe_types"
                  background-color="light-green lighten-1"
                  color="light-green darken-4"
                  :height="field_height"
                  filled
                  rounded
                  label="Typ posiłku"
                  v-model="recipe_type"
                ></v-select>
                <v-text-field
                  background-color="light-green lighten-1"
                  color="light-green darken-4"
                  :height="field_height"
                  filled
                  rounded
                  label="Opis przygotowania"
                  v-model="description"
                >
                </v-text-field>
                <v-progress-linear
                  class="rounded-corner"
                  :value="progress"
                  color="#a8c256"
                  height="40"
                  dark
                >
                  <strong>{{ progress }} %</strong>
                </v-progress-linear>

                <v-file-input
                  class="rounded-corner"
                  label="Zdjęcie przepisu"
                  background-color="light-green lighten-1"
                  color="light-green darken-4"
                  height="50"
                  v-model="file"
                  @change="selectFile"
                ></v-file-input>
              </v-col>
            </v-card>
            <v-btn
              :disabled="isFileLoading"
              @click="upload"
              color="#98AF4F"
              class="ma-3 white--text"
              >{{ 'Zapisz' }}</v-btn
            >
          </v-row>
        </v-sheet>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { uploadFile, saveNewRecipe } from '../services/api'
import Loader from '@/components/Loader'
export default {
  name: 'NewRecipe',
  data: () => ({
    loading: false,
    snackbar: false,
    color: '',
    text: '',
    y: 'top',
    dialog: false,
    field_height: 70,
    ingredients: [],
    name: '',
    description: '',
    progress: 0,
    file: {},
    recipe_types: [
      'sniadanie',
      'II sniadanie',
      'obiad',
      'podwieczorek',
      'kolacja',
    ],
    recipe_type: '',
    mass_fraction_actual: '',
    mass_whole_meal: 1,
    mass_fractions: {},
  }),
  methods: {
    ...mapActions(['getAllIngredientsFromServer']),
    async upload() {
      this.loading = true
      if (!this.file || !this.name || !this.description || !this.ingredients) {
        this.setSnackBar('Proszę uzupełnić wszystkie dane', '#C62828')
        this.loading = false
      } else {
        this.isFileLoading = true
        this.saveRecipe()
        try {
          const fileName = this.name.replaceAll(' ', '_').replaceAll(',', '')
          await uploadFile(
            this.file,
            (event) => {
              this.progress = Math.round((100 * event.loaded) / event.total)
            },
            fileName
          )
          this.setSnackBar('Nowy przepis został pomyślnie dodany', '#2E7D32')
          this.loading = false
        } catch (e) {
          this.progress = 0
          this.setSnackBar('Nie udało się załadować zdjęcia', '#C62828')
          this.loading = false
        }
        this.isFileLoading = false
      }
    },
    async saveRecipe() {
      const recipe = {
        name: this.name,
        ingredients: this.ingredients,
        description: this.description,
        recipe_type: this.recipe_type,
        mass_fractions: this.mass_fractions,
      }
      await saveNewRecipe(recipe)
    },
    saveMassFraction() {
      this.dialog = false
      this.mass_fractions[
        this.ingredients[this.ingredients.length - 1]
      ] = this.mass_fraction_actual
      this.mass_whole_meal -= this.mass_fraction_actual
    },
    checkMassFraction: function(v, max) {
      return (v) =>
        v <= max ||
        'Wartość nie może być większa niż ' + Math.round(max * 1000) / 1000
    },
    setSnackBar(text, color) {
      this.text = text
      this.color = color
      this.snackbar = true
    },
  },
  computed: {
    ...mapGetters(['getIngredients']),
  },
  components: {
    Loader,
  },
  mounted() {
    this.getAllIngredientsFromServer()
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
  background-color: #a8c256;
  color: white;
}
.theme--light.v-list {
  background: #c2f588;
}
</style>

<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col class=" mr-15" cols="12" align="center" justify="center">
        <h1>Rejestracja</h1>
        <v-container v-if="loading">
          <Loader />
        </v-container>
        <v-container v-else-if="completed">
          <Checkmark />
          <h2>Rejestracja przepiegła pomyślnie!</h2>
          <v-btn
            color="light-green darken-4"
            class="mt-10 white--text"
            @click="login"
            >{{ 'Przejdź do strony logowania' }}</v-btn
          >
        </v-container>
        <v-container v-else class="ma-10" style="width: 50%">
          <v-text-field
            background-color="light-green lighten-1"
            color="light-green darken-4"
            height="40"
            filled
            rounded
            label="Imię"
            :rules="[rules.required]"
            v-model="user.name"
          >
          </v-text-field>
          <v-text-field
            background-color="light-green lighten-1"
            color="light-green darken-4"
            height="40"
            filled
            rounded
            label="Nazwisko"
            :rules="[rules.required]"
            v-model="user.last_name"
          >
          </v-text-field>
          <v-text-field
            background-color="light-green lighten-1"
            color="light-green darken-4"
            height="40"
            filled
            rounded
            label="Wiek"
            type="number"
            :rules="[
              rules.required,
              minValue(user.age, 1),
              maxValue(user.age, 150),
            ]"
            v-model="user.age"
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
            v-model="user.gender"
          ></v-select>
          <v-text-field
            background-color="light-green lighten-1"
            color="light-green darken-4"
            height="40"
            filled
            rounded
            label="Login"
            :rules="[rules.required]"
            v-model="user.username"
          >
          </v-text-field>
          <v-text-field
            background-color="light-green lighten-1"
            color="light-green darken-4"
            height="40"
            filled
            rounded
            label="Hasło"
            type="password"
            :rules="[rules.required]"
            v-model="user.password"
          >
          </v-text-field>
          <v-text-field
            background-color="light-green lighten-1"
            color="light-green darken-4"
            height="40"
            filled
            rounded
            label="Powtórz hasło"
            type="password"
            :rules="[rules.required, checkPassword(password2, user.password)]"
            v-model="password2"
          >
          </v-text-field>
          <v-btn
            color="light-green darken-4"
            class="ma-3 white--text"
            @click="registerUser"
            >{{ 'Rejestruj' }}</v-btn
          >
          <h6 v-if="notAllData" style="color: red;">
            Proszę podać wszystkie dane
          </h6>
        </v-container>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { register } from '@/services/api'
import Loader from '@/components/Loader'
import Checkmark from '@/components/Checkmark'
export default {
  name: 'Home',

  components: {
    Loader,
    Checkmark,
  },

  data: () => ({
    user: {
      name: '',
      last_name: '',
      age: '',
      username: '',
      password: '',
      gender: '',
    },
    gender: ['Kobieta', 'Mężczyzna', 'Inna'],
    password2: '',
    rules: {
      required: (value1) => !!value1 || 'Pole wymagane',
    },
    loading: false,
    completed: false,
    notAllData: false,
  }),
  created() {},
  methods: {
    registerUser() {
      this.loading = true
      this.notAllData = false
      let canRegister = true
      for (let field in this.user) {
        if (this.user[field] === '') {
          canRegister = false
          this.notAllData = true
          break
        }
      }
      if (canRegister) {
        this.genderTranslator(this.user.gender)
        this.user.age = parseInt(this.user.age, 10)
        register(this.user).then(() => {
          this.loading = false
          this.completed = true
        })
      }
      this.loading = false
    },
    login() {
      this.$router.push({ path: '/login' })
    },
    minValue: function(v, min) {
      return (v) =>
        v >= min ||
        'Wartość nie może być mniejsza niż ' + Math.round(min * 1000) / 1000
    },
    maxValue: function(v, max) {
      return (v) =>
        v <= max ||
        'Wartość nie może być większa niż ' + Math.round(max * 1000) / 1000
    },
    checkPassword: function(v, pass) {
      return (v) =>
        v === pass || 'Wprowadzone hasło nie jest zgodne z poprzednim'
    },
    genderTranslator(gender) {
      switch (gender) {
        case 'Mężczyzna':
          this.user.gender = 'male'
          break
        case 'Kobieta':
          this.user.gender = 'female'
          break
        case 'Inna':
          this.user.gender = 'other'
          break
        default:
          break
      }
    },
  },
}
</script>

<style>
h1 {
  font-family: 'Dancing Script', cursive;
  color: #c51162;
}
h2 {
  color: #c51162;
}
.my-text-style >>> .v-text-field__slot input {
  color: red;
}
</style>

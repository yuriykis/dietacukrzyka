<template>
   <v-container>         
        <v-row>
            <v-col class="mt-10" cols=12  align="center" justify="center">
                <h1>Rejestracja</h1>
                <v-container class="ma-10" style="width: 50%">
                    <v-text-field
                        background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Imię"
                        :rules="[rules.required]"
                        :v-model="user.name"
                        >
                      </v-text-field>
                    <v-text-field
                        background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Nazwisko"
                        :rules="[rules.required]"
                        :v-model="user.last_name"
                        >
                      </v-text-field>
                    <v-text-field
                        background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Wiek"
                        type="number"
                        :rules="[rules.required,
                            minValue(user.age, 1),
                            maxValue(user.age, 150)
                        ]"
                        :v-model="user.age"
                        >
                      </v-text-field>
                    <v-text-field
                        background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Login"
                        :rules="[rules.required]"
                        :v-model="user.login"
                        >
                      </v-text-field>
                    <v-text-field
                        background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Hasło"
                        :rules="[rules.required]"
                        :v-model="user.password"
                        >
                      </v-text-field>
                    <v-text-field
                        background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        label= "Powtórz hasło"
                        :rules="[rules.required]"
                        :v-model="password2"
                        >
                      </v-text-field>                      
                    <v-btn color="light-green darken-4" class="ma-3 white--text" @click="registerUser">{{ 'Rejestruj' }}</v-btn>
                </v-container>
            </v-col>
        </v-row>
      </v-container>
</template>

<script>
import { register } from '@/services/api'
export default {
  name: 'Home',

  components: {
  },

  data: () => ({
    user: {
        name: '',
        last_name: '',
        age: '',
        login: '',
        password: ''
    },
    password2: '',
    rules: {
        required: value1 => !!value1 || 'Pole wymagane'
      }

  }),
  created () {
  },
  methods: {
    registerUser () {
      register(this.user)
    },
    minValue: function (v, min) {
      return v => v >= min || 'Wartość nie może być mniejsza niż ' + Math.round(min * 1000) / 1000
    },
    maxValue: function (v, max) {
      return v => v <= max || 'Wartość nie może być większa niż ' + Math.round(max * 1000) / 1000
    },

  }
};
</script>

<style>
h1 {
  font-family: 'Dancing Script', cursive;
  color: #c51162;
}
.my-text-style >>> .v-text-field__slot input {
    color: red
  }
</style>
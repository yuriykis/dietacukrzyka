<template>
   <v-container>         
        <v-row>
            <v-col class="mt-10" cols=12  align="center" justify="center">
                <h1>Zarestruj się</h1>
                <v-container class="ma-10" style="width: 50%">
                    <div v-for="(field, i) in fields" :key="i">
                        <v-text-field
                        background-color="light-green lighten-1"
                        color="light-green darken-4"
                        height=40
                        filled
                        rounded
                        :label= "field"
                        v-model="user[i]"
                        >
                        </v-text-field>
                    </div>
                    <v-btn color="light-green darken-4" class="ma-3 white--text" @click="registerUser">{{ 'Rejestracja' }}</v-btn>
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
        age: 0,
        login: '',
        password: ''
    },
    fields: {
        name: 'Imię',
        last_name: 'Nazwisko',
        age: 'Wiek',
        login: 'Login',
        password: 'Powtórz hasło'
    }
  }),
  created () {
  },
  methods: {
    registerUser () {
      console.log(this.user)
      register(this.user)
    }
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
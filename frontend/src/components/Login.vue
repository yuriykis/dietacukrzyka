<template>
  <v-container>
    <v-snackbar
      v-model="snackbar"
      :multi-line="multiLine"
      :top="y === 'top'"
      timeout="4000"
      color="#C62828"
    >
      {{ 'Błędne dane logowania' }}

      <template v-slot:action="{ attrs }">
        <v-btn color="blue" text v-bind="attrs" @click="snackbar = false">
          <v-icon color="blue">{{ 'mdi-close-circle-outline ' }}</v-icon>
        </v-btn>
      </template>
    </v-snackbar>
    <v-row>
      <v-col class="mt-10" cols="12" align="center" justify="center">
        <h1>Logowanie</h1>
        <v-container v-if="loading">
          <Loader />
        </v-container>
        <v-container v-else class="ma-10" style="width: 50%">
          <v-form ref="form" @submit.prevent="loginUser">
            <div>
              <v-text-field
                background-color="light-green lighten-1"
                color="light-green darken-4"
                height="40"
                filled
                rounded
                label="Login"
                v-model="user.login"
              >
              </v-text-field>
            </div>
            <div>
              <v-text-field
                background-color="light-green lighten-1"
                color="light-green darken-4"
                height="40"
                filled
                rounded
                type="password"
                label="Hasło"
                v-model="user.password"
              >
              </v-text-field>
            </div>
            <v-btn
              color="light-green darken-4"
              class="ma-3 white--text"
              type="submit"
              >{{ 'Zaloguj' }}</v-btn
            >
          </v-form>
        </v-container>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { login } from '@/services/api'
import { setLocalStorageTokens } from '@/services/auth'
import Loader from '@/components/Loader'
export default {
  name: 'Home',
  components: {
    Loader,
  },
  data: () => ({
    snackbar: false,
    y: 'top',
    dialog: true,
    user: {
      login: '',
      password: '',
    },
    loading: false,
  }),
  created() {},
  methods: {
    loginUser() {
      this.loading = true
      login(this.user)
        .then((response) => {
          if (response.status === 200) {
            setLocalStorageTokens(response.data)
            this.loading = false
            this.$router.push({ path: '/home' })
            location.reload()
          }
        })
        .catch(() => {
          this.loading = false
          this.snackbar = true
        })
    },
  },
}
</script>

<style></style>

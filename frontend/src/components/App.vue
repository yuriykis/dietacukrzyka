<template>
  <v-app>
    <v-app-bar
      app
      color="#BBD274"
      dark
      depressed
    >
    <v-row v-if="isUserLogin">
      <v-col cols="1">
        <AppIcon @click="goToHome"/>
      </v-col>
      <v-col cols="7">
        <h1>Zdrowa Dieta</h1>
      </v-col>
      <v-col cols="1">
        <PersonIcon/>
      </v-col>
      <v-col cols="1">
        <v-btn color="light-green darken-4" class="ma-3" @click="logout">{{ 'Wyloguj' }}</v-btn>
      </v-col>
      <v-col cols="1">
      </v-col>
    </v-row>
    <v-row v-else>
      <v-col cols="1">
        <AppIcon @click="goToHome"/>
      </v-col>
      <v-col cols="7">
        <h1>Zdrowa Dieta</h1>
      </v-col>
      <v-col cols="1">
      </v-col>
      <v-col cols="1">
        <v-btn color="light-green darken-4" class="ma-3" @click="login">{{ 'Logowanie' }}</v-btn>
      </v-col>
      <v-col cols="1">
        <v-btn color="light-green darken-4" class="ma-3" @click="register">{{ 'Rejestracja' }}</v-btn>
      </v-col>
    </v-row>
    </v-app-bar>

    <v-main>
      <v-row>
        <v-col lg="3" class="pt-0 pb-0">
           <Menu v-if="isUserLogin"/>
        </v-col>
        <v-col lg="7">
           <router-view/>
        </v-col>
        <v-col lg="2">
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
// @ is an alias to /src
import AppIcon from '@/assets/logo.svg';
import PersonIcon from '@/assets/person-circle.svg';
import Menu from '@/components/Menu';
import { updateAccessToken, isValidAccessToken, removeLocalStorageTokens } from '@/services/auth'

export default {
  name: 'App',
  data: () => ({
    isUserLogin: false
  }),
  components: {
    Menu,
    AppIcon,
    PersonIcon
  },
  methods: {
    goToHome () {
        this.$router.push({ path: '/home' })
      },
    register () {
      this.$router.push({ path: '/register' })
    },
    login () {
      this.$router.push({ path: '/login' })
    },
    logout () {
      removeLocalStorageTokens()
      this.$router.push({ path: '/login' })
      location.reload()
    },
    ifUserLogin () {
      this.isUserLogin = isValidAccessToken()
    }
  },
  mounted () {
        this.$nextTick(function () {
            window.setInterval(() => {
                updateAccessToken()
            },100000)
        })
  },
  created () {
    this.ifUserLogin()
  }
}
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
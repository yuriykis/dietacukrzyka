<template>
  <v-app>
    <v-app-bar app color="#1C1D1F" dark depressed>
      <v-row v-if="isUserLogin">
        <v-col cols="1">
          <AppIcon @click="goToHome" />
        </v-col>
        <v-col cols="7">
          <h1>Zdrowa Dieta</h1>
        </v-col>
        <v-col cols="1">
          <PersonIcon />
        </v-col>
        <v-col cols="1">
          <v-btn color="#98AF4F" class="ma-3" @click="logout">{{
            'Wyloguj'
          }}</v-btn>
        </v-col>
        <v-col cols="1"> </v-col>
      </v-row>
      <v-row v-else>
        <v-col cols="1">
          <AppIcon @click="goToHome" />
        </v-col>
        <v-col cols="7">
          <h1>Zdrowa Dieta</h1>
        </v-col>
        <v-col cols="1"> </v-col>
        <v-col cols="1">
          <v-btn color="#98AF4F" class="ma-3" @click="login">{{
            'Logowanie'
          }}</v-btn>
        </v-col>
        <v-col cols="1">
          <v-btn color="#98AF4F" class="ma-3" @click="register">{{
            'Rejestracja'
          }}</v-btn>
        </v-col>
      </v-row>
    </v-app-bar>

    <v-main class="set-background">
      <v-row>
        <v-col lg="3">
          <Menu style="position: fixed; padding-top: 4%;" v-if="isUserLogin" />
        </v-col>
        <v-col lg="7">
          <transition name="fade">
            <router-view />
          </transition>
        </v-col>
        <v-col lg="2"> </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
// @ is an alias to /src
import AppIcon from '@/assets/logo.svg'
import PersonIcon from '@/assets/person-circle.svg'
import Menu from '@/components/Menu'
import {
  updateAccessToken,
  isValidAccessToken,
  removeLocalStorageTokens,
} from '@/services/auth'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'App',
  data: () => ({
    isUserLogin: false,
  }),
  components: {
    Menu,
    AppIcon,
    PersonIcon,
  },
  computed: mapGetters(['getClientInfo']),
  methods: {
    ...mapActions(['fetchData']),
    goToHome() {
      this.$router.push({ path: '/home' })
    },
    register() {
      this.$router.push({ path: '/register' })
    },
    login() {
      this.$router.push({ path: '/login' })
    },
    logout() {
      removeLocalStorageTokens()
      this.$router.push({ path: '/login' })
      location.reload()
    },
    ifUserLogin() {
      this.isUserLogin = isValidAccessToken()
    },
  },
  async mounted() {
    await this.fetchData()
    console.log(this.getClientInfo)
    this.$nextTick(function() {
      window.setInterval(() => {
        updateAccessToken()
      }, 100000)
    })
  },
  created() {
    this.ifUserLogin()
  },
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
  background-image: url('../assets/background.jpg');
}
.theme--light.v-application {
  background-color: var(--v-background-base, white) !important;
  background-image: url('../assets/background.jpg');
}

.fade-enter-active,
.fade-leave-active {
  transition-property: opacity;
  transition-duration: 0.25s;
}

.fade-enter-active {
  transition-delay: 0.25s;
}

.fade-enter,
.fade-leave-active {
  opacity: 0;
}

.set-background {
  background-image: url('../assets/background.jpg');
  background-attachment: fixed; /*fixed;*/
  background-size: 1700px;
}
</style>

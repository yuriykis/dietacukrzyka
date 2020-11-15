<template>
  <v-app>
    <v-app-bar app color="#1C1D1F" dark depressed>
      <v-row v-if="isUserLogin">
        <v-col cols="1">
          <AppIcon
            class="mt-2 ml-3"
            :style="{ cursor: 'pointer' }"
            @click="goToHome"
          />
        </v-col>
        <v-col cols="7">
          <h1 class="mt-2">Zdrowa Dieta</h1>
        </v-col>
        <v-col cols="1">
          <v-tooltip v-model="show" bottom>
            <template v-slot:activator="{ on, attrs }">
              <PersonIcon
                v-bind="attrs"
                v-on="on"
                @click="goToProfile"
                class="mt-2"
              />
            </template>
            <span>Ustawienia konta</span>
          </v-tooltip>
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
          <AppIcon class="mt-2 ml-3" @click="goToHome" />
        </v-col>
        <v-col cols="8">
          <h1 class="mt-2">Zdrowa Dieta</h1>
        </v-col>
        <v-col cols="1">
          <v-btn color="#98AF4F" class="ma-3" @click="login">{{
            'Logowanie'
          }}</v-btn>
        </v-col>
        <v-col cols="2">
          <v-btn color="#98AF4F" class="ma-3 ml-10" @click="register">{{
            'Rejestracja'
          }}</v-btn>
        </v-col>
      </v-row>
    </v-app-bar>

    <v-main>
      <div
        style="background-color: black; width: 100%; height: 100%; position: absolute;"
      >
        <div class="set-background"></div>
      </div>
      <v-row style="position:relative;">
        <v-col cols="3">
          <div style="position: fixed; width: 23%;">
            <Menu v-if="isUserLogin" />
          </div>
        </v-col>
        <v-col cols="7">
          <v-row justify="center" align="center" v-if="loading">
            <Loader />
          </v-row>
          <transition v-else name="fade">
            <router-view />
          </transition>
        </v-col>
        <v-col cols="2"> </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
// @ is an alias to /src
import AppIcon from '@/assets/logo.svg'
import PersonIcon from '@/assets/person-circle.svg'
import Menu from '@/components/Menu'
import Loader from '@/components/Loader'
import { mapGetters, mapActions } from 'vuex'
import {
  updateAccessToken,
  isValidAccessToken,
  removeLocalStorageTokens,
} from '@/services/auth'
export default {
  name: 'App',
  data: () => ({
    show: false,
    isUserLogin: false,
    loading: true,
  }),
  components: {
    Menu,
    AppIcon,
    PersonIcon,
    Loader,
  },
  computed: mapGetters(['getClientInfo']),
  methods: {
    ...mapActions(['fetchData', 'getRecipesFromServer', 'fetchAllImages']),
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
    goToProfile() {
      this.$router.push({ path: '/profile' })
    },
  },
  async mounted() {
    if (this.isUserLogin) {
      await this.fetchData()
      await this.getRecipesFromServer()
      await this.fetchAllImages()
    }
    this.loading = false
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
  background-attachment: fixed;
  background-size: cover;
  filter: blur(3px);
  width: 100%;
  height: 100%;
  margin: -5px;
}
</style>

<template>
  <v-navigation-drawer
    v-model="drawer"
    :mini-variant.sync="mini"
    floating
    flat
    permanent
    color="transparent"
    width="100%"
  >
    <v-list-item class="px-2">
      <v-btn icon color="#98AF4F" @click.stop="mini = !mini">
        <v-icon large>mdi-view-headline</v-icon>
      </v-btn>
    </v-list-item>

    <v-list dense>
      <v-list-item>
        <v-list-item-icon class="my-5">
          <v-icon color="#98AF4F">{{ 'mdi-food-variant' }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-btn @click="seeDailyDetails" color="rgba(28,29,30,0.9)"
            ><h4>Dieta na dziś</h4></v-btn
          >
        </v-list-item-content>
      </v-list-item>

      <v-list-item>
        <v-list-item-icon class="my-5">
          <v-icon color="#98AF4F">{{ 'mdi-silverware-fork-knife' }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-btn @click="goToHome" color="rgba(28,29,30,0.9)"
            ><h4>Dieta na ten tydzień</h4></v-btn
          >
        </v-list-item-content>
      </v-list-item>

      <v-list-item>
        <v-list-item-icon class="my-5">
          <v-icon color="#98AF4F">{{ 'mdi-food-apple' }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-btn @click="goToFeaturedRecipes" color="rgba(28,29,30,0.9)"
            ><h4>Przepisy</h4></v-btn
          >
        </v-list-item-content>
      </v-list-item>

      <v-list-item>
        <v-list-item-icon class="my-5">
          <v-icon color="#98AF4F">{{ 'mdi-account-details-outline' }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-btn color="rgba(28,29,30,0.9)"><h4>Porady</h4></v-btn>
        </v-list-item-content>
      </v-list-item>

      <v-list-item>
        <v-list-item-icon class="my-5">
          <v-icon color="#98AF4F">{{ 'mdi-cog' }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-btn @click="goToProfile" color="rgba(28,29,30,0.9)"
            ><h4>Ustawienia Konta</h4></v-btn
          >
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Menu',
  data: () => ({
    days: [
      'Poniedziałek',
      'Wtorek',
      'Środa',
      'Czwartek',
      'Piątek',
      'Sobota',
      'Niedziela',
    ],
    current_day: '',
    current_date: '',
    drawer: true,
    mini: true,
  }),
  computed: mapGetters(['getClientInfo']),
  methods: {
    goToHome() {
      this.$router.push({ path: '/home' })
    },
    goToFeaturedRecipes() {
      this.$router.push({ path: '/featured_recipes' })
    },
    goToProfile() {
      this.$router.push({ path: '/profile' })
    },
    seeDailyDetails() {
      if (this.getClientInfo.empty) {
        this.$router.push({
          path: '/home',
        })
      } else {
        var today = new Date()
        var dd = String(today.getDate()).padStart(2, '0')
        var mm = String(today.getMonth() + 1).padStart(2, '0')
        var yyyy = today.getFullYear()

        this.current_date = yyyy + '-' + mm + '-' + dd
        this.current_day = today.getDay() - 1
        if (this.current_day === -1) {
          this.current_day = 6
        }

        this.$router
          .push({
            path: `/details/current/${this.current_date}/${
              this.days[this.current_day]
            }`,
          })
          .catch(() => {})
      }
    },
  },
}
</script>

<style scoped>
h4 {
  color: white;
}
</style>

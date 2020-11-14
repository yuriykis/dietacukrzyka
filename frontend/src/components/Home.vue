<template>
  <v-container>
    <FoodMenu v-if="!getClientInfo.empty" />
    <v-row v-else align="center" justify="center">
      <v-sheet
        class="mx-auto rounded-corner"
        elevation="8"
        width="100%"
        max-height="80"
        color="rgba(116,34,60,0.8)"
      >
        <v-row>
          <v-col align="center" justify="center">
            <h3 class="ma-4">
              Nie masz jeszcze utworzonej diety na ten tydzień. Przejdź do
              ustawień i wygeneruj pierwsze zdrowe posiłki!
            </h3>
          </v-col>
        </v-row>
      </v-sheet>
      <v-btn
        color="light-green darken-4"
        class="mt-10 white--text"
        @click="goToProfile"
        >{{ 'Ustawienia' }}</v-btn
      >
    </v-row>
  </v-container>
</template>

<script>
import FoodMenu from '@/components/FoodMenu'
import { mapGetters } from 'vuex'
export default {
  name: 'Home',
  components: {
    FoodMenu,
  },
  data: () => ({
    user: {},
  }),
  created() {},
  methods: {
    goToProfile() {
      this.$router.push({ path: '/profile' })
    },
  },
  computed: mapGetters(['getClientInfo']),
  async mounted() {},
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
h3 span {
  background-color: rgba(116, 34, 60, 0.8);
  color: white;
}
h3 {
  color: white;
}
</style>

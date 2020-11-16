<template>
  <v-dialog v-model="dialog" fullscreen transition="dialog-transition">
    <v-card dark class="frame">
      <v-row class="mb-2 no-gutters mh-100 mw-75">
        <v-col class="mh-100 ml-0  rounded-corner">
          <v-row class="mx-auto">
            <h4 class="noselect">
              Witaj
            </h4>
          </v-row>
          <v-row class="mx-auto">
            <v-btn color="green darken-1" class="mx-auto" @click="goTologin">
              Zaloguj się aby zacząć.
            </v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'Start',

  components: {},

  data: () => ({
    dialog: true,
    user: {},
  }),
  created() {},
  methods: {
    goTologin() {
      this.dialog = false
      setTimeout(() => {
        this.$router.push({ path: '/login' })
      }, 200)
    },
  },
}
</script>

<style scoped>
.rounded-corner {
  border-radius: 20px;
}
h2,
h4 {
  font-family: 'Dancing Script', cursive;
  color: white;
  font-size: 266px;
}
h3 {
  background-color: #a8c256;
  color: white;
  font-size: 26px;
}
.frame {
  height: 800px;
  background-image: url('../assets/Welcome.jpg');
  background-size: cover;
}
.test {
  /* background-color: red; */
  margin-left: -8.5%;
}
::v-deep .v-icon.notranslate.mdi.mdi-chevron-right.theme--light {
  color: white;
  background-color: #a8c256;
}
.noselect {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Old versions of Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently
                                  supported by Chrome, Edge, Opera and Firefox */
}
</style>

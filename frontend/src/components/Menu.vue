<template>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant.sync="mini"
      flat color="transparent"
      width=350
    >
      <v-list-item class="px-2">
        <v-btn
          icon
          color="#98AF4F"
          @click.stop="mini = !mini"
        >
          <v-icon large>mdi-view-headline</v-icon>
        </v-btn>
      </v-list-item>

      <v-list dense>
        <v-list-item>
          <v-list-item-icon class="my-5">
            <v-icon color="#98AF4F">{{ 'mdi-silverware-fork-knife' }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-btn @click="goToHome" color= "rgba(28,29,30,0.9)"><h4>Dieta na ten tydzień</h4></v-btn>
          </v-list-item-content>

          </v-list-item>

          <v-list-item>
            
          <v-list-item-icon class="my-5">
            <v-icon color="#98AF4F">{{ 'mdi-food-apple' }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-btn @click="goToFeaturedRecipes" color= "rgba(28,29,30,0.9)"><h4>Przepisy</h4></v-btn>
          </v-list-item-content>
          
        
        </v-list-item>
        <v-list-item
          v-for="item in items"
          :key="item.title"
        >
          <v-list-item-icon class="my-5">
            <v-icon color="#98AF4F">{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-btn color= "rgba(28,29,30,0.9)"><h4>{{ item.title }}</h4></v-btn>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
</template>

<script>
  export default {
    name: 'Menu',
    data: () => ({
      drawer: true,
        items: [
          { title: 'Porady', icon: 'mdi-account-details-outline' },
          { title: 'Konto', icon: 'mdi-account' },
          { title: 'Ustawienia', icon: 'mdi-cog' },
        ],
        mini: true,
    }),
    methods: {
      goToHome () {
        this.$router.push({ path: '/home' })
      },
      goToFeaturedRecipes () {
        this.$router.push({ path: '/featured_recipes' })
      }
    }
  }
</script>

<style scoped>
h4 {
  color: white;
}
</style>
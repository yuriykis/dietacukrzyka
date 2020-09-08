<template>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant.sync="mini"
      color="#F3D9B1"
      width=350
    >
      <v-list-item class="px-2">
        <v-btn
          icon
          color="white"
          @click.stop="mini = !mini"
        >
          <v-icon large>mdi-view-headline</v-icon>
        </v-btn>
      </v-list-item>

      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
        >
          <v-list-item-icon class="my-5">
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-btn>{{ item.title }}</v-btn>
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
          { title: 'Dieta na ten tydzień', icon: 'mdi-silverware-fork-knife' },
          { title: 'Przepisy', icon: 'mdi-food-apple' },
          { title: 'Porady', icon: 'mdi-account-details-outline' },
          { title: 'Konto', icon: 'mdi-account' },
          { title: 'Ustawienia', icon: 'mdi-cog' },
        ],
        mini: true,
    }),
  }
</script>

<style scoped>
.menu-color {
  color: '#F3D9B1';
}
</style>
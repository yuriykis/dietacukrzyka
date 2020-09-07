<template>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant.sync="mini"
      color="#F3A9A0"
    >
      <v-list-item class="px-2">
        <v-btn
          icon
          color="white"
          @click.stop="mini = !mini"
        >
          <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
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
          { title: 'Home', icon: 'mdi-home-city' },
          { title: 'My Account', icon: 'mdi-account' },
          { title: 'Users', icon: 'mdi-account-group-outline' },
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
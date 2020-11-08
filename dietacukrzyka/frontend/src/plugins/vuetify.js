import Vue from 'vue';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

export default new Vuetify({
    treeShake: true,
    theme: {
      options: {
        customProperties: true
      },
      dark: false,
      themes: {
        dark: {
          background: '#F3D9B1',
        },
        light: {
          background: '#F3D9B1'
        }
      }
    }
});

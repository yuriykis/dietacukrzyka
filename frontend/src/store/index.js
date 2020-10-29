import Vue from 'vue'
import Vuex from 'vuex'
import clientData from './modules/clientData'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    clientData
  }
})
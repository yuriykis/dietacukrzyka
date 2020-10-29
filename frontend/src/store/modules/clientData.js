import {
    getClientMenu1
  } from '@/services/api'
export default {
    actions: {
        async fetchData({ commit }) {
            const response = await getClientMenu1()
            const client_data = Object.assign(response)
            commit('updateClientData', client_data)
        },
    },
    mutations: {
      updateClientData(state, client_data){
        state.client_data = client_data
      }
    },
    state: {
        client_data: []
    },
    getters: {
        getClientInfo(state){
            return state.client_data
        }
    }
}
  
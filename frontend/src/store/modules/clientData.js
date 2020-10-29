import {
    getClientMenu1, getFile
  } from '@/services/api'
export default {
    actions: {
        async fetchData({ commit }) {
            const response = await getClientMenu1()
            const client_data = Object.assign(response)
            commit('updateClientData', client_data)
            commit('setRecipeNames', client_data)
        },
        async fetchAllImages({ commit, getters, dispatch }, index = 0) {
            const fileName = getters.getRecipeName(index)
              .replaceAll(' ', '_')
              .replaceAll(',', '')
            try {
                const response = await getFile(fileName + '.jpg')
                const image = Buffer.from(response.data, 'binary').toString('base64')
                const data = `data:${response.headers[
                    'content-type'
                ].toLowerCase()};base64,${image}`

                commit('updateClientImages', data)
                dispatch('fetchAllImages', ++index)
            } catch(e){
                console.log(e)
            }
           
          },
    },
    mutations: {
      updateClientData(state, client_data){
        state.client_data = client_data
      },
      updateClientImages(state, image){
        state.recipe_images.push(image)
      },
      setRecipeNames(state, client_data){
        for (let i = 0; i < 7; i++) {
            for (let j = 0; j < 5; j++) {
                state.recipe_names.push(client_data.data[i][j].name)
            }
        }
      }
    },
    state: {
        client_data: [],
        recipe_images: [],
        recipe_names: []
    },
    getters: {
        getClientInfo(state){
            return state.client_data
        },
        getRecipeName: (state) => (index) => {
            return state.recipe_names[index]
        }
    }
}
  
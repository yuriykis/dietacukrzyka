import {
    getClientMenu, getFile, getAllRecipes
  } from '@/services/api'
export default {
    actions: {
        async fetchData({ commit }) {
            const response = await getClientMenu()
            const client_data = Object.assign(response.data)
            commit('updateClientData', client_data)
            commit('setRecipeNames', client_data)
        },
        async fetchAllImages({ commit, getters, dispatch }, index = 0) {
            const fileNameCurrent = getters.getRecipeName(index)
            if (typeof fileNameCurrent !== 'undefined'){
              const fileName = fileNameCurrent
                .replaceAll(' ', '_')
                .replaceAll(',', '')
              try {
                  const response = await getFile(fileName + '.jpg')
                  const image = Buffer.from(response.data, 'binary').toString('base64')
                  const data = `data:${response.headers[
                      'content-type'
                  ].toLowerCase()};base64,${image}`
                  const imageObject = {}
                  imageObject[fileName] = data
                  commit('updateClientImages', imageObject)
                  await dispatch('fetchAllImages', ++index)
              } catch(e){
                  console.log(e)
              }
            }
          },

        async getRecipesFromServer({ commit }) {
          const res = await getAllRecipes()
          console.log(res)
          commit('setRecipes', res.data)
        }
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
                state.recipe_names.push(client_data[i][j].name)
            }
        }
      },
      setRecipes(state, recipes){
        state.recipes = recipes
      }
    },
    state: {
        client_data: [],
        recipe_images: [],
        recipe_names: [],
        recipes: []
    },
    getters: {
        getClientInfo(state){
            return state.client_data
        },
        getClientInfoByDay: (state) => (day) => {
          return state.client_data[day]
        },
        getClientMealByDayId: (state) => (day, id) => {
          return state.client_data[day][id]
        },
        getRecipeImageByName: (state) => (imageName) => {
          const images_object = {}
          state.recipe_images.forEach((image) => {
            images_object[Object.keys(image)[0]] = Object.values(image)[0]
          })
          return images_object[imageName]
        },
        getRecipeImages(state){
          return state.recipe_images
        },
        getRecipeName: (state) => (index) => {
            return state.recipe_names[index]
        },
        getRecipes(state){
          return state.recipes
        }
    }
}
  
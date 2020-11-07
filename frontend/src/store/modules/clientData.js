import {
    getClientMenu, getFile, getAllRecipes, getClientInfo, saveClientInfo, getAllIngredients, getAllAllergens, generateNewDiet
  } from '@/services/api'
export default {
    actions: {
        async fetchData({ commit }) {
            const response = await getClientMenu()
            const client_data = Object.assign(response.data)
            commit('updateClientData', client_data)
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
                if (index < 55) {
                  await dispatch('fetchAllImages', ++index)
                }
              }
            }
          },

        async getRecipesFromServer({ commit }) {
          const res = await getAllRecipes()
          commit('setRecipes', res.data)
          commit('setRecipeNames')
        },
        async getClientInfoFromServer({ commit }) {
          const res = await getClientInfo()
          commit('saveClientInfoInStore', res.data)
        },
        async saveClientInfoOnServer({ getters, dispatch }){
          await saveClientInfo(getters.getClientInfoFromStore)
          await dispatch('fetchData')
        },
        async getAllIngredientsFromServer({ commit }){
          const res1 = await getAllIngredients()
          commit('saveIngredientsInStore', res1.data)
          const res2 = await getAllAllergens()
          commit('saveAllergensInStore', res2.data)
        },

        async generateNewDiet(){
          await generateNewDiet()
        }

    },
    mutations: {
      updateClientData(state, client_data){
        state.client_data = client_data
      },
      updateClientImages(state, image){
        state.recipe_images.push(image)
      },
      setRecipes(state, recipes){
        state.recipes = recipes
      },
      setRecipeNames(state){
        state.recipes.forEach((recipe) => {
          state.recipe_names.push(recipe.name)
        })
      },
      saveClientInfoInStore(state, info){
        state.client_info = info
      },
      saveIngredientsInStore(state, ingredients){
        state.ingredients = ingredients
      },
      saveAllergensInStore(state, allergens){
        state.allergens = allergens
      }
    },
    state: {
        client_data: [],
        recipe_images: [],
        recipe_names: [],
        recipes: [],
        ingredients: [],
        client_info: {},
        allergens: []
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
        },
        getClientInfoFromStore(state){
          return state.client_info
        },
        getIngredients(state){
          return state.ingredients
        },
        getAllergens(state){
          return state.allergens
        }
    }
}
  
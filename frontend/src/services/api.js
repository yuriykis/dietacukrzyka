import * as Axios from 'axios'
import { getAccessToken } from '@/services/auth'


var apiHost = 'https://' + process.env.PUBLIC_IP
if (process.env.NODE_ENV === 'development') {
  apiHost = 'http://localhost:8000'
}


const api = Axios.create({
    baseURL: apiHost,
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    }
  })
  
const authenticationHeader = () => {
    return {
      Authorization: `Bearer ${getAccessToken()}`
    }
  }
  
  
export async function register (user_data) {
    return api.post('/app/register', user_data)
  }

export async function login (user) {
    return api.post('/api/token/', { username: user.login, password: user.password })
  }

export async function refresh (refToken) {
    return api.post('/api/token/refresh/', { refresh: refToken })
  }

  export async function getClientMenu () {
    return api.get(`/app/client/menu/`, { headers: authenticationHeader() })
  }
  
  export async function getClientInfo () {
    return api.get('/app/client/get', { headers: authenticationHeader() })
  }

  export async function saveClientInfo (user_data) {
    return api.put('/app/client/save', user_data, { headers: authenticationHeader() })
  }

  export async function getFile (fileName) {
    return api.get(`/app/client/${fileName}`, { responseType: 'arraybuffer', headers: authenticationHeader() })
  }

  export async function getAllRecipes () {
    return api.get(`/app/recipes/`, { headers: authenticationHeader() })
  }
  
  export async function getAllIngredients () {
    return api.get(`/app/ingredients/`, { headers: authenticationHeader() })
  }

  export async function getAllAllergens () {
    return api.get(`/app/allergens/`, { headers: authenticationHeader() })
  }

  export async function generateNewDiet () {
    return api.get(`/app/client/diet/`, { headers: authenticationHeader() })
  }
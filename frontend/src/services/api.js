import * as Axios from 'axios'
import { getAccessToken } from '@/services/auth'

var apiHost = 'http://127.0.0.1:8000'

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

  export async function getClientMenu (meal_type, menu_date) {
    return api.get(`/app/menu/${meal_type}/${menu_date}/`, { headers: authenticationHeader() })
  }
  
  export async function getClientMenuIngredients (meal_type, menu_date) {
    return api.get(`/app/menu/ingredients/${meal_type}/${menu_date}/`, { headers: authenticationHeader() })
  }
  
  export async function getClientData () {
    return api.get('/app/client/get', { headers: authenticationHeader() })
  }

  export async function saveClientData (user_data) {
    return api.put('/app/client/save', user_data, { headers: authenticationHeader() })
  }

  export async function generateClientIngredientsWeight (meal_type, date) {
    return api.get(`/app/client/${meal_type}/ingredients_weight/${date}`, { headers: authenticationHeader() })
  }

  export async function getFile (fileName) {
    return api.get(`/app/client/${fileName}`, { responseType: 'arraybuffer', headers: authenticationHeader() })
  }
  
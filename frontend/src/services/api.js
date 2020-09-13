import * as Axios from 'axios'

var apiHost = 'http://127.0.0.1:8000'

const api = Axios.create({
    baseURL: apiHost,
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    }
  })
  
  
export async function register (user_data) {
    return api.post('/app/register', user_data)
  }

export async function login (user) {
    return api.post('/api/token/', { username: user.login, password: user.password })
  }

export async function refresh (refToken) {
    return api.post('/api/token/refresh/', { refresh: refToken })
  }
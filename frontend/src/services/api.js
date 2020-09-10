import * as Axios from 'axios'

var apiHost = 'http://localhost:8000'

const api = Axios.create({
    baseURL: apiHost,
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    }
  })
  

export async function getUser () {
    return api.get('/home/users')
  }
  

import jwtDecode from 'jwt-decode'
// import { refresh } from '@/services/api'

import {
  isValid,
  toDate,
  isBefore,
} from 'date-fns'



export function getAccessToken () {
  return localStorage.getItem('access')
}

export function getRefreshToken () {
  return localStorage.getItem('refresh')
}


export function setLocalStorageTokens (tokens) {
    if (tokens.access) {
      localStorage.setItem('access', tokens.access)
    }
    if (tokens.refresh) {
      localStorage.setItem('refresh', tokens.refresh)
    }
  }
  

  export function removeLocalStorageTokens () {
    localStorage.removeItem('access')
    localStorage.removeItem('refresh')
  }

  export function isValidAccessToken () {
    return checkTokenValidity(getAccessToken())
  }

  export function checkTokenValidity (token) {
    try {  
      if (!token) {
          return false
        }
        const expToken = jwtDecode(token).exp
        const expMoment = toDate(expToken * 100000)
        if (isValid(expMoment)) {
          const res = isBefore(new Date(), expMoment)
          return res
        }
        return true
      } catch (e) {
        return false
    }
  
  }


  export function updateAccessToken () {
    const token = getAccessToken()
    if (token){
      // const refToken = getRefreshToken()
      // refresh(refToken).then((response) => {
      //   if (checkTokenValidity(response.data.access)){
      //     setLocalStorageTokens(response.data)
      //     console.log('Token updated')
      //   }
      // })
    }
  }
  
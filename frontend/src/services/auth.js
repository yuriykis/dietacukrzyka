
export const getAccessToken = () => localStorage.getItem('access')

export const getRefreshToken = () => localStorage.getItem('refresh')


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

  

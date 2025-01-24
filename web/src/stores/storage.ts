const localStorage = window.localStorage
const storage = {
  getItem: (key: string) => {
    return localStorage.getItem(key)
  },
  setItem: (key: string, value: string) => {
    localStorage.setItem(key, value)
  },
  clear: () => {
    localStorage.clear()
  },
  removeItem: (key: string) => {
    localStorage.removeItem(key)
  },
  getAll: () => {},
}

export { storage }

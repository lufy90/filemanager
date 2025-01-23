import axios from 'axios'
import { APIURL } from '@/config'
import { storage } from "@/stores/storage"
import router from '@/router'


const DEBUG = process.env.NODE_ENV === "development";

const config = {
    timeout: 2000,
  }
axios.defaults.baseURL = APIURL
const request = axios.create(config)

request.interceptors.request.use(
  config => {
    if (DEBUG) {
      console.log('request', config)
    }
    const token = storage.getItem('token')
    config.headers.Authorization = `Bearer ${token}`
    return config
  }, error => {
    if (DEBUG) {
      console.log('request error', error)
    }
    return Promise.reject(error)
  }
)

request.interceptors.response.use(
  response => {
    if (DEBUG) {
      console.log('response', response)
    }
    return response
  }, error => {
    if (DEBUG) {
      console.log('response error', error)
    }
    return Promise.reject(error)
  }
)

interface Params {
  [key: string]: null | any;
}

const ajax = {
    get:(url:string, params:Params)=>{
        return request.get(url, { params })
    },
    post:(url:string, params:Params)=>{
        return request.post(url, params)
    },
    put:(url:string, params:Params) =>{
        return request.put(url, params)
    },
    delete:(url:string, params:Params) =>{
        return request.delete(url, { params })
    },
    patch:(url:string, params:Params)=> {
        return request.patch(url, params)
    },
}

export {ajax}
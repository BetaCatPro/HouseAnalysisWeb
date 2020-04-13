import axios from 'axios'
import qs from 'qs'
import { Message } from 'element-ui'
import { Notification } from 'element-ui';

const service = axios.create({
  // baseURL: process.env.VUE_APP_BASE_API,
  baseURL: 'http://127.0.0.1:8000/v1/api',
  timeout: 5000
})

service.interceptors.request.use(config => {
  config.method === 'post'
    ? config.data = qs.stringify({ ...config.data })
    : config.params = { ...config.params }
  config.headers['Content-Type'] = 'application/x-www-form-urlencoded'

  return config
}, error => {
  Message({
    message: error,
    type: 'error',
    duration: 3 * 1000
  })
  Promise.reject(error)
})

service.interceptors.response.use(
  response => {
    if (response.statusText === 'OK') {
      return response.data
    } else {
      Notification({
        title: '错误',
        message: '访问api错误', // TODO 后端拦截错误请求
        type: 'error',
        duration: 3 * 1000
      })
    }
  },
  error => {
    let dtext = JSON.parse(JSON.stringify(error))
    try {
      if(dtext.response.status === 404) {
        Notification({
          type: 'error',
          title: '出问题404',
          message: '访问api错误或服务器忙',
          duration: 3 * 1000
        })
      }
    } catch (err) {
      Notification({
        title: '错误',
        message: '请求超时,请稍后再试或刷新页面',
        type: 'error',
        duration: 3 * 1000
      })
    }


    return Promise.reject(error)
  }
)

export default service

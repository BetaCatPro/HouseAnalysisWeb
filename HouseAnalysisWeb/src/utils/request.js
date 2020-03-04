import axios from 'axios'
import qs from 'qs'
import { Message } from 'element-ui'

const service = axios.create({
  // baseURL: process.env.VUE_APP_BASE_API,
  baseURL: 'http://127.0.0.1:8000/v1/api',
  timeout: 5000
})

service.interceptors.request.use(config => {
  Message({
    message: '请求数据中……',
    type: 'info',
    duration: 1 * 1000
  })

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
      Message({
        message: '访问api错误', // TODO 后端拦截错误请求
        type: 'warning',
        duration: 3 * 1000
      })
    }
  },
  error => {
    console.log('error')
    console.log(error)
    console.log(JSON.stringify(error))

    const dtext = JSON.parse(JSON.stringify(error)).response.status === 404
      ? '404'
      : '网络异常，请重试'
    Message({
      message: dtext,
      type: 'warning',
      duration: 3 * 1000
    })

    return Promise.reject(error)
  }
)

export default service

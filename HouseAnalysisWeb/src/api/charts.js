import request from '@/utils/request'

/**
 * @param send data
 */
export function getMean(params) {
  return request({
    url: '/meanprice',
    method: 'get',
    params
  })
}

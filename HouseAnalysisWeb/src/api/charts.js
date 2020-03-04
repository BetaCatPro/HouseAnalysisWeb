import request from '@/utils/request'

/**
 * @param send data
 */
export function getMean(params) {
  return request({
    url: '/all_house',
    method: 'get',
    params
  })
}

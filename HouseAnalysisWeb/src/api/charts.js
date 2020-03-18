import request from '@/utils/request'

/**
 * @param send data
 */
export function getAll(params) {
  return request({
    url: '/all_house',
    method: 'get',
    params
  })
}

export function getIndex(params){
  return request({
    url: '/index',
    method: 'get',
    params
  })
}

export function getRegionInfo(params){
  return request({
    url: '/region',
    method: 'get',
    params
  })
}

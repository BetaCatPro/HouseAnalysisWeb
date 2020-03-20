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

export function getIndex(params) {
  return request({
    url: '/index',
    method: 'get',
    params
  })
}

export function getRegionInfo(params) {
  return request({
    url: '/region',
    method: 'get',
    params
  })
}

export function getEelevatorInfo(params) {
  return request({
    url: '/elevator',
    method: 'get',
    params
  })
}

export function getConstructureInfo(params) {
  return request({
    url: '/constructure',
    method: 'get',
    params
  })
}

export function getPurposeInfo(params) {
  return request({
    url: '/purposes',
    method: 'get',
    params
  })
}

export function getDecorationInfo(params) {
  return request({
    url: '/decoration',
    method: 'get',
    params
  })
}

export function getFloorInfo(params) {
  return request({
    url: '/floor',
    method: 'get',
    params
  })
}

export function getLayoutInfo(params) {
  return request({
    url: '/layout',
    method: 'get',
    params
  })
}

export function getOrientationInfo(params) {
  return request({
    url: '/orientation',
    method: 'get',
    params
  })
}

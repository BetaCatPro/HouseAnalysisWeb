import request from '@/utils/request'

/**
 * @param send data
 */
export function getAllHouse(params) {
  return request({
    url: '/all_house',
    method: 'get',
    params
  })
}

// 排序
export function getOrderHouse(methods,params) {
  return request({
    url: '/all_house/?ordering='+ methods,
    method: 'get',
    params
  })
}

export function getAll(community,params) {
  return request({
    url: '/all_house/?search='+community,
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

export function getRegionInfo(id,params) {
  return request({
    url: '/region/'+id,
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
    url: '/constrcture',
    method: 'get',
    params
  })
}

export function getPurposeInfo(params) {
  return request({
    url: '/purpose',
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
    url: '/oritentation',
    method: 'get',
    params
  })
}

export function getCommunityInfo(params) {
  return request({
    url: '/community',
    method: 'get',
    params
  })
}

export function getCommunityRangeInfo(params) {
  return request({
    url: '/communityrange',
    method: 'get',
    params
  })
}

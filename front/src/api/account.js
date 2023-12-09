import request from '@/utils/request'

export function getList(params, data) {
  return request({
    url: '/api/user/account/list',
    method: 'post',
    params,
    data
  })
}

export function delAccount(data) {
  return request({
    url: '/api/user/account/del',
    method: 'post',
    data
  })
}

export function addAccount(data) {
  return request({
    url: '/api/user/account/add',
    method: 'post',
    data
  })
}

export function updateAccount(data) {
  return request({
    url: '/api/user/account/update',
    method: 'post',
    data
  })
}
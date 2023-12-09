import request from '@/utils/request'

export function getPermissions(params, data) {
  return request({
    url: '/api/user/permission/list',
    method: 'post',
    params,
    data
  })
}

export function delPermission(data) {
  return request({
    url: '/api/user/permission/del',
    method: 'post',
    data
  })
}

export function addPermission(data) {
  return request({
    url: '/api/user/permission/add',
    method: 'post',
    data
  })
}

export function updatePermission(data) {
  return request({
    url: '/api/user/permission/update',
    method: 'post',
    data
  })
}

import request from '@/utils/request'

export function getRoles(params, data) {
  return request({
    url: '/api/user/role/list',
    method: 'post',
    params,
    data
  })
}

export function delRole(data) {
  return request({
    url: '/api/user/role/del',
    method: 'post',
    data
  })
}

export function addRole(data) {
  return request({
    url: '/api/user/role/add',
    method: 'post',
    data
  })
}

export function updateRole(data) {
  return request({
    url: '/api/user/role/update',
    method: 'post',
    data
  })
}

// export function getRoutes() {
//   return request({
//     url: '/api/routes',
//     method: 'get'
//   })
// }

// export function getRoles() {
//   return request({
//     url: '/api/roles',
//     method: 'get'
//   })
// }
// export function addRole(data) {
//   return request({
//     url: '/api/role',
//     method: 'post',
//     data
//   })
// }

// export function updateRole(id, data) {
//   return request({
//     url: `/api/role/${id}`,
//     method: 'put',
//     data
//   })
// }

// export function deleteRole(id) {
//   return request({
//     url: `/api/role/${id}`,
//     method: 'delete'
//   })
// }

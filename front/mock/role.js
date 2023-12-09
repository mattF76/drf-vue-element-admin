const Mock = require('mockjs')

const data = Mock.mock({
  'items|3': [{
    roleID: '@id',
    'roleName|+1': ['admin', 'roleA', 'roleB'],
    'note|+1': ['超级管理员', '角色A,可以管理菜单A', '角色B,可以管理菜单B'],
    rolePermissions: [{'permissionID':'1', 'permissionName':'账号查看接口'}, {'permissionID':'2', 'permissionName':'账号删除接口'}],
  }]
})

module.exports = [
  {
    url: '/api/user/role/list\.*',
    type: 'post',
    response: config => {
      const items = data.items
      return {
        code: 20000,
        data: {
          total: items.length,
          items: items
        }
      }
    }
  },
  {
    url: '/api/user/role/del',
    type: 'post',
    response: config => {
      return {
        code: 20000,
        msg: "角色删除成功",
      }
    }
  },
  {
    url: '/api/user/role/add',
    type: 'post',
    response: config => {
      return {
        code: 20000,
        msg: "角色新增成功",
      }
    }
  },
  {
    url: '/api/user/role/update',
    type: 'post',
    response: config => {
      return {
        code: 20000,
        msg: "角色编辑成功",
      }
    }
  },
]

const Mock = require('mockjs')

const data = Mock.mock({
  'items|30': [{
    id: '@id',
    'permissionAPI|+1': ['/account/add', '/account/del', '/account/update'],
    'permissionName|+1': ['xx查询接口', 'xx增加接口', 'xx删除接口'],
  }]
})

module.exports = [
  {
    url: '/api/user/permission/list\.*',
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
    url: '/api/user/permission/del',
    type: 'post',
    response: config => {
      return {
        code: 20000,
        msg: "权限删除成功",
      }
    }
  },
  {
    url: '/api/user/permission/add',
    type: 'post',
    response: config => {
      return {
        code: 20000,
        msg: "权限新增成功",
      }
    }
  },
  {
    url: '/api/user/permission/update',
    type: 'post',
    response: config => {
      return {
        code: 20000,
        msg: "权限编辑成功",
      }
    }
  },
]

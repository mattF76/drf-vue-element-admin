const Mock = require('mockjs')

const data = Mock.mock({
  'items|15': [{
    id: '@id',
    username: '@word',
    realName: '@cname',
    password: '@string',
    // 'userRoles|1': '@shuffle(["admin", "user", "editor"], 1, 2)',
    userRoles: [{'roleID': '1', 'roleName':'admin'}, {'roleID': '2', 'roleName':'user1'}, {'roleID': '3', 'roleName':'user2'}],
  }]
})

module.exports = [
  {
    url: '/api/account/list\.*',
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
    url: '/api/account/del',
    type: 'post',
    response: config => {
      return {
        code: 20000,
        msg: "账号删除成功",
      }
    }
  },
  {
    url: '/api/account/add',
    type: 'post',
    response: config => {
      return {
        code: 20000,
        msg: "账号新增成功",
      }
    }
  },
  {
    url: '/api/account/update',
    type: 'post',
    response: config => {
      return {
        code: 20000,
        msg: "账号编辑成功",
      }
    }
  },
]

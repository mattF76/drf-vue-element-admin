/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const userRouter =   {
  path: '/user',
  component: Layout,
  redirect: '/user/account',
  alwaysShow: true, // will always show the root menu
  name: 'User',
  meta: {
    title: '用户管理',
    icon: 'user-manage',
    roles: ['admin'] // you can set roles in root nav
  },
  children: [
    {
      path: 'account',
      component: () => import('@/views/user/account'),
      name: 'accountUser',
      meta: {
        title: '账号管理',
      }
    },
    {
      path: 'role',
      component: () => import('@/views/user/role'),
      name: 'roleUser',
      meta: {
        title: '角色管理'
        // if do not set roles, means: this page does not require permission
      }
    },
    {
      path: 'permission',
      component: () => import('@/views/user/permission'),
      name: 'permissionUser',
      meta: {
        title: '权限管理',
      }
    }
  ]
}

export default userRouter

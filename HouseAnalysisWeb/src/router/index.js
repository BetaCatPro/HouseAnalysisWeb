import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Layout from '@/layout'

export const constantRoutes = [
  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: '房源信息', icon: 'house' }
    }]
  },

  {
    path: '/house',
    component: Layout,
    redirect: '/example/table',
    name: 'House',
    meta: { title: '房价分析', icon: 'chart' },
    children: [
      {
        path: 'Single',
        name: 'Single factor',
        component: () => import('@/views/single/index'),
        meta: { title: '单因子探索分析', icon: 'analysis' }
      },
      {
        path: 'Multifactor',
        name: 'Multifactor',
        component: () => import('@/views/multiple/index'),
        meta: { title: '多因子分析', icon: 'manalysis' }
      },
      {
        path: 'Word',
        component: () => import('@/views/word/index'),
        name: 'Word',
        meta: { title: '词云', icon: 'word' }
      },
      {
        path: 'HopMap',
        component: () => import('@/views/hotmap/index'),
        name: 'HopMap',
        meta: { title: '热力图', icon: 'hotmap' }
      }
    ]
  },

  {
    path: '/map',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'map',
      name: 'Map',
      component: () => import('@/views/map/index'),
      meta: { title: '地图找房', icon: 'wan_map' }
    }]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router

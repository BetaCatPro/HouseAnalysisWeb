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
    redirect: '/dashboard',
    name: 'House',
    meta: { title: '房价分析', icon: 'chart' },
    children: [
      {
        path: 'Single',
        name: 'Single',
        component: () => import('@/views/single/index'),
        meta: { title: '数据探索分析可视化', icon: 'analysis' }
      },
      {
        path: 'Multifactor',
        name: 'Multifactor',
        component: () => import('@/views/multiple/index'),
        meta: { title: '各区划详细信息', icon: 'manalysis' }
      }
      // {
      //   path: 'Word',
      //   component: () => import('@/views/word/index'),
      //   name: 'Word',
      //   meta: { title: '房源信息词云', icon: 'word' }
      // }
    ]
  },

  {
    path: '/search',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'house',
      name: 'Search',
      component: () => import('@/views/house/index'),
      meta: { title: '搜索房源', icon: 'search' }
    }]
  },

  // {
  //   path: '/HeatMap',
  //   component: Layout,
  //   redirect: '/dashboard',
  //   name: 'HeatMap',
  //   meta: { title: '热力图', icon: '热力图' },
  //   children: [
  //     {
  //       path: 'MeanHeatMap',
  //       component: () => import('@/views/heatmap/mean'),
  //       name: 'MeanHeatMap',
  //       meta: { title: '均价热力图', icon: 'hotmap' }
  //     }
  //   ]
  // },

  // {
  //   path: '/map',
  //   component: Layout,
  //   redirect: '/dashboard',
  //   children: [{
  //     path: 'map',
  //     name: 'Map',
  //     component: () => import('@/views/map/index'),
  //     meta: { title: '地图找房', icon: 'wan_map' }
  //   }]
  // },

  {
    path: '/show',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'houseinfo',
      name: 'HouseInfo',
      component: () => import('@/views/house/components/houseinfo')
    }]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  mode: 'history', // require service support
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

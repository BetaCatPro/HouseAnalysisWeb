import router from './router'
import NProgress from 'nprogress' // progress bar
import 'nprogress/nprogress.css'
import getPageTitle from '@/utils/get-page-title'

NProgress.configure({ showSpinner: false })

router.beforeEach(async(to, from, next) => {
  NProgress.start()
  document.title = getPageTitle(to.meta.title)
  NProgress.done()
  next()
})

router.afterEach(() => {
  NProgress.done()
})

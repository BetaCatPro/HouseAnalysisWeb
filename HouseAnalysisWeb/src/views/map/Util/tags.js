import Vue from 'vue'
import { BmPointCollection } from 'vue-baidu-map'

export default {
  newTag(points) {
    // 创建组件逻辑
    let TagClass = Vue.extend({
      // 向界面渲染的dom方法。
      render(createElement) {
        return createElement(
          'bm-point-collection',
          {
            attrs: {
              shape: 'BMAP_POINT_SHAPE_CIRCLE',
              color: 'red',
              size: 'BMAP_POINT_SIZE_BIGGER'
            },
            props: {
              points: this.point
            }
          }
        )
      },
      data() {
        return {
          point: points // 为这个tag标签使用的文字是传入的标签文字内容
        }
      },
      components: {
        BmPointCollection
      }
    })
    return new TagClass()
  }
}

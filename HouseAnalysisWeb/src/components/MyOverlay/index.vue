<template>
  <bm-overlay
    ref="customOverlay"
    :class="{sample: true}"
    :style="pointColor"
    pane="labelPane"
    @draw="draw">
    <div class="name" style="">{{ text }}<i class="arrow"></i></div>
  </bm-overlay>
</template>

<script>
  import { BmOverlay } from 'vue-baidu-map'
  export default {
    props: ['text', 'position', 'color'], // 用来接受传入的值，用来定制样式
    components: {
      BmOverlay
    },
    watch: {
      position: {
        handler () {
          this.$refs.customOverlay.reload()  // 当位置发生变化时，重新渲染，内部会调用draw
        },
        deep: true
      }
    },
    data () {
      return {
        pointColor: ''
      }
    },
    mounted () {
      this.pointColor = this.color
    },
    methods: {
      // 这是百度地图的重绘函数,用于维持覆盖物的位置（这里的值貌似会影响拖拉时的偏移度）
      draw ({ el, BMap, map }) {
        const { lng, lat } = this.position
        const pixel = map.pointToOverlayPixel(new BMap.Point(lng, lat))

        // 设置位置偏移,由于样式影响
        el.style.left = pixel.x - 26 + 'px'
        el.style.top = pixel.y - 86 + 'px'
      }
    }
  }
</script>

<style>
  .sample {
    width: 82px;
    height: 82px;
    overflow: hidden;
    color: #fff;
    text-align: center;
    position: absolute;
  }
  .name {
    position: absolute;
    left: 50%;
    width: 100px;
    text-overflow:ellipsis;
    transform: translateX(-50%);
    z-index: 2;
    line-height: 24px;
    border-radius: 2px;
    padding: 10px 14px;
    font-size: 14px;
    color: #fff;
    display: inline-block;
    background-color: #5184f9;
    box-shadow: 0 0 4px rgba(0,0,0,0.2);
    font-weight: 900;
  }
  .name:before {
    content: '';
    width: 18px;
    height: 12px;
    background: #5184f9;
    position: absolute;
    bottom: 1px;
    left: 40%;
    z-index: 2;
  }
  .name:after {
    content: '';
    width: 13px;
    height: 13px;
    background: #5184f9;
    border-radius: 50%;
    border: 3px solid #fff;
    position: absolute;
    bottom: -24px;
    left: 50%;
    margin-left: -7px;
  }
  .arrow {
    position: absolute;
    width: 10px;
    height: 10px;
    bottom: -5px;
    left: 50%;
    background: #5184f9;
    margin-left: -5px;
    display: inline-block;
    box-shadow: 0 0 6px 0 rgba(13,4,9,0.2);
    transform: rotate(45deg);
  }
</style>

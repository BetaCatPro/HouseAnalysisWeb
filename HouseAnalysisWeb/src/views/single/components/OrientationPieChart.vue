<template>
  <div ref="oripie" :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from './mixins/resize'
import { getOrientationInfo } from '@/api/charts.js'

export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '300px'
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    //      this.$nextTick(() => {
    //        this.initChart()
    //      })
    window.addEventListener('scroll', this.scrollHandle)
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    scrollHandle(e) {
      const elbar = this.$refs.oripie
      //        console.log('高度差',(elbar.getBoundingClientRect().top-document.documentElement.clientHeight)<-10)
      if ((elbar.getBoundingClientRect().top - document.documentElement.clientHeight) < -10) {
        this.initChart()
        window.removeEventListener('scroll', this.scrollHandle)
      }
    },
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')
      const orientation = []
      const number = []
      const data = []

      getOrientationInfo().then((res, err) => {
        Array.from(res).map((item, index) => {
          orientation.push(item.orientation)
          number.push(item.num)
          data.push({ value: item.num, name: item.orientation })
        })
        this.$emit('showchart7', false)

        this.chart.setOption({
          title: {
            text: '房屋朝向分布情况'
          },
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
          },
          series: [
            {
              name: '房屋朝向',
              type: 'pie',
              //              roseType: 'radius',
              //              radius: [15, 95],
              center: ['55%', '50%'],
              data: data,
              animationEasing: 'cubicInOut',
              animationDuration: 2600
            }
          ]
        })
      })
    }
  }
}
</script>

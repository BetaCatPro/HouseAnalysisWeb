<template>
  <div ref="purpie" :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from './mixins/resize'
import { getPurposeInfo } from '@/api/charts.js'

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
      default: '290px'
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
      const elbar = this.$refs.purpie
      //        console.log('高度差',(elbar.getBoundingClientRect().top-document.documentElement.clientHeight)<-10)
      if ((elbar.getBoundingClientRect().top - document.documentElement.clientHeight) < -10) {
        this.initChart()
        window.removeEventListener('scroll', this.scrollHandle)
      }
    },
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')
      const purposes = []
      const number = []
      const data = []

      getPurposeInfo().then((res, err) => {
        Array.from(res).map((item, index) => {
          purposes.push(item.purposes)
          number.push(item.num)
          data.push({ value: item.num, name: item.purposes })
        })
        this.$emit('showchart6', false)
        this.chart.setOption({
          title: {
            text: '房屋用途分布情况'
          },
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
          },
          legend: {
            left: 'center',
            bottom: '5',
            data: purposes
          },
          series: [
            {
              name: '房屋用途',
              type: 'pie',
              radius: '50%',
              center: ['50%', '45%'],
              data: data,
              animationEasing: 'cubicInOut',
              animationDuration: 2600
            }
          ]
        })

        if (err) {
          Promise.reject(err)
        }
      })
    }
  }
}
</script>

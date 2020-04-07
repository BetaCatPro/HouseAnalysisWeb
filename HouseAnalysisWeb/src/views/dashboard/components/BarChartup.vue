<template>
  <div ref="chart" :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/roma') // echarts theme
import resize from './mixins/resize'
import { getRegionInfo } from '@/api/charts.js'

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
      default: '330px'
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')
      const xAxisData = []
      const mean_unit_price = []

      getRegionInfo('').then((res, err) => {
        Array.from(res).map((item, index) => {
          xAxisData.push(item.region)
          mean_unit_price.push(item.mean_unit_price)
        })
        this.$emit('hideloading4', false)
        this.chart.setOption({
          backgroundColor: '#eee',

          title: {
            text: '成都整体房价信息'
          },
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            data: ['单价']
          },
          calculable: true,
          xAxis: [
            {
              type: 'category',
              data: xAxisData
            }
          ],
          yAxis: [
            {
              type: 'value'
            }
          ],
          series: [
            {
              name: '单价',
              type: 'bar',
              data: mean_unit_price,
              markPoint: {
                data: [
                  { type: 'max', name: '最大值' },
                  { type: 'min', name: '最小值' }
                ]
              },
              markLine: {
                data: [
                  { type: 'average', name: '平均值' }
                ]
              }
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

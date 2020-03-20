<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from './mixins/resize'
import { getEelevatorInfo } from '@/api/charts.js'

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
      default: '628px'
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
      let has_el_num = 0
      let no_el_num = 0
      let has_mean_price = []
      let no_mean_price = []
      let has_unit_mean_price = []
      let no_unit_mean_price = []

      getEelevatorInfo().then((res,err)=>{
        let results = Array.from(res)
        has_el_num = results[0].el_num
        no_el_num = results[1].el_num
        has_mean_price.push(parseFloat(results[0].mean_price))
        has_unit_mean_price.push(parseFloat(results[0].mean_unit_price))
        no_mean_price.push(parseFloat(results[1].mean_price))
        no_unit_mean_price.push(parseFloat(results[1].mean_unit_price))

        this.chart.setOption({
          title: {
            text: '电梯与房价的关系'
          },
          tooltip: {},
          legend: {
            data: ['有', '无']
          },
          grid: [{
            top:40,
            bottom: '72%'
          },
          {
            top:'72%',
            bottom: 40
          }],
          xAxis: [{
            type: 'value',
            boundaryGap: [0, 0.01],
            gridIndex:0
          },
            {
              type: 'value',
              boundaryGap: [0, 0.01],
              gridIndex:1
            }],
          yAxis: [{
            type: 'category',
            data: ['Elevator'],
            gridIndex:0
          },
            {
              type: 'category',
              data: ['Elevator'],
              gridIndex:1
            }],
          series: [
            {
              name: '有',
              type: 'bar',
              data: has_mean_price,
              xAxisIndex: 0,
              yAxisIndex: 0
            },
            {
              name: '无',
              type: 'bar',
              data: no_mean_price,
              xAxisIndex: 0,
              yAxisIndex: 0
            },
            {
              name: '有',
              type: 'bar',
              data: has_unit_mean_price,
              xAxisIndex: 1,
              yAxisIndex: 1
            },
            {
              name: '无',
              type: 'bar',
              data: no_unit_mean_price,
              xAxisIndex: 1,
              yAxisIndex: 1
            },
            {
              name: '电梯情况',
              type: 'pie',
              radius: '30%',
              center: ['47%', '52%'],
              data: [
                {value: has_el_num, name: '有电梯'},
                {value: no_el_num, name: '无电梯'}
              ],
              emphasis: {
                itemStyle: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
        })

        if(err) {
          Promise.reject(err)
        }
      })
    }
  }
}
</script>

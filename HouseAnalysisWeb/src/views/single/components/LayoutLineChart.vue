<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
  import echarts from 'echarts'
  require('echarts/theme/shine') // echarts theme
  import resize from './mixins/resize'
  import { getLayoutInfo } from '@/api/charts.js'

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
        this.chart = echarts.init(this.$el, 'shine')
        let xAxisData = []
        let num = []

        getLayoutInfo().then((res,err)=>{
          Array.from(res).map((item,index)=>{
            xAxisData.push(item.layout)
            num.push(item.num)
          })
          this.$emit('hideloading2',false)
          this.chart.setOption({
            backgroundColor: '#eee',

            title: {
              text: '户型分布情况'
            },
            tooltip: {
              trigger: 'axis'
            },
            legend: {
              data: ['户型']
            },
            xAxis: [
              {
                type: 'category',
                data: xAxisData
              }
            ],
            yAxis: [
              {
                type: 'value',
                splitLine: {
                  show: false
                }
              }
            ],
            dataZoom: [{
              endValue: '1室2厅1卫'
            }, {
              type: 'inside'
            }],
            visualMap: {
              top: 10,
              right: 10,
              pieces: [{
                gt: 0,
                lte: 100,
                color: '#096'
              }, {
                gt: 100,
                lte: 500,
                color: '#ffde33'
              }, {
                gt: 500,
                lte: 1000,
                color: '#ff9933'
              }, {
                gt: 1000,
                lte: 5000,
                color: '#cc0033'
              }, {
                gt: 5000,
                lte: 10000,
                color: '#660099'
              }, {
                gt: 10000,
                color: '#7e0023'
              }],
              outOfRange: {
                color: '#999'
              }
            },
            series: [
              {
                name: '户型',
                type: 'bar',
                data: num,
                markPoint: {
                  data: [
                    {type: 'max', name: '最大值'},
                    {type: 'min', name: '最小值'}
                  ]
                },
                markLine: {
                  data: [
                    {type: 'average', name: '平均值'}
                  ]
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

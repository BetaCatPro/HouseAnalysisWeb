<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
  import echarts from 'echarts'
  require('echarts/theme/macarons') // echarts theme
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
        var xAxisData = []
        var price = []
        var unit_price = []

        var emphasisStyle = {
          itemStyle: {
            barBorderWidth: 1,
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowOffsetY: 0,
            shadowColor: 'rgba(0,0,0,0.5)'
          }
        }

        getRegionInfo().then((res,err)=>{
          Array.from(res).map((item,index)=>{
            xAxisData.push(item.region)
            price.push(parseFloat(item.mean_price))
            unit_price.push(parseFloat(item.mean_unit_price))
          })

          this.chart.setOption({
            title: {
              text: '成都整体房价信息'
            },

            backgroundColor: '#eee',
            legend: {
              data: ['price', 'unit_price']
            },
            toolbox: {
              feature: {
                saveAsImage: {
                  pixelRatio: 2
                }
              }
            },
            tooltip: {},
            xAxis: {
              data: xAxisData,
              name: 'X Axis',
              axisLine: {onZero: true},
              splitLine: {show: false},
              splitArea: {show: false}
            },
            yAxis: {
              inverse: true,
              splitArea: {show: false}
            },
            grid: {
              left: 100
            },
            visualMap: {
              type: 'continuous',
              dimension: 1,
              text: ['High', 'Low'],
              inverse: true,
              itemHeight: 200,
              calculable: true,
              min: -2,
              max: 6,
              top: 60,
              left: 10,
              inRange: {
                colorLightness: [0.4, 0.8]
              },
              outOfRange: {
                color: '#bbb'
              },
              controller: {
                inRange: {
                  color: '#2f4554'
                }
              }
            },
            series: [
              {
                name: 'price',
                type: 'bar',
                stack: 'one',
                emphasis: emphasisStyle,
                data: price
              },
              {
                name: 'unit_price',
                type: 'bar',
                stack: 'one',
                emphasis: emphasisStyle,
                data: unit_price
              }
            ]

          })

          this.$emit('hideloading',false)

          if(err) {
            Promise.reject(err)
          }
        })
      }
    }
  }
</script>

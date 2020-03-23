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
      default: '350px'
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
      let xAxisData = []
      let num = []
      let piedata = []

      getRegionInfo('').then((res,err)=>{
        Array.from(res).map((item,index)=>{
          xAxisData.push(item.region)
          num.push(item.num)
          piedata.push({value:item.num,name:item.region})
        })
        this.$emit('hideloading',false)
        this.chart.setOption({
          backgroundColor: '#eee',

          title: {
            text: '成都整体房源数量分布'
          },
          toolbox: {
            // y: 'bottom',
            feature: {
              saveAsImage: {
                pixelRatio: 2
              }
            }
          },
          tooltip: {},
          xAxis: {
            data: xAxisData,
            splitLine: {
              show: false
            }
          },
          yAxis: {
          },
          series: [{
            name: 'bar',
            type: 'bar',
            data: num,
            animationDelay: function (idx) {
              return idx * 10;
            }
          },
          {
            name: '区划',
            type: 'pie',
            radius: '45%',
//            roseType: 'radius',
//            radius: [15, 95],
            center: ['80%', '33%'],
            data: piedata,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }],
          animationEasing: 'elasticOut',
          animationDelayUpdate: function (idx) {
            return idx * 5;
          }
        })

        if(err) {
          Promise.reject(err)
        }
      })
    }
  }
}
</script>

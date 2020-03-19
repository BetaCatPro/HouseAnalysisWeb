<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from './mixins/resize'

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
      default: '600px'
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

      this.chart.setOption({
        title: {
          text: '世界人口总量',
          subtext: '数据来自网络'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {
          data: ['2011年', '2012年']
        },
        grid: [{
          top:40,
          bottom: '58%'
        },
        {
          top:'58%',
          bottom: 40
        }],
        xAxis: [{
          type: 'value',
//          boundaryGap: [0, 0.01],
          gridIndex:0
        },
        {
          type: 'value',
//          boundaryGap: [0, 0.01],
          gridIndex:1
        }],
        yAxis: [{
          type: 'category',
          data: ['巴西', '印尼', '美国', '印度', '中国'],
          gridIndex:0
        },
        {
          type: 'category',
          data: ['巴', '印', '美', '印', '中'],
          gridIndex:1
        }],
        series: [
          {
            name: '2011年',
            type: 'bar',
            data: [18203, 23489, 29034, 104970, 131744],
            xAxisIndex: 0,
            yAxisIndex: 0
          },
          {
            name: '2012年',
            type: 'bar',
            data: [19325, 23438, 31000, 121594, 134141],
            xAxisIndex: 0,
            yAxisIndex: 0
          },
          {
            name: '2013年',
            type: 'bar',
            data: [18203, 23489, 29034, 104970, 131744],
            xAxisIndex: 1,
            yAxisIndex: 1
          },
          {
            name: '2014年',
            type: 'bar',
            data: [19325, 23438, 31000, 121594, 134141],
            xAxisIndex: 1,
            yAxisIndex: 1
          }
        ]
      })
    }
  }
}
</script>

<template>
  <div :class="className" :style="{height:height,width:width}" />
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
      default: '708px'
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
      this.chart = echarts.init(this.$el, 'roma')
      var data = []
      var regions = []
      var barHeight = 50;

      getRegionInfo('').then((res,err)=>{
        Array.from(res).map((item,index)=>{
          data.push([item.min_unit_price,item.max_unit_price,item.mean_unit_price])
          regions.push(item.region)
        })

        this.$emit('hideloading3',false)
        this.chart.setOption({
          backgroundColor: '#eee',
          title: {
            text: '成都整体房价范围'
          },
          legend: {
            show: true,
            data: ['价格范围', '均值']
          },
          grid: {
            top: 100
          },
          angleAxis: {
            type: 'category',
            data: regions
          },
          tooltip: {
            show: true,
            formatter: function (params) {
              var id = params.dataIndex;
              return regions[id] + '<br>最低：' + data[id][0] + '<br>最高：' + data[id][1] + '<br>平均：' + data[id][2];
            }
          },
          radiusAxis: {
          },
          polar: {
          },
          series: [{
            type: 'bar',
            itemStyle: {
              color: 'transparent'
            },
            data: data.map(function (d) {
              return d[0];
            }),
            coordinateSystem: 'polar',
            stack: '最大最小值',
            silent: true
          }, {
            type: 'bar',
            data: data.map(function (d) {
              return d[1] - d[0];
            }),
            coordinateSystem: 'polar',
            name: '价格范围',
            stack: '最大最小值'
          }, {
            type: 'bar',
            itemStyle: {
              color: 'transparent'
            },
            data: data.map(function (d) {
              return d[2] - barHeight;
            }),
            coordinateSystem: 'polar',
            stack: '均值',
            silent: true,
            z: 10
          }, {
            type: 'bar',
            data: data.map(function (d) {
              return barHeight * 2;
            }),
            coordinateSystem: 'polar',
            name: '均值',
            stack: '均值',
            barGap: '-100%',
            z: 10
          }]
        })

        if(err) {
          Promise.reject(err)
        }
      })
    }
  }
}
</script>

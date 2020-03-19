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
      default: '300px'
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
      this.$emit('hideloading',false)
      this.chart = echarts.init(this.$el, 'macarons')
      var xAxisData = [];
      var number = [];

      getRegionInfo().then((res,err)=>{
        Array.from(res).map((item,index)=>{
          xAxisData.push(item.region)
          number.push(item.num)
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
              data: number,
              animationDelay: function (idx) {
                return idx * 10;
              }
            }],
            animationEasing: 'elasticOut',
            animationDelayUpdate: function (idx) {
              return idx * 5;
            }
          })
        })

        if(err) {
          Promise.reject(err)
        }
      })
    }
  }
}
</script>

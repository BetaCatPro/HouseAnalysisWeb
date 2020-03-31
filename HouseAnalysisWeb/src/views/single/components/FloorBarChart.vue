<template>
  <div :class="className" :style="{height:height,width:width}" ref="flobar" />
</template>

<script>
  import echarts from 'echarts'
  require('echarts/theme/shine') // echarts theme
  import resize from './mixins/resize'
  import { getFloorInfo } from '@/api/charts.js'

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
        let elbar = this.$refs.flobar
//        console.log('高度差',(elbar.getBoundingClientRect().top-document.documentElement.clientHeight)<-10)
        if((elbar.getBoundingClientRect().top-document.documentElement.clientHeight)<-10) {
          this.initChart()
          window.removeEventListener('scroll', this.scrollHandle)
        }
      },
      initChart() {
        this.chart = echarts.init(this.$el, 'shine')
        let xAxisData = []
        let num = []

        getFloorInfo().then((res,err)=>{
          Array.from(res).map((item,index)=>{
            xAxisData.push(item.floor+'层')
            num.push(item.num)
          })
          this.$emit('showchart8',false)
          this.chart.setOption({
            backgroundColor: '#eee',

            title: {
              text: '楼层分布情况'
            },
            tooltip: {
              trigger: 'axis'
            },
            legend: {
              data: ['楼层']
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
            dataZoom: [{
              endValue: '16层'
            }, {
              type: 'inside'
            }],visualMap: {
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
                name: '楼层',
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

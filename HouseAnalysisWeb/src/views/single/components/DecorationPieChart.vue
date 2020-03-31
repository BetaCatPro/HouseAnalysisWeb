<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
  import echarts from 'echarts'
  require('echarts/theme/macarons') // echarts theme
  import resize from './mixins/resize'
  import { getDecorationInfo } from '@/api/charts.js'

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
        chart: null,
        loading: true
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
        let decoration = []
        let number = []
        let data = []

        getDecorationInfo().then((res,err)=>{
          Array.from(res).map((item,index)=>{
            decoration.push(item.decoration)
            number.push(item.num)
            data.push({value:item.num,name:item.decoration})
          })

          this.$emit('showchart1',false)

          this.chart.setOption({
            backgroundColor: '#eee',
            title: {
              text: '房屋装修程度分布情况'
            },
            tooltip: {
              trigger: 'item',
              formatter: '{a} <br/>{b} : {c} ({d}%)'
            },
            legend: {
              left: 'center',
              bottom: '10',
              data: decoration
            },
            series: [
              {
                name: '装修情况',
                type: 'pie',
                roseType: 'radius',
                radius: [15, 95],
                center: ['50%', '50%'],
                data: data,
                animationEasing: 'cubicInOut',
                animationDuration: 2600
              }
            ]
          })
        })
      }
    }
  }
</script>

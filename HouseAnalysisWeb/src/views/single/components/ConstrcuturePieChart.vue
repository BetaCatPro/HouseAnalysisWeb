<template>
  <div :class="className" :style="{height:height,width:width}" ref="conpie"/>
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from './mixins/resize'
import { getConstructureInfo } from '@/api/charts.js'

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
      default: '290px'
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
//    this.$nextTick(() => {
//      this.initChart()
//    })
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
      let elbar = this.$refs.conpie
//      console.log('高度差',(elbar.getBoundingClientRect().top-document.documentElement.clientHeight)<-10)
      if((elbar.getBoundingClientRect().top-document.documentElement.clientHeight)<-10) {
        this.initChart()
        window.removeEventListener('scroll', this.scrollHandle)
      }
    },
    initChart() {
      this.chart = echarts.init(this.$el, 'light')
      let constructure = []
      let number = []
      let data = []

      getConstructureInfo().then((res,err)=>{
        Array.from(res).map((item,index)=>{
          constructure.push(item.constructure)
          number.push(item.num)
          data.push({value:item.num,name:item.constructure})
        })
        this.$emit('showchart5',false)
        this.chart.setOption({
          title: {
            text: '建筑结构分布情况'
          },
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
          },
          legend: {
            left: 'center',
            bottom: '5',
            data: constructure
          },
          series: [
            {
              name: '建筑结构',
              type: 'pie',
              radius: '50%',
              center: ['50%', '45%'],
              data: data,
              animationEasing: 'cubicInOut',
              animationDuration: 2600
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

<template>
  <div>
    <baidu-map class="map"
               :center="{lng: 104.07, lat: 30.67}"
               :zoom="14"
               style="height:93vh"
               :scroll-wheel-zoom="true"
               ak="Qmz0VMtKw3uAI2GWClu9Q6iCnP2j2uH2">
      <bml-heatmap :data="data" :max="30000" :radius="20" />
      <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
    </baidu-map>
  </div>
</template>
<script>
import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
import { BmlHeatmap, BmNavigation } from 'vue-baidu-map'
import { getPotion } from '@/api/charts.js'
export default {
  components: {
    BaiduMap,
    BmlHeatmap,
    BmNavigation
  },
  created() {
    getPotion().then((res,err)=>{
      console.log(res)
      Array.from(res.results).map((item,index)=>{
        this.data.push({ lng: item.lng, lat: item.lat, count: item.unit_price })
      })
    })
  },
  data() {
    return {
      data: []
    }
  }
}
</script>

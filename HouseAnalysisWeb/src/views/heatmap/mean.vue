<template>
  <div>
    <baidu-map class="map"
               :center="{lng: 104.07, lat: 30.67}"
               :zoom="14"
               style="height:93vh"
               :scroll-wheel-zoom="true"
               ak="Qmz0VMtKw3uAI2GWClu9Q6iCnP2j2uH2">
      <bml-heatmap :data="data" :max="100" :radius="20" />
      <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
    </baidu-map>
  </div>
</template>
<script>
import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
import { BmlHeatmap, BmNavigation } from 'vue-baidu-map'
export default {
  components: {
    BaiduMap,
    BmlHeatmap,
    BmNavigation
  },
  data() {
    return {
      data: [
        { lng: 104.1044899, lat: 30.71436263, count: 10000 },
        { lng: 104.1043749, lat: 30.69819501, count: 16 },
        { lng: 104.1683891, lat: 30.69057974, count: 17 },
        { lng: 104.0891126, lat: 30.72407362, count: 18 }
      ]
    }
  }
}
</script>

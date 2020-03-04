<template>
  <div>
    <baidu-map class="map" :center="{lng: 116.404, lat: 39.915}" :zoom="14" style="height:100vh" ak="Qmz0VMtKw3uAI2GWClu9Q6iCnP2j2uH2">
      <bml-heatmap :data="data" :max="100" :radius="20">
      </bml-heatmap>
    </baidu-map>
  </div>
</template>
<script>
  import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
  import { BmlHeatmap } from 'vue-baidu-map'
  export default {
    components: {
      BaiduMap,
      BmlHeatmap
    },
    data() {
      return {
        data: [
          {lng: 116.418261, lat: 39.921984, count: 50},
          {lng: 116.423332, lat: 39.916532, count: 51},
          {lng: 116.419787, lat: 39.930658, count: 15}
        ]
      }
    }
  }
</script>

<template>
  <div class="mapbox">
    <baidu-map :center="center" :zoom="zoom" :scroll-wheel-zoom="true" style="height:100vh" @ready="handler" @click="getClickInfo" ak="Qmz0VMtKw3uAI2GWClu9Q6iCnP2j2uH2">
      <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
      <bm-marker :position="center" :dragging="true" @click="infoWindowOpen">
        <bm-info-window :show="show" @close="infoWindowClose" @open="infoWindowOpen">我爱北京天安门</bm-info-window>
      </bm-marker>
    </baidu-map>
  </div>
</template>
<script>
  import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
  import { BmNavigation } from 'vue-baidu-map'
  export default {
    name: "mapbox",
    data() {
      return {
        show: false,
        center: { lng: 0, lat: 0 }, //经纬度
        zoom: 13 //地图展示级别
      };
    },
    components: {
      BaiduMap,
      BmNavigation
    },
    methods: {
      infoWindowClose () {
        this.show = false
      },
      infoWindowOpen () {
        this.show = true
      },
      handler({ BMap, map }) {
        console.log(BMap, map);
        this.center.lng = 113.6313915479;
        this.center.lat = 34.7533581487;
        this.zoom = this.zoom;
      },
      getClickInfo(e) {
        console.log(e.point.lng);
        console.log(e.point.lat);
        this.center.lng = e.point.lng;
        this.center.lat = e.point.lat;
      }
    }
  };
</script>

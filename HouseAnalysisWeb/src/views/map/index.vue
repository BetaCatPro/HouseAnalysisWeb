<template>
  <div class="mapbox">
    <baidu-map :center="center" :zoom="zoom" :scroll-wheel-zoom="true" style="height:100vh" @ready="handler" @click="getClickInfo" ak="Qmz0VMtKw3uAI2GWClu9Q6iCnP2j2uH2">
      <!-- 必须给容器指高度，不然地图将显示在一个高度为0的容器中，看不到 -->
      <bml-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bml-navigation>
      <bml-geolocation anchor="BMAP_ANCHOR_BOTTOM_RIGHT" :showAddressBar="true" :autoLocation="true"></bml-geolocation>
      <bml-city-list anchor="BMAP_ANCHOR_TOP_LEFT"></bml-city-list>
    </baidu-map>
  </div>
</template>
<script>
  import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
  import {BmlNavigation, Bmlgeolocation, BmlCityList} from 'vue-baidu-map'
  export default {
    name: "mapbox",
    data() {
      return {
        center: { lng: 0, lat: 0 }, //经纬度
        zoom: 13 //地图展示级别
      };
    },
    components: {
      BaiduMap,
      BmlNavigation,
      Bmlgeolocation,
      BmlCityList
    },
    methods: {
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

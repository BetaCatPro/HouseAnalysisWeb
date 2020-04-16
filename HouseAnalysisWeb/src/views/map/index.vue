<template>
  <div class="information">
    <div class="innerHMap">
      <baidu-map  ref="baidumap"
                  class="bm-view"
                  style="width:100%;height:92vh"
                  ak="Qmz0VMtKw3uAI2GWClu9Q6iCnP2j2uH2"
                  :center="{lng: 104.07, lat: 30.67}"
                  :scroll-wheel-zoom="true"
                  :zoom="13">
        <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
        <!--<bm-marker v-for="spoi in searchResults"-->
                   <!--:position="{lng: spoi.lng, lat: spoi.lat}"-->
                   <!--:title="spoi.community_name">-->
        <!--</bm-marker>-->
        <bm-point-collection :points="searchResults"
                             shape="BMAP_POINT_SHAPE_CIRCLE"
                             color="red"
                             size="BMAP_POINT_SIZE_BIGGER">
        </bm-point-collection>
      </baidu-map>
    </div>
  </div>
</template>

<script>
  import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
  import { BmMarker, BmPointCollection, BmNavigation } from 'vue-baidu-map'
  import { getAllHouse, getPotion } from '@/api/charts.js'

  export default {
    data() {
      return {
        searchResults: [],
        interval: '',
        hasNext: true,
        next: '/all_house/'
      }
    },
    components: {
      BaiduMap,
      BmMarker,
      BmPointCollection,
      BmNavigation
    },
    created() {
//      this.interval = setInterval(()=>{
//        if(this.hasNext) {
//          this.getRes(this.next)
//        } else {
//          clearInterval(this.interval)
//        }
//      },1500)
//      this.getRes(this.next)
      this.getRes()
    },
    methods: {
      // http://127.0.0.1:8000/v1/api/all_house/?page=2
//      getRes(next) {
//        getAllHouse(next).then((res,err)=>{
//          if(res.next) {
//            this.next = '/all_house/?' + res.next.split('?')[1]
//          } else {
//            this.hasNext = false
//          }
//          Array.from(res.results).map((item,index)=>{
//            this.searchResults.push(item)
//          })
//        })
//      }
      getRes() {
        getPotion().then((res,err)=>{
          Array.from(res.results).map((item,index)=>{
            this.searchResults.push(item)
          })
        })
      }
    }
  }
</script>

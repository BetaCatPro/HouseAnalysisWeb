<template>
  <div class="information">
    <div class="colorRange">
      <ul>
        <li v-for="(color,index) in color">
          <div :style="{backgroundColor:color}"></div>
          <span>{{ range[index].min }}-{{ range[index].max }}</span>
        </li>
      </ul>
    </div>
    <div class="innerHMap"
         v-loading="loading"
         element-loading-text="拼命加载中,马上就好辣"
         element-loading-background="rgba(255, 255, 255, 0.8)">
      <baidu-map  ref="baidumap"
                  class="bm-view"
                  style="width:100%;height:93vh"
                  ak="Qmz0VMtKw3uAI2GWClu9Q6iCnP2j2uH2"
                  :center="{lng: 104.07, lat: 30.67}"
                  :scroll-wheel-zoom="true"
                  :zoom="16">
        <bm-navigation anchor="BMAP_ANCHOR_TOP_LEFT"></bm-navigation>
        <!--<bm-marker v-for="spoi in searchResults"-->
                   <!--:position="{lng: spoi.lng, lat: spoi.lat}"-->
                   <!--:title="spoi.community_name">-->
        <!--</bm-marker>-->
        <bm-point-collection v-for="(range,index) in searchResultsTmp"
                             :points="range"
                             shape="BMAP_POINT_SHAPE_CIRCLE"
                             :color="color[index]"
                             size="BMAP_POINT_SIZE_BIGGER">
        </bm-point-collection>
      </baidu-map>
    </div>
  </div>
</template>

<script>
  import { Message } from 'element-ui'
  import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
  import { BmMarker, BmPointCollection, BmNavigation } from 'vue-baidu-map'
  import { getAllHouse, getAllCommunityInfo } from '@/api/charts.js'
  import colors from './Util/color_setting.js'
  import { generateRange } from './Util/priceRange.js'

  export default {
    data() {
      return {
//        根据range进行渲染聚合点
//        通过后端实现当前功能
//        searchResultsTmp: [
//          [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
//        ],
//        searchResults: [],
        searchResultsTmp: [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
        searchResults: [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
        color: [],
        range: [],
        interval: '',
        loading: true
      }
    },
    components: {
      BaiduMap,
      BmMarker,
      BmPointCollection,
      BmNavigation
    },
    created() {
      this.color = colors
      this.range = generateRange()
      this.loadAll()
    },
    methods: {
      getRes(rangeIndex) {
        getAllCommunityInfo({rangeindex:rangeIndex}).then((res,err)=>{
          Array.from(res).map((item,index)=>{
//            let range = judgePriceRange(res.unit_price)
//            this.searchResultsTmp[range].push({lng: item.lng, lat: item.lat})

            this.searchResultsTmp[rangeIndex-1].push({
                lng: item.lng,
                lat: item.lat,
            })
          })
        })
      },
      loadAll() {
        let rangeIndex = 1
        this.interval = setInterval(function() {
          if(rangeIndex > 1) this.loading = false
          if(rangeIndex <= 17) {
            this.getRes(rangeIndex)
            rangeIndex += 1
          } else {
            Message({
              message: '数据已全部加载完成了',
              type: 'success',
              duration: 3 * 1000
            })
            clearInterval(this.interval)
          }
        }.bind(this),2500)
      }
    }
  }
</script>

<style lang="scss">
.innerHMap {
  width: 100%;
  height: 100%;
}
.colorRange {
  z-index: 99999;
  position: absolute;
  right: 8%;
  top: 0;
  bottom: 0;
  width: 180px;
  height: 100%;
  background-color: #fff;
  opacity: 0.7;

  ul,li {
    margin: 0;
    padding: 0;
  }
  ul {
    width: 100%;
    height: 100%;
    overflow: hidden;
  }
  li {
    /*float: left;*/
    list-style: none;
    margin-top:5px;
    width: 100%;
    height: 40px;
  }
  li div {
    -webkit-border-radius: 50%;
    -moz-border-radius: 50%;
    border-radius: 50%;
    width: 40px;
    height: 100%;
    float: left;
    margin-left:8px;
  }
  li span {
    width: 110px;
    height: 100%;
    float: right;
    line-height:40px;
    font-size:16px;
    font-weight:700;
  }
}
</style>

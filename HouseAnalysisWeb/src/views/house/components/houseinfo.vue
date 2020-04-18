<template>
  <div class="information">
    <el-row>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" style="background: #F5F5F6;">
        <div class="title">
          <h1>{{ houseDetail.title }}</h1>
          <div>{{ houseDetail.title }}</div>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" style="padding-left: 50px">
        <div class="houseinfo">
          <div class="img">
            <div class="big">
              <el-carousel ref="carousel" height="400px">
                <el-carousel-item v-for="(item,index) in imgs" :key="item" name="index">
                  <div ref="bigimg"
                       class="innerimg"
                       :style="{background: 'url('+ item +') no-repeat',backgroundSize:'cover'}"/>
                </el-carousel-item>
              </el-carousel>
            </div>
            <div class="small">
              <ul>
                <li v-for="(img,index) in imgs" @click="setActiveItemC(index)"><img :src="img" alt="" class="active" :onerror="errorImg"></li>
              </ul>
            </div>
          </div>
          <div class="info">
            <div class="price">
              <span class="total">{{ houseDetail.price }}</span>
              <span class="unit"><span>万</span></span>
              <div class="text">
                <div class="unitPrice">
                  <span class="unitPriceValue" style="">{{ houseDetail.unit_price }}<i style="">元/平米</i></span>
                </div>
              </div>
            </div>
            <div class="house">
              <div class="room">
                <div class="mainInfo">{{ houseDetail.type }}</div>
                <div class="subInfo">{{ houseDetail.floor }}</div>
              </div>
              <div class="type">
                <div class="mainInfo" title="西北">{{ houseDetail.orientation }}</div>
                <div class="subInfo">{{ houseDetail.decoration }}</div>
              </div>
              <div class="area">
                <div class="mainInfo">{{ houseDetail.construction_area }}平米</div>
                <div class="subInfo" />
              </div>
            </div>
            <div class="aroundInfo">
              <div class="communityName">
                <i />
                <span class="label">小区名称</span>
                <span class="infor">{{ houseDetail.community_name }}</span>
              </div>
              <div class="detail">
                <i />
                <span class="label">所在区域</span>
                <span class="infor">{{ houseDetail.region | parseArray }}</span>
              </div>
              <div class="detail">
                <i />
                <span class="label">电梯情况</span>
                <span class="infor">{{ houseDetail.elevator }}</span>
              </div>
              <div class="detail">
                <i />
                <span class="label">房屋用途</span>
                <span class="infor">{{ houseDetail.purposes }}</span>
              </div>
              <div class="detail">
                <i />
                <span class="label">挂牌时间</span>
                <span class="infor">{{ houseDetail.release_date }}</span>
              </div>
              <div class="detail">
                <i />
                <span class="label">建筑结构</span>
                <span class="infor">{{ houseDetail.house_structure }}</span>
              </div>
              <div class="detail">
                <i />
                <span class="label">房源来源</span>
                <a class="infor" style="color: red;">查看</a>
              </div>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row style="margin-top: 20px;">
      <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" style="background: #F5F5F6;">
        <div class="housemap">
          <h1>房屋周边</h1>
          <div class="innerHMap">
            <baidu-map  class="bm-view"
                        style="width:100%;height:100%"
                        ak="Qmz0VMtKw3uAI2GWClu9Q6iCnP2j2uH2"
                        :center="{lng: houseDetail.lng, lat: houseDetail.lat}"
                        :zoom="15">
              <my-overlay
                :position="{lng: houseDetail.lng, lat: houseDetail.lat}"
                :text="name"
                :color='color'
              ></my-overlay>
              <bm-marker v-for="spoi in searchResults"
                         :position="{lng: spoi.location.lng, lat: spoi.location.lat}"
                         :title="spoi.name"
                         :icon="{url: 'https://www.cnblogs.com/images/cnblogs_com/progor/1390402/o_bike2.png',size: {width: 32, height: 32}}">
              </bm-marker>
              <bm-info-window v-for="spoi in searchResults"
                              :show="showWindow"
                              :position="{lng: spoi.location.lng, lat: spoi.location.lat}"
                              :titledata="spoi.name"
                              @close="infoWindowClose"
                              @open="infoWindowOpen" ref="demo"
                              >
                <div class="contentBox">
                  <div class="itemContent">
                    <i class="icon"></i>
                    <span class="itemTitle">{{ spoi.name }}</span>
                    <br />
                    <span class="itemInfo initem">{{ spoi.address }}</span>
                  </div>
                </div>
              </bm-info-window>
            </baidu-map>
          </div>
          <div class="innerHInfo">
            <el-row>
              <el-col>
                <el-tabs type="border-card" @tab-click="processData">
                  <el-tab-pane v-for="zhoubian in allinfor" :label="zhoubian.title">
                    <el-tabs v-model="activeName" @tab-click="handleClick">
                      <el-tab-pane v-for="detail in zhoubian.sub" :label="detail.subname" :name="detail.lab">
                        <el-card class="box-card"
                                 v-loading="loading"
                                 element-loading-text="拼命加载中">
                          <div v-if="searchResults.length === 0">
                            <div class="contentBox">
                              <div class="itemContent">
                                <span class="itemTitle">暂无信息</span>
                              </div>
                            </div>
                          </div>
                          <div v-for="spoi in searchResults" :key="spoi.uid" class="text item">
                            <div class="contentBox">
                              <div class="itemContent">
                                  <i class="icon"></i>
                                  <span class="itemTitle">{{ spoi.name }}</span>
                                  <span class="itemInfo">{{ spoi.address }}</span>
                              </div>
                            </div>
                          </div>
                        </el-card>
                      </el-tab-pane>
                    </el-tabs>
                  </el-tab-pane>

                  <!--<el-tab-pane label="交通">-->
                    <!--<el-tabs v-model="activeName" @tab-click="handleClick">-->
                      <!--<el-tab-pane label="地铁站" name="first">-->
                        <!--<el-card class="box-card">-->
                          <!--<div v-for="o in 4" :key="o" class="text item">-->
                            <!--{{'列表内容 ' + o }}-->
                          <!--</div>-->
                        <!--</el-card>-->
                      <!--</el-tab-pane>-->
                      <!--<el-tab-pane label="公交站" name="second">公交站</el-tab-pane>-->
                    <!--</el-tabs>-->
                  <!--</el-tab-pane>-->
                  <!--<el-tab-pane label="教育">-->
                    <!--<el-tabs v-model="activeName" @tab-click="handleClick">-->
                      <!--<el-tab-pane label="幼儿园" name="first">幼儿园</el-tab-pane>-->
                      <!--<el-tab-pane label="小学" name="second">小学</el-tab-pane>-->
                      <!--<el-tab-pane label="中学" name="third">中学</el-tab-pane>-->
                      <!--<el-tab-pane label="大学" name="fourth">大学</el-tab-pane>-->
                    <!--</el-tabs>-->
                  <!--</el-tab-pane>-->
                  <!--<el-tab-pane label="医疗">-->
                    <!--<el-tabs v-model="activeName" @tab-click="handleClick">-->
                      <!--<el-tab-pane label="医院" name="first">医院</el-tab-pane>-->
                      <!--<el-tab-pane label="药店" name="second">药店</el-tab-pane>-->
                    <!--</el-tabs>-->
                  <!--</el-tab-pane>-->
                  <!--<el-tab-pane label="购物">-->
                    <!--<el-tabs v-model="activeName" @tab-click="handleClick">-->
                      <!--<el-tab-pane label="商场" name="first">商场</el-tab-pane>-->
                      <!--<el-tab-pane label="超市" name="second">超市</el-tab-pane>-->
                      <!--<el-tab-pane label="市场" name="third">市场</el-tab-pane>-->
                    <!--</el-tabs>-->
                  <!--</el-tab-pane>-->
                  <!--<el-tab-pane label="生活">-->
                    <!--<el-tabs v-model="activeName" @tab-click="handleClick">-->
                      <!--<el-tab-pane label="银行" name="first">银行</el-tab-pane>-->
                      <!--<el-tab-pane label="ATM" name="second">ATM</el-tab-pane>-->
                      <!--<el-tab-pane label="餐厅" name="third">餐厅</el-tab-pane>-->
                      <!--<el-tab-pane label="咖啡馆" name="fourth">咖啡馆</el-tab-pane>-->
                    <!--</el-tabs>-->
                  <!--</el-tab-pane>-->
                  <!--<el-tab-pane label="娱乐">-->
                    <!--<el-tabs v-model="activeName" @tab-click="handleClick">-->
                      <!--<el-tab-pane label="公园" name="first">公园</el-tab-pane>-->
                      <!--<el-tab-pane label="电影院" name="second">电影院</el-tab-pane>-->
                      <!--<el-tab-pane label="健身房" name="third">健身房</el-tab-pane>-->
                      <!--<el-tab-pane label="体育馆" name="fourth">体育馆</el-tab-pane>-->
                    <!--</el-tabs>-->
                  <!--</el-tab-pane>-->
                </el-tabs>
              </el-col>
            </el-row>
            <el-row></el-row>
            <el-row></el-row>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import BaiduMap from 'vue-baidu-map/components/map/Map.vue'
import { BmNavigation, BmMarker, BmOverlay, BmInfoWindow } from 'vue-baidu-map'
import MyOverlay from '@/components/MyOverlay'
import { getAllHouse } from '@/api/charts.js'
import axios from 'axios'
axios.defaults.baseURL = '/api'

export default {
  filters: {
    parseArray: function(value) {
      if (!value) return ''
      return value.replace(/\[|\]|'/g, '').split(',').join('-')
    }
  },
  data() {
    return {
      showWindowInfo: '',
      showWindow: false,
      loading: true,
      searchResults: [],
      allinfor: [{
        title:'交通',
        sub: [{
          subname: '地铁站',
          lab: 'first'
        },{
          subname: '公交站',
          lab: 'second'
        }]
      },{
        title:'教育',
        sub: [{
          subname: '幼儿园',
          lab: 'first'
        },{
          subname: '小学',
          lab: 'second'
        },{
          subname: '中学',
          lab: 'third'
        },{
          subname: '大学',
          lab: 'fourth'
        }]
      },{
        title:'医疗',
        sub: [{
          subname: '医院',
          lab: 'first'
        },{
          subname: '药店',
          lab: 'second'
        }]
      },{
        title:'购物',
        sub: [{
          subname: '商场',
          lab: 'first'
        },{
          subname: '超市',
          lab: 'second'
        },{
          subname: '市场',
          lab: 'third'
        }]
      },{
        title:'生活',
        sub: [{
          subname: '银行',
          lab: 'first'
        },{
          subname: 'ATM',
          lab: 'second'
        },{
          subname: '餐厅',
          lab: 'third'
        },{
          subname: '咖啡馆',
          lab: 'fourth'
        }]
      },{
        title:'娱乐',
        sub: [{
          subname: '公园',
          lab: 'first'
        },{
          subname: '电影院',
          lab: 'second'
        },{
          subname: '健身房',
          lab: 'third'
        },{
          subname: '体育馆',
          lab: 'fourth'
        }]
      }],
      name: '',
      color: '#fff',
      houseDetail: {},
      activeName: 'first',
      imgs: [],
      errorImg: 'this.src="' + require('../../../assets/house_detail.png') + '"'
    }
  },
//  watch: {
//    showWindowInfo(newval,oldval) {
//      let pos_arr = this.$refs.demo
//      Array.from(pos_arr).map((item,index)=>{
//        if(item.$attrs.titledata == newval){
//          return true
//        }
//      })
//    }
//  },
  components: {
    BaiduMap,
    BmNavigation,
    BmMarker,
    MyOverlay,
    BmInfoWindow
  },
  created() {
    /*
    {
      "id": 1,
      "title": "好方出售户型房子 采光好 。。。。。",
      "price": "102.0",
      "unit_price": "10933.6",
      "community_name": "新绿苑",
      "region": "['成华', '驷马桥']",
      "type": "3室2厅1卫",
      "construction_area": "93.29",
      "orientation": "北",
      "decoration": "毛坯",
      "floor": "中楼层 (共6层)",
      "elevator": "无",
      "purposes": "普通住宅",
      "release_date": "2018-09-27",
      "house_structure": "钢混结构",
      "image_urls": "['https://vrlab-image4.ljcdn.com/release/auto3dhd/52e7fb5cb2dc8f97e711541d134d6722/screenshot/1551425211_0/pc0_jeU0YM660.jpg?imageMogr2/quality/70/thumbnail/1024x', 'https://ke-image.ljcdn.com/510100-inspection/prod-86ca45e5-25be-4426-a422-116a1953ffe5.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com', 'https://ke-image.ljcdn.com/hdic-frame/prod-93f2b4da-2322-4ea7-98de-282292f1fec7.png!m_fill,w_120,h_80,f_jpg?from=ke.com', 'https://ke-image.ljcdn.com/510100-inspection/prod-7566368e-a8d3-4c01-b689-d878d9745f58.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com', 'https://ke-image.ljcdn.com/510100-inspection/prod-09213814-7ef1-4432-ac64-e343119f4439.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com', 'https://ke-image.ljcdn.com/510100-inspection/prod-4cb3f159-5478-4370-a971-1ea7405bb31b.jpg!m_fill,w_120,h_80,f_jpg?from=ke.com']",
      "from_url": "https://cd.ke.com/ershoufang/18122017710105505565.html",
      "idi": 0,
      "lat": "30.702538520",
      "lng": "104.094544000"
  }
  */
    const id = this.$route.query.id
    getAllHouse('/all_house/' + id).then((res, err) => {
      this.houseDetail = res
      this.name = res.community_name
      this.getSearchPoi('地铁站',res.lng,res.lat)
      this.loading = false
      //      this.nearby.center.lat = res.lat
      //      this.nearby.center.lng = res.lng
      res.image_urls.match(/'(.+?)'/g).map((item, index) => {
        this.imgs.push(item.replace(/\'/g, ''))
      })
    })

    this.loading = false
  },
  methods: {
    infoWindowClose () {
      this.showWindow = false
    },
    infoWindowOpen (event) {
//      let pos_arr = this.$refs.demo
//      Array.from(pos_arr).map((item,index)=>{
//        if(item.$attrs.titledata == event.target.z.title){
//          item.show = true
//        }
//      })
      this.showWindowInfo = event.target.z.title
      this.showWindow = true
    },
    getSearchPoi(searchKey, lng, lat) {
      axios.get(`/search?query=${searchKey}&location=${lat},${lng}&radius=1000&output=json&ak=Qmz0VMtKw3uAI2GWClu9Q6iCnP2j2uH2`).then((res,err)=>{
        this.searchResults = res.data.results
//        console.log(this.searchResults)
      })
    },
    setActiveItemC(index) {
      this.$refs.carousel.setActiveItem(index)
    },
    processData(tab) {
      this.loading = true
      this.activeName = 'first'
      this.allinfor.map((item,index) => {
        if(item.title == tab.label) {
          let tag = item.sub[0].subname
          this.getSearchPoi(tag,this.houseDetail.lng,this.houseDetail.lat)
          this.loading = false
        }
      })
      this.loading = false
    },
    handleClick(tab, event) {
      this.loading = true
      this.getSearchPoi(tab.label,this.houseDetail.lng,this.houseDetail.lat)
      this.loading = false
    }
  }
}
</script>

<style lang="scss">
.title {
  height: 67px;
  width: 100%;
  padding-left:70px;
  margin-bottom:40px;

  h1 {
    width: 100%;
    height: 29px;
    font-size:26px;
    font-weight:700;
    line-height:29px;
  }

  div {
    width: 100%;
    height: 17px;
    font-size: 14px;
    line-height: 17px;
    color: #AAA;
    margin-top: 15px;
  }
}

.houseinfo {
  margin-top:21px;
  height: 500px;
  width: 1150px;

  .img {
    float: left;
    width: 710px;
    height: 100%;

    .big {
      width: 100%;
      height: 400px;

      .innerimg {
        width: 100%;
        height: 100%;
      }
    }

    .small {
      width: 100%;
      height:100px;
      overflow: hidden;

      ul,li {
        margin: 0;
        padding: 0;
      }

      li {
        list-style: none;
        float: left;
        height: 90px;
        width: 120px;
        cursor: pointer;
        margin:5px 10px;

        img {
          width: 100%;
          height: 100%;
          opacity: .5;
          filter: alpha(opacity=50);
          border: 0;
          vertical-align: top;
        }
        img:hover {
          opacity: 1;
          filter: alpha(opacity=100);
        }
      }
    }
  }

  .info {
    float: right;
    width: 380px;
    height: 100%;
    border-bottom:1px solid #bfa;

    .price {
      font-size: 14px;
      font-family: "Hiragino Sans GB","Microsoft Yahei UI","Microsoft Yahei","微软雅黑",'Segoe UI',Tahoma,"宋体b8b\4f53",SimSun,sans-serif;
      text-rendering: optimizeLegibility;
      -webkit-font-smoothing: antialiased;
      color: #394043;
      user-select: none;
      line-height: 1;
      margin: 0;
      padding: 0;
      position: relative;
      height: 49px;

      .total {
        display: inline-block;
        font-size: 46px;
        line-height: 46px;
        color: #e4393c;
        font-weight: bold;
        letter-spacing: -1px;
        max-width: 165px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }

      .unit {
        user-select: none;
        line-height: 1;
        display: inline-block;
        font-size: 16px;
        color: #e4393c;
        height: 37px;
        vertical-align: 6px;
      }

      .text {
        margin: 0;
        padding: 0;
        font-size: 12px;
        color: #333333;
        display: inline-block;
        margin-left: 15px;
        vertical-align: 6px;

        .unitPriceValue {
          font-size: 16px;
          font-weight: bold;
          color: #394043;
          white-space: nowrap;
        }
      }
      }

    .house {
      box-sizing: border-box;
      margin-top: 22px;
      width: 100%;
      border-top: 1px solid #eeeeee;
      border-bottom: 1px solid #eeeeee;
      padding: 30px 0;
      *zoom: 1;

      .mainInfo {
        font-size: 20px;
        font-weight: bold;
        color: #333333;
        overflow: hidden;
        text-overflow: ellipsis;
        -o-text-overflow: ellipsis;
        white-space: nowrap;
      }

      .subInfo {
        margin-top: 8px;
        font-size: 12px;
        color: #394043;
        overflow: hidden;
        text-overflow: ellipsis;
        -o-text-overflow: ellipsis;
        white-space: nowrap;
      }

      .room {
        text-align: center;
        float: left;
        width: 33%;
      }

      .type {
        text-align: center;
        float: left;
        width: 33%;
      }

      .area {
        text-align: center;
        float: left;
        width: 33%;
      }

    }
    .house:before,.house:after {
      display: table;
      content: "";
    }
    .house:after {
      clear: both;
    }

    .aroundInfo {
      padding: 24px 0;
      line-height: 18px;
      border-bottom: 1px solid #eeeeee;
      font-size: 14px;

      i {
        display: inline-block;
      }

      .label {
        color: #aeb0b1;
        margin-right: 24px;
      }

      .infor {
        color: #333333;
      }

      .detail {
        margin-top: 14px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
    }
  }
}

.zb {
  width: 100%;
  height: 29px;
  font-size:26px;
  font-weight:700;
  line-height:29px;
}

.aroundContainer {
  margin-top:21px;
  .map {
    height: 500px;
    width: 1150px;
  }
}

.housemap {
  width: 100%;
  height:600px;
  overflow: hidden;
  padding-left:70px;
  margin-bottom:40px;

  h {
    width: 100%;
    height: 29px;
    font-size:26px;
    font-weight:700;
    line-height:29px;
  }
  .innerHMap {
    width: 68%;
    height: 80%;
    float: left;
  }
  .innerHInfo {
    width: 28%;
    height: 80%;
    float: right;
    margin-right: 20px;
  }
}
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 100%;
  height: 352px;
  overflow: scroll;
}
.contentBox {
  border-left: 2px solid #fff;
  padding: 0 23px;

  .itemContent {
    position: relative;
  }

  .itemTitle {
    font-size:14px;
    font-weight:700;
    max-width: 49%;
    margin-right: 30px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
  }
  .icon {
    background: url('../../../assets/house_detail.png') no-repeat;
    -webkit-background-size: 100% 100%;
    background-size: 100% 100%;
    position: absolute;
    left:-30px;
    width: 20px;
    height: 20px;
  }
  .itemInfo {
    color: #9c9fa1;
    font-size: 14px;
    padding: 8px 19px 0 30px;
    text-align: justify;
    overflow: hidden;
    word-break: break-all;
    word-wrap: break-word;
    white-space: normal;
  }
  .initem {
    padding:0;
  }
}
</style>

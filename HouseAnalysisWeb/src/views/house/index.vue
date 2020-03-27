<template>
  <div class='wrapper'>
    <search @gethouse="gethouse" />

    <el-row style="margin-left: 20px">
      <el-col :span="18">
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
          <el-menu-item index="1">默认</el-menu-item>
          <el-menu-item index="2">总价</el-menu-item>
          <el-menu-item index="3">单价</el-menu-item>
          <el-menu-item index="4">面积</el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
    <el-row style="margin-left: 10px">
      <el-col :span="18">
        <div class="title">共找到 <span>{{ pagenums }}</span> 套成都二手房</div>
        <ul class="houselist">
          <li class="houseitem" v-for="house in houselist" :key="house.id">
            <router-link target="_blank" :to="{path:'/show/houseinfo',query: {id: house.id}}">
              <div class="leftimg" :style="{background: 'url('+ house.image_urls.match(/'(.+?)'/g)[0].replace(/\'/g,'') +') no-repeat',backgroundSize:'cover'}"></div>
            </router-link>
            <div class="rightinfo">
              <router-link target="_blank" :to="{path:'/show/houseinfo',query: {id: house.id}}">
                <p>{{ house.title }}</p>
              </router-link>
              <div class="price">
                <span>
                  {{ house.price }} <i>万</i>
                </span>
                <span>
                  单价{{ house.unit_price }}元/平米
                </span>
              </div>
              <div><i class="el-icon-location"></i>{{ house.community_name }} | {{ house.region | parseArray }}</div>
              <div><i class="el-icon-arrow-right"></i>{{ house.type }} | {{ house.construction_area }} | {{ house.orientation }} | {{ house.decoration }}</div>
              <div><i class="el-icon-time"></i>{{ house.elevator }} | {{ house.floor }} | {{ house.purposes }}</div>
            </div>
          </li>
        </ul>
      </el-col>
    </el-row>
    <el-row style="height: 100px;">
      <div class="commpage">
        <el-pagination
          background
          :page-size=30
          layout="prev, pager, next"
          :total="pagenums">
        </el-pagination>
      </div>
    </el-row>
  </div>
</template>

<script>
  import { getOrderHouse } from '@/api/charts.js'
import Search from '@/components/Search'
export default {
  data() {
    return {
      pagenums: 0,
      houselist: [],
      activeIndex: '1',
    }
  },
  components: {
    Search
  },
  filters: {
    parseArray: function(value) {
      if (!value) return ''
      return value.replace(/\[|\]|'/g,'').split(',').join('-')
    },
    getimg: function(value) {
      re_data = value.match(/'(.+?)'/g)
      first_img = re_data[0].replace(/\'/g,'')
      return first_img
    }
  },
  methods: {
    handleSelect(key, keyPath) {
      const tags = ['','price','unit_prcie','area']
      getOrderHouse(tags[key-1]).then((res,err)=>{
        this.pagenums = res.count
        this.houselist = res.results
      })
    },
    gethouse(data) {
      let totalData = data
      this.pagenums = totalData.count
      this.houselist = totalData.results
    }
  }
}
</script>

<style lang="scss">
.wrapper {
  width: 100%;
  height: 100%;
  margin-left: 50px;
}
  .title {
    height: 55px;
    line-height:55px;
    word-spacing:0;
    font-size:22px;
    font-weight:600;

    span {
      color: #00AE66;
    }
  }

  .houselist {
    padding:0;
    width: 910px;
  }

  .houseitem {
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    display: block;
    height: 194px;
    border-bottom:1px solid #f1f1f1;
    margin: 10px 0;


    .leftimg {
      float: left;
      width: 232px;
      height: 100%;
      cursor: pointer;
    }
    .rightinfo {
      float: right;
      width: 640px;
      height: 100%;

      p {
        height: 15px;
        line-height:15px;
        word-spacing:0;
        font-size:22px;
        font-weight:600;
        margin-left:10px;
      }
      p:hover {
        color: #00AE66;
      }

      div {
        height:25px;
        line-height: 25px;
        font-size: 15px;
        color: #616669;
        white-space: nowrap;
        margin: 10px;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;

        i {
          margin-right:7px;
        }
      }

      .price {
        float: right;
        margin-right:20px;

        span {
          display: block;
        }

        span:nth-child(1) {
          color: #DB4C3F;
          height: 30px;
          line-height:30px;
          font-size:26px;
          font-weight:700;
          margin-right:13px;

          i {
            font-size:14px;
          }
        }

        span:nth-child(2) {
          height: 16px;
          line-height:16px;
          font-size:12px;
        }
      }
    }
  }
.commpage {
  width: 100%;
  height: 100%;
  position: absolute;
  top:10px;
  bottom:18px;
  left:22%;
}
</style>

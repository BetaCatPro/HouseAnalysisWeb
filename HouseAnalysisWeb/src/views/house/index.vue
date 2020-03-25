<template>
  <div class='wrapper'>
    <search />

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
    <el-row style="margin-left: 20px">
      <el-col :span="18">
        <div class="title">共找到 <span>131472</span> 套成都二手房</div>
        <ul class="houselist">
          <li class="houseitem">
              <div class="leftimg" style="background-size:cover;background: url('https://ke-image.ljcdn.com/510100-inspection/pc0_jsAP7OUNP_1.jpg!m_fill,w_710,h_400,lg_north_west,lx_0,ly_0,l_fbk,f_jpg,ls_50?from=ke.com');"></div>
              <div class="rightinfo">
                <router-link target="_blank" :to="{path:'/show/houseinfo'}">
                  <p>{{ this.house.name }}</p>
                </router-link>
                <div class="price">
                  <span>
                    165 <i>万</i>
                  </span>
                  <span>
                    单价19408元/平米
                  </span>
                </div>
                <div><i class="el-icon-location"></i>{{ house.region }}</div>
                <div><i class="el-icon-arrow-right"></i>{{ house.info }} | {{ house.area }} | {{ house.orientation }} | {{ house.decoration }}</div>
                <div><i class="el-icon-time"></i>{{ house.structure }} | {{ house.releasedate }}</div>
              </div>
          </li>
          <li class="houseitem">
            <div class="leftimg" style="background: url('@/assets/DA.png');"></div>
            <div class="rightinfo">
              <router-link target="_blank" :to="{path:'/show/houseinfo'}">
                <p>{{ this.house.name }}</p>
              </router-link>
              <div class="price">
                  <span>
                    165 <i>万</i>
                  </span>
                <span>
                    单价19408元/平米
                  </span>
              </div>
              <div><i class="el-icon-location"></i>{{ house.region }}</div>
              <div><i class="el-icon-arrow-right"></i>{{ house.info }} | {{ house.area }} | {{ house.orientation }} | {{ house.decoration }}</div>
              <div><i class="el-icon-time"></i>{{ house.structure }} | {{ house.releasedate }}</div>
            </div>
          </li>
          <li class="houseitem">
            <div class="leftimg" style="background: url('@/assets/DA.png');"></div>
            <div class="rightinfo">
              <router-link target="_blank" :to="{path:'/show/houseinfo'}">
                <p>{{ this.house.name }}</p>
              </router-link>
              <div class="price">
                  <span>
                    165 <i>万</i>
                  </span>
                <span>
                    单价19408元/平米
                  </span>
              </div>
              <div><i class="el-icon-location"></i>{{ house.region }}</div>
              <div><i class="el-icon-arrow-right"></i>{{ house.info }} | {{ house.area }} | {{ house.orientation }} | {{ house.decoration }}</div>
              <div><i class="el-icon-time"></i>{{ house.structure }} | {{ house.releasedate }}</div>
            </div>
          </li>
          <li class="houseitem">
            <div class="leftimg" style="background: url('@/assets/DA.png');"></div>
            <div class="rightinfo">
              <router-link target="_blank" :to="{path:'/show/houseinfo'}">
                <p>{{ this.house.name }}</p>
              </router-link>
              <div class="price">
                  <span>
                    165 <i>万</i>
                  </span>
                <span>
                    单价19408元/平米
                  </span>
              </div>
              <div><i class="el-icon-location"></i>{{ house.region }}</div>
              <div><i class="el-icon-arrow-right"></i>{{ house.info }} | {{ house.area }} | {{ house.orientation }} | {{ house.decoration }}</div>
              <div><i class="el-icon-time"></i>{{ house.structure }} | {{ house.releasedate }}</div>
            </div>
          </li>
        </ul>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Search from '@/components/Search'
export default {
  data() {
    return {
        house: {
          name: '这时python的乐园，走开辣',
          region: '阿斯弗',
          info: '给的',
          area: '份额',
          orientation: '然后今天',
          structure: '七二',
          releasedate: '同一伙人',
          decoration: '就化工'
      },
      activeIndex: '1',
    }
  },
  components: {
    Search
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<style lang="scss">
.wrapper {
  width: 100%;
  height: 100%;
}
  .title {
    height: 55px;
    font-size:14px;
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
    }
    .rightinfo {
      float: right;
      width: 640px;
      height: 100%;

      p {
        height: 15px;
        font-size:14px;
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
</style>

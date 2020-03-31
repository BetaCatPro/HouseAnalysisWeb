<template>
  <div>
    <div class="mask" v-if="closed"></div>
    <div class="navtags">
      <nav-tags @getCommnuity="getCommnuity"/>
    </div>
    <el-row :gutter="5">
      <el-col :xs="24" :sm="16" :lg="18">
        <table-list :community="community" :pagenum="pagenum" :rid="rid" @closeWraper="closeWraper" />
      </el-col>
      <el-col :xs="24" :sm="8" :lg="6">
        <box-card :communityRange="communityRange" />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import NavTags from './components/NavTags'
import BoxCard from './components/BoxCard'
import TableList from './components/TableList'

import { getCommunityInfo, getCommunityRangeInfo } from '@/api/charts.js'

export default {
  data() {
    return {
      closed: false,
      pagenum: 0,
      community: [],
      communityRange: [],
      rid: 0
    }
  },
  components: {
    NavTags,
    BoxCard,
    TableList
  },
  methods: {
    getCommnuity(id) {
      getCommunityInfo({rid:id}).then((res,err)=>{
        this.community.length = 0
//        页码
        this.pagenum = res.count
        this.rid = id
        Array.from(res.results).map((item,index)=>{
          this.community.push({reg:item.region.region,name:item.name,number:item.num,price:parseFloat(item.mean_unit_price)})
        })
      })
      this.communityRange.length = 0
      getCommunityRangeInfo({rid:id}).then((res,err)=>{
        Array.from(res.results).map((item,index)=>{
          this.communityRange.push({id:res.id,reg:item.region.region,name:item.name,price:item.mean_unit_price})
        })
      })
    },
    closeWraper(tag) {
      this.closed = tag
    }
  }
}
</script>

<style>
.navtags {
  padding:2px 12px;
  margin-left: 20px;
}
.mask {
  z-index: 998;
  position: absolute;
  background-color: rgba(0,0,0,.5);
  width:100%;
  height:100%;
}
</style>

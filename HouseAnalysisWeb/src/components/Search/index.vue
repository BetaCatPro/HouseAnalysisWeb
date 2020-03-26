<template>
  <el-row>
    <el-col :span="24">
      <div class="searchbox">
        <el-autocomplete
          popper-class="my-autocomplete"
          v-model="searchinfo"
          :fetch-suggestions="querySearch"
          placeholder="请输入内容"
          style="width: 55%;"
          @select="handleSelect">
          <i
            class="el-icon-search el-input__icon"
            slot="suffix"
            style="cursor: pointer;"
            @click="handleIconClick">
          </i>
          <template slot-scope="props">
            <div class="name">{{ props.item.title }}</div>
            <span class="addr">{{ props.item.community_name }}</span>
          </template>
        </el-autocomplete>
      </div>
    </el-col>
  </el-row>
</template>

<script>
import { getAll } from '@/api/charts.js'
export default {
  data() {
    return {
      activeIndex: '1',
      searchinfo:'',
      timeout: null,
      searchPoi: [],
      emitData: {}
    };
  },
  watch: {
    searchinfo(curVal, oldVal) {
      // 实现input连续输入，只发一次请求
      clearTimeout(this.timeout);
      this.timeout = setTimeout(() => {
        this.getListPOI(curVal);
      }, 300);
    }
  },
  methods: {
    querySearch(queryString, cb) {
      var searchPoi = this.searchPoi;
      console.log(queryString)
      // 调用 callback 返回建议列表的数据
      cb(searchPoi);
    },
    handleSelect(item) {
//      console.log(item.value);
      this.getListPOI(item.value);
      this.$emit('gethouse',this.emitData)
    },
    handleIconClick() {
//      console.log(this.searchinfo);
      this.$emit('gethouse',this.emitData)
    },
    async getListPOI(inputVal) {
      if (inputVal === '') {
        return false;
      }
      this.searchPoi.length = 0;
      try {
        const res = await getAll(inputVal);
        this.emitData = res
        if (this.searchinfo === inputVal) { // 关键代码 避免先请求后返回问题，确保给列表赋值是以当前输入的值为参数的
          if (res.results) {
            let data = res.results;
            if (data.length === 0) {
              this.searchPoi = [];
            } else { // 有结果
              Array.from(data).map((item,index)=>{
                this.searchPoi.push({'title':item.title,'community_name':item.community_name})
              })
            }
          } else {
            this.searchPoi = [];
          }
        }
      } catch (err) {
        console.log("请求失败", err);
      }
    }
  }
}
</script>

<style lang="scss">
.searchbox {
  width: 100%;
  height: 100px;
  line-height: 100px;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  padding-left: 20px;

  .addr {
    color: #64D9D6;
  }
}
</style>

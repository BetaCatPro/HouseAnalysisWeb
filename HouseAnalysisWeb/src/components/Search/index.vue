<template>
  <el-row>
    <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
      <div class="searchbox">
        <el-autocomplete
          v-model="searchinfo"
          popper-class="my-autocomplete"
          :fetch-suggestions="querySearch"
          placeholder="请输入内容"
          style="width: 55%;"
          @select="handleSelect"
        >
          <i
            slot="suffix"
            class="el-icon-search el-input__icon"
            style="cursor: pointer;"
            @click="handleIconClick"
          />
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
import { getAllHouse } from '@/api/charts.js'
import { Message } from 'element-ui'
export default {
  data() {
    return {
      activeIndex: '1',
      searchinfo: '',
      timeout: null,
      searchPoi: [],
      emitData: {}
    }
  },
  watch: {
    searchinfo(curVal, oldVal) {
      // 实现input连续输入，只发一次请求
      clearTimeout(this.timeout)
      this.timeout = setTimeout(() => {
        this.getListPOIWatcher(curVal)
      }, 300)
    }
  },
  beforeCreate() {
    getAllHouse('/all_house').then((res, err) => {
      console.log(res)
      this.$emit('gethouse', { 'res': res, 'value': this.searchinfo})
    })
  },
  methods: {
    querySearch(queryString, cb) {
      var searchPoi = this.searchPoi
      // 调用 callback 返回建议列表的数据
      cb(searchPoi)
    },
    handleSelect(item) {
      this.getListPOI(item.title).then((res, err) => {
        this.$emit('gethouse', { 'res': res, 'value': this.searchinfo})
        Message.close()
      })
    },
    handleIconClick() {
      this.getListPOI(this.searchinfo).then((res, err) => {
        if(res) {
          this.$emit('gethouse', { 'res': res, 'value': this.searchinfo})
        }
        Message.close()
      })
    },
    async getListPOI(inputVal) {
      if (inputVal === '') {
        Message({
          showClose: true,
          message: '输入不能为空',
          type: 'error',
          duration: 3000
        })
        return false
      } else {
        Message({
          message: '正在搜索中......',
        })
        try {
          const res = await getAll(inputVal, 1)
          return res
        } catch (err) {
          console.log('请求失败', err)
        }
      }
    },
    async getListPOIWatcher(inputVal) {
      if (inputVal === '') {
        return false
      }
      try {
        const res = await getAll(inputVal, 1)
        if (this.searchinfo === inputVal) { // 关键代码 避免先请求后返回问题，确保给列表赋值是以当前输入的值为参数的
          if (res.results) {
            const data = res.results
            if (data.length === 0) {
              this.searchPoi = []
            } else { // 有结果
              Array.from(data).map((item, index) => {
                this.searchPoi.push({ 'title': item.title, 'community_name': item.community_name })
              })
            }
          } else {
            this.searchPoi = []
          }
        }
      } catch (err) {
        console.log('请求失败', err)
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

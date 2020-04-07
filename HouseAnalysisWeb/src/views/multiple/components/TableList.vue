<template>
  <div class="table">
    <transition name="fade">
      <div v-if="isClosed" class="house">
        <div class="close" @click="closeTable">
          <el-button type="primary" icon="el-icon-close" />
        </div>
        <div
          v-loading="loadingMask"
          class="loadingwraper"
          element-loading-background="rgb(255, 255, 255)"
          element-loading-text="正在加载中"
        />
        <el-table
          v-if="hasData"
          :data="houseData"
          max-height="480"
          :stripe="true"
          style="width: 100%"
        >
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">
                <el-form-item label="名称">
                  <span>{{ props.row.title }}</span>
                </el-form-item>
                <el-form-item label="总价">
                  <span>{{ props.row.price }}</span>
                </el-form-item>
                <el-form-item label="单价">
                  <span>{{ props.row.unit_price }}</span>
                </el-form-item>
                <el-form-item label="小区名">
                  <span>{{ props.row.community_name }}</span>
                </el-form-item>
                <el-form-item label="区划">
                  <span>{{ props.row.region.replace(/\[|\]|'/g,'').split(',').join('-') }}</span>
                </el-form-item>
                <el-form-item label="户型">
                  <span>{{ props.row.type }}</span>
                </el-form-item>
                <el-form-item label="建筑面积">
                  <span>{{ props.row.construction_area }}</span>
                </el-form-item>
                <el-form-item label="朝向">
                  <span>{{ props.row.orientation }}</span>
                </el-form-item>
                <el-form-item label="装修情况">
                  <span>{{ props.row.decoration }}</span>
                </el-form-item>
                <el-form-item label="楼层">
                  <span>{{ props.row.floor }}</span>
                </el-form-item>
                <el-form-item label="电梯">
                  <span>{{ props.row.elevator }}</span>
                </el-form-item>
                <el-form-item label="房屋类型">
                  <span>{{ props.row.purposes }}</span>
                </el-form-item>
                <el-form-item label="发布时间">
                  <span>{{ props.row.release_date }}</span>
                </el-form-item>
                <el-form-item label="建筑结构">
                  <span>{{ props.row.house_structure }}</span>
                </el-form-item>
              </el-form>
            </template>
          </el-table-column>
          <el-table-column
            label="房源名称"
            prop="title"
            width="320"
          />
          <el-table-column
            label="小区名称"
            prop="community_name"
          />
          <el-table-column
            label="区划"
            prop="region"
          />
        </el-table>
        <div class="pages">
          <!--<el-pagination-->
          <!--background-->
          <!--:page-size="housePaginationData.pageSize"-->
          <!--:current-page="housePaginationData.currentPage"-->
          <!--layout="prev, pager, next"-->
          <!--:total="housePaginationData.totalNumber"-->
          <!--@current-change="housePaginationData.handleCurrentChange">-->
          <!--</el-pagination>-->
          <pagination :pagination-data="housePaginationData" />
        </div>
      </div>
    </transition>
    <div class="community">
      <el-table
        :data="communities"
        style="width: 100%"
        :row-class-name="tableRowClassName"
      >
        <el-table-column
          prop="reg"
          label="区划"
          width="180"
        />
        <el-table-column
          prop="name"
          label="小区名"
          width="190"
        />
        <el-table-column
          prop="number"
          label="房源数"
          sortable
          width="180"
        />
        <el-table-column
          prop="price"
          label="均价"
          sortable
          width="180"
        />
        <el-table-column
          fixed="right"
          label="房源详情"
          width="180"
        >
          <template slot-scope="scope">
            <el-button type="text" size="small" @click="handleClick(scope.row)">查看</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="commpage">
        <el-pagination
          background
          :page-size="commPaginationData.pageSize"
          :current-page="commPaginationData.currentPage"
          layout="prev, pager, next"
          :total="pagenum"
          @current-change="commPaginationData.handleCurrentChange"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Vue from 'Vue'
import Pagination from '@/components/Pagination'
import { getAll, getCommunityInfo } from '@/api/charts.js'
import resize from './mixins/resize'
export default {
  components: {
    Pagination
  },
  mixins: [resize],
  props: ['community', 'pagenum', 'rid'],
  data() {
    return {
      loadingMask: true,
      isClosed: false,
      row: '',
      communities: [],
      houseData: [],
      hasData: false,
      commPaginationData: {
        pageSize: 30,
        currentPage: 1,
        totalNumber: this.pagenum,
        handleCurrentChange: psize => {
          console.log(this.rid)
          getCommunityInfo({ rid: this.rid, page: psize }).then((res, err) => {
            this.community.length = 0
            //        页码
            this.pagenum = res.count
            Array.from(res.results).map((item, index) => {
              this.community.push({ reg: item.region.region, name: item.name, number: item.region.num, price: parseFloat(item.mean_unit_price) })
            })
          })
        }
      },
      housePaginationData: {
        pageSize: 30,
        currentPage: 1,
        totalNumber: 0,
        handleCurrentChange: psize => {
          this.housePaginationData.currentPage = psize
          this.handleClick(this.row, psize)
        }
      }
    }
  },
  created() {
    this.communities = this.community
  },
  methods: {
    loading() {
      this.$nextTick(() => {
        this.loadingMask = Vue.prototype.$loading({
          lock: true,
          text: 'Loading...',
          fullscreen: false,
          target: document.querySelector('.loadingwraper')
        })
      })
    },
    closeLoading() {
      this.loadingMask.close()
    },
    async handleClick(row, page = 1) {
      this.loadingMask = true
      //      this.loading()
      //      记录当前区划
      this.row = row
      this.isClosed = true
      this.$emit('closeWraper', this.isClosed)
      this.hasData = false
      const houseData = await getAll(row.name, page)
      this.housePaginationData.totalNumber = houseData.count
      this.houseData.length = 0
      Array.from(houseData.results).map((item, index) => {
        this.houseData.push({
          'title': item.title,
          'price': item.price + '万',
          'unit_price': item.unit_price + '元/平米',
          'community_name': item.community_name,
          'region': item.region,
          'type': item.type,
          'construction_area': item.construction_area + '㎡',
          'orientation': item.orientation,
          'decoration': item.decoration,
          'floor': item.floor,
          'elevator': item.elevator,
          'purposes': item.purposes,
          'release_date': item.release_date,
          'house_structure': item.house_structure
        })
      })
      //      this.closeLoading()
      this.loadingMask = false
      this.hasData = true
    },
    tableRowClassName({ row, rowIndex }) {
      if (rowIndex % 2 === 1) {
        return 'warning-row'
      } else if (rowIndex % 2 === 0) {
        return 'success-row'
      }
      return ''
    },
    closeTable() {
      this.isClosed = false
      this.$emit('closeWraper', this.isClosed)
    }
  }
}
</script>

<style lang="scss">
.table {
  padding: 5px 18px;
  margin: 0 5px;

  .house {
    z-index: 999;
    position: fixed;
    top: 85px;
    left: 20%;
    width: 60%;
    height: 600px;
    border: none;
    background-color: #fff;
    -webkit-border-radius: 4px;
    -moz-border-radius: 4px;
    border-radius: 4px;
    -webkit-box-shadow: 1px 1px 5px #ccc;
    -moz-box-shadow: 1px 1px 5px #ccc ;
    box-shadow: 1px 1px 5px #ccc;

    .close {
      float: right;
    }

    .loadingwraper {
      width: 100%;
      top: 40px;
      height: 560px;
      float: left;
      position: absolute;
      /*z-index: 10000;*/
    }

    .pages {
      position: absolute;
      bottom:18px;
      left:30%;
    }
  }

  .el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }
}

.commpage {
  margin:35px 21%;
}

.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}

.fade-enter-active {
  transition: all .3s ease;
}
.fade-leave-active {
  transition: all .3s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.fade-enter, .fade-leave-to
  /* .fade-leave-active for below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
</style>

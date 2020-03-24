<template>
  <div class="table">
    <div class="community">
      <el-table
        :data="communities"
        style="width: 100%"
        :row-class-name="tableRowClassName">
        <el-table-column
          prop="reg"
          label="区划"
          width="180">
        </el-table-column>
        <el-table-column
          prop="name"
          label="小区名"
          width="190">
        </el-table-column>
        <el-table-column
          prop="number"
          label="房源数"
          sortable
          width="180">
        </el-table-column>
        <el-table-column
          prop="price"
          label="均价"
          sortable
          width="180">
        </el-table-column>
        <el-table-column
          fixed="right"
          label="房源详情"
          width="180">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <transition name="fade">
      <div class="house" v-if="isClosed">
        <div class="close" @click="closeTable">
          <el-button type="primary" icon="el-icon-close"></el-button>
        </div>
        <el-table
          :data="tableData5"
          max-height="480"
          stripe="true"
          style="width: 100%">
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">
                <el-form-item label="商品名称">
                  <span>{{ props.row.name }}</span>
                </el-form-item>
                <el-form-item label="所属店铺">
                  <span>{{ props.row.shop }}</span>
                </el-form-item>
                <el-form-item label="商品 ID">
                  <span>{{ props.row.id }}</span>
                </el-form-item>
                <el-form-item label="店铺 ID">
                  <span>{{ props.row.shopId }}</span>
                </el-form-item>
                <el-form-item label="商品分类">
                  <span>{{ props.row.category }}</span>
                </el-form-item>
                <el-form-item label="店铺地址">
                  <span>{{ props.row.address }}</span>
                </el-form-item>
                <el-form-item label="商品描述">
                  <span>{{ props.row.desc }}</span>
                </el-form-item>
              </el-form>
            </template>
          </el-table-column>
          <el-table-column
            label="商品 ID"
            prop="id">
          </el-table-column>
          <el-table-column
            label="商品名称"
            prop="name">
          </el-table-column>
          <el-table-column
            label="描述"
            prop="desc">
          </el-table-column>
        </el-table>
        <div class="pages">
          <el-pagination
            background
            page-size="9"
            layout="prev, pager, next"
            :total="762">
          </el-pagination>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
  import { getAll } from '@/api/charts.js'
  import resize from './mixins/resize'
  export default {
    mixins: [resize],
    props: ['community'],
    data() {
      return {
        isClosed: true,
        communities: [],
        tableData5: [{
          id: '12987122',
          name: '好滋好味鸡蛋仔',
          category: '江浙小吃、小吃零食',
          desc: '荷兰优质淡奶，奶香浓而不腻',
          address: '上海市普陀区真北路',
          shop: '王小虎夫妻店',
          shopId: '10333'
        }, {
          id: '12987123',
          name: '好滋好味鸡蛋仔',
          category: '江浙小吃、小吃零食',
          desc: '荷兰优质淡奶，奶香浓而不腻',
          address: '上海市普陀区真北路',
          shop: '王小虎夫妻店',
          shopId: '10333'
        }, {
          id: '12987125',
          name: '好滋好味鸡蛋仔',
          category: '江浙小吃、小吃零食',
          desc: '荷兰优质淡奶，奶香浓而不腻',
          address: '上海市普陀区真北路',
          shop: '王小虎夫妻店',
          shopId: '10333'
        }, {
          id: '12987126',
          name: '好滋好味鸡蛋仔',
          category: '江浙小吃、小吃零食',
          desc: '荷兰优质淡奶，奶香浓而不腻',
          address: '上海市普陀区真北路',
          shop: '王小虎夫妻店',
          shopId: '10333'
        }, {
          id: '12987126',
          name: '好滋好味鸡蛋仔',
          category: '江浙小吃、小吃零食',
          desc: '荷兰优质淡奶，奶香浓而不腻',
          address: '上海市普陀区真北路',
          shop: '王小虎夫妻店',
          shopId: '10333'
        }, {
          id: '12987126',
          name: '好滋好味鸡蛋仔',
          category: '江浙小吃、小吃零食',
          desc: '荷兰优质淡奶，奶香浓而不腻',
          address: '上海市普陀区真北路',
          shop: '王小虎夫妻店',
          shopId: '10333'
        }, {
          id: '12987126',
          name: '好滋好味鸡蛋仔',
          category: '江浙小吃、小吃零食',
          desc: '荷兰优质淡奶，奶香浓而不腻',
          address: '上海市普陀区真北路',
          shop: '王小虎夫妻店',
          shopId: '10333'
        }, {
          id: '12987126',
          name: '好滋好味鸡蛋仔',
          category: '江浙小吃、小吃零食',
          desc: '荷兰优质淡奶，奶香浓而不腻',
          address: '上海市普陀区真北路',
          shop: '王小虎夫妻店',
          shopId: '10333'
        }]
      }
    },
    methods: {
      async handleClick(row) {
        this.isClosed = true
        console.log(row.name)
        let houseData = await getAll(row.name)
      },
      tableRowClassName({row, rowIndex}) {
        if (rowIndex%2 === 1) {
          return 'warning-row';
        } else if (rowIndex%2 === 0) {
          return 'success-row';
        }
        return '';
      },
      closeTable() {
        this.isClosed = false
      }
    },
    mounted() {
      this.communities = this.community
    }
  }
</script>

<style lang="scss">
.table {
  padding: 5px 18px;
  margin: 0 5px;
  position: relative;
  .community {
    z-index: -1;
  }
  .house {
    z-index: 999;
    position: absolute;
    top: 55%;
    left: 30%;
    width: 70%;
    height: 550px;
    border: none;
    -webkit-box-shadow: 1px 1px 5px #ccc;
    -moz-box-shadow: 1px 1px 5px #ccc ;
    box-shadow: 1px 1px 5px #ccc;

    .close {
      /*position: absolute;*/
      /*right:1px;*/
      /*top:0;*/
      float: right;
      z-index: 999;
    }

    .pages {
      position: absolute;
      bottom:10px;
      left:20%;
    }
  }

  .el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }
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
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.fade-enter, .fade-leave-to
  /* .fade-leave-active for below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
</style>

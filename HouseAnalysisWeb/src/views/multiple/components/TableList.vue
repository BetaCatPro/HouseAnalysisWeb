<template>
  <div class="table">
    <el-table
      :data="communities"
      style="width: 100%"
      :row-class-name="tableRowClassName">
      <el-table-column
        prop="reg"
        label="区划"
        width="200">
      </el-table-column>
      <el-table-column
        prop="name"
        label="小区名"
        width="200">
      </el-table-column>
      <el-table-column
        prop="number"
        label="房源数"
        width="200">
      </el-table-column>
      <el-table-column
        prop="price"
        label="均价"
        width="200">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  import resize from './mixins/resize'
  export default {
    mixins: [resize],
    props: ['community'],
    methods: {
      tableRowClassName({row, rowIndex}) {
        if (rowIndex%2 === 1) {
          return 'warning-row';
        } else if (rowIndex%2 === 0) {
          return 'success-row';
        }
        return '';
      }
    },
    data() {
      return {
        communities: []
      }
    },
    mounted() {
      this.communities = this.community
    }
  }
</script>

<style>
.table {
  padding: 5px 18px;
  margin:0 5px;
}
.el-table .warning-row {
  background: oldlace;
}

.el-table .success-row {
  background: #f0f9eb;
}
</style>

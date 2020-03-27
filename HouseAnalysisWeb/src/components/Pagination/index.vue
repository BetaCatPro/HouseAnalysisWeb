<template>
  <el-pagination
    background
    :page-size="paginationData.pageSize"
    :current-page="paginationData.currentPage"
    layout="prev, pager, next"
    :total="paginationData.totalNumber"
    @current-change="paginationData.handleCurrentChange">
  </el-pagination>
</template>

<script>
  export default {
      props: ['paginationData']
  }
</script>

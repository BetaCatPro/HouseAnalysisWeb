<template>
  <div>
    <div class="navtags">
      <nav-tags />
    </div>
    <el-row :gutter="20">
      <el-col :span="18">
        <table-list />
      </el-col>
      <el-col :span="6">
        <box-card />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import NavTags from './components/NavTags'
import BoxCard from './components/BoxCard'
import TableList from './components/TableList'

export default {
  components: {
    NavTags,
    BoxCard,
    TableList
  }
}
</script>

<style lang="scss">
.navtags {
  padding:5px 18px;
}
</style>

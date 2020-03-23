<template>
  <el-card style="width: 280px;">
    <div slot="header" class="clearfix">
      <span>{{ this.region }}小区排行</span>
    </div>
    <div v-for="community in this.communityRange" :key="community.id" class="text item">
      <div class="name">{{ community.name }}均价<span>{{ community.price }}</span></div>
    </div>
  </el-card>
</template>

<script>
import resize from './mixins/resize'
export default {
  mixins: [resize],
  props: ['communityRange'],
  data() {
    return {
      region: '',
      statisticsData: {
        article_count: 1024,
        pageviews_count: 1024
      }
    }
  },
  mounted() {
    this.region = this.communityRange.reg
  }
}
</script>

<style lang="scss" >
.box-card-component{
  .el-card__header {
    padding: 0px!important;
  }
}
</style>
<style lang="scss" scoped>
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both
}
</style>

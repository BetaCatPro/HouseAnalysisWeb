<template>
  <div class="card">
    <el-card style="width: 320px;">
      <div slot="header" class="clearfix">
        <span>{{ this.region }}小区排行TOP10</span>
      </div>
      <div v-for="community in this.communityRange" :key="community.id" class="text item">
        <div class="name">
          <el-tooltip :content=community.name placement="top">
            <span class="na">{{ community.name }}</span>
          </el-tooltip>
          <span class="pr">{{ community.price+'元/平米' }}</span>
        </div>
      </div>
    </el-card>
  </div>
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
.card {
  margin-top: 50px;
}
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.name{
  width: 100%;
  height: 36px;
  backgroundColor: rgb(255,255,255);
  transition:all 1s ease,left 1s ease-in-out;
  opacity:1;
  filter:alpha(opacity=100);
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;
  text-indent: 10px;
}

.name span {
  display: block;
  height: 100%;
  line-height: 36px;
}

.na{
  float: left;
  width: 125px;
  overflow: hidden;
  text-overflow:ellipsis;
  white-space: nowrap;
}

.pr {
  float: right;
  margin-right: 20px;
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

<template>
  <div class="dashboard-editor-container">
    <panel-group/>

    <el-row v-loading="loading" element-loading-text="拼命加载中"
            element-loading-background="rgba(255, 255, 255, 0.8)"
            style="background:#fff;padding:16px 16px;margin-bottom:30px;">
      <bar-chart @hideloading="hideLoading" />
    </el-row>

    <el-row :gutter="32">
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper">
          <pie-chart />
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="12"
              v-loading="loading"
              element-loading-text="拼命加载中"
              element-loading-background="rgba(255, 255, 255, 0.8)">
        <div class="chart-wrapper">
          <bar-chartp @hideloading="hideLoading" />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import PanelGroup from './components/PanelGroup'
import PieChart from './components/PieChart'
import BarChart from './components/BarChart'
import BarChartp from './components/BarChartp'

export default {
  name: 'DashboardAdmin',
  components: {
    PanelGroup,
    PieChart,
    BarChart,
    BarChartp
  },
  data() {
    return {
      loading: true
    }
  },
  methods: {
    hideLoading(val) {
      this.loading = val
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  position: relative;

  .chart-wrapper {
    background: #fff;
    padding: 16px 16px;
    margin-bottom: 32px;
  }
}

@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>

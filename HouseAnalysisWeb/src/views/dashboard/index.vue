<template>
  <div class="dashboard-editor-container">
    <panel-group/>

    <el-row v-loading="loading" element-loading-text="拼命加载中"
            element-loading-background="rgba(255, 255, 255, 0.8)"
            style="background:#fff;padding:16px 16px;margin-bottom:30px;">
      <bar-chart @hideloading="hideloading" />
    </el-row>

    <el-row :gutter="32">
      <el-col :xs="24" :sm="24" :lg="12"
              v-loading="loading3"
              element-loading-text="拼命加载中"
              element-loading-background="rgba(255, 255, 255, 0.8)">
        <div class="chart-wrapper">
          <pie-chart @hideloading3="hideloading3" />
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="12"
              v-loading="loading2"
              element-loading-text="拼命加载中"
              element-loading-background="rgba(255, 255, 255, 0.8)">
        <div class="chart-wrapper">
          <bar-chartp @hideloading2="hideloading2" />
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="12"
              v-loading="loading4"
              element-loading-text="拼命加载中"
              element-loading-background="rgba(255, 255, 255, 0.8)">
        <div class="chart-wrapper">
          <bar-chartup @hideloading4="hideloading4" />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import PanelGroup from './components/PanelGroup'
import BarChart from './components/BarChart'
import PieChart from './components/PieChart'
import BarChartp from './components/BarChartp'
import BarChartup from './components/BarChartup'

export default {
  name: 'DashboardAdmin',
  components: {
    PanelGroup,
    BarChart,
    PieChart,
    BarChartp,
    BarChartup
  },
  data() {
    return {
      loading: true,
      loading2: true,
      loading3: true,
      loading4: true
    }
  },
  methods: {
    hideloading(val) {
      this.loading = val
    },
    hideloading2(val) {
      this.loading2 = val
    },
    hideloading3(val) {
      this.loading3 = val
    },
    hideloading4(val) {
      this.loading4 = val
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
    margin-bottom: 16px;
  }
}

@media (max-width:1024px) {
  .chart-wrapper {
    padding: 8px;
  }
}
</style>

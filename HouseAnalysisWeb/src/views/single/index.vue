<template>
  <div class="dashboard-editor-container">

    <el-row :gutter="32">
      <el-col :xs="24" :sm="24" :lg="12"
              v-loading="loading"
              element-loading-text="拼命加载中"
              element-loading-background="rgba(255, 255, 255, 0.8)">
        <div class="chart-wrapper">
          <elevator-bar-chart @hideloading="hideloading" />
        </div>
      </el-col>

      <el-col :xs="24" :sm="24" :lg="12"
              v-loading="loading"
              element-loading-text="拼命加载中"
              element-loading-background="rgba(255, 255, 255, 0.8)">
        <div class="chart-wrapper">
          <constrcuture-bar-chart @hideloading="hideloading" />
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import ElevatorBarChart from './components/ElevatorBarChart'
import ConstrcutureBarChart from './components/ConstrcutureBarChart'

export default {
  name: 'DashboardAdmin',
  components: {
    ElevatorBarChart,
    ConstrcutureBarChart
  },
  data() {
    return {
      loading: false
    }
  },
  methods: {
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

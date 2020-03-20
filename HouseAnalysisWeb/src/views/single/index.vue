<template>
  <div class="dashboard-editor-container">

    <el-row :gutter="32">
      <el-col :xs="24" :sm="24" :lg="12"
              v-loading="loading"
              element-loading-text="拼命加载中"
              element-loading-background="rgba(255, 255, 255, 0.8)">
        <div class="chart-wrapper">
          <elevator-bar-chart/>
        </div>
      </el-col>

      <el-col :xs="24" :sm="24" :lg="12"
              v-loading="loading"
              element-loading-text="拼命加载中"
              element-loading-background="rgba(255, 255, 255, 0.8)">
        <div class="chart-wrapper">
          <constrcuture-pie-chart/>
        </div>
      </el-col>

      <el-col :xs="24" :sm="24" :lg="12"
              v-loading="loading"
              element-loading-text="拼命加载中"
              element-loading-background="rgba(255, 255, 255, 0.8)">
        <div class="chart-wrapper">
          <purpose-pie-chart/>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import ElevatorBarChart from './components/ElevatorBarChart'
import ConstrcuturePieChart from './components/ConstrcuturePieChart'
import PurposePieChart from './components/PurposePieChart.vue'

export default {
  name: 'DataAnalysis',
  components: {
    ElevatorBarChart,
    ConstrcuturePieChart,
    PurposePieChart
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

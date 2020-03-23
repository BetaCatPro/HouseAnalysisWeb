<template>
  <div class="dashboard-editor-container">
    <el-row :gutter="32">
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper">
          <decoration-pie-chart></decoration-pie-chart>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper">
          <decoration-bar-chart></decoration-bar-chart>
        </div>
      </el-col>
      <el-col>
        <div class="chart-wrapper">
          <layout-line-chart></layout-line-chart>
        </div>
      </el-col>
    </el-row>

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

    <el-row :gutter="32">
      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper">
          <orientatation-pie-chart></orientatation-pie-chart>
        </div>
      </el-col>

      <el-col :xs="24" :sm="24" :lg="12">
        <div class="chart-wrapper">
          <floor-bar-chart></floor-bar-chart>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import ElevatorBarChart from './components/ElevatorBarChart'
import ConstrcuturePieChart from './components/ConstrcuturePieChart'
import PurposePieChart from './components/PurposePieChart'
import DecorationPieChart from './components/DecorationPieChart'
import DecorationBarChart from './components/DecorationBarChart'
import FloorBarChart from './components/FloorBarChart'
import LayoutLineChart from './components/LayoutLineChart'
import OrientatationPieChart from './components/OrientationPieChart'

export default {
  name: 'DataAnalysis',
  components: {
    ElevatorBarChart,
    ConstrcuturePieChart,
    PurposePieChart,
    DecorationPieChart,
    DecorationBarChart,
    FloorBarChart,
    LayoutLineChart,
    OrientatationPieChart
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

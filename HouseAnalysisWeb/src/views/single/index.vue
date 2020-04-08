<template>
  <div class="dashboard-editor-container">
    <el-row :gutter="32">
      <el-col
        v-loading="loading1"
        :xs="24"
        :sm="24"
        :lg="12"
        element-loading-text="拼命加载中"
        element-loading-background="rgba(255, 255, 255, 0.8)"
      >
        <div class="chart-wrapper">
          <decoration-pie-chart @showchart1="showchart1" />
        </div>
      </el-col>
      <el-col
        v-loading="loading2"
        :xs="24"
        :sm="24"
        :lg="12"
        element-loading-text="拼命加载中"
        element-loading-background="rgba(255, 255, 255, 0.8)"
      >
        <div class="chart-wrapper">
          <decoration-bar-chart @showchart2="showchart2" />
        </div>
      </el-col>
      <el-col
        v-loading="loading3"
        element-loading-text="拼命加载中"
        element-loading-background="rgba(255, 255, 255, 0.8)"
      >
        <div class="chart-wrapper">
          <layout-line-chart @showchart3="showchart3" />
        </div>
      </el-col>
    </el-row>

    <el-row :gutter="32">
      <el-col
        v-loading="loading4"
        :xs="24"
        :sm="24"
        :lg="12"
        element-loading-text="拼命加载中"
        element-loading-background="rgba(255, 255, 255, 0.8)"
      >
        <div class="chart-wrapper">
          <elevator-bar-chart @showchart4="showchart4" />
        </div>
      </el-col>

      <el-col
        v-loading="loading5"
        :xs="24"
        :sm="24"
        :lg="12"
        element-loading-text="拼命加载中"
        element-loading-background="rgba(255, 255, 255, 0.8)"
      >
        <div class="chart-wrapper">
          <constrcuture-pie-chart @showchart5="showchart5" />
        </div>
      </el-col>

      <el-col
        v-loading="loading6"
        :xs="24"
        :sm="24"
        :lg="12"
        element-loading-text="拼命加载中"
        element-loading-background="rgba(255, 255, 255, 0.8)"
      >
        <div class="chart-wrapper">
          <purpose-pie-chart @showchart6="showchart6" />
        </div>
      </el-col>
    </el-row>

    <el-row :gutter="32">
      <el-col
        v-loading="loading7"
        :xs="24"
        :sm="24"
        :lg="12"
        element-loading-text="拼命加载中"
        element-loading-background="rgba(255, 255, 255, 0.8)"
      >
        <div class="chart-wrapper">
          <orientatation-pie-chart @showchart7="showchart7" />
        </div>
      </el-col>

      <el-col
        v-loading="loading8"
        :xs="24"
        :sm="24"
        :lg="12"
        element-loading-text="拼命加载中"
        element-loading-background="rgba(255, 255, 255, 0.8)"
      >
        <div class="chart-wrapper">
          <floor-bar-chart @showchart8="showchart8" />
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
      loading1: true,
      loading2: true,
      loading3: true,
      loading4: true,
      loading5: true,
      loading6: true,
      loading7: true,
      loading8: true
    }
  },
  methods: {
    // TODO:面积图表
    showchart1(val) {
      this.loading1 = val
    },
    showchart2(val) {
      this.loading2 = val
    },
    showchart3(val) {
      this.loading3 = val
    },
    showchart4(val) {
      this.loading4 = val
    },
    showchart5(val) {
      this.loading5 = val
    },
    showchart6(val) {
      this.loading6 = val
    },
    showchart7(val) {
      this.loading7 = val
    },
    showchart8(val) {
      this.loading8 = val
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

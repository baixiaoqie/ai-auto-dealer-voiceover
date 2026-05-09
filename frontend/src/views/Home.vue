<template>
  <div class="home">
    <el-row :gutter="20" class="welcome-section">
      <el-col :span="24">
        <el-card class="welcome-card">
          <h2>👋 欢迎使用 AI 智能口播系统</h2>
          <p>第一阶段：抖音文案解析与改写</p>
          <div class="status-check">
            <el-tag :type="backendStatus === 'ok' ? 'success' : backendStatus === 'checking' ? 'warning' : 'danger'">
              后端状态: {{ statusText[backendStatus] || statusText.error }}
            </el-tag>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="20" class="features-section">
      <el-col :xs="24" :sm="12" :md="8" v-for="(feature, index) in features" :key="index">
        <el-card class="feature-card" shadow="hover">
          <div class="feature-icon">{{ feature.icon }}</div>
          <h3>{{ feature.title }}</h3>
          <p>{{ feature.description }}</p>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="20" class="tech-section">
      <el-col :span="24">
        <el-card>
          <template #header>
            <div class="card-header">
              <span>🛠️ 技术栈</span>
            </div>
          </template>
          <el-tag type="primary" style="margin: 5px;">Vue 3</el-tag>
          <el-tag type="success" style="margin: 5px;">FastAPI</el-tag>
          <el-tag type="info" style="margin: 5px;">Element Plus</el-tag>
          <el-tag type="warning" style="margin: 5px;">Playwright</el-tag>
          <el-tag type="danger" style="margin: 5px;">OpenAI</el-tag>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import api from '@/utils/api'

const backendStatus = ref('checking')

const statusText = {
  ok: '✅ 运行中',
  checking: '⏳ 检测中...',
  error: '❌ 未连接',
}

const features = ref([
  {
    icon: '🎬',
    title: '抖音文案解析',
    description: '自动从抖音视频提取标题、字幕、描述等文案'
  },
  {
    icon: '✨',
    title: 'AI 智能改写',
    description: '基于大模型，多种风格一键改写文案'
  },
  {
    icon: '📊',
    title: '批量处理',
    description: '支持批量导入，高效处理多个视频'
  }
])

let timer = null

const checkBackend = async () => {
  try {
    const response = await api.get('/api/v1/health')
    backendStatus.value = response.data.status
  } catch {
    backendStatus.value = 'error'
  }
}

onMounted(() => {
  checkBackend()
  timer = setInterval(checkBackend, 30000)
})

onUnmounted(() => {
  if (timer) {
    clearInterval(timer)
  }
})
</script>

<style scoped>
.home {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.welcome-section {
  margin-bottom: 30px;
}

.welcome-card {
  text-align: center;
  padding: 40px 20px;
}

.welcome-card h2 {
  margin: 0 0 10px 0;
  color: #303133;
}

.welcome-card p {
  color: #909399;
  font-size: 16px;
}

.status-check {
  margin-top: 20px;
}

.features-section {
  margin-bottom: 30px;
}

.feature-card {
  text-align: center;
  padding: 30px 20px;
  margin-bottom: 20px;
}

.feature-icon {
  font-size: 48px;
  margin-bottom: 15px;
}

.feature-card h3 {
  margin: 10px 0;
  color: #303133;
}

.feature-card p {
  color: #606266;
  margin: 0;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: bold;
}
</style>

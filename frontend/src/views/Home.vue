<template>
  <div class="home">
    <div class="hero-section">
      <div class="hero-content">
        <div class="hero-accent">
          <div class="accent-dot"></div>
          <span class="accent-label">STAGE ONE</span>
        </div>
        <h2 class="hero-title">
          <span class="title-line">抖音文案</span>
          <span class="title-line highlight">解析与改写</span>
        </h2>
        <p class="hero-description">
          专为汽车经销商打造的 AI 智能口播系统<br>
          让您的视频文案闪耀卓越品质
        </p>
        
        <div class="status-container">
          <div class="status-label">系统状态</div>
          <div class="status-indicator" :class="backendStatus">
            <span class="status-dot"></span>
            <span class="status-text">{{ statusText[backendStatus] || statusText.error }}</span>
          </div>
        </div>
      </div>
      
      <div class="hero-decoration">
        <div class="decoration-circle"></div>
        <div class="decoration-grid"></div>
      </div>
    </div>
    
    <div class="features-section">
      <div class="section-header">
        <span class="section-label">核心功能</span>
        <h3 class="section-title">FEATURES</h3>
      </div>
      
      <div class="features-grid">
        <div class="feature-card" v-for="(feature, index) in features" :key="index">
          <div class="feature-number">{{ String(index + 1).padStart(2, '0') }}</div>
          <div class="feature-content">
            <div class="feature-icon">{{ feature.icon }}</div>
            <h4 class="feature-title">{{ feature.title }}</h4>
            <p class="feature-description">{{ feature.description }}</p>
          </div>
          <div class="feature-border"></div>
        </div>
      </div>
    </div>
    
    <div class="tech-section">
      <div class="tech-container">
        <div class="tech-header">
          <span class="tech-label">技术栈</span>
          <h3 class="tech-title">TECHNOLOGY</h3>
        </div>
        <div class="tech-tags">
          <span class="tech-tag" v-for="(tech, index) in techStack" :key="index">{{ tech }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import api from '@/utils/api'

const backendStatus = ref('checking')

const statusText = {
  ok: '运行中',
  checking: '检测中...',
  error: '未连接',
}

const features = ref([
  {
    icon: '🎬',
    title: '抖音文案解析',
    description: '自动从抖音视频提取标题、字幕、描述等文案信息'
  },
  {
    icon: '✨',
    title: 'AI 智能改写',
    description: '基于大模型，多种风格一键改写，打造专属口播文案'
  },
  {
    icon: '📊',
    title: '批量处理',
    description: '支持批量导入，高效处理多个视频，提升工作效率'
  }
])

const techStack = ['Vue 3', 'FastAPI', 'Element Plus', 'Playwright', 'OpenAI']

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
  max-width: 1400px;
  margin: 0 auto;
}

.hero-section {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 80px;
  margin-bottom: 120px;
  align-items: center;
}

.hero-content {
  position: relative;
  z-index: 1;
}

.hero-accent {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 32px;
}

.accent-dot {
  width: 8px;
  height: 8px;
  background: var(--accent-gold);
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.6; transform: scale(1.2); }
}

.accent-label {
  font-family: 'Montserrat', sans-serif;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 4px;
  color: var(--accent-gold);
  text-transform: uppercase;
}

.hero-title {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 0 0 32px 0;
}

.title-line {
  font-family: 'Playfair Display', 'Noto Serif SC', serif;
  font-size: 64px;
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: 2px;
  color: var(--text-primary);
}

.title-line.highlight {
  background: linear-gradient(135deg, var(--accent-gold) 0%, var(--accent-gold-light) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-description {
  font-family: 'Noto Serif SC', serif;
  font-size: 18px;
  line-height: 1.8;
  color: var(--text-secondary);
  margin: 0 0 48px 0;
}

.status-container {
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 24px 32px;
  background: var(--primary-medium);
  border: 1px solid var(--border-subtle);
  border-radius: 4px;
}

.status-label {
  font-family: 'Montserrat', sans-serif;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 2px;
  color: var(--text-muted);
  text-transform: uppercase;
}

.status-indicator {
  display: flex;
  align-items: center;
  gap: 12px;
}

.status-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--text-muted);
}

.status-indicator.ok .status-dot {
  background: #4ade80;
  box-shadow: 0 0 12px rgba(74, 222, 128, 0.4);
}

.status-indicator.checking .status-dot {
  background: #fbbf24;
  animation: pulse 1s ease-in-out infinite;
}

.status-indicator.error .status-dot {
  background: #f87171;
}

.status-text {
  font-family: 'Montserrat', sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: var(--text-primary);
}

.hero-decoration {
  position: relative;
  height: 500px;
}

.decoration-circle {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 320px;
  height: 320px;
  border: 1px solid var(--border-subtle);
  border-radius: 50%;
}

.decoration-circle::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 220px;
  height: 220px;
  border: 1px solid var(--accent-gold);
  border-radius: 50%;
  opacity: 0.3;
}

.decoration-grid {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 200px;
  height: 200px;
  background-image: 
    linear-gradient(var(--border-subtle) 1px, transparent 1px),
    linear-gradient(90deg, var(--border-subtle) 1px, transparent 1px);
  background-size: 40px 40px;
  opacity: 0.3;
}

.features-section {
  margin-bottom: 120px;
}

.section-header {
  text-align: center;
  margin-bottom: 80px;
}

.section-label {
  display: inline-block;
  font-family: 'Montserrat', sans-serif;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 4px;
  color: var(--accent-gold);
  text-transform: uppercase;
  margin-bottom: 16px;
}

.section-title {
  font-family: 'Playfair Display', serif;
  font-size: 48px;
  font-weight: 700;
  letter-spacing: 8px;
  color: var(--text-primary);
  margin: 0;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}

.feature-card {
  position: relative;
  padding: 48px 40px;
  background: var(--primary-medium);
  border: 1px solid var(--border-subtle);
  transition: all 0.4s ease;
  overflow: hidden;
}

.feature-card:hover {
  transform: translateY(-8px);
  border-color: var(--accent-gold);
  box-shadow: var(--shadow-glow);
}

.feature-number {
  position: absolute;
  top: 24px;
  right: 24px;
  font-family: 'Montserrat', sans-serif;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 2px;
  color: var(--text-muted);
}

.feature-content {
  position: relative;
  z-index: 1;
}

.feature-icon {
  font-size: 48px;
  margin-bottom: 24px;
}

.feature-title {
  font-family: 'Playfair Display', 'Noto Serif SC', serif;
  font-size: 24px;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0 0 12px 0;
}

.feature-description {
  font-family: 'Noto Serif SC', serif;
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-secondary);
  margin: 0;
}

.feature-border {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background: linear-gradient(90deg, transparent 0%, var(--accent-gold) 50%, transparent 100%);
  opacity: 0;
  transition: opacity 0.4s ease;
}

.feature-card:hover .feature-border {
  opacity: 1;
}

.tech-section {
  padding: 60px 0;
  border-top: 1px solid var(--border-subtle);
  border-bottom: 1px solid var(--border-subtle);
}

.tech-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 60px;
}

.tech-header {
  flex-shrink: 0;
}

.tech-label {
  display: block;
  font-family: 'Montserrat', sans-serif;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 4px;
  color: var(--accent-gold);
  text-transform: uppercase;
  margin-bottom: 12px;
}

.tech-title {
  font-family: 'Playfair Display', serif;
  font-size: 36px;
  font-weight: 700;
  letter-spacing: 6px;
  color: var(--text-primary);
  margin: 0;
}

.tech-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  justify-content: flex-end;
}

.tech-tag {
  padding: 12px 28px;
  background: var(--primary-light);
  border: 1px solid var(--border-subtle);
  font-family: 'Montserrat', sans-serif;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 1px;
  color: var(--text-secondary);
  transition: all 0.3s ease;
}

.tech-tag:hover {
  border-color: var(--accent-gold);
  color: var(--accent-gold);
}

@media (max-width: 1024px) {
  .hero-section {
    grid-template-columns: 1fr;
    gap: 60px;
  }
  
  .hero-decoration {
    display: none;
  }
  
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .tech-container {
    flex-direction: column;
    text-align: center;
  }
  
  .tech-tags {
    justify-content: center;
  }
}

@media (max-width: 768px) {
  .title-line {
    font-size: 42px;
  }
  
  .section-title {
    font-size: 32px;
  }
}
</style>

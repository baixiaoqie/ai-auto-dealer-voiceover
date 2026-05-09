# 🚗 AI智能口播系统

> 面向汽车经销商的一键口播视频生成系统

## 项目简介

基于会议纪要开发，第一阶段实现抖音文案解析与AI改写功能。

## 📋 开发路线

| 阶段 | 功能 | 状态 |
|------|------|------|
| **第一阶段** | 抖音文案解析与改写 | 🏗️ 框架搭建中 |
| **第二阶段** | 语音合成与视频合成 | ⏳ 待开发 |
| **第三阶段** | 对口型与字幕生成 | ⏳ 待开发 |
| **第四阶段** | 视频混剪与多镜头 | ⏳ 待开发 |
| **第五阶段** | 商业化与全平台 | ⏳ 待开发 |

## 🛠️ 技术栈

### 后端
- **框架**: FastAPI
- **数据库**: SQLite → PostgreSQL
- **任务队列**: Celery + Redis
- **大模型**: OpenAI / 智谱AI
- **爬虫**: Playwright

### 前端
- **框架**: Vue 3
- **UI**: Element Plus
- **路由**: Vue Router
- **状态**: Pinia
- **构建**: Vite

## 📁 项目结构

```
ai-voice-broadcast/
├── backend/          # 后端服务
├── frontend/         # 前端应用
├── docs/             # 文档
├── scripts/          # 脚本
├── 第一阶段技术方案.md
├── 第二阶段技术方案.md
├── 第三阶段技术方案.md
├── 第四阶段技术方案.md
├── 第五阶段技术方案.md
└── README.md
```

## 🚀 快速开始

### 后端启动

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

后端文档: http://localhost:8000/docs

### 前端启动

```bash
cd frontend
npm install
npm run dev
```

前端访问: http://localhost:5173

## 📝 开发规范

### Git 提交规范

- `feat`: 新功能
- `fix`: 修复
- `docs`: 文档
- `style`: 格式
- `refactor`: 重构
- `test`: 测试
- `chore`: 构建/工具

### 代码风格

- **Python**: Black + Ruff
- **Vue**: ESLint + Prettier

## 🔧 验证框架

框架搭建完成后，请按以下步骤验证：

1. 启动后端服务，访问 http://localhost:8000/docs
2. 测试 `/api/v1/health` 接口
3. 启动前端服务，访问 http://localhost:5173
4. 检查前后端连接状态显示

## 📄 相关文档

- 各阶段技术方案: `*阶段技术方案.md`
- 会议纪要: `智能纪要*.docx`

## 🤝 开发团队

按会议纪要执行开发。

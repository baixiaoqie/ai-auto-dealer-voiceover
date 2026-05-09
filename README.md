# AI 智能口播系统

专为汽车经销商打造的 AI 驱动视频创作平台，提供从文案解析到多平台发布的全流程解决方案。

## 项目简介

本系统通过 AI 技术帮助汽车经销商快速生成高质量口播视频，降低视频创作门槛，提升营销效率。

## 功能特性

### 🎬 第一阶段（MVP）- 抖音文案解析与改写
- 抖音视频文案自动提取
- AI 智能文案改写（多种风格）
- 批量处理支持
- 标题和话题自动生成

### 🎤 第二阶段 - 语音合成与视频基础合成
- 多音色语音合成
- 背景音乐混合
- 视频素材与音频合成
- 音量调节与音效处理

### 🎭 第三阶段 - 对口型与字幕自动生成
- AI 口型同步
- 自动字幕生成与编辑
- 视频封面智能生成
- 字幕样式自定义

### ✂️ 第四阶段 - 视频混剪与多镜头生成
- 素材库智能管理
- 模板化智能混剪
- 爆款视频分析与二创
- AI 故事板生成

### 🚀 第五阶段 - 商业化与全平台发布
- 一键多平台发布（抖音、视频号、小红书、快手）
- API 中转服务
- 会员订阅体系
- 数据分析面板

## 技术栈

### 前端
- **框架**: Vue 3 + Composition API
- **UI 组件库**: Element Plus
- **构建工具**: Vite
- **状态管理**: Pinia
- **路由**: Vue Router

### 后端
- **Web 框架**: FastAPI
- **任务队列**: Celery + Redis
- **爬虫工具**: Playwright
- **视频处理**: FFmpeg
- **数据库**: SQLite（MVP）→ PostgreSQL

### AI 服务
- **大模型**: OpenAI GPT / Claude / 国产大模型
- **语音合成**: Minimax / 阿里云TTS / 百度TTS
- **对口型**: Wav2Lip / infinitalk
- **语音识别**: OpenAI Whisper

## 快速开始

### 环境要求
- Python 3.10+
- Node.js 18+
- FFmpeg

### 后端启动

```bash
# 进入后端目录
cd backend

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件填入配置

# 启动服务
python run.py
```

后端服务将在 http://localhost:8000 启动，API 文档访问 http://localhost:8000/docs

### 前端启动

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端服务将在 http://localhost:5173 启动

## 项目结构

```
.
├── backend/                 # 后端服务
│   ├── app/
│   │   ├── api/            # API 路由
│   │   ├── core/           # 核心配置
│   │   ├── schemas/        # Pydantic 模型
│   │   ├── services/       # 业务逻辑
│   │   └── main.py         # 应用入口
│   ├── tests/              # 测试
│   └── requirements.txt
├── frontend/               # 前端应用
│   ├── src/
│   │   ├── components/     # 组件
│   │   ├── views/          # 页面
│   │   ├── router/         # 路由
│   │   ├── stores/         # 状态管理
│   │   ├── styles/         # 样式
│   │   └── main.js         # 入口
│   └── package.json
├── docs/                   # 技术方案文档
└── README.md
```

## 开发计划

- ✅ **第一阶段（24天）**: 抖音文案解析与改写
- ⏳ **第二阶段（16天）**: 语音合成与视频基础合成
- ⏳ **第三阶段（16天）**: 对口型与字幕自动生成
- ⏳ **第四阶段（18天）**: 视频混剪与多镜头生成
- ⏳ **第五阶段（20天）**: 商业化与全平台发布

详细技术方案请查看 `docs/` 目录下的各阶段技术文档。

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

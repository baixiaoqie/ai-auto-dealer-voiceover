# AI智能口播 - 前端

## 技术栈

- **框架**: Vue 3
- **UI组件**: Element Plus
- **路由**: Vue Router
- **状态管理**: Pinia
- **HTTP客户端**: Axios
- **构建工具**: Vite

## 项目结构

```
frontend/
├── src/
│   ├── components/    # 组件
│   ├── views/         # 页面
│   ├── stores/        # Pinia状态
│   ├── router/        # 路由
│   ├── utils/         # 工具
│   ├── assets/        # 静态资源
│   ├── App.vue        # 根组件
│   └── main.js        # 入口
├── public/            # 公共资源
├── index.html         # HTML入口
├── vite.config.js     # Vite配置
└── package.json       # 依赖配置
```

## 快速开始

### 1. 安装依赖

```bash
npm install
```

### 2. 启动开发服务器

```bash
npm run dev
```

访问 http://localhost:5173

### 3. 构建生产版本

```bash
npm run build
```

### 4. 预览生产构建

```bash
npm run preview
```

## 开发规范

- 使用 Composition API (`<script setup>`)
- 组件命名: PascalCase
- 使用 Type Hints (可选)
- ESLint 代码检查

## API 配置

通过 Vite 代理转发到后端：
- 开发环境: `/api` → `http://localhost:8000`

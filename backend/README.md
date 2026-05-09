# AI智能口播 - 后端服务

## 技术栈

- **框架**: FastAPI
- **数据库**: SQLite (MVP) → PostgreSQL (后期)
- **任务队列**: Celery + Redis
- **大模型**: OpenAI / 智谱AI
- **爬虫**: Playwright
- **日志**: Loguru

## 项目结构

```
backend/
├── app/
│   ├── api/           # API路由
│   ├── core/          # 核心配置
│   ├── models/        # 数据库模型
│   ├── schemas/       # Pydantic模式
│   ├── services/      # 业务逻辑
│   ├── utils/         # 工具函数
│   └── main.py        # 应用入口
├── tests/             # 测试
├── alembic/           # 数据库迁移
├── logs/              # 日志文件
├── .env               # 环境变量
├── requirements.txt   # 依赖
└── run.py             # 启动脚本
```

## 快速开始

### 1. 创建虚拟环境

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

复制 `.env.example` 为 `.env` 并填入配置：

```bash
cp .env.example .env
# 编辑 .env 文件
```

### 4. 启动服务

```bash
python run.py
# 或
uvicorn app.main:app --reload
```

### 5. 访问文档

- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

## 开发规范

### 代码风格

- 使用 `black` 格式化 Python 代码
- 使用 `ruff` 进行代码检查
- 类型提示: 使用 Type Hints

### Git 提交规范

- `feat`: 新功能
- `fix`: 修复
- `docs`: 文档
- `style`: 格式
- `refactor`: 重构
- `test`: 测试
- `chore`: 构建/工具

## 模块占位说明

- `api/`: 按功能模块划分子路由
- `services/`: 核心业务逻辑（文案解析、改写等）
- `models/`: SQLAlchemy 数据库模型
- `schemas/`: Pydantic 请求/响应模式

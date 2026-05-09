#!/usr/bin/env python3
"""
后端框架验证脚本
检查核心模块是否能正常导入
"""

import sys
from pathlib import Path

# 添加后端目录到路径
backend_path = Path(__file__).parent.parent / 'backend'
sys.path.insert(0, str(backend_path))

print("=" * 60)
print("AI智能口播 - 后端框架验证")
print("=" * 60)

tests = [
    ("配置模块", "from app.core.config import settings"),
    ("数据库模块", "from app.core.database import Base, engine"),
    ("日志模块", "from app.core import logger"),
    ("FastAPI应用", "from app.main import app"),
    ("健康检查路由", "from app.api.health import router"),
]

passed = 0
failed = 0

for name, import_stmt in tests:
    try:
        print(f"\n[检查: {name}")
        exec(import_stmt)
        print(f"[OK] {name} - 通过")
        passed += 1
    except Exception as e:
        print(f"[FAIL] {name} - 失败: {e}")
        failed += 1

print("\n" + "=" * 60)
print(f"验证结果: {passed}/{len(tests)} 通过")
if failed == 0:
    print("所有测试通过！框架搭建成功！")
else:
    print(f"有 {failed} 个测试失败，请检查")
print("=" * 60)

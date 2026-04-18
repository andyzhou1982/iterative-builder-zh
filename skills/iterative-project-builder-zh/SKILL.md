---
name: iterative-project-builder-zh
description: 从需求文档循序渐进构建生产级项目。适用于：(1) 创建教程式多阶段项目，(2) 将复杂系统拆分为可学习阶段，(3) 从 MVP 构建到生产系统，(4) 用户请求"循序渐进"或"分阶段"项目结构，(5) 需要独立可运行的增量阶段。将需求转化为分阶段实现，每阶段基于前一阶段构建。
---

# 循序渐进项目构建器

通过增量、可学习的阶段构建生产级系统。

## 核心方法论

```
需求文档
    |
    v
[阶段规划]
    |
+---+---+
|   |   |
Day1 Day2 ... DayN
MVP  +功能  生产级
|
v
每天：独立 + 可运行 + 有文档
```

## 第一阶段：分析需求

### 1.1 提取核心模块
从需求文档中识别：
- **核心功能**（MVP 必须有）
- **增强功能**（锦上添花）
- **生产功能**（部署、监控、安全）

### 1.2 技术栈决策
实现之前，提出技术栈选项让用户选择：
```
| 组件 | 选项 A | 选项 B | 理由 |
|------|--------|--------|------|
| 后端 | FastAPI | Flask | ... |
| 前端 | React | Vue | ... |
| 数据库 | PostgreSQL | MongoDB | ... |
```

### 1.3 创建规划文件
运行 `scripts/init_planning.py` 创建：
- `task_plan.md` - 阶段、决策、进度
- `findings.md` - 研究、技术笔记
- `progress.md` - 会话日志、测试结果

## 第二阶段：规划天数

### 2.1 天数分解策略
参见 [references/stage-patterns.md](references/stage-patterns.md) 了解常见模式。

**典型分解**：
| 天数 | 主题 | 目标 |
|------|------|------|
| Day 1 | MVP | 核心流程：输入 → 处理 → 输出 |
| Day 2 | 增强1 | 添加功能 X |
| Day 3 | 增强2 | 添加功能 Y |
| Day N | 生产 | 部署、监控、优化 |

### 2.2 阶段独立性规则
每个阶段必须：
- 有自己的目录（`day1/`、`day2/`、...）
- 无需其他阶段即可完整运行
- 包含完整的前端和后端
- 有自己的 README 和文档

### 2.3 记录到 task_plan.md
```markdown
## 阶段概览

### Day 1: [主题]
- [ ] 功能 A
- [ ] 功能 B
- **状态:** pending
- **目标:** [本阶段达成什么]

### Day 2: [主题]
...
```

## 第三阶段：实现 Day 1（MVP）

### 3.1 目录结构
```
day1/
├── backend/
│   ├── src/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── routers/
│   │   ├── services/
│   │   └── models/
│   └── test/
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── components/
│   │   └── api/
│   └── package.json
├── readme.md
└── readme_cn.md
```

### 3.2 MVP 原则
- **最小但完整** - 核心流程端到端可用
- **不偷工减料** - 正确的错误处理、验证
- **清晰架构** - 可扩展的模式
- **双语注释** - 见 [references/bilingual-comments.md](references/bilingual-comments.md)

### 3.3 验证 Day 1
```bash
# 后端编译检查
cd day1/backend && python -m py_compile src/*.py

# 前端构建检查
cd day1/frontend && npm run build
```

## 第四阶段：实现后续天数

### 4.1 复制前一天
```bash
cp -r day1 day2
```

### 4.2 增量添加功能
每天添加一个主要功能领域：
- Day 2: 增强预处理
- Day 3: 优化检索
- Day 4: 改进生成
- 等等

### 4.3 记录变更
为每天创建 `CHANGES.md`：
```markdown
# Day N 变更

## 新增功能
- 功能 X: 描述

## 修改文件
- `file.py`: 添加了函数 Y

## 新增依赖
- `library`: 用途
```

### 4.4 更新规划文件
每天完成后：
1. 更新 `task_plan.md` - 标记完成
2. 更新 `findings.md` - 记录学习
3. 更新 `progress.md` - 记录操作

## 第五阶段：最终天（生产级）

### 5.1 生产检查清单
- [ ] 缓存（Redis/内存）
- [ ] 错误处理与重试
- [ ] 速率限制
- [ ] 性能指标
- [ ] Docker 配置
- [ ] 健康检查
- [ ] 完整文档

### 5.2 Docker 配置
```
docker-compose.yml
├── postgres（带扩展）
├── redis（缓存）
├── backend（FastAPI）
└── frontend（nginx）
```

### 5.3 文档
- 中英文 README
- API 文档（自动生成）
- 架构图
- 部署指南

## 资源

### scripts/
- `init_planning.py` - 初始化规划文件

### references/
- `stage-patterns.md` - 常见阶段划分模式
- `bilingual-comments.md` - 注释格式规范

### assets/
- `task_plan.md` - 阶段规划模板
- `findings.md` - 研究笔记模板
- `progress.md` - 会话日志模板

## 快速参考

| 任务 | 命令 |
|------|------|
| 初始化规划文件 | `python scripts/init_planning.py` |
| 开始 Day N | 复制 `day(N-1)` 到 `dayN` |
| 验证阶段 | 构建检查 + 手动测试 |
| 完成阶段 | 更新所有规划文件 |

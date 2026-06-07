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
    v
[Git 仓库初始化]
    |
+---+---+
|   |   |
day1 day2 ... dayN (分支)
MVP  +功能  生产级
|
v
每个分支：独立 + 可运行 + 有提交记录
```

**通过 Git 分支管理每个阶段，单一目录结构，无需 dayN 子目录。**

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
- 独立的 Git 分支（`day1`、`day2`、...）
- 切换到该分支后无需其他阶段即可完整运行
- 包含完整的前端和后端
- 有清晰的提交记录和说明

**查看某阶段代码**：`git checkout day<N>`
**继续开发某阶段**：`git checkout day<N>` 后在当前分支修改

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

### 3.1 初始化 Git 并创建 day1 分支

```bash
# 初始化 Git 仓库
git init

# 创建并切换到 day1 分支
git checkout -b day1
```

### 3.2 项目目录结构
```
project/
├── .git/
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
├── task_plan.md
├── findings.md
├── progress.md
├── README.md
└── README_CN.md
```

### 3.2 MVP 原则
- **最小但完整** - 核心流程端到端可用
- **不偷工减料** - 正确的错误处理、验证
- **清晰架构** - 可扩展的模式
- **中文注释** - 代码注释统一使用中文

### 3.3 验证 Day 1
```bash
# 后端编译检查
cd backend && python -m py_compile src/*.py

# 前端构建检查
cd frontend && npm run build

# 提交 Day 1 代码
git add .
git commit -m "Day 1: MVP - 核心功能实现"
```

## 第四阶段：实现后续天数

### 4.1 基于前一天创建新分支
```bash
# 基于 day1 创建 day2 分支
git checkout -b day2 day1

# 或者基于当前分支（如果你已经在 day1 上）
git checkout -b day2
```

### 4.2 增量添加功能
每天添加一个主要功能领域：
- Day 2: 增强预处理
- Day 3: 优化检索
- Day 4: 改进生成
- 等等

### 4.3 双重变更记录

**方式一：CHANGES.md 文件**（人类可读摘要）
为每天更新 `CHANGES.md`：
```markdown
# Day N 变更

## 新增功能
- 功能 X: 描述

## 修改文件
- `file.py`: 添加了函数 Y

## 新增依赖
- `library`: 用途
```

**方式二：Git 提交记录**（技术细节）
```bash
git add .
git commit -m "Day N: <主题>"
```

**查看某阶段的变更**：
```bash
# 通过 Git 查看代码差异
git diff day1..day2

# 通过 CHANGES.md 查看变更摘要
cat CHANGES.md
```

### 4.4 更新规划文件
每天完成后：
1. 更新 `task_plan.md` - 标记完成
2. 更新 `findings.md` - 记录学习
3. 更新 `progress.md` - 记录操作
4. 提交到 Git：`git add task_plan.md findings.md progress.md CHANGES.md && git commit -m "Day N: 更新规划文件"`

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
注释格式规范已移除，统一使用中文注释

### assets/
- `task_plan.md` - 阶段规划模板
- `findings.md` - 研究笔记模板
- `progress.md` - 会话日志模板

## 快速参考

| 任务 | 命令 |
|------|------|
| 初始化规划文件 | `python scripts/init_planning.py` |
| 初始化 Git 仓库 | `git init && git checkout -b day1` |
| 开始 Day N | `git checkout -b day<N> day<N-1>` |
| 切换到某阶段查看 | `git checkout day<N>` |
| 查看阶段差异 | `git diff day<N-1>..day<N>` |
| 验证阶段 | 构建检查 + 手动测试 |
| 完成阶段 | 更新规划文件 + `git commit` |

## 分支管理最佳实践

### 分支命名
- `day1`, `day2`, `day3` ... - 主线阶段分支
- `day3-experiment-a` - 某阶段的实验性变体
- `day3-bugfix` - 某阶段的 bug 修复分支

### 跨阶段修复
如果发现 Day 2 的 bug 需要应用到 Day 3、Day 4：

```bash
# 在 day2 分支修复 bug
git checkout day2
# 修复代码...
git commit -m "Day 2: 修复 XXX bug"

# Cherry-pick 到后续阶段
git checkout day3
git cherry-pick day2

git checkout day4
git cherry-pick day2
```

### 查看演进历史
```bash
# 查看所有阶段分支
git branch -a

# 查看某阶段的提交历史
git log day3 --oneline --graph

# 比较两个阶段的代码差异
git diff day2..day3 --stat
```

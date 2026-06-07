---
name: iterative-builder-zh:build
description: 从需求描述循序渐进构建生产级项目。将复杂系统拆分为可学习的增量阶段，从 MVP 到生产级。用法：/iterative-builder-zh:build <需求描述>
argument-hint: <需求描述文本>
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
  - Agent
---

# 项目构建命令

你是一个循序渐进项目构建专家。用户提供了项目需求，你需要：

## 工作流程

### 第一步：分析需求

1. 从用户的需求描述中提取：
   - **核心功能**（MVP 必须有）
   - **增强功能**（锦上添花）
   - **生产功能**（部署、监控、安全）

2. 识别项目类型：
   - RAG 系统
   - Web 应用
   - API 服务
   - 数据管道
   - 其他

### 第二步：技术栈决策

**必须停下来询问用户**，使用 AskUserQuestion 工具展示技术栈选项：

```
| 组件 | 选项 A | 选项 B | 选项 C |
|------|--------|--------|--------|
| 后端 | [框架1] | [框架2] | [框架3] |
| 前端 | [框架1] | [框架2] | [框架3] |
| 数据库 | [数据库1] | [数据库2] | [数据库3] |
```

**重要**：
- 选项 C 必须是"其他（用户自定义）"
- 等待用户选择或输入自定义技术栈
- 如果用户说"你决定"，根据项目类型选择最佳方案

### 第三步：阶段规划

1. **加载 skill** - 自动激活 `iterative-project-builder-zh` skill 获取详细指导

2. **创建项目目录** - 在当前工作目录下创建项目文件夹（基于需求推断项目名称）

3. **初始化规划文件** - **必须运行 skill 中的初始化脚本创建，不得自行编写**：

   ```bash
   cd <项目目录> && python skills/iterative-project-builder-zh/scripts/init_planning.py <项目名称>
   ```

   脚本会自动创建：
   - `task_plan.md` - 阶段规划
   - `findings.md` - 研究笔记
   - `progress.md` - 进度日志

   **禁止**使用 Write/Edit 工具自行创建这三个文件，必须通过脚本生成。

4. **制定阶段计划**：
   | 天数 | 主题 | 目标 |
   |------|------|------|
   | Day 1 | MVP | 核心流程 |
   | Day 2 | 增强1 | 添加功能 |
   | ... | ... | ... |
   | Day N | 生产 | 部署就绪 |

### 第四步：逐日实现（Day 1 → Day N）

**每个 Day 都遵循以下循环：**

#### 4.1 实现当前 Day

按照 skill 中的方法论实现当前阶段：

**Day 1（首个阶段）**：
1. 初始化 Git 仓库（如果未初始化）
2. 创建并切换到 `day1` 分支：`git checkout -b day1`
3. 实现核心功能
4. 提交代码：`git add . && git commit -m "Day 1: MVP"`

**Day N+1（后续阶段）**：
1. 基于前一天创建新分支：`git checkout -b day<N+1> day<N>`
2. 在新分支上添加本阶段新功能
3. 确保端到端可用
4. 添加中文注释
5. 提交代码：`git add . && git commit -m "Day <N+1>: <主题>"`

#### 4.2 验证当前 Day

完成实现后执行验证：
```bash
# 后端编译检查
cd backend && python -m py_compile src/*.py

# 前端构建检查
cd frontend && npm run build
```

#### 4.3 更新规划文件

更新 task_plan.md、findings.md、progress.md 记录本阶段进度。

#### 4.4 询问是否进行代码审查

**每个 Day 完成后必须先询问是否进行代码审查**，使用 AskUserQuestion：

```json
{
  "questions": [{
    "question": "Day N [主题] 已完成并通过验证！是否对 Day N 的代码进行审查？",
    "header": "代码审查",
    "options": [
      {"label": "进行审查", "description": "对 Day N 执行代码审查，检查质量、安全、性能等问题"},
      {"label": "跳过审查", "description": "跳过审查，直接进入下一步"}
    ]
  }]
}
```

**如果用户选择审查**：使用 Agent 工具调用 `iterative-builder-zh:code-reviewer` agent 执行审查，以减轻主 agent 上下文负担。

```json
{
  "subagent_type": "iterative-builder-zh:code-reviewer",
  "prompt": "请对项目 <项目路径> 的 Day N 分支进行代码审查。先读取 task_plan.md、findings.md、progress.md 了解项目上下文，确保在 day<N> 分支上，然后对当前代码进行五维度审查。"
}
```

agent 会返回审查报告和修改建议。审查完成后再进入步骤 4.5。

**如果用户跳过**：直接进入步骤 4.5。

#### 4.5 询问用户是否继续下一个 Day

**必须使用 AskUserQuestion 询问用户**，不得自动开始下一个 Day：

```json
{
  "questions": [{
    "question": "是否继续开始 Day N+1: [下一阶段主题]？",
    "header": "继续构建",
    "options": [
      {"label": "继续 Day N+1", "description": "开始实现下一阶段: [下一阶段主题]"},
      {"label": "暂停", "description": "保存进度，稍后用 /iterative-builder-zh:continue 恢复"},
      {"label": "修改计划", "description": "调整后续阶段的规划后再继续"}
    ]
  }]
}
```

**等待用户响应后：**
- **继续** → 执行 Day N+1，回到步骤 4.1
- **暂停** → 更新 progress.md 记录停止点，结束本次会话
- **修改计划** → 询问用户如何调整，更新 task_plan.md 后继续

**重复此循环直到所有 Day 完成。**

## 使用 AskUserQuestion 示例

### 技术栈选择
```json
{
  "questions": [{
    "question": "请选择后端框架：",
    "header": "后端",
    "options": [
      {"label": "FastAPI (推荐)", "description": "现代异步框架，适合 API 服务"},
      {"label": "Flask", "description": "轻量级，灵活度高"},
      {"label": "其他", "description": "自定义输入你想要的框架"}
    ]
  }]
}
```

### 阶段完成确认
```json
{
  "questions": [{
    "question": "Day 2 数据预处理已完成并通过验证！是否对 Day 2 的代码进行审查？",
    "header": "代码审查",
    "options": [
      {"label": "进行审查", "description": "检查 Day 2 的代码质量、安全性等"},
      {"label": "跳过审查", "description": "跳过审查，继续下一步"}
    ]
  }]
}
```

### 继续下一个 Day
```json
{
  "questions": [{
    "question": "是否继续开始 Day 3: 检索优化？",
    "header": "继续构建",
    "options": [
      {"label": "继续 Day 3", "description": "开始实现检索优化"},
      {"label": "暂停", "description": "保存进度，稍后恢复"},
      {"label": "修改计划", "description": "调整后续阶段规划"}
    ]
  }]
}
```

## 注意事项

- 每个阶段必须独立可运行
- 代码注释使用中文
- 在每个阶段完成后验证构建
- 更新规划文件记录进度
- **每个 Day 完成后必须询问用户，不得自动进入下一个 Day**

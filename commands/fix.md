---
name: iterative-builder-zh:fix
description: 报告并修复项目构建过程中的 bug。会自动分析影响范围，判断其他阶段是否需要同步修改。用法：/iterative-builder-zh:fix <bug描述>
argument-hint: <bug描述或问题现象>
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
---

# Bug 修复命令

报告并修复项目构建过程中的 bug。

## 执行步骤

### 第一步：验证项目上下文

检查当前目录是否存在规划文件：`task_plan.md`、`findings.md`、`progress.md`

**如果不存在**：
> 请在项目目录中运行此命令。

### 第二步：确认 Bug 描述和分支

向用户确认 Bug 信息并检查当前分支：

```
## Bug 报告确认

**问题描述**: [用户描述]
**当前分支**: [git branch --show-current]

**请补充以下信息（可选）**：
1. 这个 bug 在哪个阶段（Day X）被发现？
2. 需要切换到哪个分支修复？
```

**如果不在正确分支**，询问用户是否切换：`git checkout day<X>`

```
## Bug 报告确认

**问题描述**: [用户描述]

**请补充以下信息（可选）**：
1. 这个 bug 在哪个阶段（Day X）被发现？
2. 期望行为是什么？
3. 实际发生了什么？
4. 有错误信息吗？

回复"确认"开始分析。
```

### 第三步：调用 Bug Fixer Agent

**使用 Agent 工具调用** `iterative-builder-zh:bug-fixer`：
- prompt: 包含完整的 bug 描述和项目上下文

Agent 会返回：
- Bug 分析和定位
- 影响范围分析（是否影响其他分支）
- 修复方案
- Cherry-pick 建议（跨分支同步）

### 第四步：执行修复

根据 agent 返回的方案，询问用户是否批准执行。

## 使用示例

```bash
/fix Day 2 的 API 返回格式和前端期望不一致
/fix 文档上传后分块数量总是 0
/fix 搜索响应时间超过 10 秒
/fix 数据库索引缺失导致查询慢
```

## 关键约束

- ✅ **必须在项目目录中运行**
- ✅ **修复逻辑由 bug-fixer agent 执行**
- ✅ **跨分支修复使用 git cherry-pick**

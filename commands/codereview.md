---
name: iterative-builder-zh:codereview
description: 对项目某个阶段的代码进行全面审查，包括代码质量、架构、安全、性能和可维护性，并分析修改是否影响其他阶段。用法：/iterative-builder-zh:codereview [Day编号]
argument-hint: "[Day编号，如 Day2，默认审查最近完成的 Day]"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
---

# 代码审查命令

对迭代项目的某个阶段进行代码审查。

## 执行步骤

### 第一步：验证项目上下文

检查当前目录是否存在规划文件：`task_plan.md`、`findings.md`、`progress.md`

**如果不存在**：
> 请在项目目录中运行此命令。

### 第二步：确定审查目标

1. 如果用户指定了 Day 编号，审查该分支
2. 如果未指定，从 progress.md 中找到最近完成的 Day
3. **切换到对应分支**：`git checkout day<N>`
4. 向用户确认：
   ```
   将对 Day N: [主题] 进行代码审查
   当前分支: day<N>
   ```

### 第三步：调用 Code Reviewer Agent

**使用 Agent 工具调用** `iterative-builder-zh:code-reviewer`：
- prompt: 包含审查目标和项目上下文

Agent 会执行五维度审查：
- 代码质量、架构设计、安全性、性能、可维护性

Agent 返回：
- 审查报告（评分、问题列表）
- 修改建议
- 跨阶段影响分析

### 第四步：询问是否修改

使用 AskUserQuestion 询问用户：

```json
{
  "questions": [{
    "question": "审查发现 X 个问题（Y 个严重）。是否进行修改？",
    "header": "审查结果",
    "options": [
      {"label": "全部修复", "description": "修复所有严重问题和建议"},
      {"label": "只修严重的", "description": "只修复 🔴 严重问题"},
      {"label": "暂不修改", "description": "记录问题，稍后处理"}
    ]
  }]
}
```

### 第五步：跨阶段影响处理

如果有跨阶段影响，询问用户是否同步其他分支。

## 使用示例

```bash
# 审查最近完成的 Day
/iterative-builder-zh:codereview

# 审查指定 Day
/iterative-builder-zh:codereview Day2
```

## 关键约束

- ✅ **必须在项目目录中运行**
- ✅ **审查逻辑由 code-reviewer agent 执行**
- ✅ **跨分支修改使用 git cherry-pick**

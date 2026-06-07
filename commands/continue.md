---
name: iterative-builder-zh:continue
description: 恢复中断的项目构建会话。读取 task_plan.md、findings.md、progress.md 恢复上下文，继续完成项目。用法：/iterative-builder-zh:continue
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
---

# 继续项目构建命令

恢复中断的循序渐进项目构建会话。

## 执行步骤

### 第一步：验证规划文件

检查当前目录是否存在：
- `task_plan.md`
- `findings.md`
- `progress.md`

**如果不存在**，提示用户：
> 未找到项目规划文件。请确保在项目目录中运行此命令。

### 第二步：读取并提取上下文

读取三个规划文件，提取：
- 项目名称、当前阶段、技术栈
- 已完成/进行中/待完成的阶段
- 上次停止点

### 第三步：5 问重启检查（必须）

向用户展示项目恢复摘要：

```
## 项目恢复摘要

**项目名称**: [名称]
**当前阶段**: [阶段]
**技术栈**: [技术栈]
**已完成**: Day X
**进行中**: Day Y
**待完成**: Day Z, ...
**上次停止点**: [从 progress.md 提取]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

请确认以上信息是否正确？
```

### 第四步：继续构建

用户确认后：

1. **加载 skill** - 激活 `iterative-project-builder-zh` skill
2. **切换 Git 分支**：
   - 有 in_progress → `git checkout day<N>`
   - 需要开始新阶段 → `git checkout -b day<N+1> day<N>`
3. **继续实现** - 按 SKILL.md 中的详细方法论
4. **更新 progress.md** - 记录恢复会话

## 关键约束

- ✅ **必须在项目目录中运行**
- ✅ **必须执行 5 问重启检查**
- ✅ **详细实现方法参考 SKILL.md**

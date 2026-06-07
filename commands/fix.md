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

在迭代项目构建过程中报告并修复 bug，同时分析对其他阶段的影响。

## 执行步骤

### 第一步：确认项目上下文

1. 检查当前目录或父目录中是否存在规划文件：
   - `task_plan.md`
   - `findings.md`
   - `progress.md`

2. 如果不在项目目录，提示用户：
   > 请在项目目录中运行此命令，或使用 `/continue <项目目录>` 先恢复项目上下文。

### 第二步：记录 Bug 报告

向用户确认 Bug 信息：

```
## Bug 报告确认

**问题描述**: [用户提供的描述]

**请补充以下信息（可选）**：
1. 这个 bug 在哪个阶段（Day X）被发现？
2. 期望行为是什么？
3. 实际发生了什么？
4. 有错误信息吗？

回复"确认"开始分析，或补充更多信息。
```

### 第三步：触发 Bug Fixer Agent

用户确认后，调用 `bug-fixer` agent：

**使用 Agent 工具调用 agent**：
- subagent_type: `iterative-builder-zh:bug-fixer`
- prompt: 包含完整的 bug 描述和项目上下文

### 第四步：审查修复方案

Agent 返回修复方案后，展示给用户：

```
## 修复方案审查

### Bug 分析
[Agent 分析结果]

### 影响范围
| 阶段 | 是否受影响 | 需要的操作 |
|------|-----------|-----------|
| Day X | ✅ | [操作] |

### 待执行修改
1. [文件 1]: [修改描述]
2. [文件 2]: [修改描述]

**是否批准执行修复？** (确认/取消/部分执行)
```

### 第五步：执行或等待确认

- 用户确认 → 执行修复
- 用户取消 → 终止并记录到 progress.md
- 用户选择部分执行 → 只执行选定的修改

### 第六步：验证和总结

修复完成后：

```
## 修复完成

✅ **修改文件**: X 个
✅ **影响阶段**: Day X, Day Y
✅ **已更新**: progress.md

**建议验证步骤**:
1. git checkout <相关分支>
2. cd backend && python -m py_compile src/*.py
3. cd frontend && npm run build
4. [运行相关测试]

是否立即执行验证？
```

## 使用示例

```bash
# 报告数据格式问题
/fix Day 2 的 API 返回格式和前端期望不一致

# 报告功能 bug
/fix 文档上传后分块数量总是 0

# 报告性能问题
/fix 搜索响应时间超过 10 秒

# 报告发现的设计缺陷
/fix 数据库索引缺失导致查询慢
```

## 注意事项

- Bug 描述越具体，定位越准确
- 如果影响多个阶段，agent 会列出所有需要修改的地方
- 修复遵循最小化原则，避免过度重构
- 所有修复都会记录到 progress.md

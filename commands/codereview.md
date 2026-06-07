---
name: iterative-builder-zh:codereview
description: 对项目某个阶段的代码进行全面审查，包括代码质量、架构、安全、性能和可维护性，并分析修改是否影响其他阶段。用法：/iterative-builder-zh:codereview [Day编号]
argument-hint: "[Day编号，如 Day1，默认审查最近完成的 Day]"
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

对迭代项目的某个阶段进行代码审查，并分析修改的跨阶段影响。

## 执行步骤

### 第一步：确认项目上下文

1. 检查当前目录中是否存在规划文件（task_plan.md, findings.md, progress.md）
2. 如果不在项目目录，提示用户切换到项目目录

### 第二步：确定审查目标

1. 如果用户指定了 Day 编号（如 `Day2`），审查该天代码
2. 如果未指定，从 progress.md 中找到最近完成的 Day
3. **切换到对应分支**：`git checkout day<N>`
4. 向用户确认审查范围：
   ```
   将对 Day N: [主题] 进行代码审查
   当前分支: day<N>
   ```

### 第三步：加载审查 Skill

**自动激活 `code-review-zh` skill**，按照 skill 中的五个维度执行审查：

1. **代码质量** - 命名、函数长度、重复代码、错误处理
2. **架构设计** - 层次分离、依赖方向、接口设计
3. **安全性** - 输入验证、注入防护、认证授权
4. **性能** - 查询优化、内存使用、缓存
5. **可维护性** - 配置管理、日志、测试、文档

### 第四步：展示审查报告

按 skill 定义的格式输出报告，包含：

- 概要评分表
- 严重问题（🔴）
- 建议改进（🟡）
- 值得肯定（🟢）

### 第五步：询问修改方案

如果发现问题，**使用 AskUserQuestion 询问用户**：

```json
{
  "questions": [{
    "question": "审查发现 X 个问题（Y 个严重，Z 个建议）。是否进行修改？",
    "header": "审查结果",
    "options": [
      {"label": "全部修复", "description": "修复所有严重问题和建议改进"},
      {"label": "只修严重的", "description": "只修复 🔴 严重问题"},
      {"label": "暂不修改", "description": "记录问题，稍后处理"}
    ]
  }]
}
```

### 第六步：执行修改与影响分析

用户确认修改后：

1. **执行修改** - 按审查报告逐项修复
2. **跨阶段影响分析** - 判断每个修改是否影响其他 Day：

   ```
   | 修改项 | 影响的 Day | 需要操作 |
   |--------|-----------|---------|
   | 接口参数变更 | Day 3, Day 4 | ✅ |
   | 工具函数修复 | Day 2 | ✅ |
   | 样式优化 | - | ❌ |
   ```

3. **如果有跨阶段影响**，向用户确认是否同步修改其他 Day：

   ```json
   {
     "questions": [{
       "question": "以下修改会影响其他阶段，是否同步更新？",
       "header": "跨阶段影响",
       "options": [
         {"label": "全部同步", "description": "将修改 cherry-pick 到所有受影响的分支"},
         {"label": "选择性同步", "description": "逐个确认是否同步每个修改"},
         {"label": "仅修改当前分支", "description": "只修改当前分支，其他后续处理"}
       ]
     }]
   }
   ```

4. **执行同步修改**（如用户确认）
   - 提交当前分支的修改
   - 对每个受影响的分支执行 `git cherry-pick`

### 第七步：更新规划文件

更新 progress.md 记录此次审查：

```markdown
### 代码审查: Day N - [日期]
- **评分**: ⭐⭐⭐⭐
- **问题数**: X 严重, Y 建议
- **已修复**: [数量]
- **跨阶段影响**: [影响说明]
```

## 使用示例

```bash
# 审查最近完成的 Day
/iterative-builder-zh:codereview

# 审查指定 Day
/iterative-builder-zh:codereview Day2
```

## 注意事项

- 审查应客观公正，既指出问题也肯定好的实践
- 修改建议要具体，包含代码示例
- 跨阶段影响分析不可遗漏，确保修改不会破坏其他 Day 的独立性
- 审查后更新的代码仍需保持每个 Day 独立可运行

# Iterative Builder (中文版)

循序渐进构建生产级项目的 Claude Code 插件。

## 功能

- 从需求文本描述自动分析并规划分阶段实施方案
- 支持 RAG 系统、Web 应用、API 服务、数据管道等常见场景
- 会话中断后可恢复上下文继续构建
- 支持 bug 修复并自动分析影响范围
- 每个阶段完成后可进行代码审查，修改自动同步到其他阶段

## 安装

将此插件目录复制到 Claude Code 插件目录，或使用：

```bash
cc --plugin-dir /path/to/iterative-builder-zh
```

## 命令

### `/iterative-builder-zh:build` - 启动新项目

从需求描述开始构建项目，支持技术栈选择。

```bash
/iterative-builder-zh:build <需求描述>
```

示例：
```bash
/iterative-builder-zh:build 创建一个 RAG 文档问答系统，支持 PDF 上传、智能分块和流式回答
```

每个 Day 完成后会依次询问：
1. 是否对该 Day 进行代码审查
2. 是否继续下一个 Day

### `/iterative-builder-zh:continue` - 恢复项目

读取项目规划文件，恢复上下文后继续构建。

```bash
/iterative-builder-zh:continue [项目目录]
```

示例：
```bash
/iterative-builder-zh:continue                    # 当前目录
/iterative-builder-zh:continue ./my-rag-project   # 指定目录
```

### `/iterative-builder-zh:fix` - 修复 Bug

报告 bug 并触发修复，自动分析影响范围。

```bash
/iterative-builder-zh:fix <bug描述>
```

示例：
```bash
/iterative-builder-zh:fix Day 2 的 API 返回格式和前端期望不一致
/iterative-builder-zh:fix 文档上传后分块数量总是 0
/iterative-builder-zh:fix 搜索响应时间超过 10 秒
```

### `/iterative-builder-zh:codereview` - 代码审查

对某个阶段的代码进行五维度审查，并分析修改的跨阶段影响。

```bash
/iterative-builder-zh:codereview [Day编号]
```

示例：
```bash
/iterative-builder-zh:codereview          # 审查最近完成的 Day
/iterative-builder-zh:codereview Day2     # 审查指定 Day
```

审查维度：
| 维度 | 检查内容 |
|------|---------|
| 代码质量 | 命名规范、函数长度、重复代码、错误处理 |
| 架构设计 | 层次分离、依赖方向、接口设计 |
| 安全性 | 输入验证、注入防护、认证授权 |
| 性能 | 查询优化、内存使用、缓存策略 |
| 可维护性 | 配置管理、日志、测试、文档 |

## 工作流程

1. **需求分析** - 从描述中提取核心功能
2. **技术栈选择** - 展示选项供用户选择或自定义
3. **阶段规划** - 通过初始化脚本创建规划文件
4. **增量实现** - Day 1 MVP 开始，逐步增强到生产级
5. **代码审查** - 每个 Day 完成后可进行审查
6. **中断恢复** - 随时使用 `/continue` 恢复上下文
7. **Bug 修复** - 使用 `/fix` 修复问题并评估影响

## 组件

| 组件 | 名称 | 说明 |
|------|------|------|
| Command | `/iterative-builder-zh:build` | 启动项目构建流程 |
| Command | `/iterative-builder-zh:continue` | 恢复中断的项目会话 |
| Command | `/iterative-builder-zh:fix` | 触发 bug 修复流程 |
| Command | `/iterative-builder-zh:codereview` | 手动触发代码审查 |
| Agent | `bug-fixer` | 修正 bug 并分析影响范围 |
| Agent | `code-reviewer` | 代码审查与跨阶段影响分析 |
| Skill | `iterative-project-builder-zh` | 项目构建方法论和模板 |
| Skill | `code-review-zh` | 代码审查方法论 |

## 规划文件

每个项目包含三个核心文件（通过 `init_planning.py` 脚本初始化）：

| 文件 | 用途 |
|------|------|
| `task_plan.md` | 阶段规划、技术决策、进度 |
| `findings.md` | 研究发现、技术笔记 |
| `progress.md` | 会话日志、测试结果、修复记录 |

## 许可证

MIT

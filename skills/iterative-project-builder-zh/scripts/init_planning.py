#!/usr/bin/env python3
"""
Initialize planning files for iterative project
初始化迭代项目的规划文件

用法: python init_planning.py [项目名称]
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# Planning file templates / 规划文件模板
TASK_PLAN_TEMPLATE = '''# 任务计划: {project_name}
<!--
  WHAT: {project_name} 的分阶段实施方案
  WHY: 将复杂系统拆解为可学习的阶段性模块
  WHEN: 在开始任何工作之前创建，每个阶段完成后更新
-->

## 目标
<!--
  目标：创建一个循序渐进的项目，从最小化实现逐步演进到完整系统
-->
[描述项目目标]

## 当前阶段
阶段 1: 规划完成 - 准备开始 Day 1

## 技术栈决策
| 组件 | 选择 | 理由 |
|------|------|------|
| 后端 | [待定] | [原因] |
| 前端 | [待定] | [原因] |
| 数据库 | [待定] | [原因] |

## 阶段概览

### Day 1: [MVP 主题]
- [ ] [功能 A]
- [ ] [功能 B]
- **状态:** pending
- **目标:** [Day 1 达成什么]

### Day 2: [增强主题]
- [ ] [功能 C]
- **状态:** pending
- **目标:** [Day 2 添加什么]

### Day 3: [增强主题]
- [ ] [功能 D]
- **状态:** pending
- **目标:** [Day 3 添加什么]

### Day N: 生产就绪
- [ ] 性能优化
- [ ] Docker 部署
- [ ] 完整文档
- **状态:** pending
- **目标:** 生产部署就绪

## 关键问题
1. 技术栈选择？
2. 每个阶段的验收标准？
3. 如何确保每个阶段独立可运行？

## 已做决策
| 决策 | 理由 |
|------|------|
| (待填写) | - |

## 遇到的错误
| 错误 | 尝试 | 解决方案 |
|------|------|----------|
| (待填写) | - | - |

## 备注
- 每个阶段必须独立可运行
- 所有代码注释使用双语格式
- 每个阶段后验证端到端功能
'''

FINDINGS_TEMPLATE = '''# 研究发现与决策
<!--
  WHAT: {project_name} 的研究发现和技术决策记录
  WHY: 持久化存储关键信息，防止上下文丢失
  WHEN: 每次有新发现时更新
-->

## 需求摘要
<!--
  从需求文档提取的核心需求
-->
- 核心需求 1
- 核心需求 2
- 核心需求 3

## 技术栈详情

### 后端
| 组件 | 库 | 用途 |
|------|------|------|
| [组件] | [库] | [用途] |

### 前端
| 组件 | 库 | 用途 |
|------|------|------|
| [组件] | [库] | [用途] |

## 研究发现

### 核心架构
```
┌─────────────┐
│   前端      │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   后端      │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   数据库    │
└─────────────┘
```

### 关键模式
1. 模式 A: 描述
2. 模式 B: 描述

## 技术决策
| 决策 | 理由 |
|------|------|
| | |

## 实现模式

### 双语注释格式
```python
# English comment
# 中文备注
code here
```

### API 响应格式
```json
{{
  "success": true,
  "data": {{}},
  "error": null
}}
```

## 资源
- [资源 1](url)
- [资源 2](url)

## 遇到的问题
| 问题 | 解决方案 |
|------|----------|
| | |

## Day X 研究: [主题]
/*
  Day X 研究：[主题]
  Updated: [日期]
*/
### 关键组件
1. **组件 A**
   - 详情
2. **组件 B**
   - 详情

### 配置
```python
# 配置示例
```
'''

PROGRESS_TEMPLATE = '''# 进度日志
<!--
  WHAT: {project_name} 的进度日志
  WHY: 记录每个阶段的详细进展
  WHEN: 每个阶段完成或有重要进展时更新
-->

## 会话: [日期]

### 阶段 1: 规划
- **状态:** complete
- **开始:** [日期]
- 执行操作:
  - 读取 requirement.md
  - 创建规划文件
  - 提出技术栈建议
- 创建/修改文件:
  - task_plan.md
  - findings.md
  - progress.md

### 阶段 2: Day 1 实现
- **状态:** [pending/in_progress/complete]
- **开始:** [日期]
- 执行操作:
  - [操作 1]
  - [操作 2]
- 创建/修改文件:
  - [文件 1]
  - [文件 2]

### 阶段 3: Day 2 实现
- **状态:** pending
- **开始:** [日期]
- 执行操作:
  - [操作]
- 创建/修改文件:
  - [文件]

## 每日进度计划

| 天数 | 计划 | 状态 | 关键交付物 |
|------|------|------|------------|
| Day 1 | MVP | pending | 核心功能 |
| Day 2 | 增强 | pending | 新功能 |
| Day N | 生产 | pending | 完整系统 |

## 测试结果

| 测试 | 输入 | 预期 | 实际 | 状态 |
|------|------|------|------|------|
| 测试 1 | 输入 | 预期 | 实际 | 通过/失败 |

## 错误日志

| 时间戳 | 错误 | 尝试 | 解决方案 |
|--------|------|------|----------|
| | | | |

## 5 问重启检查

| 问题 | 答案 |
|------|------|
| 我在哪？ | [当前阶段] |
| 我要去哪？ | [后续阶段] |
| 目标是什么？ | [项目目标] |
| 我学到了什么？ | [关键学习] |
| 我做了什么？ | [已完成工作] |

## 下一步行动

1. [行动 1]
2. [行动 2]

---
*每个阶段完成或遇到错误后更新*
'''


def create_planning_files(project_name: str, output_dir: Path):
    """Create planning files in the project directory"""
    """在项目目录中创建规划文件"""
    date = datetime.now().strftime("%Y-%m-%d")

    # Create planning files / 创建规划文件
    files = {
        "task_plan.md": TASK_PLAN_TEMPLATE.format(project_name=project_name),
        "findings.md": FINDINGS_TEMPLATE.format(project_name=project_name),
        "progress.md": PROGRESS_TEMPLATE.format(
            project_name=project_name,
            date=date
        )
    }

    for filename, content in files.items():
        filepath = output_dir / filename
        if not filepath.exists():
            filepath.write_text(content, encoding='utf-8')
            print(f"Created / 已创建: {filepath}")
        else:
            print(f"Exists / 已存在: {filepath}")

    print(f"\nPlanning files initialized for / 规划文件已初始化: {project_name}")
    print("Next steps / 下一步:")
    print("1. Edit task_plan.md with phase breakdown / 编辑 task_plan.md 添加阶段划分")
    print("2. Update findings.md with research notes / 更新 findings.md 添加研究笔记")
    print("3. Start Day 1 implementation / 开始 Day 1 实现")


def main():
    if len(sys.argv) < 2:
        print("Usage / 用法: python init_planning.py <project_name>")
        print("Example / 示例: python init_planning.py my-rag-project")
        sys.exit(1)

    project_name = sys.argv[1]
    output_dir = Path.cwd()

    create_planning_files(project_name, output_dir)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Initialize planning files for iterative project
初始化迭代项目的规划文件

用法: python init_planning.py [项目名称]
"""

import sys
from pathlib import Path
from datetime import datetime


def get_assets_dir() -> Path:
    """Get the assets directory path / 获取 assets 目录路径"""
    # Get the script directory / 获取脚本所在目录
    script_dir = Path(__file__).parent
    assets_dir = script_dir.parent / "assets"
    return assets_dir


def load_template(template_name: str) -> str:
    """Load template from assets directory / 从 assets 目录加载模板"""
    assets_dir = get_assets_dir()
    template_file = assets_dir / template_name
    if not template_file.exists():
        raise FileNotFoundError(f"Template not found / 模板文件不存在: {template_file}")
    return template_file.read_text(encoding='utf-8')


def create_planning_files(project_name: str, output_dir: Path):
    """Create planning files in the project directory"""
    """在项目目录中创建规划文件"""
    date = datetime.now().strftime("%Y-%m-%d")

    # Load templates from assets directory / 从 assets 目录加载模板
    task_plan_template = load_template("task_plan.md")
    findings_template = load_template("findings.md")
    progress_template = load_template("progress.md")

    # Create planning files / 创建规划文件
    files = {
        "task_plan.md": task_plan_template.format(project_name=project_name),
        "findings.md": findings_template.format(project_name=project_name),
        "progress.md": progress_template.format(
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

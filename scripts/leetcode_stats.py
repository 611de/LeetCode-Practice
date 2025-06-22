import os
import re
import argparse
from collections import defaultdict, OrderedDict
import datetime

# 配置参数 - 根据你的仓库结构调整
PROBLEM_DIR = "."  # 存放题解的根目录
README_PATH = "README.md"  # README文件路径
IGNORE_DIRS = {".git", "scripts", "docs"}  # 忽略的目录
DIFFICULTY_MAPPING = {
    "easy": "Easy",
    "medium": "Medium",
    "hard": "Hard",
}
PROGRESS_SECTION_START = "## **📈 Progress**"  # README中进度部分的开始标记
PROGRESS_SECTION_END = "## **🤝 Connect With Me**"  # README中进度部分的结束标记

# SVG图表配置
SVG_WIDTH = 600
SVG_HEIGHT = 250
BAR_WIDTH = 40
BAR_SPACING = 10
COLORS = {
    "Easy": "#34D399",    # 绿色
    "Medium": "#FBBF24",  # 黄色
    "Hard": "#EF4444",    # 红色
    "Total": "#60A5FA",   # 蓝色
}


def get_problem_info(file_path):
    """从文件名和内容中提取题目信息"""
    file_name = os.path.basename(file_path)
    file_name = os.path.splitext(file_name)[0]  # 去除扩展名
    
    # 从文件名提取题号和标题 (示例格式: "1_two_sum.py" 或 "1. Two Sum.py")
    match = re.match(r"(\d+)[._\s]*(.*)", file_name)
    if not match:
        return None, None, None, None, None
    
    problem_id, title = match.groups()
    title = title.replace("_", " ").strip().title()
    
    # 从文件内容提取难度 (如果有标注)
    difficulty = None
    created_date = None
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().lower()
            for key, value in DIFFICULTY_MAPPING.items():
                if key in content:
                    difficulty = value
                    break
            
            # 尝试从文件内容提取创建日期
            date_match = re.search(r"date: (\d{4}-\d{2}-\d{2})", content)
            if date_match:
                created_date = date_match.group(1)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    # 如果文件内容中没有标注难度，尝试从文件夹名推断
    if not difficulty:
        dir_name = os.path.basename(os.path.dirname(file_path)).lower()
        for key, value in DIFFICULTY_MAPPING.items():
            if key in dir_name:
                difficulty = value
                break
    
    # 如果没有找到日期，使用文件修改时间（近似创建时间）
    if not created_date:
        try:
            timestamp = os.path.getmtime(file_path)
            created_date = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
        except Exception:
            created_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    return problem_id, title, difficulty, file_path, created_date


def collect_problems():
    """收集所有题目信息"""
    problems = []
    for root, dirs, files in os.walk(PROBLEM_DIR):
        # 跳过忽略的目录
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            # 只处理代码文件 (根据你的语言调整)
            if file.endswith((".py", ".java", ".cpp", ".js", ".ts")):
                file_path = os.path.join(root, file)
                problem_info = get_problem_info(file_path)
                if all(problem_info[:3]):  # 确保题号、标题和难度都有效
                    problems.append(problem_info)
    
    # 按题号排序
    problems.sort(key=lambda x: int(x[0]))
    return problems


def generate_monthly_chart(problems):
    """生成月度解题量柱状图"""
    # 统计每月解题量
    monthly_counts = defaultdict(lambda: defaultdict(int))
    for _, _, difficulty, _, date in problems:
        year_month = date[:7]  # YYYY-MM
        monthly_counts[year_month][difficulty] += 1
        monthly_counts[year_month]["Total"] += 1
    
    # 获取最近6个月的数据
    today = datetime.datetime.now()
    months = []
    for i in range(6, 0, -1):
        month = today - datetime.timedelta(days=i*30)
        months.append(month.strftime("%Y-%m"))
    
    # 确保每个月都有数据（即使为0）
    for month in months:
        if month not in monthly_counts:
            monthly_counts[month] = {d: 0 for d in DIFFICULTY_MAPPING.values()}
            monthly_counts[month]["Total"] = 0
    
    # 排序
    monthly_counts = OrderedDict(sorted(monthly_counts.items()))
    recent_months = list(monthly_counts.keys())[-6:]
    
    # 计算最大解题数，用于缩放
    max_count = max(sum(monthly_counts[m].values()) for m in recent_months)
    if max_count == 0:
        max_count = 1  # 避免除零错误
    
    # 生成SVG
    svg = [
        f'<svg width="{SVG_WIDTH}" height="{SVG_HEIGHT}" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}" xmlns="http://www.w3.org/2000/svg">',
        '  <style>',
        '    .axis { stroke: #333; stroke-width: 1; }',
        '    .grid { stroke: #ddd; stroke-width: 0.5; stroke-dasharray: 2,2; }',
        '    .label { font-family: Arial; font-size: 12px; fill: #333; }',
        '    .title { font-family: Arial; font-size: 14px; font-weight: bold; fill: #333; }',
        '  </style>',
        f'  <text x="{SVG_WIDTH//2}" y="20" text-anchor="middle" class="title">Monthly Problem Solving</text>',
        # 绘制坐标轴
        f'  <line x1="50" y1="{SVG_HEIGHT-50}" x2="{SVG_WIDTH-20}" y2="{SVG_HEIGHT-50}" class="axis" />',
        f'  <line x1="50" y1="25" x2="50" y2="{SVG_HEIGHT-50}" class="axis" />',
    ]
    
    # 绘制网格线和Y轴标签
    for i in range(6):
        y = SVG_HEIGHT - 50 - (i * (SVG_HEIGHT - 75) // 5)
        value = (i * max_count) // 5
        svg.append(f'  <line x1="50" y1="{y}" x2="{SVG_WIDTH-20}" y2="{y}" class="grid" />')
        svg.append(f'  <text x="45" y="{y+5}" text-anchor="end" class="label">{value}</text>')
    
    # 绘制柱状图
    bar_group_width = BAR_WIDTH * len(DIFFICULTY_MAPPING) + BAR_SPACING * (len(DIFFICULTY_MAPPING) - 1)
    total_width = bar_group_width * len(recent_months) + BAR_SPACING * (len(recent_months) - 1)
    start_x = 50 + (SVG_WIDTH - 70 - total_width) // 2
    
    for i, month in enumerate(recent_months):
        x_pos = start_x + i * (bar_group_width + BAR_SPACING)
        month_name = datetime.datetime.strptime(month, "%Y-%m").strftime("%b %Y")
        svg.append(f'  <text x="{x_pos + bar_group_width/2}" y="{SVG_HEIGHT-35}" text-anchor="middle" class="label">{month_name}</text>')
        
        # 为每种难度绘制柱子
        offset = 0
        for j, difficulty in enumerate(DIFFICULTY_MAPPING.values()):
            count = monthly_counts[month][difficulty]
            height = (count * (SVG_HEIGHT - 75)) // max_count
            bar_x = x_pos + offset
            bar_y = SVG_HEIGHT - 50 - height
            
            svg.append(f'  <rect x="{bar_x}" y="{bar_y}" width="{BAR_WIDTH}" height="{height}" fill="{COLORS[difficulty]}" opacity="0.8">')
            svg.append(f'    <title>{difficulty}: {count}</title>')
            svg.append('  </rect>')
            
            offset += BAR_WIDTH + BAR_SPACING
    
    # 添加图例
    legend_x = SVG_WIDTH - 150
    legend_y = 30
    for i, difficulty in enumerate(DIFFICULTY_MAPPING.values()):
        svg.append(f'  <rect x="{legend_x}" y="{legend_y + i*20}" width="15" height="10" fill="{COLORS[difficulty]}" />')
        svg.append(f'  <text x="{legend_x+20}" y="{legend_y + i*20 + 9}" class="label">{difficulty}</text>')
    
    svg.append('</svg>')
    return '\n'.join(svg)


def generate_weekly_chart(problems):
    """生成周度解题量折线图"""
    # 统计每周解题量
    weekly_counts = defaultdict(lambda: defaultdict(int))
    for _, _, difficulty, _, date in problems:
        year_week = datetime.datetime.strptime(date, "%Y-%m-%d").isocalendar()[:2]
        week_key = f"{year_week[0]}-W{year_week[1]:02d}"
        weekly_counts[week_key][difficulty] += 1
        weekly_counts[week_key]["Total"] += 1
    
    # 获取最近8周的数据
    today = datetime.datetime.now()
    weeks = []
    for i in range(8, 0, -1):
        week = today - datetime.timedelta(days=i*7)
        year, week_num, _ = week.isocalendar()
        weeks.append(f"{year}-W{week_num:02d}")
    
    # 确保每周都有数据（即使为0）
    for week in weeks:
        if week not in weekly_counts:
            weekly_counts[week] = {d: 0 for d in DIFFICULTY_MAPPING.values()}
            weekly_counts[week]["Total"] = 0
    
    # 排序
    weekly_counts = OrderedDict(sorted(weekly_counts.items()))
    recent_weeks = list(weekly_counts.keys())[-8:]
    
    # 计算最大解题数，用于缩放
    max_count = max(sum(weekly_counts[w].values()) for w in recent_weeks)
    if max_count == 0:
        max_count = 1  # 避免除零错误
    
    # 生成SVG
    svg = [
        f'<svg width="{SVG_WIDTH}" height="{SVG_HEIGHT}" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}" xmlns="http://www.w3.org/2000/svg">',
        '  <style>',
        '    .axis { stroke: #333; stroke-width: 1; }',
        '    .grid { stroke: #ddd; stroke-width: 0.5; stroke-dasharray: 2,2; }',
        '    .label { font-family: Arial; font-size: 12px; fill: #333; }',
        '    .title { font-family: Arial; font-size: 14px; font-weight: bold; fill: #333; }',
        '    .line { fill: none; stroke-width: 2; }',
        '    .point { r: 4; }',
        '  </style>',
        f'  <text x="{SVG_WIDTH//2}" y="20" text-anchor="middle" class="title">Weekly Problem Solving Trend</text>',
        # 绘制坐标轴
        f'  <line x1="50" y1="{SVG_HEIGHT-50}" x2="{SVG_WIDTH-20}" y2="{SVG_HEIGHT-50}" class="axis" />',
        f'  <line x1="50" y1="25" x2="50" y2="{SVG_HEIGHT-50}" class="axis" />',
    ]
    
    # 绘制网格线和Y轴标签
    for i in range(6):
        y = SVG_HEIGHT - 50 - (i * (SVG_HEIGHT - 75) // 5)
        value = (i * max_count) // 5
        svg.append(f'  <line x1="50" y1="{y}" x2="{SVG_WIDTH-20}" y2="{y}" class="grid" />')
        svg.append(f'  <text x="45" y="{y+5}" text-anchor="end" class="label">{value}</text>')
    
    # 绘制折线图
    points_per_week = (SVG_WIDTH - 70) / len(recent_weeks)
    start_x = 50 + points_per_week / 2
    
    # 为每种难度绘制折线
    for difficulty in DIFFICULTY_MAPPING.values():
        # 收集点坐标
        points = []
        for i, week in enumerate(recent_weeks):
            count = weekly_counts[week][difficulty]
            x = start_x + i * points_per_week
            y = SVG_HEIGHT - 50 - (count * (SVG_HEIGHT - 75)) // max_count
            points.append((x, y))
        
        # 绘制折线
        if points:
            path_data = "M" + " L".join([f"{x},{y}" for x, y in points])
            svg.append(f'  <path d="{path_data}" class="line" stroke="{COLORS[difficulty]}" />')
            
            # 绘制数据点
            for x, y in points:
                svg.append(f'  <circle cx="{x}" cy="{y}" class="point" fill="{COLORS[difficulty]}" />')
    
    # 添加X轴标签
    for i, week in enumerate(recent_weeks):
        x = start_x + i * points_per_week
        # 简化周标签显示（只显示周数）
        week_display = week.split('-W')[1]
        svg.append(f'  <text x="{x}" y="{SVG_HEIGHT-35}" text-anchor="middle" class="label" transform="rotate(45,{x},{SVG_HEIGHT-35})">{week_display}</text>')
    
    # 添加图例
    legend_x = SVG_WIDTH - 150
    legend_y = 30
    for i, difficulty in enumerate(DIFFICULTY_MAPPING.values()):
        svg.append(f'  <line x1="{legend_x}" y1="{legend_y + i*20 + 5}" x2="{legend_x+20}" y2="{legend_y + i*20 + 5}" class="line" stroke="{COLORS[difficulty]}" />')
        svg.append(f'  <circle cx="{legend_x+10}" cy="{legend_y + i*20 + 5}" class="point" fill="{COLORS[difficulty]}" />')
        svg.append(f'  <text x="{legend_x+25}" y="{legend_y + i*20 + 9}" class="label">{difficulty}</text>')
    
    svg.append('</svg>')
    return '\n'.join(svg)


def generate_progress_table(problems):
    """生成题目表格"""
    table = "| Problem | Difficulty | Solution |\n|---------|------------|----------|\n"
    for problem_id, title, difficulty, file_path, _ in problems:
        leetcode_url = f"https://leetcode.com/problems/{title.replace(' ', '-').lower()}/"
        repo_url = f"./{file_path}"
        table += f"| [{title}]({leetcode_url}) | {difficulty} | [Code]({repo_url}) |\n"
    return table


def generate_stats(problems):
    """生成统计信息"""
    total = len(problems)
    difficulty_counts = defaultdict(int)
    
    for _, _, difficulty, _, _ in problems:
        difficulty_counts[difficulty] += 1
    
    # 确保包含所有难度级别（即使为0）
    for difficulty in DIFFICULTY_MAPPING.values():
        if difficulty not in difficulty_counts:
            difficulty_counts[difficulty] = 0
    
    # 生成进度条
    progress_bars = []
    for difficulty in ["Easy", "Medium", "Hard"]:
        count = difficulty_counts[difficulty]
        percentage = int((count / total) * 100) if total > 0 else 0
        progress_bar = f"{'█' * (percentage // 10)}{'░' * (10 - percentage // 10)}"
        progress_bars.append(f"{difficulty}: {progress_bar} {count}/{total} ({percentage}%)")
    
    stats = (
        f"- **Total Solved**: `{total}` problems "
        f"(Easy: `{difficulty_counts['Easy']}`, "
        f"Medium: `{difficulty_counts['Medium']}`, "
        f"Hard: `{difficulty_counts['Hard']}`)\n"
        f"- {' | '.join(progress_bars)}\n"
        f"- **Current Focus**: Advanced algorithms (e.g., graph traversal, advanced DP)\n"
        f"- **Daily Goal**: Solve `1-2` problems to maintain consistency."
    )
    return stats


def update_readme(readme_path, problems):
    """更新README中的进度部分"""
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 生成图表
        monthly_chart = generate_monthly_chart(problems)
        weekly_chart = generate_weekly_chart(problems)
        
        # 生成新的进度内容
        progress_table = generate_progress_table(problems)
        stats = generate_stats(problems)
        
        new_progress_section = (
            f"{PROGRESS_SECTION_START}\n\n"
            f"{stats}\n\n"
            f"### 📊 Problem Solving Charts\n\n"
            f"**Monthly Progress**\n\n"
            f"{monthly_chart}\n\n"
            f"**Weekly Trend**\n\n"
            f"{weekly_chart}\n\n"
            f"### 📃 Problem List\n\n"
            f"{progress_table}\n\n"
            f"{PROGRESS_SECTION_END}"
        )
        
        # 替换旧的进度部分
        start_idx = content.find(PROGRESS_SECTION_START)
        end_idx = content.find(PROGRESS_SECTION_END)
        
        if start_idx == -1 or end_idx == -1:
            print("Warning: Could not find progress section markers in README.")
            return
        
        end_idx += len(PROGRESS_SECTION_END)
        new_content = content[:start_idx] + new_progress_section + content[end_idx:]
        
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print(f"Successfully updated {readme_path}")
    except Exception as e:
        print(f"Error updating README: {e}")


def main():
    parser = argparse.ArgumentParser(description="Update LeetCode progress in README")
    parser.add_argument("--readme", default=README_PATH, help="Path to README file")
    args = parser.parse_args()
    
    problems = collect_problems()
    update_readme(args.readme, problems)


if __name__ == "__main__":
    main()
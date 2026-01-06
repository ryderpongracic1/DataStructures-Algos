#!/usr/bin/env python3
"""
Script to automatically generate README.md for LeetCode submissions tracker
"""

import os
import re
from pathlib import Path
from collections import defaultdict


def extract_problem_info(readme_path):
    """Extract problem information from individual README files"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title and URL
    title_match = re.search(r'<a href="(https://leetcode\.com/problems/[^"]+)">([^<]+)</a>', content)
    if not title_match:
        return None

    url = title_match.group(1)
    title = title_match.group(2)

    # Extract difficulty
    difficulty_match = re.search(r"Difficulty-(\w+)-", content)
    difficulty = difficulty_match.group(1) if difficulty_match else "Unknown"

    return {
        'title': title,
        'url': url,
        'difficulty': difficulty
    }


def get_all_problems(base_path):
    """Scan directory for all LeetCode problems"""
    problems = []

    for item in sorted(os.listdir(base_path)):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path) and re.match(r'^\d+', item):
            readme_path = os.path.join(item_path, 'README.md')
            if os.path.exists(readme_path):
                info = extract_problem_info(readme_path)
                if info:
                    # Extract problem number from directory name
                    problem_num = re.match(r'^(\d+)', item).group(1)
                    info['number'] = int(problem_num)
                    info['folder'] = item

                    # Find solution file
                    for file in os.listdir(item_path):
                        if file.endswith(('.py', '.java', '.cpp', '.js', '.c')):
                            info['solution_file'] = file
                            info['language'] = get_language(file)
                            break

                    problems.append(info)

    return sorted(problems, key=lambda x: x['number'])


def get_language(filename):
    """Get programming language from file extension"""
    ext_map = {
        '.py': 'Python',
        '.java': 'Java',
        '.cpp': 'C++',
        '.c': 'C',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.go': 'Go',
        '.rs': 'Rust'
    }
    ext = os.path.splitext(filename)[1]
    return ext_map.get(ext, 'Unknown')


def get_difficulty_badge(difficulty):
    """Get colored badge for difficulty"""
    badges = {
        'Easy': '![Easy](https://img.shields.io/badge/Easy-5CB85C?style=flat-square)',
        'Medium': '![Medium](https://img.shields.io/badge/Medium-FFA500?style=flat-square)',
        'Hard': '![Hard](https://img.shields.io/badge/Hard-D9534F?style=flat-square)'
    }
    return badges.get(difficulty, f'![{difficulty}](https://img.shields.io/badge/{difficulty}-gray?style=flat-square)')


def generate_readme(problems):
    """Generate the main README content"""

    # Calculate statistics
    total = len(problems)
    by_difficulty = defaultdict(int)
    by_language = defaultdict(int)

    for problem in problems:
        by_difficulty[problem['difficulty']] += 1
        if 'language' in problem:
            by_language[problem['language']] += 1

    # Start building README
    readme = []
    readme.append("# 🚀 LeetCode Solutions")
    readme.append("")
    readme.append("A collection of my LeetCode problem solutions, automatically tracked and organized.")
    readme.append("")

    # Statistics section
    readme.append("## 📊 Statistics")
    readme.append("")
    readme.append(f"**Total Problems Solved:** {total}")
    readme.append("")
    readme.append("| Difficulty | Count |")
    readme.append("|------------|-------|")
    for diff in ['Easy', 'Medium', 'Hard']:
        count = by_difficulty.get(diff, 0)
        readme.append(f"| {get_difficulty_badge(diff)} | {count} |")
    readme.append("")

    # Languages section
    if by_language:
        readme.append("**Languages Used:**")
        readme.append("")
        for lang, count in sorted(by_language.items(), key=lambda x: x[1], reverse=True):
            readme.append(f"- {lang}: {count}")
        readme.append("")

    # Problems table
    readme.append("## 📝 Problems")
    readme.append("")
    readme.append("| # | Title | Difficulty | Solution |")
    readme.append("|---|-------|------------|----------|")

    for problem in problems:
        number = problem['number']
        title = problem['title']
        url = problem['url']
        difficulty = get_difficulty_badge(problem['difficulty'])
        folder = problem['folder']
        solution = f"[{problem.get('language', 'View')}](./{folder})" if 'solution_file' in problem else "N/A"

        readme.append(f"| {number} | [{title}]({url}) | {difficulty} | {solution} |")

    readme.append("")

    # Footer
    readme.append("---")
    readme.append("")
    readme.append("### 🔄 Auto-Update")
    readme.append("")
    readme.append("This README is automatically generated. To update it after adding new solutions:")
    readme.append("")
    readme.append("```bash")
    readme.append("python3 generate_readme.py")
    readme.append("```")
    readme.append("")
    readme.append("### 📌 Repository Structure")
    readme.append("")
    readme.append("```")
    readme.append("DataStructures-Algos/")
    readme.append("├── README.md")
    readme.append("├── generate_readme.py")
    readme.append("└── [problem-number]-[problem-name]/")
    readme.append("    ├── README.md")
    readme.append("    └── solution.[ext]")
    readme.append("```")
    readme.append("")
    readme.append("---")
    readme.append("")
    readme.append("*Last updated: Auto-generated by generate_readme.py*")

    return '\n'.join(readme)


def main():
    """Main function"""
    script_dir = Path(__file__).parent
    problems = get_all_problems(script_dir)

    readme_content = generate_readme(problems)

    readme_path = script_dir / 'README.md'
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"✅ README.md generated successfully!")
    print(f"📊 Total problems: {len(problems)}")
    print(f"📝 File: {readme_path}")


if __name__ == '__main__':
    main()

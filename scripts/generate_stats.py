#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 GitHub 主页统计卡片 stats.svg

数据来源：GitHub 官方 REST API（https://api.github.com）
依赖：仅 Python 标准库，无任何第三方包。

用法：
    GITHUB_TOKEN=<your_token> python generate_stats.py

统计指标（已验证 GitHub API 可准确获取）：
    - Total Stars      ：对用户所有公开仓库的 stargazers_count 求和
    - Total PRs        ：search issues type:pr author:<user>
    - Total Issues     ：search issues type:issue author:<user>
    - Public Repos     ：user.public_repos
    - Followers        ：user.followers
    - 等级评分          ：由 stars + followers 综合计算（纯装饰）
"""
import json
import os
import sys
import urllib.request
import urllib.parse

# 从环境变量 GITHUB_TOKEN 读取（GitHub Actions 里自动注入 ${{ secrets.GITHUB_TOKEN }}）
USERNAME = "wzxgA"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

API = "https://api.github.com"
HEADERS = {
    "User-Agent": "profile-stats-generator",
    "Accept": "application/vnd.github.v3+json",
}
if TOKEN:
    HEADERS["Authorization"] = f"token {TOKEN}"


def api_get(path: str, params: dict | None = None) -> dict | list:
    """请求 GitHub API，自动处理分页返回合并并正确处理 204/错误。"""
    all_items = []
    url = f"{API}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    page = 1
    while True:
        page_url = f"{url}&page={page}&per_page=100" if "?" in url else f"{url}?page={page}&per_page=100"
        req = urllib.request.Request(page_url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 401:
                print(f"[错误] GITHUB_TOKEN 无效或权限不足：{e}", file=sys.stderr)
                sys.exit(1)
            if e.code == 403:
                print(f"[错误] 触发 API 限流：{e}", file=sys.stderr)
                sys.exit(1)
            print(f"[错误] 请求 {path} 失败：HTTP {e.code}", file=sys.stderr)
            sys.exit(1)
        if isinstance(data, list):
            all_items.extend(data)
            if len(data) < 100:  # 没有更多页
                break
            page += 1
        else:
            return data
    return all_items


def get_stats() -> dict:
    """抓取所有统计指标。"""
    user = api_get(f"/users/{USERNAME}")

    # 1. 总 Star：遍历所有公开仓库求 stargazers_count 之和
    repos = api_get(f"/users/{USERNAME}/repos")
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)

    # 2. PR 数
    pr_data = api_get(f"/search/issues", {"q": f"author:{USERNAME} type:pr"})
    total_prs = pr_data.get("total_count", 0) if isinstance(pr_data, dict) else 0

    # 3. Issue 数
    issue_data = api_get(f"/search/issues", {"q": f"author:{USERNAME} type:issue"})
    total_issues = issue_data.get("total_count", 0) if isinstance(issue_data, dict) else 0

    # 4. 仓库数 / 5. 粉丝数
    total_repos = user.get("public_repos", 0)
    total_followers = user.get("followers", 0)

    return {
        "stars": total_stars,
        "prs": total_prs,
        "issues": total_issues,
        "repos": total_repos,
        "followers": total_followers,
    }


def compute_grade(stars: int, followers: int) -> str:
    """根据 stars + followers 综合计算等级（装饰用）。"""
    score = stars + followers * 2
    if score >= 2000:
        return "S"
    if score >= 1200:
        return "A+"
    if score >= 700:
        return "A"
    if score >= 350:
        return "A-"
    if score >= 150:
        return "B+"
    return "B"


# ---------- 渲染 SVG ----------
def render_svg(stats: dict, grade: str) -> str:
    """按现有卡片样式生成 stats.svg。"""
    # grade 影响环形填充比例，满分视为 2000 分
    score = stats["stars"] + stats["followers"] * 2
    ratio = min(score / 2000, 1.0)
    dash_offset = int(402 * (1 - ratio))  # 环周长约 402

    rows = [
        ("⭐", "#ffd166", "Total Stars Earned:", stats["stars"]),
        ("🔀", "#60a5fa", "Total Pull Requests:", stats["prs"]),
        ("⚠️", "#f87171", "Total Issues Opened:", stats["issues"]),
        ("📦", "#a78bfa", "Public Repositories:", stats["repos"]),
        ("👥", "#fbbf24", "Followers:", stats["followers"]),
    ]

    rows_svg = ""
    y = 105
    delays = [0.0, 0.2, 0.4, 0.6, 0.8]
    for (icon, color, label, value), delay in zip(rows, delays):
        rows_svg += f"""
  <g>
    <circle cx="55" cy="{y}" r="9" fill="{color}" opacity="0.15"/>
    <text x="48" y="{y + 7}" font-size="18">{icon}</text>
    <text x="85" y="{y + 7}" font-family="'Segoe UI',sans-serif" font-size="17" fill="#e4e4e7" font-weight="500">{label}</text>
    <text x="420" y="{y + 7}" font-family="'Segoe UI',sans-serif" font-size="20" font-weight="700" fill="#f0f0f0" text-anchor="middle">
      {value}
      <animate attributeName="opacity" values="0.6;1;0.6" dur="2.5s" begin="{delay}s" repeatCount="indefinite"/>
    </text>
  </g>"""
        y += 40

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="760" height="280" viewBox="0 0 760 280">
  <defs>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000" flood-opacity="0.25"/>
    </filter>
    <linearGradient id="ringGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#c471ed"/>
      <stop offset="50%" stop-color="#e94560"/>
      <stop offset="100%" stop-color="#ff6b9d"/>
    </linearGradient>
  </defs>

  <!-- 卡片背景 -->
  <rect x="10" y="10" width="740" height="260" rx="12" fill="#21222c" stroke="#3a3c4e" stroke-width="1.5" filter="url(#cardShadow)"/>

  <!-- 标题 -->
  <text x="40" y="55" font-family="'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif" font-size="24" font-weight="700" fill="#e94560">
    {USERNAME}'s GitHub Stats
  </text>

  <!-- 分隔线 -->
  <line x1="40" y1="75" x2="480" y2="75" stroke="#3a3c4e" stroke-width="1"/>
{rows_svg}
  <!-- 右侧环形等级评分 -->
  <g transform="translate(620, 175)">
    <circle cx="0" cy="0" r="64" fill="none" stroke="#3a3c4e" stroke-width="10"/>
    <circle cx="0" cy="0" r="64" fill="none" stroke="url(#ringGrad)" stroke-width="10"
      stroke-linecap="round"
      stroke-dasharray="402" stroke-dashoffset="{dash_offset}"
      transform="rotate(-90)">
      <animate attributeName="stroke-dashoffset" values="402;{dash_offset};{dash_offset}" dur="2s" begin="0.5s" fill="freeze"/>
    </circle>

    <text x="0" y="15" font-family="'Segoe UI',sans-serif" font-size="46" font-weight="800" text-anchor="middle" fill="#e94560" opacity="0">
      {grade}
      <animate attributeName="opacity" values="0;1" dur="0.8s" begin="1.8s" fill="freeze"/>
    </text>
    <text x="0" y="40" font-family="'Segoe UI',sans-serif" font-size="11" text-anchor="middle" fill="#8b8d98" opacity="0">
      GRADE
      <animate attributeName="opacity" values="0;1" dur="0.6s" begin="2.2s" fill="freeze"/>
    </text>
  </g>
</svg>
"""
    return svg


def main() -> None:
    print(f"[1/3] 正在抓取 {USERNAME} 的 GitHub 统计……")
    stats = get_stats()
    print(f"       Stars={stats['stars']}  PRs={stats['prs']}  Issues={stats['issues']}  "
          f"Repos={stats['repos']}  Followers={stats['followers']}")

    grade = compute_grade(stats["stars"], stats["followers"])
    print(f"[2/3] 计算等级：{grade}")

    svg = render_svg(stats, grade)
    here = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(os.path.dirname(here), "stats.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"[3/3] 已写入 {out_path}")


if __name__ == "__main__":
    main()
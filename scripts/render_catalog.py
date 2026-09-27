#!/usr/bin/env python3
"""Render the hand-curated CSV for MkDocs. Run manually after weekly edits."""

import argparse
import csv
from datetime import date
from html import escape
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.csv"
DOCS = ROOT / "docs"
FIELDS = (
    "id", "title", "year", "topic", "type", "question", "mechanism",
    "evaluation", "conclusion", "limitation", "paper_url", "code_url",
    "verified_on", "route", "source_status",
)


def load_rows():
    with DATA.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise ValueError("CSV columns do not match the documented schema")
        rows = list(reader)
    if len(rows) < 30:
        raise ValueError("The catalog must retain at least 30 core records")
    seen = set()
    for row in rows:
        paper_id = row["id"]
        if not re.fullmatch(r"\d{4}\.\d{4,5}", paper_id):
            raise ValueError(f"Invalid arXiv ID: {paper_id}")
        if paper_id in seen:
            raise ValueError(f"Duplicate arXiv ID: {paper_id}")
        seen.add(paper_id)
        if any(not row[key].strip() for key in FIELDS if key != "code_url"):
            raise ValueError(f"Missing required field: {paper_id}")
        if row["paper_url"] != f"https://arxiv.org/abs/{paper_id}":
            raise ValueError(f"Paper URL mismatch: {paper_id}")
        if row["code_url"] and not row["code_url"].startswith("https://"):
            raise ValueError(f"Invalid code URL: {paper_id}")
        if row["year"] != "20" + paper_id[:2]:
            raise ValueError(f"Year and arXiv ID differ: {paper_id}")
        date.fromisoformat(row["verified_on"])
    return rows


def h(value):
    return escape(value, quote=True)


def paper_table(rows):
    lines = [
        "# 论文库",
        "",
        f"> 共 **{len(rows)}** 篇人工精选论文。最近记录核验：**{max(row['verified_on'] for row in rows)}**。"
        " 收录表示值得阅读，不代表论文结论已独立复现。代码栏留空表示未登记已核验的官方仓库。",
        "",
        "[阅读路线](reading-path.md) · [收录标准与每周 SOP](update-sop.md) · "
        "[下载 CSV](https://github.com/Scodive/AI-Agent-Guide/blob/main/data/papers.csv)",
        "",
        '<div class="paper-controls">',
        '  <label>搜索标题、问题或机制 <input id="paper-search" type="search" placeholder="例如：记忆、OSWorld、工具调用"></label>',
        '  <label>主题 <select id="paper-topic"><option value="">全部主题</option>',
    ]
    for topic in sorted({row["topic"] for row in rows}):
        lines.append(f'    <option value="{h(topic)}">{h(topic)}</option>')
    lines += ['  </select></label>', '  <label>年份 <select id="paper-year"><option value="">全部年份</option>']
    for year in sorted({row["year"] for row in rows}, reverse=True):
        lines.append(f'    <option value="{h(year)}">{h(year)}</option>')
    lines += ['  </select></label>', '  <label>类型 <select id="paper-type"><option value="">全部类型</option>']
    for kind in sorted({row["type"] for row in rows}):
        lines.append(f'    <option value="{h(kind)}">{h(kind)}</option>')
    lines += [
        '  </select></label>',
        '</div>',
        f'<p id="paper-count" aria-live="polite">显示 {len(rows)} / {len(rows)} 篇</p>',
        '<div class="paper-table-wrap"><table id="paper-table">',
        '<thead><tr><th>论文 / 年份</th><th>主题 / 类型</th><th>研究问题</th><th>核心机制</th><th>环境与指标</th><th>主要结论</th><th>局限</th><th>链接 / 核验</th></tr></thead><tbody>',
    ]
    for row in rows:
        code = f' · <a href="{h(row["code_url"])}">代码</a>' if row["code_url"] else ""
        lines.append(
            f'<tr id="paper-{h(row["id"])}" data-topic="{h(row["topic"])}" data-year="{h(row["year"])}" '
            f'data-type="{h(row["type"])}">'
            f'<td><strong>{h(row["title"])}</strong><br><small>{h(row["year"])} · {h(row["id"])}</small></td>'
            f'<td>{h(row["topic"])}<br><small>{h(row["type"])} · {h(row["route"])}</small></td>'
            f'<td>{h(row["question"])}</td><td>{h(row["mechanism"])}</td>'
            f'<td>{h(row["evaluation"])}</td><td>{h(row["conclusion"])}</td>'
            f'<td>{h(row["limitation"])}</td>'
            f'<td><a href="{h(row["paper_url"])}">论文</a>{code}'
            f'<br><small>{h(row["verified_on"])}<br>{h(row["source_status"])}</small></td></tr>'
        )
    lines += ["</tbody></table></div>", ""]
    return "\n".join(lines)


def guide_copy(name):
    source = (ROOT / name).read_text(encoding="utf-8")
    # MkDocs provides its own table of contents. GitHub's hand-written anchors
    # do not match MkDocs anchors, so omit that block in the site copies.
    if name == "README.md":
        source = re.sub(r"^## 目录\n.*?(?=^## 基础综述与概述)", "", source, flags=re.M | re.S)
    else:
        source = re.sub(r"^## Table of Contents\n.*?(?=^## Foundational Overviews & Surveys)", "", source, flags=re.M | re.S)
    return (source.replace("(README_EN.md)", "(guide-en.md)")
            .replace("(README.md)", "(guide-zh.md)")
            .replace("CONTRIBUTING.md", "contributing.md")
            .replace("(contributing.md#paper-template)", "(contributing.md)")
            .replace("(docs/", "(")
            .replace("(data/papers.csv)", "(https://github.com/Scodive/AI-Agent-Guide/blob/main/data/papers.csv)"))


def contributing_copy():
    return (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8").replace(
        "(docs/update-sop.md)", "(update-sop.md)"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify generated files without writing")
    args = parser.parse_args()
    rows = load_rows()
    outputs = {
        DOCS / "papers.md": paper_table(rows),
        DOCS / "guide-zh.md": guide_copy("README.md"),
        DOCS / "guide-en.md": guide_copy("README_EN.md"),
        DOCS / "contributing.md": contributing_copy(),
    }
    stale = [str(path.relative_to(ROOT)) for path, content in outputs.items()
             if not path.exists() or path.read_text(encoding="utf-8") != content]
    if args.check:
        if stale:
            print("Out of date: " + ", ".join(stale), file=sys.stderr)
            return 1
    else:
        for path, content in outputs.items():
            path.write_text(content, encoding="utf-8")
    print(f"Validated {len(rows)} records; {'checked' if args.check else 'rendered'} {len(outputs)} pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

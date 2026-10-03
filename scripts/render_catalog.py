#!/usr/bin/env python3
"""Validate the curated CSV and render a GitHub Markdown table manually."""

import argparse
import csv
from datetime import date
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


def cell(value):
    return value.replace("|", "\\|").replace("\r\n", "<br>").replace("\n", "<br>")


def paper_table(rows):
    lines = [
        "# 论文库",
        "",
        f"> 共 **{len(rows)}** 篇人工精选论文。最近记录核验：**{max(row['verified_on'] for row in rows)}**。"
        " 收录表示值得阅读，不代表论文结论已独立复现。代码栏留空表示未登记已核验的官方仓库。",
        "",
        "[阅读路线](reading-path.md) · [收录标准与每周 SOP](update-sop.md) · "
        "[原始 CSV](../data/papers.csv)",
        "",
        "此处为仓库内的静态表格；展示网站从 CSV 读取数据并负责搜索与筛选。",
        "",
        "| 论文 / 年份 | 主题 / 类型 | 研究问题 | 核心机制 | 环境与指标 | 主要结论 | 局限 | 链接 / 核验 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        code = f' · [代码]({row["code_url"]})' if row["code_url"] else ""
        values = [
            f'<a name="paper-{row["id"]}"></a>**{row["title"]}**<br>{row["year"]} · {row["id"]}',
            f'{row["topic"]}<br>{row["type"]} · {row["route"]}',
            row["question"], row["mechanism"], row["evaluation"],
            row["conclusion"], row["limitation"],
            f'[论文]({row["paper_url"]}){code}<br>{row["verified_on"]}<br>{row["source_status"]}',
        ]
        lines.append("| " + " | ".join(cell(value) for value in values) + " |")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify generated files without writing")
    args = parser.parse_args()
    rows = load_rows()
    outputs = {
        DOCS / "papers.md": paper_table(rows),
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

# Contributing to AI-Agent-Guide

Thank you for helping maintain the guide. The long-form `README.md` and `README_EN.md` explain the field; `data/papers.csv` is the single source for the curated paper table. Read the [selection criteria and weekly SOP](docs/update-sop.md) before submitting a paper.

## Suggest a paper

Open an Issue with its stable paper URL, the research problem it addresses, its main mechanism, the evaluation setting, and why it adds something missing from the current catalog. A new preprint is welcome when its identity and evidence can be checked. Citation counts, GitHub stars, and venue labels alone are not selection criteria.

## Submit a catalog change

1. Confirm the title, authors, arXiv ID, year, and any venue claim on the paper or official proceedings page. Confirm that a code repository is linked by the authors before filling `code_url`.
2. Search `data/papers.csv` for the arXiv ID and title. Update an existing row for a new version or a correction.
3. Add or edit one CSV row. Complete the question, mechanism, evaluation setting and metrics, supported conclusion, and limitation. Put the date you checked sources in `verified_on`. Leave unconfirmed code links blank.
4. Record the candidate, source, and decision in `data/candidate-log.md`.
5. Run `python3 scripts/render_catalog.py` and `python3 scripts/render_catalog.py --check`. Commit the CSV and generated `docs/papers.md` together.
6. In the PR, state what was added or corrected and link the primary sources. If the paper changes the recommended path or monthly selection, update those pages too.

The render script is run **manually** and uses only the Python standard library. This repository does not automatically fetch or accept new papers, and does not build or deploy a website. The separate presentation website consumes the CSV and topic Markdown files.

## Other contributions

Broken links, factual corrections, clearer limitations, reading-path improvements, translations, and accessibility fixes are welcome. Please link the relevant source when correcting a factual claim. For large taxonomy changes, open an Issue first so readers can review the proposed categories.

## Weekly review

Weekly maintenance reviews recent papers, older omissions, the technical coverage of the whole guide, and the teaching logic of the reading paths. Each proposed conceptual change should identify the current passage, the learning problem, the primary evidence, the relationship between old and new methods, and the concrete revision. Follow the [weekly SOP](docs/update-sop.md) and [report template](docs/weekly-review-template.md).

Save the completed analysis in `data/weekly-reviews/YYYY-MM-DD.md` and leave the proposed edits local for the maintainer to review. Wait for explicit approval for that week's changes before staging, committing, pushing, or creating a PR. Preserve previous unreviewed work and distinguish it from the current week's edits.

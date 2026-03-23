# Contributing to AI-Agent-Guide

Thank you for your interest in contributing! This guide is a community-maintained reference for AI Agents, and contributions are what make it great.

---

## Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Paper Submission Template](#paper-submission-template)
- [Quality Standards](#quality-standards)
- [How to Submit a PR](#how-to-submit-a-pr)
- [Suggesting New Sections](#suggesting-new-sections)
- [Code of Conduct](#code-of-conduct)

---

## Ways to Contribute

| Contribution Type | How |
|:---|:---|
| 📄 Add a paper / resource | Open a Pull Request with your addition |
| 🐛 Fix a broken link | Open a Pull Request with the corrected URL |
| ✏️ Correct inaccurate info | Open a Pull Request with the fix |
| 💡 Suggest a new section | Open a GitHub Issue or Discussion |
| 🌐 Translation improvements | Open a Pull Request targeting `README.md` or `README_EN.md` |

---

## Paper Submission Template

When adding a new paper, please use the following format in the appropriate section:

```markdown
- **[Paper Title]** ([Authors], [Year])

  [2-3 sentence description: what problem it solves, what method it proposes, why it matters for AI Agents.]

  [arXiv: XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX) / [GitHub](https://github.com/...)
```

**Example:**

```markdown
- **ReAct: Synergizing Reasoning and Acting in Language Models** (Yao et al., 2022)

  ReAct interleaves reasoning traces and task-specific actions in LLMs, enabling dynamic reasoning grounded in real-world information through a Think-Act-Observe loop. This effectively reduces hallucination in tool-augmented agents and became a standard agent paradigm.

  [arXiv: 2210.03629](https://arxiv.org/abs/2210.03629) / [GitHub](https://github.com/ysymyth/ReAct)
```

---

## Quality Standards

To maintain the guide's reliability, submitted papers or resources must meet **at least one** of these criteria:

### For Academic Papers
- [ ] Published at a major venue: NeurIPS, ICLR, ICML, ACL, EMNLP, CVPR, AAAI, IJCAI, etc.
- [ ] **OR** Highly-cited preprint: 100+ citations on Semantic Scholar / Google Scholar
- [ ] **OR** Widely recognized work that significantly influenced the field

### For Open-Source Projects / Tools
- [ ] 500+ GitHub stars
- [ ] Actively maintained (commit within the last 6 months)
- [ ] Directly relevant to building, evaluating, or understanding AI Agents

### For All Entries
- [ ] Publicly accessible (arXiv link, open GitHub repo, or open-access paper)
- [ ] Directly relevant to AI Agent architecture, capabilities, safety, or evaluation
- [ ] Not a duplicate of an existing entry
- [ ] Description is written in **the language of the file being edited** (English for `README_EN.md`, Chinese for `README.md`)

---

## How to Submit a PR

1. **Fork** this repository
2. **Create a new branch**: `git checkout -b add/paper-name-or-feature`
3. **Make your changes** to `README.md` and/or `README_EN.md`
4. **Verify** all links work by clicking them
5. **Submit a Pull Request** with:
   - A clear title: `[Add] Paper Title` or `[Fix] Description of fix`
   - A brief description of what you added and why it belongs
6. A maintainer will review and merge within a few days

---

## Suggesting New Sections

If you believe an important topic area is missing entirely:

1. **Check existing issues/discussions** to avoid duplicates
2. **Open a GitHub Issue** titled: `[Section Proposal] Topic Name`
3. Include:
   - Why this topic is important for AI Agents
   - 3-5 key papers or resources you would include
   - Which existing section it most closely relates to

Large structural changes (new top-level sections) require discussion before a PR is submitted.

---

## Updating Both READMEs

This repo maintains parallel Chinese (`README.md`) and English (`README_EN.md`) versions. When adding content, please update **both files** if possible. If you're not comfortable with both languages, note this in your PR and a maintainer can handle the translation.

---

## Code of Conduct

Be respectful and constructive. We welcome contributors from all backgrounds and experience levels. Focus on the merit of ideas, not the person proposing them.

Any form of harassment or discrimination will not be tolerated.

---

**Thank you for helping make AI-Agent-Guide better for everyone! ⭐**

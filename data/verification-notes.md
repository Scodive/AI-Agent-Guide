# 文献核验记录 · 截至 2026-09-27

首批 40 篇核心条目的标题与 arXiv 编号已对照原始摘要页，使用初次上载年份作为 CSV 的 `year`。表格中的研究问题、机制、环境和局限是供阅读导航的简述；没有逐项复现论文实验，也没有批量确认正式会议录状态。首批 `source_status` 标为 `arXiv record (venue unverified)`。

## 9 月精选增补（10 篇）

2026-09-26 再核对 10 篇的 arXiv 摘要页，将标题、初次提交月份、研究对象、作者报告的样本量或任务量与结论边界写入 [本月精选](../docs/monthly-picks.md)及 CSV。新增条目 `source_status` 标为 `arXiv preprint (venue unverified)`；精选页里的数字均为作者报告，未独立复现。CoCoBench 初次提交于 8 月 28 日，其余 9 篇在 9 月提交。Scanning the Harness 采用 9 月 24 日修订版的标题。没有可确认的官方代码仓库时，`code_url` 留空。

原始摘要页：[DAREBench](https://arxiv.org/abs/2609.06059)、[τ^τ-Bench](https://arxiv.org/abs/2609.04611)、[Spurious Tool Use](https://arxiv.org/abs/2609.16268)、[DolphinBench](https://arxiv.org/abs/2609.24971)、[CoCoBench](https://arxiv.org/abs/2608.28266)、[Are We There Yet?](https://arxiv.org/abs/2609.00524)、[Scanning the Harness](https://arxiv.org/abs/2609.07360)、[Who Finishes the Job?](https://arxiv.org/abs/2609.26847)、[The Work Behind Delegation](https://arxiv.org/abs/2609.24234)、[AI-Research Agents in the Wild](https://arxiv.org/abs/2609.11975)。

## Harness 与 RSI 专题增补（2026-09-27，7 篇）

本次新增 [Code as Agent Harness](https://arxiv.org/abs/2605.18747)、[The Scaffold Effect](https://arxiv.org/abs/2607.22585)、[GEPA](https://arxiv.org/abs/2507.19457)、[Gödel Agent](https://arxiv.org/abs/2410.04444)、[Darwin Gödel Machine](https://arxiv.org/abs/2505.22954)、[AlphaEvolve](https://arxiv.org/abs/2506.13131)、[Recursive self-improvement of AI research agents](https://arxiv.org/abs/2609.26457)。标题、首次上载年份、摘要中的机制和实验范围已对照 arXiv 原始页面；GEPA、Gödel Agent 和 Darwin Gödel Machine 的代码链接由论文页面所指向的项目仓库核对。其余新增条目不填未经确认的代码链接。论文库共 57 篇；专题仅作人工选读与机制导航。

**概念边界：**GEPA 论文研究提示词优化；AlphaEvolve 的主要优化对象是目标算法；Darwin Gödel Machine 和 AIDE² 研究 Agent 自身代码的迭代修改。不能把这些工作合并为“基础模型自行升级”的证据。Codex 的产品机制以 [OpenAI 官方架构文档](https://developers.openai.com/api/docs/guides/agents-api/architecture)和[长任务案例](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)为准，单独作为产品资料，不作为 arXiv 论文行。

旧导读中已更正的串号包括：

| 原条目 | 错误链接 | 核对后的链接 |
| --- | --- | --- |
| A-MEM | `2501.09136`（实际为 Agentic RAG 综述）；英文版另用 `2502.00592`（M+） | [arXiv:2502.12110](https://arxiv.org/abs/2502.12110) |
| Self-Evolving Agents 综述 | `2502.12345`（数学论文） | [arXiv:2507.21046](https://arxiv.org/abs/2507.21046)，并改用该论文的真实标题 |
| Agent-R1 | `2601.08888`（引力物理论文） | [arXiv:2511.14460](https://arxiv.org/abs/2511.14460)，并改用该论文的真实标题 |
| SeeClick | `2401.09045`（数学论文） | [arXiv:2401.10935](https://arxiv.org/abs/2401.10935) |
| MultiAgentBench | 中文版代码链接指向 AgentBench | 去掉未核验的错误代码链接 |

每周新增或修订的具体来源与去留原因记在 [candidate-log.md](candidate-log.md)。本文是截至上述日期的核验记录，不应被解释成对整个领域的穷尽检索。

# AI Agent 研究指南

从研究问题出发阅读 Agent 论文。导读解释概念与脉络；[论文库](papers.md)保存可筛选、可核验的核心条目。

> 核心库每周人工维护，**不承诺收录每天所有新论文**。当前篇数及最近核验日期见[论文库](papers.md)。

## 新手阅读路线

先读综述和架构，再看一个完整的“推理—行动”循环，最后进入你关心的环境与评估。推荐的 10 个阅读步骤见[新手阅读路线](reading-path.md)。

## 按问题探索

| 我想了解的问题 | 从这里开始 |
| --- | --- |
| Agent 如何规划并使用工具？ | [规划与推理、工具与行动](papers.md) |
| Coding Agent 的模型、工具和运行环境怎样协同工作？ | [Agent Harness 与 Codex](harness.md) |
| Agent 如何记住并利用过去的经验？ | [记忆与检索](papers.md) |
| Agent 怎样改进自己的提示词、逻辑或代码？ | [RSI 与自我改进](rsi.md) |
| Agent 如何操作界面与代码仓库？ | [感知与 GUI、代码智能体](papers.md) |
| 多 Agent 协作到底解决什么问题？ | [多智能体](papers.md) |
| 如何评估能力、安全和自我演进？ | [评估与安全、自我演进](papers.md) |

仓库内的论文库提供静态表格，展示网站从 `data/papers.csv` 读取论文并负责搜索与筛选。每条记录列出实验环境与指标、主要结论、局限和核验日期。

## 本月精选

最近一期是[2026 年 9 月编辑精选](monthly-picks.md)，共十篇，并说明推荐理由与证据边界。10 月精选按 SOP 在月底整理。

**2026-10-03 周更：**论文库新增 5 篇，含 3 篇 10 月 1 日提交的新论文和 2 篇 9 月遗漏补收。先从 [VISTA](papers.md#paper-2610.02200)、[Mingbird](papers.md#paper-2610.02001)了解视觉和小模型 Harness，再用 [Beyond the Model](papers.md#paper-2609.32459)比较组件效果；[RAC](papers.md#paper-2610.00980)与 [Self-Healing Harness](papers.md#paper-2609.24130)分别讨论动态协作和持久规则修改。它们均按预印本收录。

**2026-10-05 周审查：**库从 62 增至 67 篇：新增近期的 [CMP](papers.md#paper-2610.02070)、[Incident-Arena](papers.md#paper-2610.00648)，补收 [MemGPT](papers.md#paper-2310.08560)、[LATS](papers.md#paper-2310.04406)、[τ²-Bench](papers.md#paper-2506.07982)。重点修订记忆可见性、搜索反馈、RSI 分类、MCP 权限和多 Agent 协作边界，详见[完整周报](../data/weekly-reviews/2026-10-05.md)。均为本地待审修改，网站上线另行核验。

## 保留的完整指南

[中文完整指南](../README.md) · [English guide](../README_EN.md)

新论文建议按[收录标准与每周更新 SOP](update-sop.md)提交。核心库中的简短结论是阅读导航，不替代原论文，也不表示独立复现。

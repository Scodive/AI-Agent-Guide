# 新手阅读路线

这条路线从概念走到可执行 Agent，再到评估。按顺序读前六步，就能建立主要术语；后四步可按兴趣选读。完整字段见[论文库](papers.md)。

| 顺序 | 论文 | 读它要回答的问题 |
| --- | --- | --- |
| 1 | [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) | Agent 的基本模块是什么？ |
| 2 | [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) | 如何描述记忆、行动空间与决策循环？ |
| 3 | [ReAct](https://arxiv.org/abs/2210.03629) | 推理与行动如何交替？ |
| 4 | [Toolformer](https://arxiv.org/abs/2302.04761) | 模型如何学习工具调用？ |
| 5 | [A-MEM](https://arxiv.org/abs/2502.12110) | 长期记忆如何动态组织？ |
| 6 | [AgentBench](https://arxiv.org/abs/2308.03688) | 如何跨交互环境评估 Agent？ |
| 7 | [OSWorld](https://arxiv.org/abs/2404.07972) | 桌面操作与文本任务的评估差异是什么？ |
| 8 | [SWE-bench](https://arxiv.org/abs/2310.06770) + [SWE-agent](https://arxiv.org/abs/2405.15793) | 任务设计和 Agent 接口如何共同影响代码修复？ |
| 9 | [MetaGPT](https://arxiv.org/abs/2308.00352) | 多 Agent 的角色分工如何设计？ |
| 10 | [AgentHarm](https://arxiv.org/abs/2410.09024) | 有害行为怎样进入多步 Agent 评估？ |

**阅读时记录四件事：**研究问题、关键机制、实验环境与指标、结论适用的边界。基础方法论文（例如 CoT）可作为背景阅读，但不应被当成完整 Agent 系统的实证结果。

完成基础路线后，可按兴趣进入[Agent Harness 与 Coding Agent](harness.md)或[RSI 与自我改进](rsi.md)。前者关注模型如何在工具、环境和验证循环中工作；后者关注系统实际修改了自身的哪一部分。

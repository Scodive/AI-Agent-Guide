# 新手阅读路线

这条路线从概念走到可执行 Agent，再到评估。按顺序读前六步，就能建立主要术语；后四步可按兴趣选读。完整字段见[论文库](papers.md)。

| 顺序 | 论文 | 读它要回答的问题 |
| --- | --- | --- |
| 1 | [A Survey on Large Language Model based Autonomous Agents](https://arxiv.org/abs/2308.11432) | Agent 的基本模块是什么？ |
| 2 | [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) | 如何描述记忆、行动空间与决策循环？ |
| 3 | [ReAct](https://arxiv.org/abs/2210.03629) | 推理与行动如何交替？ |
| 4 | [Toolformer](https://arxiv.org/abs/2302.04761) | 模型如何学习工具调用？ |
| 5 | [MemGPT](https://arxiv.org/abs/2310.08560) → [A-MEM](https://arxiv.org/abs/2502.12110) | 先理解外部记忆如何进入上下文，再看长期记忆如何动态组织。 |
| 6 | [AgentBench](https://arxiv.org/abs/2308.03688) | 如何跨交互环境评估 Agent？ |
| 7 | [OSWorld](https://arxiv.org/abs/2404.07972) | 桌面操作与文本任务的评估差异是什么？ |
| 8 | [SWE-bench](https://arxiv.org/abs/2310.06770) + [SWE-agent](https://arxiv.org/abs/2405.15793) | 任务设计和 Agent 接口如何共同影响代码修复？ |
| 9 | [MetaGPT](https://arxiv.org/abs/2308.00352) | 多 Agent 的角色分工如何设计？ |
| 10 | [AgentHarm](https://arxiv.org/abs/2410.09024) | 有害行为怎样进入多步 Agent 评估？ |

**阅读时记录四件事：**研究问题、关键机制、实验环境与指标、结论适用的边界。基础方法论文（例如 CoT）可作为背景阅读，但不应被当成完整 Agent 系统的实证结果。

完成基础路线后，可按兴趣进入[Agent Harness 与 Coding Agent](harness.md)或[RSI 与自我改进](rsi.md)。前者关注模型如何在工具、环境和验证循环中工作；后者关注系统实际修改了自身的哪一部分。

## 把经典机制接到近期问题

- **开始前**：区分模型、运行框架、执行环境和任务；知道工具请求、工具执行与状态变化是三件事。遇到不熟悉的运行循环，先读 [Harness](harness.md) 的五步拆解。
- **步骤 3 之后**：ReAct → ToT → [LATS](https://arxiv.org/abs/2310.04406) → SWE-Search。比较搜索对象、反馈来源、回退能力与预算，而非按年份理解成升级阶梯。LATS 的正确性 oracle 是要识别的实验条件。
- **步骤 5 之后**：[CMP](https://arxiv.org/abs/2610.02070)检查未曝光记忆的效用是否可识别，再用 DolphinBench 看任务、成本与时延。CMP 的实验池包含相关性标签，尚不支持直接部署淘汰策略。
- **步骤 5/7 之后**：[Component Routing](https://arxiv.org/abs/2610.01787)比较同一份 GUI 经验进入上下文还是权重；先区分信息可见性与参数学习，再看状态依赖、留出任务和费用。它不是通用路由定律，也不单独证明 RSI。
- **步骤 8 的对照**：SWE-bench → [Agentless](https://arxiv.org/abs/2407.01489) → SWE-agent → SWE-Search。分别看预定阶段、动态动作接口和分支搜索，比较相同任务/模型/预算下新增机制的价值；保留原十步，只补固定流程基线。
- **步骤 6/8 之后**：[τ²-Bench](https://arxiv.org/abs/2506.07982)看人与 Agent 共同控制状态；[τ^τ-Bench](https://arxiv.org/abs/2609.04611)看构建 Agent；[Incident-Arena](https://arxiv.org/abs/2610.00648)看服务恢复、修改范围与修复持久性。三个研究对象分别是协作执行、系统构建、运维恢复。
- **步骤 6/10 之后**：[时间跨度统计审查](https://arxiv.org/abs/2610.12466)区分人类完成时间与 Agent 运行时间；[HarnessSecurity-Bench](https://arxiv.org/abs/2610.07639)把正常任务收益、攻击效果和成本分开。前者是统计估计阅读，后者是运行对照；不能只看一个总分。
- **步骤 9 之后**：[RAC](https://arxiv.org/abs/2610.00980)用运行时选择补固定分工，并提供“增加机制未必增益”的小样本边界；不要从这一项推断所有多 Agent 系统的优劣。

每个分支都补问：论文测的是哪个任务分母、是否等预算、失败由谁定义、收益能迁移到哪里？2026-10-12 增补保留原十步；Agentless、Component Routing、VERSE 是较早补收。RSI 拓展读 GEPA/DGM/AIDE² 后进入 [VERSE 的两层改进](rsi.md#执行器改进与改进器改进2026-10-12)。CMP 已核对 v3（10 月 8 日），曝光预算随候选池扩张，动态记忆流的相关性还会影响方差；不据此推荐自动淘汰。

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

## 按问题进入拓展路线

所有分支先区分模型、Harness、执行环境和工作负载；再记录任务分母、预算、反馈来源、失败与未评分运行。不按发表年份理解成升级阶梯。

### 规划需要什么时候读取环境？

步骤 3 之后，对照 ReAct 的逐步观察与 [ReWOO](papers.md#paper-2305.18323)的“预写计划—工具填证据—合并答案”。再读 ToT → [LATS](papers.md#paper-2310.04406) → SWE-Search，区分思维分支和可执行动作搜索。预规划可能受未知环境限制；搜索的节点、轨迹、token 和环境调用要一起计费，LATS 的正确性 oracle 与状态可回退是假设，真实不可逆动作要另处理。

在 ReAct/ReWOO 之后加读 [DynaRev](papers.md#paper-2610.40133)：把“目标固定、观察变化”与“用户修改目标”分开，保留有效约束和环境进度。先看修订何时送达，再读 WRA 与完整任务成功，二者分母不同。

### 界面操作后如何确认结果与切换模型？

步骤 7 之后，OSWorld → [VeriCUA](papers.md#paper-2610.40578) → [LEASH](papers.md#paper-2610.22280)。先区分画面、动作历史和持久产物，再区分未决结果与模型失败风险。LEASH 是 10 月 15 日的较早补收，需要隐状态、参考库和门控校准的前置知识；切换强模型不同于人工批准，也不自动扩大权限。见 [Harness 的结果取证与接管](harness.md#界面结果取证与模型接管)。

### 保存、共享和学习分别改变了什么？

步骤 5 之后，MemGPT → A-MEM → [CMP](papers.md#paper-2610.02070) → [DolphinBench](papers.md#paper-2609.24971)：从存取、组织、效用识别走到任务与成本。CMP 的实验池含相关性标签，不能直接当淘汰策略。用 [MCCL](papers.md#paper-2610.29357)的载体/内容/策略分类回看这条路线，再问延迟、干扰、变化与迁移，而不把检索命中当持续学习。

ReAct 与步骤 5 之后先补经典 [Reflexion](papers.md#paper-2303.11366)：反馈怎样写入下一次尝试的记忆？比较每轮、累计成功与内部重试预算，再进入 RSI；固定反思规则不等于规则自身演化。

步骤5/6之后加读[Harness the Memory](papers.md#paper-2608.15008)：先固定模型与框架，再比较记忆配置、检索宽度和写/读/管理成本。其路由的随机问题分折与新对话留出结果不同，oracle组合也不是可部署选择器。四主套件、两个近似实现与单次主表限制要一起读，不能据“图记忆”或“权重记忆”名称判断优劣。

步骤 5/7 之后，[Component Routing](papers.md#paper-2610.01787)比较同一 GUI 经验进入上下文还是权重；先补参数训练与成本概念。步骤 9 之后，对照 MetaGPT/ChatDev 的固定分工、[RAC](papers.md#paper-2610.00980)的运行时选择与 [Muffin](papers.md#paper-2610.31355)的异步发现共享，再用 [CoCoBench](papers.md#paper-2608.28266)看环境协作。推理缓冲区不等于跨会话记忆，增加协调和共享条目都未必增益。

### 框架、任务结果和交付目标怎样分别验证？

步骤 8 之后，SWE-bench → [Agentless](papers.md#paper-2407.01489) → SWE-agent → SWE-Search，比较固定流程、动态接口和分支搜索。[Doc2Harness](papers.md#paper-2610.20344)另检验框架实现是否符合约定；先读 [Harness 五步循环及框架测试](harness.md#框架实现测试与任务评估分开)，理解 mock、确定性检查与正对照，再读其构建/测试协议。公开场景不是全量用例。

步骤 4/6 之后，用 [Prefix Executability](papers.md#paper-2610.40444)补过程层：参数/依赖/状态前提、首次无效动作、恢复与最终成功分别记。先读 [Harness 的过程解释](harness.md#从接口契约到过程可执行性)；PEC 不是条件错误率，RR 只在有无效前缀的轨迹上计算。

步骤4/6之后，[ToolSpace](papers.md#paper-2611.05036)补工具环境与训练数据的来历：数据/状态/重试依赖 → 状态游走 → 反向任务与断言 → 初态重放。先区分模拟/缓存和实时服务，再读训练/Pro评估；回放可解不等于所有目标断言完备。

步骤 6/8 之后，[τ²-Bench](papers.md#paper-2506.07982)测共同控制状态的执行，[τ^τ-Bench](papers.md#paper-2609.04611)测构建 Agent，[FDE-Gym](papers.md#paper-2610.22350)测需求与交付收益，[Incident-Arena](papers.md#paper-2610.00648)测恢复安全与持久性。保留各自任务对象，不合并分数；模拟客户与实际用户分开。

### 信息不足、攻击和执行错误怎样区分？

步骤 4/6 之后，先读 [写入超时查状态](harness.md#写入超时后先确认状态2026-10-19)，再看 [AgentPerturb](papers.md#paper-2610.21624)的交互扰动、[EpiSEM-Bench](papers.md#paper-2610.31650)的真实但不完整证据、[HarnessSecurity-Bench](papers.md#paper-2610.07639)的安全/效用对照。主动查证后分别检验禁止动作和允许动作；不把一律拒绝当有用恢复。

步骤 6/10 之后，[时间跨度统计审查](papers.md#paper-2610.12466)补量尺解释：人类任务用时与 Agent 运行时间不同。持续成功 `pass^k`、至少一次成功 `pass@k`、任务出现过任一违规的比例也分别解释。

### 自我改进的下一轮使用了什么？

先用 Reflexion 区分反思记忆与改进器变化，再读 [RSI 专题](rsi.md)中的 GEPA → Gödel Agent/DGM → AIDE² → [VERSE](papers.md#paper-2610.02616)，逐项记修改对象、筛选反馈和下一轮继承。该顺序是概念展开，不是能力排名。[MCCL 的状态/策略区分](rsi.md#记忆状态变化与管理策略变化)帮助判断增加记忆与改变管理规则。

在GEPA/VERSE之后读[Meta²](papers.md#paper-2611.05139)，逐项标记指导、局部补丁、模型参数、演化器谁被保留。[RSI继承面](rsi.md#可复用指导与任务内编辑)解释为何部署时冻结指导、每run重置补丁，与持续修改改进器是不同路径。

完成多 Agent 与 RSI 阅读、具备 SFT/LoRA/策略优化/价值估计基础后，再比较 [MASS](papers.md#paper-2610.12176)的工作流/共享权重与 [Terminal-RSI](papers.md#paper-2610.22192)的 actor/critic 更新；详见[反馈来源](rsi.md#参数更新与反馈来源2026-10-19)。这些拓展不改变前十步的入门顺序。

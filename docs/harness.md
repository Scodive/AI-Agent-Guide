# Agent Harness：Coding Agent 如何工作

*资料核对：2026-09-27。产品行为以链接的官方文档为准。*

**Harness（运行框架）**是围绕模型组织任务、工具、执行环境和反馈的程序。模型决定下一步要做什么；harness 决定它能看到哪些信息、怎样调用工具、命令在哪里执行、结果如何回到上下文，以及何时验证、停止或请人介入。不要把模型、harness、执行环境和评测任务混成一个“Agent 能力”数字。[OpenAI 官方架构说明](https://developers.openai.com/api/docs/guides/agents-api/architecture)明确区分 harness、environment 和 application server；[Code as Agent Harness](https://arxiv.org/abs/2605.18747)从研究角度梳理这些层次。

## 一个 Coding Agent 的工作循环

1. **接收任务和仓库上下文**：目标、约束、文件、已有差异、项目说明和可用工具进入会话。
2. **选择动作**：模型根据当前上下文提出检索、读取文件、编辑代码或运行命令等动作。
3. **执行并观察**：harness 把动作交给有权限的工具或沙箱；输出、错误和文件变化返回会话。
4. **验证与修复**：运行相关测试、构建或人工可检查的演示；失败时根据反馈修改，而非只凭“代码已写”结束。
5. **交付与监督**：展示差异、验证结果及剩余风险；需要权限或方向判断时交由人决定。

这是一种**概念性拆解**，不是某个产品内部代码的逐行复刻。[OpenAI 对 Codex 长任务的说明](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)将其概括为计划、编辑、运行工具、观察、修复和重复；[官方 Agents API 文档](https://developers.openai.com/api/docs/guides/agents-api/overview)说明 Codex harness 管理会话、编排、上下文压缩与恢复，执行环境负责命令和文件。Codex 是帮助理解这一结构的实例，不等于所有 Coding Agent 共用同一实现。

## 哪些设计会改变结果？

| 设计问题 | 观察重点 | 代表阅读 |
| --- | --- | --- |
| 模型怎样操作代码库？ | 工具的动作粒度、文件编辑接口、报错是否足够明确。 | [SWE-agent](https://arxiv.org/abs/2405.15793)研究 Agent–Computer Interface；[SWE-bench](https://arxiv.org/abs/2310.06770)提供问题修复任务。 |
| 状态怎样跨步骤保留？ | 仓库文件、上下文摘要、会话与可复查的中间产物。 | [Code as Agent Harness](https://arxiv.org/abs/2605.18747)梳理长程执行、记忆与反馈控制；[Codex 官方架构](https://developers.openai.com/api/docs/guides/agents-api/architecture)区分会话与环境。 |
| 如何判断做完？ | 测试与构建、隐藏用例、成本、超时和人工复核。 | [DAREBench](https://arxiv.org/abs/2609.06059)同时报告任务表现和资源；[τ^τ-Bench](https://arxiv.org/abs/2609.04611)检验交付的 Agent。 |
| 框架本身有多大影响？ | 固定模型时比较工具、上下文和停止策略，报告 token、时延与失败类型。 | [The Scaffold Effect](https://arxiv.org/abs/2607.22585)在有限的模型、框架和任务组合上给出初步对照。 |
| 工具与配置是否安全？ | 沙箱、权限、依赖固定、技能和 MCP 配置的来源及作用范围。 | [Scanning the Harness](https://arxiv.org/abs/2609.07360)审计公开仓库配置；配置暴露不等于真实利用。 |

## 阅读 Codex 时应分清的边界

- **Codex 模型与 Codex harness**：模型产生判断与工具请求；harness 维护循环和会话，连接工具与执行环境。不同运行方式提供的工具、权限和环境可能不同。以上以[OpenAI 官方架构文档](https://developers.openai.com/api/docs/guides/agents-api/architecture)为准。
- **仓库指令与验证**：`AGENTS.md`、技能或任务说明可以给出项目约束；它们不能代替运行测试、检查差异和确认交付条件。[OpenAI 的长任务案例](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)是一个有说明文件和阶段验证的实例，不是所有任务的效果保证。
- **安全边界**：工具可访问的文件、网络与凭据取决于执行环境；评估 Coding Agent 时应记录权限、沙箱和人工审批设置。[官方环境文档](https://developers.openai.com/api/docs/guides/agents-api/architecture)区分托管与自有执行环境。

**推荐顺序：**先读 SWE-agent 理解接口，再读 Codex 官方架构理解产品中的循环，之后用 The Scaffold Effect 和 DAREBench 检查“同一模型/不同框架”和“不同工作负载”的比较边界。相关论文的研究问题、指标、局限与核验日期见[论文库](papers.md)。

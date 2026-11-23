# AI-Agent-Guide

[English](README_EN.md) | [中文](README.md)

[![GitHub Stars](https://img.shields.io/github/stars/Scodive/AI-Agent-Guide?style=social)](https://github.com/Scodive/AI-Agent-Guide/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Scodive/AI-Agent-Guide)](https://github.com/Scodive/AI-Agent-Guide/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Scodive/AI-Agent-Guide/blob/main/CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/github/license/Scodive/AI-Agent-Guide)](https://github.com/Scodive/AI-Agent-Guide/blob/main/LICENSE)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

欢迎来到 **AI-Agent-Guide**！本仓库致力于提供一份系统、清晰且持续更新的 AI 智能体（AI Agent）研究与工程指南，帮助你从零建立完整的知识框架，并快速定位关键论文、核心机制与开源项目。

> **GitHub 看论文地图，网站学系统课程与实战代码：**
> 我们把指南进一步整理成了免费可追踪进度的在线学习站 **[AI 学习笔记（ai-notes）](https://ai-notes-red-two.vercel.app/)** —— 包含 **Agent 基础与实战、RL 与大模型后训练、AI Infra 源码精读、工程面试** 四条完整学习路线（共 70 节课程 + 配套代码实验包）。
>
> <a href="https://ai-notes-red-two.vercel.app/"><img src="assets/open-guide-zh.svg" alt="打开网站 · 开始学习" width="150" height="46"></a>

**快速导航：** [新手 10 步阅读路线](docs/reading-path.md) · [96 篇精选论文总表](docs/papers.md) · [月度精选](docs/monthly-picks.md) · [Coding Agent 与 Harness 专题](docs/harness.md) · [自我改进（RSI）专题](docs/rsi.md) · [原始数据 CSV](data/papers.csv)

> 本周审查 · 2026-11-23：增补[意图契约](docs/papers.md#paper-2611.24025)、[提示更新接受门](docs/papers.md#paper-2611.23651)、[记忆部署经验](docs/papers.md#paper-2611.26361)，以及本周修订的早期工作 [Agent Meltdowns](docs/papers.md#paper-2605.19149)；H2E 更新到 v3。分析与证据见[本期报告](data/weekly-reviews/2026-11-23.md)。

## 如何使用这份指南

如果你想系统学习基础架构，请按下方目录顺读；如果你想直接追踪最新研究问题，可以从下表切入（完整 96 篇论文检索与实验细节见 [论文库总表](docs/papers.md)）：

| 你关心的问题 | 推荐切入论文 | 在指南中的位置 |
| --- | --- | --- |
| Agent 声明了行动意图，怎样确认它真的获准？ | [Intent Contracts](docs/papers.md#paper-2611.24025) · [Agent Meltdowns](docs/papers.md#paper-2605.19149) | [Harness 与运行时](docs/harness.md#意图声明授权与环境证据) |
| 怎样确认 Agent 真正写入并读回了经验？ | [How Much Should an Agent Remember?](docs/papers.md#paper-2611.26361) | 记忆与检索 |
| 可复用提示词更新要通过哪些检查才应采用？ | [Safe Personal RSI](docs/papers.md#paper-2611.23651) | [自我改进](docs/rsi.md#提示更新的接受门与静态规则对照) |
| 跨任务的代码修改，哪些经验值得保存给下一个任务？ | [CoReMem](https://arxiv.org/abs/2611.17316) | 记忆模块 / 代码智能体 |
| 如何把大模型的规划经验蒸馏给轻量级执行器？ | [H2E](https://arxiv.org/abs/2611.16246) | 感知与具身训练 |
| 开发集上领先的 Agent 框架改动，换到新任务还有效吗？ | [drydock-eval](https://arxiv.org/abs/2611.16485) | [Harness 与评估专题](docs/harness.md) |
| 如何构建、配置并监督一个真实可用的 Coding Agent？ | [τ^τ-Bench](https://arxiv.org/abs/2609.04611)、[Scanning the Harness](https://arxiv.org/abs/2609.07360)、[The Work Behind Delegation](https://arxiv.org/abs/2609.24234) | Agentic Coding / 安全与监督 |
| 执行中途用户改了目标，或者界面变化后怎么验证真的做完了？ | [DynaRev](https://arxiv.org/abs/2610.40133)、[VeriCUA](https://arxiv.org/abs/2610.40578)、[Prefix Executability](https://arxiv.org/abs/2610.40444) | 规划、GUI 感知与过程验证 |
| 强化学习训练工具调用时，Agent 会学到哪些“偷懒捷径”？ | [Spurious Tool Use](https://arxiv.org/abs/2609.16268) | 行动与工具学习 |
| 如何科学评估长期记忆与多智能体协作？ | [DolphinBench](https://arxiv.org/abs/2609.24971)、[CoCoBench](https://arxiv.org/abs/2608.28266) | 记忆检索 / 多智能体 |
| 如何衡量真实部署下的成本、成功率与后续返工率？ | [DAREBench](https://arxiv.org/abs/2609.06059)、[Are We There Yet?](https://arxiv.org/abs/2609.00524)、[Who Finishes the Job?](https://arxiv.org/abs/2609.26847) | 评估与安全 / 代码智能体 |

## 目录

- [如何使用这份指南](#如何使用这份指南)
- [基础综述与概述](#基础综述与概述)
  - [通用智能体综述](#通用智能体综述)
  - [特定领域应用综述](#特定领域应用综述)
  - [基础模型与决策综述](#基础模型与决策综述)
- [AI智能体剖析：核心架构蓝图](#ai智能体剖析核心架构蓝图)
  - [架构蓝图相关核心论文](#架构蓝图相关核心论文)
- [感知模块：感知数字与物理世界](#感知模块感知数字与物理世界)
  - [文本感知](#文本感知)
  - [多模态感知](#多模态感知)
  - [核心技术：视觉语言模型 (Vision-Language Models, VLMs)](#核心技术视觉语言模型-vision-language-models-vlms)
  - [关键挑战](#关键挑战)
  - [相关论文与资源](#相关论文与资源)
- [规划与推理模块：智能体的认知核心](#规划与推理模块智能体的认知核心)
  - [基础推理技术演进](#基础推理技术演进)
  - [从思维树到环境反馈搜索](#从思维树到环境反馈搜索)
  - [核心推理技术对比](#核心推理技术对比)
- [记忆模块：实现学习与情境感知](#记忆模块实现学习与情境感知)
  - [记忆架构](#记忆架构)
  - [长期记忆的关键机制](#长期记忆的关键机制)
  - [相关论文与资源](#相关论文与资源-1)
  - [记忆从保存到产生作用](#记忆从保存到产生作用)
- [行动模块：执行任务与使用工具](#行动模块执行任务与使用工具)
  - [工具使用范式](#工具使用范式)
  - [工具创造范式](#工具创造范式)
  - [相关论文与资源](#相关论文与资源-2)
  - [MCP：模型上下文协议](#mcp模型上下文协议)
- [Agentic Coding：软件工程新前沿](#agentic-coding软件工程新前沿)
  - [核心系统与基准测试](#核心系统与基准测试)
  - [相关论文与资源](#相关论文与资源-3)
- [智能体开发框架：从理论到实践](#智能体开发框架从理论到实践)
  - [主流框架深度解析](#主流框架深度解析)
  - [智能体开发框架对比](#智能体开发框架对比)
  - [实战：科研技能库 (Paper-Agent-Skills)](#实战科研技能库-paper-agent-skills)
- [Self-Evolving 智能体：自我进化与自适应机制](#self-evolving-智能体自我进化与自适应机制)
  - [三类适应机制与 RSI 边界](#三类适应机制与-rsi-边界)
  - [相关论文与资源](#相关论文与资源-4)
- [多智能体系统（MAS）：协作产生的涌现智能](#多智能体系统mas协作产生的涌现智能)
  - [MAS范式与架构](#mas范式与架构)
  - [典型应用](#典型应用)
  - [关键挑战](#关键挑战-1)
  - [相关论文与资源](#相关论文与资源-5)
- [可信度：安全、对齐与评估](#可信度安全对齐与评估)
  - [对齐方法论](#对齐方法论)
  - [从结果到评估协议](#从结果到评估协议)
  - [上下文与执行权限的连接](#上下文与执行权限的连接)
  - [评估与基准测试](#评估与基准测试)
  - [相关论文与资源](#相关论文与资源-6)
- [经典与背景延伸阅读](#经典与背景延伸阅读)
  - [计算机视觉与多模态 (CV/Multimodal & GUI)](#计算机视觉与多模态-cvmultimodal--gui)
  - [自然语言处理、长链条推理与 RL (NLP/Reasoning & RL)](#自然语言处理长链条推理与-rl-nlpreasoning--rl)
  - [软件工程与系统架构 (SE/Systems)](#软件工程与系统架构-sesystems)
  - [可信度、安全与压力评估 (Trustworthiness & Safety)](#可信度安全与压力评估-trustworthiness--safety)
- [如何贡献](#如何贡献)
- [引用](#引用)

---

## 基础综述与概述
对于任何希望深入了解AI智能体领域的研究者而言，从权威的综述性论文开始是至关重要的。这些文献为整个领域提供了宏观视角、核心概念定义以及系统的技术分类，是构建知识体系的基石。本节精选了一系列高质量的综述论文，涵盖了从通用智能体架构到特定领域应用的广泛主题。

### 通用智能体综述
*   **A Survey on Large Language Model based Autonomous Agents** (Wang et al., 2023)

    这篇奠基性综述提出了一个关于 LLM 自主智能体的整体框架，系统地从构建、应用和评估三个维度梳理了早期研究，并以“画像（Profile）—记忆（Memory）—规划（Planning）—行动（Action）”来组织相关文献。

    [arXiv: 2308.11432](https://arxiv.org/abs/2308.11432)

*   **Large Language Model Agent: A Survey on Methodology, Applications and Challenges** (Luo et al., 2025)

    该综述以方法论为中心，系统地解构了LLM智能体系统。它深入探讨了智能体的架构基础、协作机制和演化路径，旨在统一碎片化的研究线索，揭示智能体设计原则与其复杂环境中涌现行为之间的内在联系 。

    [arXiv: 2503.21460](https://arxiv.org/abs/2503.21460) / [GitHub仓库](https://github.com/luo-junyu/Awesome-Agent-Papers)

*   **Agentic Large Language Models, a survey** (Plaat et al., 2025)

    这篇综述将智能体LLM（Agentic LLM）的核心能力归纳为三个方面：推理（reason）、行动（act）和交互（interact）。论文围绕这三个类别组织文献，清晰地展示了不同研究方向如何相互促进，例如，信息检索如何赋能工具使用，反思机制如何改善多智能体协作等 。

    [arXiv: 2503.23037](https://arxiv.org/abs/2503.23037) / [Website](https://askeplaat.github.io/agentic-llm-survey-site/)

### 特定领域应用综述
*   **A Survey of Large Language Model Agents for Question Answering** (2025)

    专注于智能体在问答（QA）任务中的应用。该文系统回顾了LLM智能体在QA流程中的设计，涵盖了规划、问题理解、信息检索和答案生成等关键阶段，并探讨了当前面临的挑战与未来研究方向 。

    [arXiv: 2503.19213](https://arxiv.org/abs/2503.19213)

*   **A Survey of Large Language Model Empowered Agents for Recommendation and Search** (Zhang et al., 2025)

    探讨了LLM智能体在增强推荐系统和搜索引擎方面的变革性潜力。论文首次系统地回顾和分类了LLM智能体在信息检索领域的研究，为下一代信息检索系统提供了新的视角 。

    [arXiv: 2503.05659](https://arxiv.org/abs/2503.05659)

*   **Large Language Model-based Data Science Agent: A Survey** (Wang et al., 2025)

    该综述全面分析了专为数据科学任务设计的LLM智能体。它从智能体和数据科学两个视角出发，构建了一个双重视角框架，将通用的智能体设计原则与数据科学的实际工作流程（如数据预处理、模型开发、评估、可视化等）联系起来 。

    [arXiv: 2508.02744](https://arxiv.org/abs/2508.02744)

### 基础模型与决策综述
*   **Foundation Models for Decision Making: Problems, Methods, and Opportunities** (Yang et al., 2023)

    这篇论文探讨了基础模型在更广泛的决策制定领域的应用，为理解智能体的行为提供了必要的背景知识。它回顾了如何通过提示、生成建模、规划、最优控制和强化学习等方法，将基础模型应用于实际的决策任务中 。

    [arXiv: 2303.04129](https://arxiv.org/abs/2303.04129)


---


## AI智能体剖析：核心架构蓝图
一个现代 AI 智能体通常可以从**感知、规划与推理、记忆、行动**四个核心视角来拆解。它们共同构成智能体与环境持续交互的决策循环：

*   **感知模块 (Perception Module)**：智能体与环境交互的入口，负责接收并处理来自外部世界的原始信息（用户指令、API 返回文本、屏幕截图等），转化为内部可理解的结构化表示。

*   **规划与推理模块 (Planning & Reasoning Module)**：智能体的认知核心，负责理解目标并制定执行策略，将复杂任务拆解为具体的子步骤或行动序列。

*   **记忆模块 (Memory Module)**：赋予智能体跨步骤和跨会话学习能力的关键，包括短期记忆（当前上下文）与长期记忆（历史经验、偏好与外部知识库）。

*   **行动模块 (Action Module)**：将内部决策转化为真实世界影响的执行器，通过调用外部工具（代码解释器、搜索引擎、API、数据库等）完成实际操作。

信息在这四个部分之间形成闭环：**感知环境状态 → 结合记忆进行规划 → 执行行动改变环境 → 再次感知新状态**，如此循环直至任务完成。

在工程落地时，除了大模型本身的决策能力，外部的 **运行框架（Agent Harness）** 同样决定系统上限——它负责上下文组织、工具接口、执行权限、状态持久化以及停止/验收条件（详见 [Code as Agent Harness](https://arxiv.org/abs/2605.18747) 与 [Harness 专题](docs/harness.md)）。

### 架构蓝图相关核心论文

*   **Cognitive Architectures for Language Agents (CoALA)** (Sumers et al., 2023)
    
    借鉴认知科学与符号 AI，提出了模块化记忆、内外部行动空间与标准化决策循环，为设计和比较不同语言智能体提供了清晰的理论词汇。
    
    [arXiv: 2309.02427](https://arxiv.org/abs/2309.02427)

*   **OpenAgents: An Open Platform for Language Agents in the Wild** (Xie et al., 2023)
    
    开源通用智能体平台，集成了数据分析、插件调用与网页浏览三类 Agent 及交互界面，是学习工具宿主与真实用户工作流的经典工程实例。
    
    [arXiv: 2310.10634](https://arxiv.org/abs/2310.10634) / [GitHub仓库](https://github.com/xlang-ai/OpenAgents)

---

## 感知模块：感知数字与物理世界
感知是智能体连接世界的桥梁，是其所有后续思考和行动的基础。该模块负责从环境中接收原始数据，并将其转化为规划模块能够理解和利用的结构化信息 。感知能力的强弱，直接决定了智能体能够有效运作的环境的复杂性。

### 文本感知
这是最基础的感知形式，智能体通过处理纯文本输入来理解其任务和环境。这些输入可以来自多种来源，例如用户的自然语言指令、从文件中读取的文档内容，或是调用API后返回的文本结果 。

### 多模态感知
随着智能体应用场景从纯文本环境扩展到图形用户界面（GUI）、网页乃至物理世界，多模态感知能力变得至关重要。它使智能体能够“看见”和理解视觉信息，从而与为人类设计的系统进行交互。

### 核心技术：视觉语言模型 (Vision-Language Models, VLMs)
VLMs是多模态感知的技术基石。这类模型通过结合视觉编码器和语言模型，学习图像/视频等视觉数据与文本数据之间的深层关联 。这使得智能体不仅能处理文本，还能理解屏幕截图中的按钮、文本框、图标等视觉元素，这是执行任何GUI操作的前提 。

### 关键挑战
尽管VLMs取得了巨大进展，但在智能体感知应用中仍面临诸多挑战：

*   **元素定位 (Element Grounding)**：精确识别并定位GUI界面上可交互元素（如按钮、输入框）的坐标是极其困难的。即便是最先进的通用VLM，在这方面的表现也常常不尽如人意，这是因为它们通常被训练用于图像描述或分类，而非像素级的精确定位 。

*   **高分辨率输入处理**：GUI截图通常是高分辨率的，将其输入VLM会产生极长的Token序列，导致计算成本高昂且效率低下。需要专门的优化技术来处理UI视觉信息中的冗余和结构化特征 。

*   **环境干扰**：真实世界中的GUI环境充满了与核心任务无关的视觉信息，如广告弹窗、促销信息、推荐内容等。研究表明，即使是顶尖的GUI智能体也容易被这些视觉“干扰物”分散注意力，从而偏离用户的原始意图，影响其任务的忠实度 。

### 相关论文与资源
*   **综述: Agent AI: Surveying the Horizons of Multimodal Interaction** (Durante et al., 2024)

    该综述将“Agent AI”定义为能够感知视觉刺激和其他接地数据以产生具身行动的系统，为多模态智能体的研究划定了范围。

    [arXiv: 2401.03568](https://arxiv.org/abs/2401.03568)

*   **论文: OmniParser for Pure Vision Based GUI Agent** (Lu et al., 2024)

    微软开源的纯视觉 UI 解析器，通过可交互区域检测、图标语义描述与 OCR 生成结构化元素，辅助 VLM 精确定位屏幕按钮与输入框，在 ScreenSpot、Mind2Web 等基准上显著提升了操作准确率。

    [arXiv: 2408.00203](https://arxiv.org/abs/2408.00203) / [GitHub仓库](https://github.com/microsoft/OmniParser)

*   **论文: Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception** (Wang et al., 2024)

    介绍了一个纯视觉驱动的移动设备智能体，它无需依赖系统底层的 XML 布局文件，仅通过分析屏幕截图就能自主导航和操作 App，展示了视觉感知在跨平台通用性方面的潜力。

    [arXiv: 2401.16158](https://arxiv.org/abs/2401.16158) / [GitHub仓库](https://github.com/X-PLUG/MobileAgent)

*   **论文: ScreenSpot: A Grounding Benchmark for GUI Agents** (Cheng et al., 2024)

    专门评测 GUI 元素定位能力的跨平台基准，覆盖移动端、桌面端和网页端，揭示了通用 VLM 在细粒度界面坐标定位上的核心瓶颈。

    [arXiv: 2401.10935](https://arxiv.org/abs/2401.10935) / [GitHub仓库](https://github.com/njucckevin/SeeClick)

**GUI 操作后的结果验证与执行器训练：**
在真实界面操作中，看懂按钮不等于任务真的成功——完整的链路应拆解为**元素定位 → 执行动作 → 持久状态改变 → 满足目标**。[VeriCUA](https://arxiv.org/abs/2610.40578) 在动作执行后联合检查屏幕画面、操作历史与底层文件/数据库状态，解决“按钮点完但文件没保存”的假成功问题（详见 [Harness 专题](docs/harness.md#界面结果取证与模型接管)）。在具身与导航场景中，[H2E](https://arxiv.org/abs/2611.16246) 提出将大模型规划器的工具调用与 VLA 运动统一重标为任务动作、训练轻量执行器并移除教师模型，显著降低了部署开销。

H2E 的 11 月 16–17 日修订新增 NavRAG-CE，并从第一轮失败轨迹收集教师恢复会话再训练；因此更新 v1 的实验范围，不能沿用 v1“未学会偏航恢复”的笼统结论。恢复指标有特定偏航定义，并不表示解决所有偏航；100 题教师比较的蒸馏配方也与主表不同。这些仍是导航仿真结果，详见[论文库记录](docs/papers.md#paper-2611.16246)。

---

## 规划与推理模块：智能体的认知核心
规划与推理模块是智能体的“大脑”，负责制定实现目标的策略。它接收来自感知模块的信息，并将其核心任务——即一个高层次的用户目标——分解成一个具体的、可执行的步骤序列 。LLM推理能力的演进是驱动智能体能力发展的核心动力，从最初简单的线性思维链，发展到能够与环境交互并进行复杂探索的策略。


### 基础推理技术演进
1.  **思维链 (Chain-of-Thought, CoT) 与自洽性 (Self-Consistency)**
    概念：CoT是解锁LLM复杂推理能力的奠基性技术。它通过在提示中加入“一步一步地思考”（Let's think step by step）的指令或示例，引导模型在给出最终答案前，先生成一系列中间推理步骤 。这种方式模拟了人类解决问题的过程，显著提升了模型在算术、常识和符号推理任务上的表现。

    自洽性是对CoT的进一步增强，它通过对同一个问题进行多次采样，生成多个不同的思维链，然后通过“投票”选出最一致的答案，从而提高了结果的鲁棒性和准确性 。

    奠基论文:
    *   **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (Wei et al., 2022)

        [arXiv: 2201.11903](https://arxiv.org/abs/2201.11903)
    *   **Self-Consistency Improves Chain of Thought Reasoning in Language Models** (Wang et al., 2022)

        [arXiv: 2203.11171](https://arxiv.org/abs/2203.11171)

2.  **ReAct: 融合推理与行动**
    概念：ReAct框架是一个范式上的飞跃，它将推理（Thought）和行动（Action）交错进行。智能体首先生成一个“思考”，用于分析当前情况并制定下一步计划；然后，它执行一个“行动”，例如调用搜索引擎API来获取缺失的信息。行动的结果会作为新的观察被反馈给智能体，用于下一轮的“思考”。这种“思考-行动-观察”的循环，使得智能体的推理能够被外部世界的真实信息所“接地”，有效缓解了纯内部推理（如CoT）容易产生的知识幻觉问题 。

    奠基论文: **ReAct: Synergizing Reasoning and Acting in Language Models** (Yao et al., 2022)

    [arXiv: 2210.03629](https://arxiv.org/abs/2210.03629) / [GitHub仓库](https://github.com/ysymyth/ReAct)


3.  **思维树 (Tree of Thoughts, ToT)**
    概念：ToT进一步突破了CoT和ReAct的线性推理模式。当面对需要探索或深思熟虑的问题时，ToT允许模型同时探索多条不同的推理路径，并将这些路径组织成一棵“思维树”。在这个过程中，LLM不仅扮演着“思考者”的角色，还扮演着“评估者”的角色：它会自我评估树中每个节点（即每个中间“想法”）的价值和前景，然后决定是继续深入探索某条路径（lookahead），还是放弃当前路径并返回到之前的节点尝试其他可能性（backtracking）。这种机制赋予了智能体进行系统性搜索和深思熟虑决策的能力 。

    奠基论文: **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (Yao et al., 2023)

    [arXiv: 2305.10601](https://arxiv.org/abs/2305.10601) / [GitHub仓库](https://github.com/princeton-nlp/tree-of-thought-llm)
    
### 从思维树到环境反馈搜索

- **搜索可执行行动（[LATS](https://arxiv.org/abs/2310.04406)）**：将 ReAct 与 ToT 结合，用蒙特卡洛树搜索（MCTS）在真实环境反馈下探索多条行动轨迹，并在失败后回传反思。适合代码修复、网页导航等可回溯环境；若涉及不可逆操作（如支付或生产变更），需先做沙盒隔离或人工确认。
- **固定流程 vs. 动态搜索**：在代码修复领域，[Agentless](https://arxiv.org/abs/2407.01489) 采用“定位 → 生成 → 验证”的固定三段式流水线，成本可控；SWE-agent 允许模型动态决定工具动作；SWE-Search 则引入分支搜索。三者各有成本与自由度权衡，选型时需结合预算与任务复杂度比较。
- **先规划、再填证据（[ReWOO](https://arxiv.org/abs/2305.18323)）**：由 Planner 一次性写出带依赖变量的完整计划，Worker 并行调用工具填入证据，最后由 Solver 汇总，大幅减少多轮回传观察带来的 Token 消耗。适合工具依赖关系明确的任务；若环境信息需逐步试探发现，仍更适合 ReAct 循环。
- **动态目标修订（[DynaRev](https://arxiv.org/abs/2610.40133)）**：针对用户在中途追加或修改需求的情况，先区分当前仍有效的约束、已作废的约束与可复用的进度再重规划，避免盲目从头重跑。

### 核心推理技术对比
下表总结了不同推理范式的核心思路与适用场景，实际工程中常按任务成本与环境特征组合使用：

| 技术名称      | 核心思想                                     | 主要优势                                           | 适用场景                                         |
| :------------ | :------------------------------------------- | :------------------------------------------------- | :----------------------------------------------- |
| Chain-of-Thought (CoT) | 通过中间步骤分解复杂问题                     | 提升LLM在复杂推理任务上的性能                  | 算术、常识和符号推理                               |
| Self-Consistency | 对CoT结果进行多样本投票，提高鲁棒性         | 提高答案的准确性和稳定性                           | 对结果准确性要求高的推理任务                     |
| ReAct         | 交错的“思考-行动-观察”循环                     | 缓解知识幻觉，将推理与外部世界“接地”           | 需要与外部工具（如搜索引擎）交互的任务           |
| Tree of Thoughts (ToT) | 探索多条推理路径，自我评估和回溯             | 应对需要探索和深思熟虑的复杂问题，系统性搜索     | 需要多步决策、有多种可能路径的问题               |
| MCTS-based (LATS / SWE-Search) | 基于环境反馈的蒙特卡洛树搜索与迭代优化 | 系统性探索大状态空间，支持失败反思回传 | 代码库修复、复杂网页交互等长链条任务 |

---

## 记忆模块：实现学习与情境感知
记忆使智能体能够利用历史交互与经验来优化后续决策。理解记忆系统时，可以重点关注三类载体：**当前可见的上下文、跨会话持久化的外部存储、以及固化在模型参数中的知识**。

### 记忆架构
*   **短期记忆 (Short-Term Memory)**：模型当前调用可见的上下文窗口，受限于窗口长度。运行框架通常通过滑动窗口、摘要压缩等方式决定哪些会话历史被保留或重新载入。

*   **长期记忆 (Long-Term Memory)**：跨会话持久化保存事实、用户偏好和历史经验，通常存储在外部文件、数据库或向量索引中，在需要时检索注入上下文。

### 长期记忆的关键机制
*   **检索增强生成 (Retrieval-Augmented Generation, RAG)**：在响应请求前先从外部知识库（文档、数据库或历史经验库）中检索相关片段作为上下文，让生成有据可依，减少知识幻觉。

*   **智能体化RAG (Agentic RAG)**：将自主决策引入检索流程——智能体可以根据检索效果动态重构查询、切换数据源，或协同执行多跳检索，以应对复杂问题。

*   **向量数据库 (Vector Databases)**：高效 RAG 的基础设施，将非结构化数据转化为向量以支持语义相似度搜索；工程上常与关键词检索（BM25）结合使用以兼顾精确匹配与语义召回。

### 相关论文与资源
*   **论文: Cognitive Memory in Large Language Models** (2025)

    该论文深入探讨了LLM中的记忆机制，并巧妙地将人类的认知记忆架构（感觉记忆、短时记忆、长时记忆）与LLM的记忆系统进行了类比分析。

    [arXiv: 2504.02441](https://arxiv.org/abs/2504.02441)

*   **论文: A-Mem: Agentic Memory for LLM Agents** (2025)

    提出了一种新颖的“智能体化记忆”系统（A-Mem）。受知识管理方法Zettelkasten的启发，该系统允许智能体根据新的经验动态地组织、链接和演化其记忆，而不是简单地被动存储。

    [arXiv: 2502.12110](https://arxiv.org/abs/2502.12110) / [GitHub仓库](https://github.com/agiresearch/A-mem)

*   **论文: From Local to Global: A Graph RAG Approach to Query-Focused Summarization** (Edge et al., 2024)

    微软提出的一种结合知识图谱与大语言模型的检索增强生成技术 (GraphRAG)。通过在全量文本上构建结构化的知识图谱，它能够掌握文档集中的全局信息并应对复杂的针对性总结任务，大幅提升了 RAG 处理海量关联信息的能力。

    [arXiv: 2404.16130](https://arxiv.org/abs/2404.16130) / [GitHub仓库](https://github.com/microsoft/graphrag)

*   **综述: Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG** (Singh et al., 2025)

    这是一篇关于Agentic RAG的全面综述，详细介绍了将智能体集成到RAG流程中的各种架构、应用和挑战。

    [arXiv: 2501.09136](https://arxiv.org/abs/2501.09136)

*   **向量数据库:** [Weaviate](https://weaviate.io/) · [Chroma](https://www.trychroma.com/) · [Qdrant](https://qdrant.tech/) · [Pinecone](https://www.pinecone.io/)

### 记忆从保存到产生作用

一条经验要真正提升后续任务表现，需经过**保存 → 检索 → 注入上下文 → 影响决策 → 定期淘汰/更新**五个环节。近期研究围绕这五个环节提出了关键方法：

- **分页与分层调度（[MemGPT](https://arxiv.org/abs/2310.08560)）**：借鉴操作系统的虚拟内存机制，通过函数调用在“有限上下文”与“外部持久存储”之间动态换入换出信息（A-MEM 侧重知识图式组织，MemGPT 侧重调度控制，两者互补）。
- **失败反思记忆（[Reflexion](https://arxiv.org/abs/2303.11366)）**：将失败轨迹转化为自然语言“教训”写入有界记忆，供固定权重模型在下一轮尝试时规避重复错误（注意：多次试错的累计成功率应与单次通过率分开评估）。
- **记忆效用识别（[CMP](https://arxiv.org/abs/2610.02070)）**：一条从未被检索进上下文的记忆，日志里显示“无贡献”可能只是没被测试到；通过随机曝光与留存评估才能更准确地做记忆淘汰。
- **经验载体路由（[Component Routing](https://arxiv.org/abs/2610.01787)）**：把 GUI 经验拆成元素定位、操作流程、状态事实和失败教训四类，分别判断哪些适合放进提示词上下文、哪些更适合微调进模型权重。
- **持续学习与配置比较（[MCCL](https://arxiv.org/abs/2610.29357) / [Harness the Memory](https://arxiv.org/abs/2608.15008)）**：在固定框架下对齐检索宽度与写入成本，区分“内容更新”与“管理策略更新”，并在新对话留出集上验证长期留存与跨任务迁移能力。
- **面向下一任务的记忆估值（[CoReMem](https://arxiv.org/abs/2611.17316)）**：从同一仓库历史状态出发，配对对比“带记忆 vs. 无记忆”在下一未知代码任务上的表现，把真正带来修复收益的定位线索与检查项保留下来。

[How Much Should an Agent Remember?](https://arxiv.org/abs/2611.26361) 把检查延伸到写入链路：提炼教训、保留来源与支持计数地合并、再回读确认 Agent 确实使用了指导。高频教训仍可能错误；测试集调参和有限重复也限制其“不同模型需要不同记忆量”的解释。另需区分删除一条记录和持续遗忘：Safe Personal RSI 的单条删除探针保留了可再提取的来源，未测试独立的主体级遗忘路径。见[记忆验证与遗忘](docs/rsi.md#单条删除与持续遗忘分开检验)。

---

## 行动模块：执行任务与使用工具
行动模块是智能体将其内部决策转化为外部世界实际影响的桥梁。正是通过这个模块，智能体才得以超越单纯的语言生成，通过调用API、执行代码或操作软件等方式与环境进行交互，成为一个能够解决实际问题的“实干家” 。

### 工具使用范式
赋予智能体使用工具的能力是提升其实用价值的关键。当前的研究主要集中在两个方向：如何让智能体学会使用已有的工具，以及如何让智能体创造新的工具。

1.  **自监督的工具学习**
    这种范式旨在让LLM能够在没有大量人工标注的情况下，自主学会如何使用外部工具。

    *   **Toolformer**: 这是一项开创性的工作。其核心思想是，让一个预训练的LLM在大量文本上进行“自我训练”。模型会尝试在文本的各个位置插入API调用，并观察这样做是否能帮助它更好地预测后续的文本。如果一个API调用（及其返回结果）显著降低了模型预测的难度（即降低了损失函数的值），那么这个API调用就被认为是有益的，并被保留下来形成一条新的训练数据。通过在这种自生成的数据上进行微调，LLM最终学会了在合适的时机、以合适的参数调用合适的API 。

2.  **掌握海量真实世界API**
    要让智能体在现实世界中发挥作用，它必须能够调用成千上万个真实、多样的API。

    *   **Gorilla**: 针对LLM在生成API调用时准确性不足的问题，Gorilla项目通过在一个大规模、高质量的API调用数据集上微调LLaMA模型，使其在API调用的准确性上超越了GPT-4。特别地，它引入了“检索器感知训练”（Retriever-Aware Training）机制，使得模型能够在推理时结合最新的API文档进行决策，从而适应API的频繁变更 。

    *   **ToolLLM**: 该框架旨在弥合开源模型与闭源模型在工具使用能力上的差距。研究者构建了一个名为ToolBench的超大规模指令微调数据集，其中包含了超过16000个真实世界的RESTful API。通过在ToolBench上微调LLaMA，得到的ToolLLaMA模型在处理复杂指令和泛化到未见过的API方面，表现出与ChatGPT相当的强大能力 。

### 工具创造范式
这代表了智能体能力的一个新高度：从工具的使用者变为工具的创造者。

*   **LLMs as Tool Makers (LATM)**: 该框架提出了一个创新的两阶段流程。在“工具创造”阶段，一个能力强大但成本高昂的LLM（如GPT-4）扮演“工具创造者”的角色，根据任务需求生成可复用的Python函数作为工具。在“工具使用”阶段，一个更轻量、更经济的LLM扮演“工具使用者”的角色，直接调用这些已生成好的工具来完成任务。这种分工模式，将一次性的高昂创造成本分摊到多次的低成本使用中，极大地优化了智能体系统的整体效费比 。

### 相关论文与资源
*   **论文: Toolformer: Language Models Can Teach Themselves to Use Tools** (Schick et al., 2023)

    [arXiv: 2302.04761](https://arxiv.org/abs/2302.04761)

*   **论文: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering** (Jimenez et al., 2024)

    针对自动化软件工程任务，该研究团队提出了 SWE-agent 系统。它通过专门设计的“智能体-计算机接口” (Agent-Computer Interface, ACI)，极大地提升了 LLM 在浏览代码库、查看、编辑和执行代码时的效率，在 SWE-bench 测试中表现卓越。

    [arXiv: 2405.15793](https://arxiv.org/abs/2405.15793) / [GitHub仓库](https://github.com/princeton-nlp/SWE-agent)

*   **论文: Gorilla: Large Language Model Connected with Massive APIs** (Patil et al., 2023)

    [arXiv: 2305.15334](https://arxiv.org/abs/2305.15334) / [GitHub仓库](https://github.com/ShishirPatil/gorilla)
    

*   **论文: ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs** (Qin et al., 2023)

    [arXiv: 2307.16789](https://arxiv.org/abs/2307.16789) / [GitHub仓库](https://github.com/OpenBMB/ToolBench)
    

*   **论文: LLMs as Tool Makers** (Cai et al., 2023)

    [arXiv: 2305.17126](https://arxiv.org/abs/2305.17126)

### MCP：模型上下文协议

**模型上下文协议（Model Context Protocol, MCP）** 是 Anthropic 提出的开放标准，为 AI 智能体与外部工具、数据源之间提供“USB-C 式”的统一连接协议，大幅降低了重复编写工具适配代码的工作量。

在工程落地 MCP 时，建议重点把控三件事：
1. **权限与安全分层**：MCP 协议只负责工具描述与通信，认证、授权与沙盒隔离必须由服务端和运行框架分别落实，遵循最小权限原则（参见官方 [MCP 安全实践](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices)）。
2. **区分失败类型与超时恢复**：[MCP 工具规范](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)区分了协议错误与业务执行错误（`isError`）；遇到写操作超时，应先查服务端回执确认状态再决定是否幂等重试（具体恢复流程见 [Harness 专题](docs/harness.md#写入超时后先确认状态2026-10-19)）。
3. **过程可执行性与合成环境验证**：
   - [AgentPerturb](https://arxiv.org/abs/2610.21624) 评测了输入缺失、冗余和错误扰动下的工具调用鲁棒性。
   - [Prefix Executability](https://arxiv.org/abs/2610.40444) 在工具契约和当前状态下追踪“首个无效动作”，把参数合法性与最终任务成功分开评估（详见 [Harness 专题](docs/harness.md#从接口契约到过程可执行性)）。
   - [ToolSpace](https://arxiv.org/abs/2611.05036) 通过提取工具间的数据流与状态依赖自动合成可重放训练任务，为工具学习提供低成本沙盒环境。

**关键资源：**
- [官方 MCP 规范](https://modelcontextprotocol.io/)
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)——社区精选服务器列表
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)


---

## Agentic Coding：软件工程新前沿

Agentic Coding（智能体化编码）是 AI 智能体商业影响力最显著的前沿方向之一。有别于简单的代码补全，这类智能体能够操作完整代码库——理解复杂软件架构、定位 Bug、撰写跨文件补丁、执行测试并迭代优化，直到问题解决。

### 核心系统与基准测试

**标准基准：**

- **SWE-bench**：评估编码智能体的标准基准，包含来自主流 Python 项目（Django、scikit-learn 等）的 2,294 个真实 GitHub Issue。智能体须分析代码库并提交能解决 Issue 的补丁。SWE-bench Verified 为人工核验的高质量子集。

  [官网](https://www.swebench.com/) / [arXiv: 2310.06770](https://arxiv.org/abs/2310.06770) / [GitHub](https://github.com/princeton-nlp/SWE-bench)

**开源智能体与基线：**

- **Agentless**：一个极具启发性且极简的非 Agent 固定流水线基线——依次完成定位、补丁/测试采样与投票筛选，不依赖模型自主选择工具动作，为衡量复杂 Agent 架构的“额外投入产出比”提供了清晰参照。

  [arXiv: 2407.01489](https://arxiv.org/abs/2407.01489) / [GitHub](https://github.com/OpenAutoCoder/Agentless)

- **SWE-agent**（普林斯顿，2024）：设计了专门用于导航和编辑大型代码库的智能体-计算机接口（ACI），提供带行号的文件查看器、定向搜索和编辑命令等专为 LLM 优化的工具，在 SWE-bench 上表现优异。

  [arXiv: 2405.15793](https://arxiv.org/abs/2405.15793) / [GitHub](https://github.com/princeton-nlp/SWE-agent)

- **OpenHands（原 OpenDevin）**：开源 AI 软件开发智能体平台，可浏览网页、编写和执行代码、管理文件，支持多种后端 LLM。

  [GitHub](https://github.com/All-Hands-AI/OpenHands)

- **SWE-Search**（2024）：将蒙特卡洛树搜索（MCTS）与 LLM 软件智能体深度融合，通过在大型代码-行动空间中进行系统性探索与迭代优化，显著提升了 Issue 解决率。

  [arXiv: 2410.20285](https://arxiv.org/abs/2410.20285) / [GitHub](https://github.com/aorwall/moatless-tools)

- **AutoCodeRover**（2024）：结合程序抽象语法树（AST）结构搜索与 LLM 推理，高效定位并修复代码缺陷。

  [arXiv: 2404.05427](https://arxiv.org/abs/2404.05427) / [GitHub](https://github.com/nus-apr/auto-code-rover)

**从补丁生成到真实软件交付：**
写对一个补丁只是第一步。工程实践中还需要关注**运行框架设计（[Harness 导读](docs/harness.md)）、PR 合并后的后续返工维护（[Who Finishes the Job?](https://arxiv.org/abs/2609.26847)）以及持续负载与重启下的故障恢复能力（[Incident-Arena](https://arxiv.org/abs/2610.00648)）**。

### 相关论文与资源
- **SWE-bench: Can Language Models Resolve Real-world GitHub Issues?** (Jimenez et al., 2023) — [arXiv: 2310.06770](https://arxiv.org/abs/2310.06770)
- **Devin: The First AI Software Engineer** (Cognition AI, 2024) — [官方博客](https://cognition.ai/blog/introducing-devin) / [官网](https://cognition.ai/)
- **SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search** (2024) — [arXiv: 2410.20285](https://arxiv.org/abs/2410.20285)

---

## 智能体开发框架：从理论到实践
理解智能体的模块化架构是理论基础，但从零开始构建一个功能完备、稳定可靠的智能体应用仍然是一项复杂的工程。智能体开发框架的出现，通过提供高级抽象、丰富的集成和强大的工具集，极大地简化了这一过程，使开发者能够更专注于业务逻辑而非底层实现 。

### 主流框架深度解析
当前，社区已经涌现出几个主流的智能体开发框架，它们各自具有不同的设计哲学和最佳适用场景。

1.  **LangChain & LangGraph**
    核心定位: 一个高度模块化的通用LLM应用开发框架。

    特点: LangChain的核心思想是将LLM应用中的各个环节（如模型调用、数据连接、记忆管理）封装成可互操作的“组件”，然后通过“链”（Chains）或“图”（Graphs）的方式将这些组件灵活地组合起来。其最大的优势在于其庞大的集成生态（支持数百种LLM、数据库、API）和极高的灵活性，非常适合快速原型验证和构建功能多样的智能体应用 。LangGraph作为其演进，提供了对智能体循环和状态管理的更精细化、更明确的控制，适合构建更复杂的、有状态的智能体 。

    代码库: [LangChain GitHub](https://github.com/langchain-ai/langchain)

2.  **LlamaIndex**
    核心定位: 一个以数据为中心的RAG应用开发框架。

    特点: LlamaIndex的独特价值主张是为基于私有数据构建LLM应用提供一站式解决方案。它的核心功能围绕着数据的摄取（Ingestion）、索引（Indexing）和查询（Querying）展开。如果你应用的核心需求是让LLM能够高效、准确地查询和理解你的私有知识库（无论是PDF、数据库还是API），LlamaIndex提供了最优化的工具链和抽象层 。

    代码库: [LlamaIndex GitHub](https://github.com/run-llama/llama_index)

3.  **AutoGen**
    核心定位: 一个专注于多智能体对话的框架。

    特点: 由微软研究院推出，提供了一套定义不同角色、对话模式与多智能体协同的抽象层，是学习多智能体对话编排的经典项目（注：截至 2026 年 10 月其[官方仓库](https://github.com/microsoft/autogen)已进入维护模式，新项目可关注其继任者 Microsoft Agent Framework）。

    代码库: [AutoGen GitHub](https://github.com/microsoft/autogen)

4.  **MS-Agent**
    核心定位: 一个轻量级框架，赋能智能体自主探索复杂任务场景。

    特点: MS-Agent 提供了一个灵活且可扩展的架构，使开发者能够创建具备复杂任务处理能力的智能体，例如代码生成、数据分析以及支持 MCP（模型上下文协议）的通用工具调用。其特点包括：
    *   **通用多智能体 (Multi-Agent for general purpose)**: 支持基于 MCP 的工具调用能力，实现智能体对话。
    *   **深度研究 (Deep Research)**: 赋能智能体进行自主探索和执行复杂研究任务的高级能力。
    *   **代码生成 (Code Generation)**: 支持代码生成任务，并产生相应的产物。
    *   **轻量级与可扩展 (Lightweight and Extensible)**: 易于扩展和定制，适用于各种应用场景。

    代码库: [MS-Agent GitHub](https://github.com/modelscope/ms-agent)

5.  **CrewAI**
    核心定位: 面向团队角色扮演的多智能体编排框架。

    特点: CrewAI 将智能体组织为职责明确的“团队（Crew）”，支持层级式与顺序式任务流，API 简洁直观，社区生态活跃，适合快速搭建角色分工明确的多智能体工作流。

    代码库: [CrewAI GitHub](https://github.com/crewAIInc/crewAI)

### 智能体开发框架对比
对于开发者而言，选择合适的框架是项目成功的关键第一步。下表根据各个框架的核心设计理念和主要优势，提供了一个清晰的选型指南。

| 框架        | 核心抽象         | 主要用例                   | 关键优势                         |
| :---------- | :--------------- | :------------------------- | :------------------------------- |
| LangChain / LangGraph | 组件链/状态图 | 复杂、有状态的通用 LLM 应用 | 极高的模块化程度与集成生态 |
| LlamaIndex  | 数据索引/查询引擎 | 构建基于私有数据的智能体 (RAG) | 以数据为中心的索引和检索优化     |
| AutoGen     | 可对话的智能体 (Conversable Agents) | 多智能体对话原型（维护模式） | 灵活的多智能体对话编排范式     |
| MS-Agent    | 自主探索、工具调用 | 代码生成、数据分析、通用工具调用 | 轻量级、多模态、支持 MCP         |
| CrewAI      | 角色驱动团队 (Crews) | 团队协作与角色分工工作流   | API 简洁直观，上手成本低         |

### 实战：科研技能库 (Paper-Agent-Skills)
为了展示智能体如何学习并执行复杂的垂直领域任务，我们提供了一个实战项目：**[Paper-Agent-Skills](https://github.com/Scodive/Paper-Agent-Skills)**。

该项目采用了基于技能（Skill-based）的架构，将学术研究中的高阶能力（如论文撰写、Rebuttal 策略、Slides 生成）封装为可复用的智能体模块。

*   **核心特性**:
    *   **模式提取**: 从顶会（NeurIPS, ICLR, CVPR）的 Best Paper 中提取论证逻辑和修辞模式。
    *   **可解释性**: 不同于黑盒生成，智能体通过明确的“技能工作流”展示其思考过程。
    *   **安全对齐**: 内置引用校验机制，防止学术幻觉。
*   **应用价值**: 该库展示了如何将 LLM 的通用推理能力转化为高度专业化的科研生产力工具。

---

## Self-Evolving 智能体：自我进化与自适应机制

“自我进化（Self-Evolving）”涵盖了从经验积累到修改自身源码的多个层次。理解这个方向时，建议按**修改对象、反馈来源、是否持续继承**三个维度来区分：

### 三类适应机制与 RSI 边界

1. **技能与记忆积累**：如 Voyager 持续沉淀可执行技能库，A-MEM 动态组织知识图谱，[Reflexion](https://arxiv.org/abs/2303.11366) 将错误反馈总结成文字教训。这类方式扩充的是“外部经验”，模型参数和底层逻辑保持不变。
2. **提示词与程序自我修改（RSI）**：如 [GEPA](https://arxiv.org/abs/2507.19457) 优化提示词与工作流，[Darwin Gödel Machine](https://arxiv.org/abs/2505.22954) 让智能体直接修改自身代码并在基准上筛选保留，实现真正的**递归自我改进（RSI）**。关键看两点：被接受的新版本是否继续参与下一轮改进，以及在留出任务上是否产生真实迁移收益。
   - [VERSE](https://arxiv.org/abs/2610.02616) 进一步把“改进执行器”和“改进优化器自身的 Harness”拆成两层闭环，验证优化器自我演化的作用边界。
   - [Meta²](https://arxiv.org/abs/2611.05139) 则提供另一种运行时思路：离线提炼通用指导原则并在部署时冻结，单次任务中只做局部 Harness 补丁，任务结束后重置，避免局部补丁污染后续任务。
3. **参数级自我演进与 Agentic RL**：如 DeepSeek-R1、Agent-R1 利用可验证奖励训练推理与工具策略；[MASS](https://arxiv.org/abs/2610.12176) 交替优化多智能体工作流与共享模型权重；[Terminal-RSI](https://arxiv.org/abs/2610.22192) 则在终端任务中结合轨迹监督与策略优化进行迭代强化（更多细节见 [RSI 专题](docs/rsi.md)）。

[Safe Personal RSI](https://arxiv.org/abs/2611.23651) 补充可复用提示更新的接受门：比较现版与提案，诊断失败、尝试修复，没有通过就保留父版本。模型权重和运行时固定；已知攻击族重用、宽泛手写规则达到同样结果，限制了自主改进的解释。先理解采用条件，再讨论递归性，详见 [RSI 专题](docs/rsi.md#提示更新的接受门与静态规则对照)。

### 相关论文与资源

*   **论文: Voyager: An Open-Ended Embodied Agent with Large Language Models** (Wang et al., 2023)

    开创性的自演进具身智能体系统。在《Minecraft》开放世界中，Voyager 提出了包含“自动课程生成”、“无尽技能库”与“迭代自我反思”的三元架构，实现了无需人类标注的技能自演进与持续探索。

    [arXiv: 2305.16291](https://arxiv.org/abs/2305.16291) / [GitHub仓库](https://github.com/MineDojo/Voyager)

*   **论文: A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence** (2025)

    系统梳理了自我演进智能体的分类体系，从演进组件（模型、记忆、工具、架构）、适应阶段与反馈机制三个角度搭建全景图谱。

    [arXiv: 2507.21046](https://arxiv.org/abs/2507.21046)

*   **论文: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** (DeepSeek, 2025)

    展示了纯强化学习（R1-Zero）与冷启动多阶段 RL（R1）在长链条推理和自我反思上的突破，为推理型 Agent 的基座训练奠定了基础。

    [arXiv: 2501.12948](https://arxiv.org/abs/2501.12948) / [GitHub仓库](https://github.com/deepseek-ai/DeepSeek-R1)

*   **论文: Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning** (2025)

    将端到端强化学习引入多步环境交互智能体，直接基于环境反馈优化工具调用与规划决策。

    [arXiv: 2511.14460](https://arxiv.org/abs/2511.14460) / [GitHub](https://github.com/AgentR1/Agent-R1)

*   **论文: MOAE: Multi-Objective Agent Evolution with Pareto-Preserving Search** (2026)

    在固定模型权重下，针对任务表现、轨迹质量与安全性进行多目标诊断并演化执行策略，通过保留 Pareto 非支配候选在多个基准上实现无参数更新的稳健权衡。

    [arXiv: 2609.05992](https://arxiv.org/abs/2609.05992)

---

## 多智能体系统（MAS）：协作产生的涌现智能
多智能体系统（Multi-Agent Systems, MAS）通过角色分工、通信与共享产物来解决复杂任务。设计 MAS 时不仅要看角色编排，也要在同等预算下对比“单智能体 + 强工具”是否更划算，并留意交接开销与错误级联。

近期在协作机制上的前沿探索包括：
- **运行时动态选人（[RAC](https://arxiv.org/abs/2610.00980)）**：根据当前执行状态动态选择下一位协作者，并揭示了过度堆叠“契约 + 验证”规则反而可能拖累协作效率的现象。
- **共享模型训练（[MASS](https://arxiv.org/abs/2610.12176)）**：把编排者与执行者的多 Agent 交互轨迹汇总，用于联合微调同一个共享基座模型。
- **异步共享缓冲区（[Muffin](https://arxiv.org/abs/2610.31355)）**：各智能体把局部推理保留在内部，仅将带来源标注的阶段性发现追加写入共享缓冲区，同伴可按窗口异步读取而无需等待整轮同步。

### MAS范式与架构

*   **协作模式**: MAS中的智能体可以根据任务需求组织成不同的拓扑结构。这可以是一个简单的线性流水线，每个智能体负责一个环节；也可以是一个扁平化的“圆桌会议”，所有智能体平等地进行辩论和投票；还可以是一个层级化的结构，由一个“管理者”智能体进行任务分解和协调，并将子任务分配给“执行者”智能体 。

*   **沟通机制**: 沟通是MAS的命脉，是实现集体智能的关键。智能体之间的交互通常通过结构化的自然语言进行。有效的沟通机制设计，包括通信协议、内容格式以及交互策略（如何时发言、向谁发言），对于确保协作效率和避免混乱至关重要 。

### 典型应用
*   **协同软件开发 (ChatDev)**: ChatDev项目生动地展示了MAS在复杂任务中的应用潜力。它构建了一个虚拟的软件开发公司，其中包含了CEO、产品经理、程序员、测试工程师、文档工程师等多个角色的智能体。当接收到一个高级需求（例如，“开发一个五子棋游戏”）后，这些智能体会通过一个预设的“聊天链”（Chat Chain）流程，遵循经典的瀑布模型，依次进行设计、编码、测试和文档编写等阶段的协作，最终交付一个完整的软件包。这展示了如何通过结构化的多智能体对话来自动化复杂的、创造性的工作流程 。

### 关键挑战
尽管MAS前景广阔，但其设计和实现也带来了新的、独特的挑战：

*   **任务分配优化**: 如何根据每个智能体的专长，动态且最优地分配任务和子任务 。

*   **上下文管理**: MAS中的上下文是多层次的，既有全局任务的上下文，也有每个智能体自身的上下文，还有智能体之间共享的局部上下文。如何有效管理这些复杂的、分层的上下文信息是一个巨大的挑战 。

*   **群体记忆**: 除了单个智能体的记忆，如何为整个智能体团队设计一个共享的、一致的、可更新的“集体记忆”系统，以支持长期协作和学习，也是一个开放的研究问题 。

### 相关论文与资源
*   **综述: Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems** (2025)

    该综述从“沟通”这一核心视角来剖析MAS，为理解多智能体协作的内在机制提供了一个新颖的框架。

    [arXiv: 2502.14321](https://arxiv.org/abs/2502.14321)

*   **论文: MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework** (Hong et al., 2023)

    利用标准操作程序 (SOPs) 对大语言模型进行元编程，将人类工作流编排进多智能体协作框架中，通过角色分工与结构化文档产物组织需求、设计与代码生成。

    [arXiv: 2308.00352](https://arxiv.org/abs/2308.00352) / [GitHub仓库](https://github.com/geekan/MetaGPT)

*   **论文: Generative Agents: Interactive Simulacra of Human Behavior** (Park et al., 2023)

    著名的“斯坦福小镇”研究。该工作赋予了沙盒环境中25个虚拟角色各自的记忆流 (Memory Stream)，角色可以观察、回忆、反思并与其他成员自然交流，展现出惊人的社会互动涌现能力，为构建真实的社会化多智能体系统提供了开创性范式。

    [arXiv: 2304.03442](https://arxiv.org/abs/2304.03442) / [GitHub仓库](https://github.com/joonspk-research/generative_agents)

*   **论文: ChatDev: Communicative Agents for Software Development** (Qian et al., 2023)

    [arXiv: 2307.07924](https://arxiv.org/abs/2307.07924) / [GitHub仓库](https://github.com/OpenBMB/ChatDev)
    

*   **开发框架**: AutoGen（维护模式）与 CrewAI 等框架为多智能体对话与团队编排提供了工程起点，详见上方开发框架章节。

---

## 可信度：安全、对齐与评估
随着智能体变得日益自主，并被赋予在真实世界中采取行动的能力，确保其行为的可信度（Trustworthiness）已成为该领域最重要、最紧迫的议题。一个强大的智能体如果行为不可预测、不符合人类价值观或存在安全漏洞，其潜在风险将远超其带来的益处。因此，智能体的安全（Safety）、与人类价值观的对齐（Alignment）以及对其行为的严格评估（Evaluation）构成了可信度研究的三大支柱 。

### 对齐方法论
*   **宪法AI (Constitutional AI, CAI)**: 由Anthropic公司提出的一种创新的对齐技术。传统对齐方法（如RLHF）严重依赖人类标注者来判断模型的输出是否“好”。CAI则试图让AI在一定程度上“自我对齐”。其核心思想是，首先为AI制定一套原则或价值观，即“宪法”（Constitution）。然后，在训练过程中，模型不仅要生成对用户问题的回答，还要根据“宪法”自我批判和修正其回答。这个过程被称为“来自AI反馈的强化学习”（Reinforcement Learning from AI Feedback, RLAIF）。通过这种方式，CAI旨在使对齐过程更具可扩展性、透明度和一致性，减少对大规模人工标注的依赖 。

*   **防御机制**: 除了在训练阶段进行对齐，还需要在部署时采取防御措施。研究人员正在探索多种防御策略，例如，在智能体的“大脑”前后部署外部的“守卫”模型，用于过滤恶意输入和审查不安全的输出；或者利用多智能体系统，通过辩论、审查等方式，集体增强决策的鲁棒性和安全性 。

### 从结果到评估协议

评价一个智能体不能只看单次任务的表面通过率，近年评测研究正在向**交互协议、过程合规、成本与恢复力**四个维度演进：

- **交互与构建基准**：[τ²-Bench](https://arxiv.org/abs/2506.07982) 评测 Agent 与用户在共享环境中的协同执行；[τ^τ-Bench](https://arxiv.org/abs/2609.04611) 进一步要求端到端构建并交付一个可运行的客服 Agent；[FDE-Gym](https://arxiv.org/abs/2610.22350) 则评估需求信息不完整时的澄清与交付收益。
- **过程可执行性与结果取证**：[Prefix Executability](https://arxiv.org/abs/2610.40444) 定位工具调用序列中的首个无效步骤，[VeriCUA](https://arxiv.org/abs/2610.40578) 在操作后结合底层状态检查持久化结果，[Incident-Arena](https://arxiv.org/abs/2610.00648) 将验收延伸到持续负载与系统重启后的故障恢复。
- **统计规范与鲁棒性**：报告实验时需同时给出预算（token、时延、调用次数）并区分 `pass@k`（至少成功一次）与 `pass^k`（多次稳定成功）。关于“时间跨度（horizon）”统计口径、[AgentPerturb](https://arxiv.org/abs/2610.21624) 扰动测试、[EpiSEM-Bench](https://arxiv.org/abs/2610.31650) 证据缺失查证，以及 [Doc2Harness](https://arxiv.org/abs/2610.20344) / [drydock-eval](https://arxiv.org/abs/2611.16485) 对运行框架实现契约与留出集确认的检验，详见 [Harness 专题](docs/harness.md) 与 [METR 统计审查](https://arxiv.org/abs/2610.12466)。

### 上下文与执行权限的连接

智能体安全不能只靠模型自身对齐或外挂“守卫”模型，必须建立**上下文信任边界**与**最小执行权限隔离**：
- [CPE](https://arxiv.org/abs/2609.01222) 揭示了低信任来源的内容如何被提升到高优先级或持久化上下文中从而引发越权风险。
- [HarnessSecurity-Bench](https://arxiv.org/abs/2610.07639) 在同一模型与任务下同时对比“正常任务效用”与“攻击成功率”，帮助衡量安全开关的实际代价（详见 [Harness 安全对照](docs/harness.md#保护是否有效同时测正常任务与攻击效果)）。

[Intent Contracts](https://arxiv.org/abs/2611.24025) 把规划器声明的目标与执行器生成的命令分开，但执行器缺少环境证据时，未授权动作并未优于盲审。[Agent Meltdowns](https://arxiv.org/abs/2605.19149) 则补普通工具故障下的越界恢复：没有攻击者也可能出错。应分别核对声明、真实目标、权限和执行效果，不能由意图清楚或任务完成推断已获授权；详见 [Harness 专题](docs/harness.md#意图声明授权与环境证据)。

### 评估与基准测试
*   **AgentBench**: 这是一个针对单智能体能力的综合性评估基准。它包含了8个不同的、精心设计的环境，覆盖了从操作系统交互、数据库查询到网页浏览等多种真实世界任务，旨在全面评估LLM作为智能体的推理和决策能力 。

*   **MultiAgentBench**: 这是一个专为多智能体系统设计的评估基准。与AgentBench不同，它不仅关注最终的任务完成情况，更侧重于评估智能体在协作和竞争场景中的互动质量。它通过新颖的、基于里程碑的关键绩效指标（KPIs）来衡量智能体之间的协作效率和竞争策略的有效性 。

### 相关论文与资源
*   **论文: Why Agents Compromise Safety Under Pressure** (Jiang et al., 2026)

    首个提出智能体压力概念，探讨非主动攻击情况下智能体和环境交互影响准确性的现象，为智能体安全开辟了新的视角。
    
    [arXiv: 2603.14975](https://arxiv.org/abs/2603.14975)

*   **论文: Constitutional AI: Harmlessness from AI Feedback** (Bai et al., 2022)

    [arXiv: 2212.08073](https://arxiv.org/abs/2212.08073)

*   **综述: A Survey on Trustworthy LLM Agents: Threats and Countermeasures** (2025)

    该综述提出了一个名为TrustAgent的框架，全面地研究了智能体可信度的各个方面。

    [arXiv: 2503.09648](https://arxiv.org/abs/2503.09648)

*   **论文: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments** (Xie et al., 2024)

    首个在真实全桌面操作系统环境中针对多模态智能体执行开放式计算机任务的基准测试框架，支持跨系统（Windows/Linux/macOS）以及鼠标键盘联合操作的复杂任务评估，极大推动了计算机控制智能体的标准化测试。

    [arXiv: 2404.07972](https://arxiv.org/abs/2404.07972) / [GitHub仓库](https://github.com/xlang-ai/OSWorld)

*   **论文: AgentBench: Evaluating LLMs as Agents** (Liu et al., 2023)

    [arXiv: 2308.03688](https://arxiv.org/abs/2308.03688) / [GitHub仓库](https://github.com/THUDM/AgentBench)
    

*   **论文: MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents** (Zhu et al., 2025)

    [arXiv: 2503.01935](https://arxiv.org/abs/2503.01935) / [GitHub仓库](https://github.com/THUDM/MultiAgentBench)

*   **论文: AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents** (ICLR 2025)

    评估工具型智能体在对抗攻击与有害多步任务中的鲁棒性与拒答能力。

    [arXiv: 2410.09024](https://arxiv.org/abs/2410.09024)

---

<a name="2025-2026-研究选读"></a>

## 经典与背景延伸阅读

本节按主题汇总代表性经典方法与背景文献；完整实验指标与最新周更动态可进入[论文库总表](docs/papers.md)或[月度精选](docs/monthly-picks.md)。

### 计算机视觉与多模态 (CV/Multimodal & GUI)
*   **UI-TARS: Pioneering Automated GUI Interaction with Native Agents** (ByteDance, 2025)

    端到端原生视觉 GUI 智能体，直接从屏幕截图与历史轨迹映射到统一动作空间，结合反思轨迹与 DPO 优化在 ScreenSpot、OSWorld 等基准上表现突出（原仓库已于 2026-11 归档，保留作技术路线参考）。

    [arXiv: 2501.12326](https://arxiv.org/abs/2501.12326) / [GitHub仓库](https://github.com/bytedance/UI-TARS)

*   **Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making** (NeurIPS 2024)
    
    提出了首个针对具身决策任务的大语言模型基准框架，填补了智能体在复杂三维环境中交互评估的空白。
    
    [arXiv: 2410.07166](https://arxiv.org/abs/2410.07166)

### 自然语言处理、长链条推理与 RL (NLP/Reasoning & RL)
*   **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** (DeepSeek, 2025)

    系统验证了纯强化学习（R1-Zero）与冷启动多阶段 RL（R1）对模型自主推理、自我反思和长链条规划能力的激发作用。

    [arXiv: 2501.12948](https://arxiv.org/abs/2501.12948) / [GitHub仓库](https://github.com/deepseek-ai/DeepSeek-R1)

*   **Large Language Model Agent: A Survey on Methodology, Applications and Challenges** (2025)

    全面梳理 LLM 智能体的方法论、典型应用与核心挑战，适合作为建立全局视野的综述入口。
    
    [arXiv: 2503.21460](https://arxiv.org/abs/2503.21460)

*   **Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents** (2024)

    将引导式蒙特卡洛树搜索（MCTS）、自我批判与基于交互轨迹的离策略 DPO 训练结合，显著提升自主网页任务的执行表现。

    [arXiv: 2408.07199](https://arxiv.org/abs/2408.07199)

### 软件工程与系统架构 (SE/Systems)
*   **SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement** (ICLR 2025)
    
    将蒙特卡洛树搜索（MCTS）与大语言模型软件开发智能体结合，提升代码库导航与自动化 Issue 修复效果。

    [arXiv: 2410.20285](https://arxiv.org/abs/2410.20285)

### 可信度、安全与压力评估 (Trustworthiness & Safety)
*   **Why Agents Compromise Safety Under Pressure** (Jiang et al., 2026)

    首个系统提出“智能体压力 (Agent Pressure)”概念的研究，探讨在非恶意对抗的日常压力与环境摩擦下，智能体产生安全妥协行为的成因与评测方式。

    [arXiv: 2603.14975](https://arxiv.org/abs/2603.14975)

*   **AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents** (ICLR 2025)
    
    面向工具调用型智能体的有害任务与对抗鲁棒性评测基准。

    [arXiv: 2410.09024](https://arxiv.org/abs/2410.09024)

---

## 如何贡献
我们热烈欢迎社区的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解完整贡献指南。

**快速开始：**
- 📄 **添加论文**：提交 PR，按照[论文模板](CONTRIBUTING.md)添加条目
- 🐛 **报告问题**：通过 GitHub Issue 报告失效链接、过时信息或错误
- 💡 **建议新章节**：在 GitHub Discussions 发起讨论

论文收录要求：与 Agent 的机制、系统、使用或评估直接相关；有可核验的原始论文页面；能写清研究问题、证据与局限。新预印本可以收录，但要注明来源状态。引用数、GitHub stars 和会议名都不是单独的门槛。完整规则见[收录标准与每周 SOP](docs/update-sop.md)。

---

## 引用

如果本指南对您的研究有所帮助，请考虑引用相关的原始论文。本仓库旨在作为导航和索引，而非原创性研究的来源。

```bibtex
@misc{ai_agent_guide,
  title        = {{AI-Agent-Guide}: A Comprehensive Guide to LLM-based AI Agents},
  author       = {Hengle Jiang},
  year         = {2025},
  publisher    = {GitHub},
  journal      = {GitHub repository},
  howpublished = {\url{https://github.com/Scodive/AI-Agent-Guide}}
}
```

---

<p align="center">
  <sub>⭐ 如果本指南对您有帮助，请考虑给仓库点个 Star，帮助更多人发现它！</sub>
</p>

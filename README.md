# AI-Agent-Guide
[![GitHub Stars](https://img.shields.io/github/stars/Scodive/AI-Agent-Guide?style=social)](https://github.com/Scodive/AI-Agent-Guide/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Scodive/AI-Agent-Guide)](https://github.com/Scodive/AI-Agent-Guide/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Scodive/AI-Agent-Guide/blob/main/CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/github/license/Scodive/AI-Agent-Guide)](https://github.com/Scodive/AI-Agent-Guide/blob/main/LICENSE)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README_EN.md) | [中文](README.md)

欢迎来到 AI-Agent-Guide。本指南梳理 AI 智能体的架构、关键技术与研究问题，并保留原有的长篇导读。论文库采用人工精选和逐条核验，不追求收齐每天的新论文；每条记录提供研究问题、机制、实验环境与指标、结论、局限和核验日期。

**快速入口：** [网站首页](https://ai-notes-red-two.vercel.app) · [新手阅读路线](docs/reading-path.md) · [论文库表格](docs/papers.md) · [2026 年 9 月精选](docs/monthly-picks.md) · [Harness 与 Coding Agent](docs/harness.md) · [RSI 与自我改进](docs/rsi.md)

论文库的原始数据在 [`data/papers.csv`](data/papers.csv)。截至 2026-10-05，共收录 67 篇；其中 10 篇作为九月精选。本周补充记忆效用识别、服务恢复评估，以及 MemGPT、LATS、τ²-Bench 三项早期漏收路线；讲解修订与待核验事项见[本周审查](data/weekly-reviews/2026-10-05.md)。展示由独立网站负责，本仓库维护数据与导读。收录不代表对论文结论的独立复现；发现错误请提交 Issue 或 PR。

## 如何使用这份指南

下文的长篇导读以感知、规划、记忆、行动等基础模块建立概念，不应当作截至今天的完整技术清单。要了解近期研究，请结合[本月精选](docs/monthly-picks.md)和[论文库](docs/papers.md)阅读：

| 近期问题 | 从哪篇开始 | 在指南中的位置 |
| --- | --- | --- |
| Agent 如何被构建、配置和监督？ | [τ^τ-Bench](https://arxiv.org/abs/2609.04611)、[Scanning the Harness](https://arxiv.org/abs/2609.07360)、[The Work Behind Delegation](https://arxiv.org/abs/2609.24234) | 软件工程、工具与安全；运行框架和人工监督跨越多个基础模块。 |
| 工具调用策略会学到什么捷径？ | [Spurious Tool Use](https://arxiv.org/abs/2609.16268) | 工具与行动、自我演进。 |
| 长期记忆和多 Agent 协作如何评估？ | [DolphinBench](https://arxiv.org/abs/2609.24971)、[CoCoBench](https://arxiv.org/abs/2608.28266) | 记忆与检索、多智能体。 |
| Agent 的实际使用和交付结果怎样衡量？ | [DAREBench](https://arxiv.org/abs/2609.06059)、[Are We There Yet?](https://arxiv.org/abs/2609.00524)、[Who Finishes the Job?](https://arxiv.org/abs/2609.26847) | 评估与安全、GUI、代码智能体；需同时看成本、用户和后续修复。 |

**覆盖边界：**现有论文库是人工精选的阅读路线，不是对所有最新模型、框架或论文的实时盘点。[Harness 专题](docs/harness.md)说明运行框架与 Coding Agent，[RSI 专题](docs/rsi.md)区分提示词、Agent 程序和目标算法的改进。两者是入门导读，新增论文仍先记录在库中，再按[每周 SOP](docs/update-sop.md)更新解释。

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
- [智能体开发框架：从理论到实践](#智能体开发框架从理论到实践)
  - [主流框架深度解析](#主流框架深度解析)
  - [智能体开发框架对比](#智能体开发框架对比)
  - [实战：科研技能库 (Paper-Agent-Skills)](#实战科研技能库-paper-agent-skills)
- [Self-Evolving 智能体：自我进化与自适应机制](#self-evolving-智能体自我进化与自适应机制)
  - [三类适应机制与 RSI 边界](#三类适应机制与-rsi-边界)
  - [相关论文与资源](#相关论文与资源-3)
- [多智能体系统（MAS）：协作产生的涌现智能](#多智能体系统mas协作产生的涌现智能)
  - [MAS范式与架构](#mas范式与架构)
  - [典型应用](#典型应用)
  - [关键挑战](#关键挑战-1)
  - [相关论文与资源](#相关论文与资源-4)
- [可信度：安全、对齐与评估](#可信度安全对齐与评估)
  - [对齐方法论](#对齐方法论)
  - [从结果到评估协议](#从结果到评估协议)
  - [上下文与执行权限的连接](#上下文与执行权限的连接)
  - [评估与基准测试](#评估与基准测试)
  - [相关论文与资源](#相关论文与资源-5)
- [2025-2026 研究选读](#2025-2026-研究选读)
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

    这篇论文提出了一个关于LLM驱动的自主智能体的整体性框架，系统地从构建、应用和评估三个维度对现有研究进行了梳理。它提出的智能体架构（包括画像、记忆、规划、行动模块）已成为该领域广泛引用的标准模型 。

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
本指南用感知、规划与推理、记忆、行动四个视角拆解决策循环，便于从概念走到系统。它们是分析视角，不要求实现中四个独立模块一一对应。Wang 等人的综述使用画像、记忆、规划与行动分类；这里将输入处理单列为感知，不能把两套分类直接视为同一个标准。

LLM 可以提出决策，但运行框架还要组织上下文、执行工具、保存状态并判定停止条件。学习每个模块时都要继续问：信息怎样进入模型、动作由谁执行、结果由什么证据验证？

智能体的四个核心模块分别是：

*   **感知模块 (Perception Module)**：智能体与环境交互的入口，负责接收和处理来自外部世界的原始信息，如用户指令、API返回的文本、网页的视觉截图等，并将其转化为内部可理解的结构化表示。

*   **规划与推理模块 (Planning & Reasoning Module)**：智能体的认知核心。它接收感知模块处理后的信息，并根据预设的目标进行思考。这包括将宏大、复杂的目标分解为一系列更小、更具体的可执行步骤或子任务 。

*   **记忆模块 (Memory Module)**：赋予智能体学习和适应能力的关键。它负责存储和检索信息，包括短期记忆（如当前对话的上下文）和长期记忆（如过去的经验、用户偏好、知识库），为规划和行动提供必要的背景信息。

*   **行动模块 (Action Module)**：将规划模块制定的决策转化为与外部环境的实际交互。这通常通过调用外部工具（如代码解释器、搜索引擎API、数据库查询）来实现，从而使智能体能够超越其内部知识的限制，获取实时信息并执行具体任务。

信息在这些模块间的流动形成了一个动态的循环：感知模块获取环境状态，规划模块基于这些信息和记忆进行决策，行动模块执行决策并改变环境状态，而新的环境状态又被感知模块捕获，如此循环往复，直至任务完成。这个架构不仅清晰地划分了功能，也为模块化的设计和迭代优化提供了便利。

这四个模块主要描述 **Agent 内部决策循环**。构建和评估可运行系统时，还需要单独说明运行框架：工具接口、上下文与状态管理、执行权限、验证与停止条件，以及人工监督。运行框架会影响相同模型的任务表现和资源开销，不能只用模型名称概括系统能力。参见 [Code as Agent Harness](https://arxiv.org/abs/2605.18747) 和 [DAREBench](https://arxiv.org/abs/2609.06059)；这是对基础蓝图的补充，不表示这些机制已有统一标准实现。


### 架构蓝图相关核心论文

*   **Cognitive Architectures for Language Agents (CoALA)** (Sumers et al., 2023)
    
    该论文将现代大语言模型与经典的认知科学架构（如ACT-R、SOAR）深度融合，构建了极具影响力的语言智能体认知架构标准（CoALA）。该工作严密地定义了通过程序/记忆模块组成的“内部行动”和“外部环境”循环协同关系，极大深化了通用智能体的底层基础架构设计理论。
    
    [arXiv: 2309.02427](https://arxiv.org/abs/2309.02427)

*   **OpenAgents: An Open Platform for Language Agents in the Wild** (Xie et al., 2023)
    
    从架构工程落地层面探讨智能体的统一设计模型。该工作的意义在于，它以一套极其标准化的感知、规划、记忆与执行框架，并行孵化了三种复杂度极高的特化智能体体系（数据分析智能体、插件智能体、网页智能体），属于验证复杂多模态模块化架构的经典且综合的系统工程实现。
    
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

    针对现有多模态模型在定位 GUI 界面元素时精确度低、严重依赖底层结构树 (DOM/XML) 的问题，微软提出了 OmniParser。这是一个能够在任意屏幕上精准提取与推断可交互元素及其语义的纯视觉解析系统，显著提升了 GPT-4V 等模型在真实设备上的操作成功率。

    [arXiv: 2408.00203](https://arxiv.org/abs/2408.00203) / [GitHub仓库](https://github.com/microsoft/OmniParser)

*   **论文: Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception** (Wang et al., 2024)

    介绍了一个纯视觉驱动的移动设备智能体，它无需依赖系统底层的元数据（如XML布局文件），仅通过分析屏幕截图就能自主导航和操作App，充分展示了视觉感知在跨平台通用性方面的巨大潜力。

    [arXiv: 2401.16158](https://arxiv.org/abs/2401.16158) / [GitHub仓库](https://github.com/X-PLUG/MobileAgent)
    

<!-- *   **论文: Are Multimodal Agents Faithful in a Risky World?** (2024)

    这是一篇至关重要的论文，它首次系统地探讨了GUI智能体在面对环境中无关干扰信息时的脆弱性，对智能体的可靠性和忠实度提出了深刻的质疑。

    [arXiv: 2402.17641](https://arxiv.org/abs/2402.17641) -->

从文本到视觉的跨越是智能体走向通用性的关键一步。然而，当前的技术发展表明，感知，特别是可靠且忠实的多模态感知，是实现这一目标的主要瓶颈。最初的智能体在纯文本环境中运行，其感知等同于读取输入。为了在为人类设计的、以视觉为主导的数字世界（如操作系统、网页）中发挥实际作用，智能体必须具备由VLM驱动的多模态感知能力。然而，研究明确指出，通用VLM在精确的UI元素定位方面存在困难，并且容易受到视觉干扰信息的影响，这会直接损害任务的成功率和用户信任。因此，如果一个智能体无法准确、忠实地感知其所处的环境，那么其再强大的规划、记忆和行动能力也无从发挥。整个智能体技术栈的可靠性，最终都建立在其感知模块的保真度之上。

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
    概念：ReAct框架是一个范式上的飞跃，它将**推理（Thought）和行动（Action）**交错进行。智能体首先生成一个“思考”，用于分析当前情况并制定下一步计划；然后，它执行一个“行动”，例如调用搜索引擎API来获取缺失的信息。行动的结果会作为新的观察被反馈给智能体，用于下一轮的“思考”。这种“思考-行动-观察”的循环，使得智能体的推理能够被外部世界的真实信息所“接地”，有效缓解了纯内部推理（如CoT）容易产生的知识幻觉问题 。

    奠基论文: **ReAct: Synergizing Reasoning and Acting in Language Models** (Yao et al., 2022)

    [arXiv: 2210.03629](https://arxiv.org/abs/2210.03629) / [GitHub仓库](https://github.com/ysymyth/ReAct)


3.  **思维树 (Tree of Thoughts, ToT)**
    概念：ToT进一步突破了CoT和ReAct的线性推理模式。当面对需要探索或深思熟虑的问题时，ToT允许模型同时探索多条不同的推理路径，并将这些路径组织成一棵“思维树”。在这个过程中，LLM不仅扮演着“思考者”的角色，还扮演着“评估者”的角色：它会自我评估树中每个节点（即每个中间“想法”）的价值和前景，然后决定是继续深入探索某条路径（lookahead），还是放弃当前路径并返回到之前的节点尝试其他可能性（backtracking）。这种机制赋予了智能体进行系统性搜索和深思熟虑决策的能力 。

    奠基论文: **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (Yao et al., 2023)

    [arXiv: 2305.10601](https://arxiv.org/abs/2305.10601) / [GitHub仓库](https://github.com/princeton-nlp/tree-of-thought-llm)
    
### 从思维树到环境反馈搜索

[LATS](https://arxiv.org/abs/2310.04406)补上“怎样把行动结果放进搜索”的连接：用 MCTS 选择和扩展轨迹，在获得环境观察后估计价值，再用终局反馈回传并保存失败反思。读完 ReAct 和 ToT 后，可用它区分**搜索想法**与**搜索可执行行动**；之后再读 SWE-Search 的代码环境实现。

这些方法是可组合的设计选择。比较时同时记录节点数、轨迹数、token 和环境调用；LATS 的 HotpotQA 实验使用正确性 oracle，且依赖可回退状态。不能把测试环境中的回溯直接用于不可逆的付款或生产修改。完整边界见[库内记录](docs/papers.md#paper-2310.04406)。

### 核心推理技术对比
为了帮助研究者和开发者快速理解不同推理技术的特点和适用场景，下表对上述核心技术进行了对比。CoT、自洽性、ReAct 和树搜索分别处理推理分解、采样一致性、外部交互与分支探索；它们不构成必然越来越好的线性升级路线。

| 技术名称      | 核心思想                                     | 主要优势                                           | 适用场景                                         |
| :------------ | :------------------------------------------- | :------------------------------------------------- | :----------------------------------------------- |
| Chain-of-Thought (CoT) | 通过中间步骤分解复杂问题                     | 提升LLM在复杂推理任务上的性能                  | 算术、常识和符号推理                               |
| Self-Consistency | 对CoT结果进行多样本投票，提高鲁棒性         | 提高答案的准确性和稳定性                           | 对结果准确性要求高的推理任务                     |
| ReAct         | 交错的“思考-行动-观察”循环                     | 缓解知识幻觉，将推理与外部世界“接地”           | 需要与外部工具（如搜索引擎）交互的任务           |
| Tree of Thoughts (ToT) | 探索多条推理路径，自我评估和回溯             | 应对需要探索和深思熟虑的复杂问题，系统性搜索     | 需要多步决策、有多种可能路径的问题               |

---

## 记忆模块：实现学习与情境感知
如果说规划与推理是智能体的“大脑”，那么记忆就是其获得智慧、实现成长的基石。记忆模块使得智能体能够摆脱“一次性”工具的局限，成为一个能够从经验中学习、在持续交互中保持情境感知的状态化实体 。没有记忆，每一次交互都将是冷启动，智能体也无法实现真正的个性化和自适应。

### 记忆架构
智能体的记忆系统通常被设计为模仿人类认知架构，分为两种主要类型：

*   **短期记忆 (Short-Term Memory)**：这部分记忆对应于LLM在单次交互中能够处理的上下文窗口（Context Window）。它存储了当前对话的即时信息，访问速度快，但容量有限且是短暂的。一旦会话结束或上下文窗口被填满，这部分记忆就会丢失 。

*   **长期记忆 (Long-Term Memory)**：为了实现跨会话的知识保留和学习，智能体需要长期记忆。这通常通过将信息存储在外部数据库中来实现，使得智能体能够持久地保存和回忆过去的交互、用户偏好、成功或失败的经验等。长期记忆是智能体实现持续学习和能力演进的关键 。

### 长期记忆的关键机制
*   **检索增强生成 (Retrieval-Augmented Generation, RAG)**：RAG 是将外部知识或经验检索进当前上下文的一类机制；外部知识库、个人经验记忆与当前上下文应分别描述。其核心思想是，在响应用户请求时，首先从一个外部知识库（如文档、数据库）中检索出与当前任务最相关的信息，然后将这些检索到的信息作为附加上下文增强（augment）输入给LLM，最后由LLM生成最终的答案 。检索可能提供相关证据，但其准确性取决于来源质量、召回和模型的使用方式，不能保证回答正确。

*   **智能体化RAG (Agentic RAG)**：这是对标准RAG的演进。在Agentic RAG中，一个或多个自主智能体被集成到检索流程中。这些智能体可以动态地管理检索策略，例如，通过自我反思来重构查询语句、决定何时以及从哪个数据源进行检索，甚至协同工作来处理复杂的多步查询，从而使整个检索过程更加智能、灵活和高效 。

*   **向量数据库 (Vector Databases)**：向量数据库是实现高效RAG的底层技术支撑。它将文本、图片等非结构化数据通过嵌入模型（Embedding Model）转换为高维向量，并存储起来。当需要检索时，系统会将用户的查询也转换为一个向量，然后在数据库中快速执行语义相似度搜索，找到与查询向量在“意义”上最接近的存储向量。语义检索和关键词检索各有适用范围，应在目标任务上比较召回、精度与成本。

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

*   **向量数据库:**
    *   [Weaviate](https://weaviate.io/)

### 记忆从保存到产生作用

将过程拆成**保存 → 检索 → 放入当前上下文 → 影响任务结果 → 决定以后保留什么**。[MemGPT](https://arxiv.org/abs/2310.08560)解释前几步的分层存储、分页与控制流；A-MEM 解释内容如何组织，两者并非替代关系。

[CMP](https://arxiv.org/abs/2610.02070)补充效用估计的边界：某条记忆从未进入上下文时，日志里的“没贡献”可能是没被测试，而不是无用。论文用固定槽位的随机曝光改善识别，但曝光池利用相关记忆标签，未来查询上的留存策略仍未解决。它适合作为评估方法阅读，不能直接当作可部署的自动淘汰规则。

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

**模型上下文协议（Model Context Protocol, MCP）**统一客户端与服务器交换工具、资源等信息的接口。它帮助减少重复集成，但任务状态、业务权限与工具执行结果仍由具体实现负责。

**需要分开的三层：**协议负责描述与交互；服务器和下游服务负责认证、授权；运行框架和执行环境负责进程、文件与网络权限。支持 MCP 不自动保证隔离。官方[安全实践](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices)明确讨论令牌透传、混淆代理与最小权限问题（资料核对：2026-10-05）。

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

- **SWE-bench**：评估编码智能体的标准基准，包含来自主流 Python 项目（Django、scikit-learn 等）的 2,294 个真实 GitHub Issue。智能体须分析代码库并提交能解决 Issue 的补丁。

  [官网](https://www.swebench.com/) / [arXiv: 2310.06770](https://arxiv.org/abs/2310.06770) / [GitHub](https://github.com/princeton-nlp/SWE-bench)

**开源智能体：**

- **SWE-agent**（普林斯顿，2024）：设计了专门用于导航和编辑大型代码库的智能体-计算机接口（ACI），提供带行号的文件查看器、定向搜索和编辑命令等专为 LLM 优化的工具，在 SWE-bench 上表现优异。

  [arXiv: 2405.15793](https://arxiv.org/abs/2405.15793) / [GitHub](https://github.com/princeton-nlp/SWE-agent)

- **OpenHands（原 OpenDevin）**：开源 AI 软件开发智能体平台，可浏览网页、编写和执行代码、管理文件，支持多种后端 LLM。

  [GitHub](https://github.com/All-Hands-AI/OpenHands)

- **SWE-Search**（2024）：将蒙特卡洛树搜索（MCTS）与 LLM 软件智能体深度融合，通过在大型代码-行动空间中进行系统性探索与迭代优化，显著提升了 Issue 解决率。

  [arXiv: 2410.20285](https://arxiv.org/abs/2410.20285) / [GitHub](https://github.com/aorwall/moatless-tools)

**理解完整交付：**模型生成补丁、测试通过、人工接受、合并后维护，以及线上服务恢复是不同观察点。先用 [Harness 导读](docs/harness.md)拆解接口、上下文和验证，再用 [Who Finishes the Job?](https://arxiv.org/abs/2609.26847)检查后续维护。[Incident-Arena](https://arxiv.org/abs/2610.00648)将边界延伸到故障恢复：持续负载和重启之后，服务、数据和允许修改范围是否仍满足要求？其有限任务与模型/Harness 组合不构成商业产品排名。

---|:---|:---|
| Cursor / Composer | Anysphere | AI 原生 IDE，支持多文件智能体编辑 |
| GitHub Copilot Workspace | GitHub | 从 Issue 到 Pull Request 的全流程智能体 |
| Devin | Cognition AI | 自主软件工程师 |
| Windsurf | Codeium | 支持 MCP 的智能体 IDE |

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

    特点: LlamaIndex的独特价值主张是为基于私有数据构建LLM应用提供一站式解决方案。它的核心功能围绕着数据的摄取（Ingestion）、**索引（Indexing）和查询（Querying）**展开。如果你应用的核心需求是让LLM能够高效、准确地查询和理解你的私有知识库（无论是PDF、数据库还是API），LlamaIndex提供了最优化的工具链和抽象层 。

    代码库: [LlamaIndex GitHub](https://github.com/run-llama/llama_index)

3.  **AutoGen**
    核心定位: 一个专注于多智能体对话的框架。

    特点: 由微软研究院推出的AutoGen，其核心设计理念是简化多智能体协作系统的构建。它提供了一套强大的抽象，用于定义具有不同角色、能力和对话模式的智能体，并协调它们之间的交互来共同完成复杂任务。如果你需要构建一个由多个专家智能体（如“程序员”、“测试员”、“项目经理”）组成的虚拟团队，AutoGen 可作为多智能体编排的历史实例。截至 2026-10-05，其[官方仓库](https://github.com/microsoft/autogen)标注维护模式，建议新项目查看 Microsoft Agent Framework；本文不据此保证后继框架的性能。

    代码库: [AutoGen GitHub](https://github.com/microsoft/autogen)

4.  **MS-Agent**
    核心定位: 一个轻量级框架，赋能智能体自主探索复杂任务场景。

    特点: MS-Agent 提供了一个灵活且可扩展的架构，使开发者能够创建具备复杂任务处理能力的智能体，例如代码生成、数据分析以及支持 MCP（模型上下文协议）的通用工具调用。其特点包括：
    *   **通用多智能体 (Multi-Agent for general purpose)**: 支持基于 MCP 的工具调用能力，实现智能体对话。
    *   **深度研究 (Deep Research)**: 赋能智能体进行自主探索和执行复杂研究任务的高级能力。
    *   **代码生成 (Code Generation)**: 支持代码生成任务，并产生相应的产物。
    *   **轻量级与可扩展 (Lightweight and Extensible)**: 易于扩展和定制，适用于各种应用场景。

    代码库: [MS-Agent GitHub](https://github.com/modelscope/ms-agent)

### 智能体开发框架对比
对于开发者而言，选择合适的框架是项目成功的关键第一步。这个决策将深刻影响应用的架构、开发效率和未来的可扩展性。下表根据各个框架的核心设计理念和主要优势，提供了一个清晰的选型指南。

| 框架        | 核心抽象         | 主要用例                   | 关键优势                         |
| :---------- | :--------------- | :------------------------- | :------------------------------- |
| LangChain   | 组件链/图 (Chains/Graphs) | 快速原型化各类LLM应用      | 极高的模块化程度和庞大的集成生态 |
| LlamaIndex  | 数据索引/查询引擎 | 构建基于私有数据的智能体 (RAG) | 以数据为中心的索引和检索优化     |
| AutoGen     | 可对话的智能体 (Conversable Agents) | 多智能体协作系统           | 灵活的多智能体对话编排与管理     |
| MS-Agent    | 自主探索、工具调用 | 代码生成、数据分析、通用工具调用 | 轻量级、多模态、高效、可扩展      |

### 实战：科研技能库 (Paper-Agent-Skills)
为了展示智能体如何学习并执行复杂的垂直领域任务，我们提供了一个实战项目：**[Paper-Agent-Skills](https://github.com/Scodive/Paper-Agent-Skills)**。

该项目采用了**基于技能（Skill-based）**的架构，将学术研究中的高阶能力（如论文撰写、Rebuttal 策略、Slides 生成）封装为可复用的智能体模块。

*   **核心特性**:
    *   **模式提取**: 从顶会（NeurIPS, ICLR, CVPR）的 Best Paper 中提取论证逻辑和修辞模式。
    *   **可解释性**: 不同于黑盒生成，智能体通过明确的“技能工作流”展示其思考过程。
    *   **安全对齐**: 内置引用校验机制，防止学术幻觉。
*   **应用价值**: 该库展示了如何将 LLM 的通用推理能力转化为高度专业化的科研生产力工具。

---

---

## Self-Evolving 智能体：自我进化与自适应机制

自我演进应先按**修改对象、反馈来源和发生阶段**分类。经验积累、推理时反思、训练时参数更新，以及递归修改自身程序，对应不同机制和证据；“自我进化”不意味着无人监督或保证持续增长。

### 三类适应机制与 RSI 边界

1. **技能与记忆积累**：Voyager 保存可复用技能，A-MEM 组织经验。它们可以改变后续可用信息，但不保证避免重复错误或指数增长。
2. **提示词与程序优化**：[GEPA](https://arxiv.org/abs/2507.19457)优化提示词，[Darwin Gödel Machine](https://arxiv.org/abs/2505.22954)修改 Agent 程序。检查新版本是否进入下一轮改进、反馈是否独立、旧任务是否退化，才能判断递归性和收益。
3. **模型训练**：DeepSeek-R1 与 Agent-R1 提供参数学习背景。训练后的固定模型能反思，不等于运行时会修改自身改进器；DPO 等偏好优化也不能统一写成在线自博弈。

**RSI 阅读入口：**[专题](docs/rsi.md)逐项比较 GEPA、Gödel Agent、DGM、AIDE² 的修改面和递归性，并说明 AlphaEvolve 改进目标算法的相邻边界。外部验证、留出任务与版本回滚都是要报告的条件，而非通用效果保证。

### 相关论文与资源

*   **论文: Voyager: An Open-Ended Embodied Agent with Large Language Models** (Wang et al., 2023)

    开创性的自演进具身智能体系统。在《Minecraft》开放世界中，Voyager 提出了包含“自动课程生成”、“无尽技能库”与“迭代自我反思”的三元架构，实现了无需人类标注的技能自演进与持续探索。

    [arXiv: 2305.16291](https://arxiv.org/abs/2305.16291) / [GitHub仓库](https://github.com/MineDojo/Voyager)

*   **论文: A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence** (2025)

    该综述从智能体组件、适应阶段和反馈机制等角度整理自我演进研究；具体方法与实验结论仍需查阅原论文。

    [arXiv: 2507.21046](https://arxiv.org/abs/2507.21046)

*   **论文: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** (DeepSeek, 2025)

    模型推理训练的基础阅读。R1-Zero 研究不经 SFT 的纯 RL；R1 采用冷启动数据、SFT 与多阶段 RL。两者都不直接证明环境交互 Agent 的运行时 RSI。

    [arXiv: 2501.12948](https://arxiv.org/abs/2501.12948) / [GitHub仓库](https://github.com/deepseek-ai/DeepSeek-R1)

*   **论文: Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning** (2025)

    研究使用环境反馈对多步交互 Agent 进行端到端强化学习；适用范围取决于训练环境与奖励设计。

    [arXiv: 2511.14460](https://arxiv.org/abs/2511.14460) / [GitHub](https://github.com/AgentR1/Agent-R1)

## 多智能体系统（MAS）：协作产生的涌现智能
多智能体系统（Multi-Agent Systems, MAS）通过分工、通信和共享产物组织任务。角色设计是机制选择；能否优于单 Agent，需在相同任务、预算与工具条件下测量，也要计入交接开销和错误传播。

[RAC](https://arxiv.org/abs/2610.00980)提供已有经典角色分工之外的对照：根据执行状态选择下一位协作者，在三个科研宿主中取得最高观察均分，但联合加入契约和验证后均分下降。该结果来自单种子小样本，不能分别归因到契约或验证，也不能推广为“协作无用”。用它检查复杂机制是否值得预算，而保留 MetaGPT、ChatDev 作为固定工作流阅读。

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
*   **综述: A Communication-Centric Perspective on Large Language Model based Multi-Agent Systems** (2025)

    该综述从“沟通”这一核心视角来剖析MAS，为理解多智能体协作的内在机制提供了一个新颖的框架。

    [arXiv: 2502.14321](https://arxiv.org/abs/2502.14321)

*   **论文: MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework** (Hong et al., 2023)

    利用标准操作程序 (SOPs) 对大语言模型进行元编程，将人类工作流编排进多智能体协作框架中。以角色和结构化产物组织需求、设计与代码生成；是否正确仍需任务验证，不能从角色数量或文档完整性推断。

    [arXiv: 2308.00352](https://arxiv.org/abs/2308.00352) / [GitHub仓库](https://github.com/geekan/MetaGPT)

*   **论文: Generative Agents: Interactive Simulacra of Human Behavior** (Park et al., 2023)

    著名的“斯坦福小镇”研究。该工作赋予了沙盒环境中25个虚拟角色各自的记忆流 (Memory Stream)，角色可以观察、回忆、反思并与其他成员自然交流，展现出惊人的社会互动涌现能力，为构建真实的社会化多智能体系统提供了开创性范式。

    [arXiv: 2304.03442](https://arxiv.org/abs/2304.03442) / [GitHub仓库](https://github.com/joonspk-research/generative_agents)

*   **论文: ChatDev: Communicative Agents for Software Development** (Qian et al., 2023)

    [arXiv: 2307.07924](https://arxiv.org/abs/2307.07924) / [GitHub仓库](https://github.com/OpenBMB/ChatDev)
    

*   **开发框架**: AutoGen 提供多智能体对话的历史实例；当前维护状态与后继项目见上方框架章节及[官方仓库](https://github.com/microsoft/autogen)。

---

## 可信度：安全、对齐与评估
随着智能体变得日益自主，并被赋予在真实世界中采取行动的能力，确保其行为的可信度（Trustworthiness）已成为该领域最重要、最紧迫的议题。一个强大的智能体如果行为不可预测、不符合人类价值观或存在安全漏洞，其潜在风险将远超其带来的益处。因此，智能体的安全（Safety）、与人类价值观的**对齐（Alignment）以及对其行为的严格评估（Evaluation）**构成了可信度研究的三大支柱 。

### 对齐方法论
*   **宪法AI (Constitutional AI, CAI)**: 由Anthropic公司提出的一种创新的对齐技术。传统对齐方法（如RLHF）严重依赖人类标注者来判断模型的输出是否“好”。CAI则试图让AI在一定程度上“自我对齐”。其核心思想是，首先为AI制定一套原则或价值观，即“宪法”（Constitution）。然后，在训练过程中，模型不仅要生成对用户问题的回答，还要根据“宪法”自我批判和修正其回答。这个过程被称为“来自AI反馈的强化学习”（Reinforcement Learning from AI Feedback, RLAIF）。通过这种方式，CAI旨在使对齐过程更具可扩展性、透明度和一致性，减少对大规模人工标注的依赖 。

*   **防御机制**: 除了在训练阶段进行对齐，还需要在部署时采取防御措施。研究人员正在探索多种防御策略，例如，在智能体的“大脑”前后部署外部的“守卫”模型，用于过滤恶意输入和审查不安全的输出；或者利用多智能体系统，通过辩论、审查等方式，集体增强决策的鲁棒性和安全性 。

### 从结果到评估协议

- **谁改变环境？**[τ²-Bench](https://arxiv.org/abs/2506.07982)让 Agent 与模拟用户都能操作共享状态；No-User/Oracle Plan 对照区分推理与协作负担。它测执行中的协作；[τ^τ-Bench](https://arxiv.org/abs/2609.04611)测构建并交付一个 Agent，二者不是同一个基准或版本。
- **什么时候算完成？**[Incident-Arena](https://arxiv.org/abs/2610.00648)要求恢复与安全条件同时通过，并检查负载和重启后的结果。主成功判定使用功能验证；论文另行分析奖励投机时使用 LLM judge，不能把整篇工作概括为完全无模型判分。
- **分母与预算是什么？**报告任务集版本、抽样数、重复次数、token/时延/费用、工具权限及停止规则。`pass^k` 的多次一致成功与 `pass@k` 的至少一次成功含义不同。区分模型失败、工具/验证器故障与缺失结果，并报告不确定性；真实用户研究与模拟用户也分开。

### 上下文与执行权限的连接

训练对齐、输入/输出守卫、上下文信任边界和执行权限分别约束不同环节。[CPE 研究](https://arxiv.org/abs/2609.01222)说明低信任内容可能被搬入更高优先级或更持久的上下文；[Harness 专题](docs/harness.md)区分它与配置暴露。论文版本中的攻击路径不代表当前产品版本仍可利用，守卫或多 Agent 审查也不是权限隔离的替代。

### 评估与基准测试
*   **AgentBench**: 这是一个针对单智能体能力的综合性评估基准。它包含了8个不同的、精心设计的环境，覆盖了从操作系统交互、数据库查询到网页浏览等多种真实世界任务，旨在全面评估LLM作为智能体的推理和决策能力 。

*   **MultiAgentBench**: 这是一个专为多智能体系统设计的评估基准。与AgentBench不同，它不仅关注最终的任务完成情况，更侧重于评估智能体在协作和竞争场景中的互动质量。它通过新颖的、基于里程碑的关键绩效指标（KPIs）来衡量智能体之间的协作效率和竞争策略的有效性 。

### 相关论文与资源
*   **论文: Why Agents Compromise Safety Under Pressure** (Jiang et al., 2026)

    首个提出智能体压力概念，探讨非主动攻击情况下智能体和环境交互影响准确性的现象，为智能体安全开辟了新的视角。
    
    [arXiv: 2603.14975](https://arxiv.org/abs/2603.14975)

*   **论文: Constitutional AI: Harmlessness from AI Feedback** (Bai et al., 2022)

    [arXiv: 2212.08073](https://arxiv.org/abs/2212.08073)

*   **综述: A Survey on Trustworthiness in LLM-based Agents** (2025)

    该综述提出了一个名为TrustAgent的框架，全面地研究了智能体可信度的各个方面。

    [arXiv: 2503.09648](https://arxiv.org/abs/2503.09648)

*   **论文: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments** (Xie et al., 2024)

    首个在真实全桌面操作系统环境中针对多模态智能体执行开放式计算机任务的基准测试框架，支持跨系统（Windows/Linux/macOS）以及鼠标键盘联合操作的复杂任务评估，极大推动了计算机控制智能体的标准化测试。

    [arXiv: 2404.07972](https://arxiv.org/abs/2404.07972) / [GitHub仓库](https://github.com/xlang-ai/OSWorld)

*   **论文: AgentBench: Evaluating LLMs as Agents** (Liu et al., 2023)

    [arXiv: 2308.03688](https://arxiv.org/abs/2308.03688) / [GitHub仓库](https://github.com/THUDM/AgentBench)
    

*   **论文: MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents** (Zhu et al., 2025)

    [arXiv: 2503.01935](https://arxiv.org/abs/2503.01935)
    

智能体研究领域正处在一个关键的转折点。早期的研究重心在于证明和提升智能体的核心能力：它能否推理？能否使用工具？能否完成指定的任务？像AgentBench这样的基准测试正是为了回答这些问题而设计的。然而，随着这些能力的日益强大，并将智能体部署到真实世界的应用中，研究的焦点正不可避免地从“它能做什么？”转向“我们能信任它吗？”。这种转变体现在对齐技术（如宪法AI）、主动风险评估以及综合性可信度框架的研究日益增多。MultiAgentBench的出现进一步凸显了这一趋势，因为它认识到评估单个智能体的安全性与评估一个群体涌现出的、可能无法预测的行为是截然不同的挑战。因此，未来智能体领域的前沿探索，其衡量标准将越来越少地依赖于任务成功率等能力指标，而更多地依赖于可靠性、对齐度和安全性等可信度指标。如何构建可验证的、安全的、符合伦理的智能体系统，已成为该领域最核心的开放性问题。

---

## 2025-2026 研究选读

本节保留一组历史延伸阅读。2026 年 9 月的新工作及其证据边界集中在[本月精选](docs/monthly-picks.md)；下列条目不构成最新成果榜单。论文的发表状态和实验结论应以原始论文及正式会议页面为准。

### 计算机视觉与多模态 (CV/Multimodal & GUI)
*   **UI-TARS: Pioneering Automated GUI Interaction with Native Agents** (ByteDance, 2025)

    首个原生端到端 GUI 智能体模型，通过直接感知屏幕截图输出精确定位坐标与键盘操作，在 ScreenSpot、OSWorld 和 AndroidWorld 等三大权威基准上刷榜，大幅推动了 Computer-Using Agent 的跨平台落地。

    [arXiv: 2501.12326](https://arxiv.org/abs/2501.12326) / [GitHub仓库](https://github.com/bytedance/UI-TARS)

*   **Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making** (NeurIPS 2024)
    
    提出了首个针对具身决策任务的大语言模型基准框架，填补了智能体在复杂三维环境中交互评估的空白，引领了具身人工智能的下一步评价标准。
    
    [arXiv: 2410.07166](https://arxiv.org/abs/2410.07166) / [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=Embodied+Agent+Interface+Benchmarking+LLMs+Embodied+Decision+Making)

### 自然语言处理、长链条推理与 RL (NLP/Reasoning & RL)
*   **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** (DeepSeek, 2025)

    区分 R1-Zero 的纯 RL 与 R1 的多阶段训练。可用于理解推理模型的训练反馈；推理时生成更长轨迹、训练时参数更新和 Agent 自改程序是不同过程。

    [arXiv: 2501.12948](https://arxiv.org/abs/2501.12948) / [GitHub仓库](https://github.com/deepseek-ai/DeepSeek-R1)

*   **Large Language Model Agent: A Survey on Methodology, Applications and Challenges** (ACL 2025 / 核心工作)

    全面系统地梳理了大型语言模型智能体的发展脉络，涵盖从基础架构到多智能体系统的前沿挑战，是了解最新全貌的必读神级综述。
    
    [arXiv: 2503.21460](https://arxiv.org/abs/2503.21460) / [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=Large+Language+Model+Agent+Survey+Methodology+Applications+Challenges+2025)

*   **Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents** (2024)

    将引导式 MCTS、自我批判与基于交互轨迹的离策略 DPO 微调结合。搜索和训练是不同环节；这里作为历史方法入口，实验数字仍需阅读全文核验。

    [arXiv: 2408.07199](https://arxiv.org/abs/2408.07199)

### 软件工程与系统架构 (SE/Systems)
*   **SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement** (ICLR 2025)
    
    创新性地将蒙特卡洛树搜索（MCTS）与大语言模型软件开发智能体深入融合，在代码库导航和错误自动修复 (Issue Resolution) 任务中实现了惊人优化。

    [arXiv: 2410.20285](https://arxiv.org/abs/2410.20285) / [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=SWE-Search+Software+Agents+Monte+Carlo+Tree+Search)

### 可信度、安全与压力评估 (Trustworthiness & Safety)
*   **Why Agents Compromise Safety Under Pressure** (Jiang et al., 2026)

    首个提出“智能体压力 (Agent Pressure)”概念的研究，探讨在非主动恶意攻击的复杂真实交互下，任务压力与环境反馈如何导致智能体产生安全妥协行为，为构建可靠的可信 Agent 提供了全新的分析维度。

    [arXiv: 2603.14975](https://arxiv.org/abs/2603.14975)

*   **AgentHarm: Benchmarking Robustness of LLM Agents on Harmful Tasks** (ICLR 2025)
    
    该研究直面智能体安全性与脆弱性的痛点，提出了首个针对对抗性及有害连续交互任务进行防御评测的鲁棒性标杆。

    [arXiv: 2410.09024](https://arxiv.org/abs/2410.09024) / [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=AgentHarm+Benchmarking+Robustness+LLM+Agents+Harmful)

---

## 如何贡献
我们热烈欢迎社区的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解完整贡献指南。

**快速开始：**
- 📄 **添加论文**：提交 PR，按照[论文模板](CONTRIBUTING.md)添加条目
- 🐛 **报告问题**：通过 GitHub Issue 报告失效链接、过时信息或错误
- 💡 **建议新章节**：在 GitHub Discussions 发起讨论

**论文收录要求：**与 Agent 的机制、系统、使用或评估直接相关；有可核验的原始论文页面；能写清研究问题、证据与局限。新预印本可以收录，但要注明来源状态。引用数、GitHub stars 和会议名都不是单独的门槛。完整规则见[收录标准与每周 SOP](docs/update-sop.md)。

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

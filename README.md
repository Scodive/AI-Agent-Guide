# AI-Agent-Guide

[English](README_EN.md) | [中文](README.md)

[![GitHub Stars](https://img.shields.io/github/stars/Scodive/AI-Agent-Guide?style=social)](https://github.com/Scodive/AI-Agent-Guide/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Scodive/AI-Agent-Guide)](https://github.com/Scodive/AI-Agent-Guide/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Scodive/AI-Agent-Guide/blob/main/CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/github/license/Scodive/AI-Agent-Guide)](https://github.com/Scodive/AI-Agent-Guide/blob/main/LICENSE)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

欢迎来到 AI-Agent-Guide！本仓库旨在为研究人员、开发人员和爱好者提供一份AI智能体（AI Agent）的全面、权威且持续更新的指南。随着人工智能从被动的文本生成工具演变为能够感知、规划、记忆和行动的主动实体，一个全新的“智能体时代”已经到来。本指南将系统性地剖析AI智能体的核心架构，梳理关键技术，并提供相关的学术论文和开源代码库，以帮助您深入理解并构建下一代智能应用。

本指南的结构和内容经过精心设计，确保所有引用的论文和代码库都真实可查，为该领域的学习和研究提供一个坚实可靠的基础。

## 目录
*   [基础综述与概述](#基础综述与概述)
    *   [通用智能体综述](#通用智能体综述)
    *   [特定领域应用综述](#特定领域应用综述)
    *   [基础模型与决策综述](#基础模型与决策综述)
*   [AI智能体剖析：核心架构蓝图](#ai智能体剖析：核心架构蓝图)
*   [感知模块：感知数字与物理世界](#感知模块：感知数字与物理世界)
    *   [文本感知](#文本感知)
    *   [多模态感知](#多模态感知)
    *   [核心技术：视觉语言模型 (Vision-Language Models, VLMs)](#核心技术：视觉语言模型-vision-language-models-vlms)
    *   [关键挑战](#关键挑战)
    *   [相关论文与资源](#相关论文与资源)
*   [规划与推理模块：智能体的认知核心](#规划与推理模块：智能体的认知核心)
    *   [基础推理技术演进](#基础推理技术演进)
    *   [核心推理技术对比](#核心推理技术对比)
*   [记忆模块：实现学习与情境感知](#记忆模块：实现学习与情境感知)
    *   [记忆架构](#记忆架构)
    *   [长期记忆的关键机制](#长期记忆的关键机制)
    *   [相关论文与资源](#相关论文与资源-1)
*   [行动模块：执行任务与使用工具](#行动模块：执行任务与使用工具)
    *   [工具使用范式](#工具使用范式)
    *   [工具创造范式](#工具创造范式)
    *   [MCP：模型上下文协议](#mcp模型上下文协议)
    *   [相关论文与资源](#相关论文与资源-2)
*   [Agentic Coding：软件工程新前沿](#agentic-coding软件工程新前沿)
*   [智能体开发框架：从理论到实践](#智能体开发框架：从理论到实践)
    *   [主流框架深度解析](#主流框架深度解析)
    *   [智能体开发框架对比](#智能体开发框架对比)
    *   [实战：科研技能库 (Paper-Agent-Skills)](#实战科研技能库-paper-agent-skills)
*   [多智能体系统（MAS）：协作产生的涌现智能](#多智能体系统mas：协作产生的涌现智能)
    *   [MAS范式与架构](#mas范式与架构)
    *   [典型应用](#典型应用)
    *   [关键挑战](#关键挑战)
    *   [相关论文与资源](#相关论文与资源-3)
*   [可信度：安全、对齐与评估](#可信度：安全、对齐与评估)
    *   [对齐方法论](#对齐方法论)
    *   [评估与基准测试](#评估与基准测试)
    *   [相关论文与资源](#相关论文与资源-4)
*   [2025-2026 顶会前沿速递](#2025-2026-顶会前沿速递)
    *   [计算机视觉与多模态 (CV/Multimodal)](#计算机视觉与多模态-cvmultimodal)
    *   [自然语言处理与认知推理 (NLP/Reasoning)](#自然语言处理与认知推理-nlpreasoning)
    *   [软件工程与系统架构 (SE/Systems)](#软件工程与系统架构-sesystems)
    *   [垂直领域赋能 (Domain-Specific)](#垂直领域赋能-domain-specific)
*   [如何贡献](#如何贡献)
*   [引用](#引用)

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
为了系统地理解AI智能体，我们需要一个清晰的架构蓝图。尽管具体的实现各有不同，但大多数基于LLM的单体智能体都可以被解构成一个包含四个核心模块的统一框架。这个框架由Wang等人（2023）在其广受引用的综述中提出，为我们提供了一个分析和构建智能体的通用模型 。

这个架构的核心思想是将智能体的复杂行为分解为几个功能独立的但又紧密协作的组件。LLM在其中扮演着“大脑”或中央处理器的角色，负责协调各个模块，利用其强大的语言理解和推理能力来驱动整个系统的运作 。

智能体的四个核心模块分别是：

*   **感知模块 (Perception Module)**：智能体与环境交互的入口，负责接收和处理来自外部世界的原始信息，如用户指令、API返回的文本、网页的视觉截图等，并将其转化为内部可理解的结构化表示。

*   **规划与推理模块 (Planning & Reasoning Module)**：智能体的认知核心。它接收感知模块处理后的信息，并根据预设的目标进行思考。这包括将宏大、复杂的目标分解为一系列更小、更具体的可执行步骤或子任务 。

*   **记忆模块 (Memory Module)**：赋予智能体学习和适应能力的关键。它负责存储和检索信息，包括短期记忆（如当前对话的上下文）和长期记忆（如过去的经验、用户偏好、知识库），为规划和行动提供必要的背景信息。

*   **行动模块 (Action Module)**：将规划模块制定的决策转化为与外部环境的实际交互。这通常通过调用外部工具（如代码解释器、搜索引擎API、数据库查询）来实现，从而使智能体能够超越其内部知识的限制，获取实时信息并执行具体任务。

信息在这些模块间的流动形成了一个动态的循环：感知模块获取环境状态，规划模块基于这些信息和记忆进行决策，行动模块执行决策并改变环境状态，而新的环境状态又被感知模块捕获，如此循环往复，直至任务完成。这个架构不仅清晰地划分了功能，也为模块化的设计和迭代优化提供了便利。

```mermaid
graph TB
    E[🌍 环境] -->|原始输入| P
    
    subgraph Agent ["🤖 AI 智能体"]
        P["👁️ 感知模块\n文本 · 视觉 · 音频"]
        R["🧠 规划与推理\nCoT · ReAct · ToT"]
        M["💾 记忆模块\n短期 · 长期 · RAG"]
        A["⚡ 行动模块\n工具 · 代码 · API · MCP"]
        
        P -->|结构化信息| R
        R <-->|上下文检索| M
        R -->|决策| A
    end
    
    A -->|行动与影响| E
    
    style Agent fill:#1e1e2e,stroke:#cba6f7,color:#cdd6f4
    style P fill:#313244,stroke:#89b4fa,color:#cdd6f4
    style R fill:#313244,stroke:#a6e3a1,color:#cdd6f4
    style M fill:#313244,stroke:#f9e2af,color:#cdd6f4
    style A fill:#313244,stroke:#f38ba8,color:#cdd6f4
    style E fill:#181825,stroke:#6c7086,color:#cdd6f4
```

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

```mermaid
graph LR
    A["📝 CoT 线性推理"] -->|"自洽性投票"| B["🔄 Self-Consistency 鲁棒答案"]
    B -->|"加入行动循环"| C["⚙️ ReAct 思考→行动→观察"]
    C -->|"扩展为树"| D["🌳 ToT 系统搜索"]
    D -->|"蒙特卡洛"| E["🎲 MCTS SWE-Search等"]
    
    style A fill:#313244,stroke:#89b4fa,color:#cdd6f4
    style B fill:#313244,stroke:#a6e3a1,color:#cdd6f4
    style C fill:#313244,stroke:#f9e2af,color:#cdd6f4
    style D fill:#313244,stroke:#f38ba8,color:#cdd6f4
    style E fill:#313244,stroke:#cba6f7,color:#cdd6f4
```

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
    
### 核心推理技术对比
为了帮助研究者和开发者快速理解不同推理技术的特点和适用场景，下表对上述核心技术进行了对比。从CoT到ReAct再到ToT的演变，清晰地展示了智能体认知能力从简单的线性演绎，到与环境互动的接地推理，再到复杂问题空间的主动探索这一发展轨迹。

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
*   **检索增强生成 (Retrieval-Augmented Generation, RAG)**：RAG是当前实现长期记忆的主流范式。其核心思想是，在响应用户请求时，首先从一个外部知识库（如文档、数据库）中检索出与当前任务最相关的信息，然后将这些检索到的信息作为附加上下文增强（augment）输入给LLM，最后由LLM生成最终的答案 。通过这种方式，RAG将智能体的回答“锚定”在可靠的外部事实上，不仅能有效减少知识幻觉，还能让智能体利用最新的或私有的数据 。

*   **智能体化RAG (Agentic RAG)**：这是对标准RAG的演进。在Agentic RAG中，一个或多个自主智能体被集成到检索流程中。这些智能体可以动态地管理检索策略，例如，通过自我反思来重构查询语句、决定何时以及从哪个数据源进行检索，甚至协同工作来处理复杂的多步查询，从而使整个检索过程更加智能、灵活和高效 。

*   **向量数据库 (Vector Databases)**：向量数据库是实现高效RAG的底层技术支撑。它将文本、图片等非结构化数据通过嵌入模型（Embedding Model）转换为高维向量，并存储起来。当需要检索时，系统会将用户的查询也转换为一个向量，然后在数据库中快速执行语义相似度搜索，找到与查询向量在“意义”上最接近的存储向量。这种基于语义的检索方式远比传统的关键词匹配更为强大和精准 。

### 相关论文与资源
*   **论文: Cognitive Memory in Large Language Models** (2025)

    该论文深入探讨了LLM中的记忆机制，并巧妙地将人类的认知记忆架构（感觉记忆、短时记忆、长时记忆）与LLM的记忆系统进行了类比分析。

    [arXiv: 2504.02441](https://arxiv.org/abs/2504.02441)

*   **论文: A-Mem: Agentic Memory for LLM Agents** (2025)

    提出了一种新颖的“智能体化记忆”系统（A-Mem）。受知识管理方法Zettelkasten的启发，该系统允许智能体根据新的经验动态地组织、链接和演化其记忆，而不是简单地被动存储。

    [arXiv: 2501.09136](https://arxiv.org/abs/2501.09136)

*   **论文: From Local to Global: A Graph RAG Approach to Query-Focused Summarization** (Edge et al., 2024)

    微软提出的一种结合知识图谱与大语言模型的检索增强生成技术 (GraphRAG)。通过在全量文本上构建结构化的知识图谱，它能够掌握文档集中的全局信息并应对复杂的针对性总结任务，大幅提升了 RAG 处理海量关联信息的能力。

    [arXiv: 2404.16130](https://arxiv.org/abs/2404.16130) / [GitHub仓库](https://github.com/microsoft/graphrag)

*   **综述: Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG** (Singh et al., 2025)

    这是一篇关于Agentic RAG的全面综述，详细介绍了将智能体集成到RAG流程中的各种架构、应用和挑战。

    [arXiv: 2501.09136](https://arxiv.org/abs/2501.09136)

*   **向量数据库:**
    *   [Weaviate](https://weaviate.io/)

记忆机制的发展揭示了智能体能力演进的一个深层逻辑。最初，智能体的能力受限于其预训练知识。长期记忆，特别是通过RAG实现的记忆，允许智能体接入外部知识，极大地扩展了其信息边界。然而，仅仅拥有一个庞大的、静态的知识库并不足以实现真正的适应性。更进一步的发展，如A-Mem系统所展示的，是智能体开始能够主动地构建和组织自己的记忆，根据新的交互经验创建知识间的联系，并不断演化其内部的知识结构。这种自组织的记忆，实际上构成了一个基于个体经验的、独一无二的个性化知识图谱。这意味着，记忆不仅仅是一个被动的存储模块，而是驱动智能体专业化和能力演进的核心引擎。两个从相同基础模型出发的智能体，如果被置于不同的任务环境中，随着时间的推移，它们将发展出截然不同的记忆结构，从而演化为在各自领域具有独特专长的“专家”。因此，记忆是构建智能体身份和专业能力的基石。

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

**模型上下文协议（Model Context Protocol, MCP）** 是 Anthropic 于 2024 年底提出的开放标准，正在迅速成为 AI 智能体连接外部工具、数据源和服务的通用接口。可以将 MCP 理解为"智能体的 USB-C 接口"——一种标准化的即插即用协议，无需为每个工具单独构建集成。

```mermaid
graph LR
    subgraph Host ["🖥️ MCP 宿主（如 Claude Desktop、Cursor）"]
        A[AI 智能体]
        C1[MCP 客户端 1]
        C2[MCP 客户端 2]
        A <--> C1
        A <--> C2
    end
    
    subgraph Servers ["⚙️ MCP 服务器"]
        S1["📁 文件系统"]
        S2["🗄️ 数据库"]
        S3["🌐 网络搜索"]
        S4["💻 代码执行"]
    end
    
    C1 <-->|"MCP 协议 JSON-RPC"| S1
    C1 <-->|MCP 协议| S2
    C2 <-->|MCP 协议| S3
    C2 <-->|MCP 协议| S4
    
    style Host fill:#1e1e2e,stroke:#cba6f7,color:#cdd6f4
    style Servers fill:#181825,stroke:#6c7086,color:#cdd6f4
    style A fill:#313244,stroke:#a6e3a1,color:#cdd6f4
```

**为什么 MCP 重要：**
- **标准化**：任何智能体框架都可以使用任何兼容 MCP 的工具，无需定制集成代码
- **安全性**：服务器定义明确权限，智能体无法访问授权范围之外的资源
- **生态系统**：社区已构建数百个 MCP 服务器，覆盖 GitHub、Slack、数据库、浏览器、文件系统等
- **广泛采用**：Cursor、Windsurf、Claude Desktop 及各主流智能体框架已原生支持 MCP

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

**商业系统对比：**

| 系统 | 开发商 | 核心能力 |
|:---|:---|:---|
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

    特点: 由微软研究院推出的AutoGen，其核心设计理念是简化多智能体协作系统的构建。它提供了一套强大的抽象，用于定义具有不同角色、能力和对话模式的智能体，并协调它们之间的交互来共同完成复杂任务。如果你需要构建一个由多个专家智能体（如“程序员”、“测试员”、“项目经理”）组成的虚拟团队，AutoGen是该领域的首选框架 。

    代码库: [AutoGen GitHub](https://github.com/microsoft/autogen)

4.  **MS-Agent**
    核心定位: 一个轻量级框架，赋能智能体自主探索复杂任务场景。

    特点: MS-Agent 提供了一个灵活且可扩展的架构，使开发者能够创建具备复杂任务处理能力的智能体，例如代码生成、数据分析以及支持 MCP（模型调用协议）的通用工具调用。其特点包括：
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

## 多智能体系统（MAS）：协作产生的涌现智能
当单个智能体的能力达到瓶颈时，人工智能的下一个前沿阵地便转向了由多个智能体协作解决复杂问题的多智能体系统（Multi-Agent Systems, MAS）。在MAS中，任务不再由一个全能的智能体完成，而是被分解并分配给一个由多个具有不同角色、技能和视角的“专家”智能体组成的团队。它们通过相互沟通、协作、辩论甚至竞争，来达成单个智能体无法企及的目标 。

### MAS范式与架构
```mermaid
graph TB
    subgraph Pipeline ["📋 流水线（顺序执行）"]
        direction LR
        PA[智能体 A] -->|输出| PB[智能体 B] -->|输出| PC[智能体 C]
    end
    
    subgraph Flat ["🔄 扁平（同级讨论）"]
        direction LR
        FA[智能体 1] <-->|辩论| FB[智能体 2]
        FB <-->|辩论| FC[智能体 3]
        FA <-->|辩论| FC
    end
    
    subgraph Hierarchical ["🏗️ 层级（管理者-执行者）"]
        direction TB
        M[管理者智能体]
        M -->|子任务| W1[执行者 1]
        M -->|子任务| W2[执行者 2]
        M -->|子任务| W3[执行者 3]
    end
    
    style Pipeline fill:#1e1e2e,stroke:#89b4fa,color:#cdd6f4
    style Flat fill:#1e1e2e,stroke:#a6e3a1,color:#cdd6f4
    style Hierarchical fill:#1e1e2e,stroke:#f38ba8,color:#cdd6f4
```

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

    利用标准操作程序 (SOPs) 对大语言模型进行元编程，将人类工作流编排进多智能体协作框架中。通过一行需求即可生成包括产品文档、架构图、任务列表和可执行代码的完整软件系统，极大降低了幻觉。

    [arXiv: 2308.00352](https://arxiv.org/abs/2308.00352) / [GitHub仓库](https://github.com/geekan/MetaGPT)

*   **论文: Generative Agents: Interactive Simulacra of Human Behavior** (Park et al., 2023)

    著名的“斯坦福小镇”研究。该工作赋予了沙盒环境中25个虚拟角色各自的记忆流 (Memory Stream)，角色可以观察、回忆、反思并与其他成员自然交流，展现出惊人的社会互动涌现能力，为构建真实的社会化多智能体系统提供了开创性范式。

    [arXiv: 2304.03442](https://arxiv.org/abs/2304.03442) / [GitHub仓库](https://github.com/joonspk-research/generative_agents)

*   **论文: ChatDev: Communicative Agents for Software Development** (Qian et al., 2023)

    [arXiv: 2307.07924](https://arxiv.org/abs/2307.07924) / [GitHub仓库](https://github.com/OpenBMB/ChatDev)
    

*   **开发框架**: AutoGen 是当前构建MAS的首选框架，它为定义和协调多智能体对话提供了强大的支持 。

---

## 可信度：安全、对齐与评估
随着智能体变得日益自主，并被赋予在真实世界中采取行动的能力，确保其行为的可信度（Trustworthiness）已成为该领域最重要、最紧迫的议题。一个强大的智能体如果行为不可预测、不符合人类价值观或存在安全漏洞，其潜在风险将远超其带来的益处。因此，智能体的安全（Safety）、与人类价值观的**对齐（Alignment）以及对其行为的严格评估（Evaluation）**构成了可信度研究的三大支柱 。

### 对齐方法论
*   **宪法AI (Constitutional AI, CAI)**: 由Anthropic公司提出的一种创新的对齐技术。传统对齐方法（如RLHF）严重依赖人类标注者来判断模型的输出是否“好”。CAI则试图让AI在一定程度上“自我对齐”。其核心思想是，首先为AI制定一套原则或价值观，即“宪法”（Constitution）。然后，在训练过程中，模型不仅要生成对用户问题的回答，还要根据“宪法”自我批判和修正其回答。这个过程被称为“来自AI反馈的强化学习”（Reinforcement Learning from AI Feedback, RLAIF）。通过这种方式，CAI旨在使对齐过程更具可扩展性、透明度和一致性，减少对大规模人工标注的依赖 。

*   **防御机制**: 除了在训练阶段进行对齐，还需要在部署时采取防御措施。研究人员正在探索多种防御策略，例如，在智能体的“大脑”前后部署外部的“守卫”模型，用于过滤恶意输入和审查不安全的输出；或者利用多智能体系统，通过辩论、审查等方式，集体增强决策的鲁棒性和安全性 。

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

    [arXiv: 2503.01935](https://arxiv.org/abs/2503.01935) / [GitHub仓库](https://github.com/THUDM/AgentBench)
    

智能体研究领域正处在一个关键的转折点。早期的研究重心在于证明和提升智能体的核心能力：它能否推理？能否使用工具？能否完成指定的任务？像AgentBench这样的基准测试正是为了回答这些问题而设计的。然而，随着这些能力的日益强大，并将智能体部署到真实世界的应用中，研究的焦点正不可避免地从“它能做什么？”转向“我们能信任它吗？”。这种转变体现在对齐技术（如宪法AI）、主动风险评估以及综合性可信度框架的研究日益增多。MultiAgentBench的出现进一步凸显了这一趋势，因为它认识到评估单个智能体的安全性与评估一个群体涌现出的、可能无法预测的行为是截然不同的挑战。因此，未来智能体领域的前沿探索，其衡量标准将越来越少地依赖于任务成功率等能力指标，而更多地依赖于可靠性、对齐度和安全性等可信度指标。如何构建可验证的、安全的、符合伦理的智能体系统，已成为该领域最核心的开放性问题。

---

## 2025-2026 顶会前沿速递

为了保持指南的前沿性，本节专门收录 2025 至 2026 年间在各大 AI 顶级会议（ACL, EMNLP, NeurIPS, ICLR, AAAI 等）上发表的影响力极大、引用量极高的代表性智能体论文。这些论文均在各自子领域引起了巨大反响。

### 计算机视觉与多模态 (CV/Multimodal)
*   **Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making** (NeurIPS 2024)
    
    提出了首个针对具身决策任务的大语言模型基准框架，填补了智能体在复杂三维环境中交互评估的空白，引领了具身人工智能的下一步评价标准。
    
    [arXiv: 2410.07166](https://arxiv.org/abs/2410.07166) / [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=Embodied+Agent+Interface+Benchmarking+LLMs+Embodied+Decision+Making)

### 自然语言处理与认知推理 (NLP/Reasoning)
*   **Large Language Model Agent: A Survey on Methodology, Applications and Challenges** (ACL 2025 / 核心工作)

    全面系统地梳理了大型语言模型智能体的发展脉络，涵盖从基础架构到多智能体系统的前沿挑战，是了解最新全貌的必读神级综述。
    
    [arXiv: 2503.21460](https://arxiv.org/abs/2503.21460) / [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=Large+Language+Model+Agent+Survey+Methodology+Applications+Challenges+2025)

*   **Planning with Multi-Constraints via Collaborative Language Agents** (ACL 2025)

    针对复杂约束条件下的任务规划难题，该工作提出了一种协作语言智能体框架，大幅提高了系统在严苛自然语言指令下的规划成功率。

    [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=Planning+Multi-Constraints+Collaborative+Language+Agents)

### 软件工程与系统架构 (SE/Systems)
*   **SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement** (ICLR 2025)
    
    创新性地将蒙特卡洛树搜索（MCTS）与大语言模型软件开发智能体深入融合，在代码库导航和错误自动修复 (Issue Resolution) 任务中实现了惊人优化。

    [arXiv: 2410.20285](https://arxiv.org/abs/2410.20285) / [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=SWE-Search+Software+Agents+Monte+Carlo+Tree+Search)

*   **AgentHarm: Benchmarking Robustness of LLM Agents on Harmful Tasks** (ICLR 2025)
    
    该研究直面智能体安全性与脆弱性的痛点，提出了首个针对对抗性及有害连续交互任务进行防御评测的鲁棒性标杆。

    [arXiv: 2410.09024](https://arxiv.org/abs/2410.09024) / [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=AgentHarm+Benchmarking+Robustness+LLM+Agents+Harmful)

### 垂直领域赋能 (Domain-Specific)
*   **AgentMD: Empowering language agents for risk prediction with large-scale clinical tool learning** (NeurIPS / Nature Comms 2025) 
    
    不仅限于通用推理，该文揭示了语言智能体如何通过整合上万种真实临床工具，实现多模态病情分析与精准风险预测，是领域数字医疗智能体的天花板之作。
    
    [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=AgentMD+Empowering+Language+Agents+Risk+Prediction+Clinical)

---

## 如何贡献
我们热烈欢迎社区的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解完整贡献指南。

**快速开始：**
- 📄 **添加论文**：提交 PR，按照[论文模板](CONTRIBUTING.md)添加条目
- 🐛 **报告问题**：通过 GitHub Issue 报告失效链接、过时信息或错误
- 💡 **建议新章节**：在 GitHub Discussions 发起讨论

**论文质量要求：**
- 在主要会议（NeurIPS/ICLR/ACL/CVPR/AAAI 等）发表，或被高引用（100+ 引用）的预印本，或有影响力的开源项目（500+ stars）
- 可公开访问的预印本（arXiv 等）
- 与 AI 智能体架构、能力或评估直接相关

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

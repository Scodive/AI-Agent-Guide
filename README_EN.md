# AI-Agent-Guide

[English](README_EN.md) | [中文](README.md)

[![GitHub Stars](https://img.shields.io/github/stars/Scodive/AI-Agent-Guide?style=social)](https://github.com/Scodive/AI-Agent-Guide/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Scodive/AI-Agent-Guide)](https://github.com/Scodive/AI-Agent-Guide/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Scodive/AI-Agent-Guide/blob/main/CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/github/license/Scodive/AI-Agent-Guide)](https://github.com/Scodive/AI-Agent-Guide/blob/main/LICENSE)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Welcome to **AI-Agent-Guide**. This repository keeps its long-form guide and adds a manually curated paper catalog. Each catalog record links to a primary paper page and records the research question, mechanism, evaluation setting, conclusion, limitation, and verification date.

**Start here:** [Site](https://ai-notes-red-two.vercel.app) · [Reading path](docs/reading-path.md) · [Paper table](docs/papers.md) · [September 2026 picks](docs/monthly-picks.md) · [Harness and coding agents](docs/harness.md) · [RSI and self-improvement](docs/rsi.md) · [Weekly maintenance SOP](docs/update-sop.md) · [CSV data](data/papers.csv).

As of October 5, 2026, the catalog contains 67 papers, including 10 September picks. This review adds memory-utility identification, incident-recovery evaluation, and three older omissions: MemGPT, LATS, and τ²-Bench. See the [weekly review](data/weekly-reviews/2026-10-05.md) for teaching changes and pending verification. The separate presentation website consumes the CSV; this repository maintains the data and guide. Catalog inclusion does not mean independent replication. Please report incorrect links or descriptions through an Issue or PR.

## How to use this guide

The long-form guide below introduces foundational modules such as perception, planning, memory, and action. It is a conceptual starting point, not an exhaustive list of current techniques. For recent work, use the [monthly picks](docs/monthly-picks.md) alongside the [paper catalog](docs/papers.md):

| Recent question | Start with | Where it fits |
| --- | --- | --- |
| How are agents built, configured, and supervised? | [τ^τ-Bench](https://arxiv.org/abs/2609.04611), [Scanning the Harness](https://arxiv.org/abs/2609.07360), [The Work Behind Delegation](https://arxiv.org/abs/2609.24234) | Coding, tools, and safety; harnesses and human oversight span several modules. |
| What shortcuts can tool-use policies learn? | [Spurious Tool Use](https://arxiv.org/abs/2609.16268) | Tools and action; agent improvement. |
| How should long-term memory and multi-agent coordination be evaluated? | [DolphinBench](https://arxiv.org/abs/2609.24971), [CoCoBench](https://arxiv.org/abs/2608.28266) | Memory and retrieval; multi-agent systems. |
| How do we measure real use and downstream outcomes? | [DAREBench](https://arxiv.org/abs/2609.06059), [Are We There Yet?](https://arxiv.org/abs/2609.00524), [Who Finishes the Job?](https://arxiv.org/abs/2609.26847) | Evaluation, GUI, and coding; include cost, users, and follow-up fixes. |

**Coverage limit:** This is a curated reading path, not a live inventory of every new model, framework, or paper. The [harness chapter](docs/harness.md) explains coding-agent runtimes; the [RSI chapter](docs/rsi.md) separates prompt, agent-program, and target-algorithm improvement. Both are introductory syntheses. New papers enter the catalog first; the [weekly SOP](docs/update-sop.md) governs updates to the guide.

---

## Table of Contents

- [How to use this guide](#how-to-use-this-guide)
- [Foundational Overviews & Surveys](#foundational-overviews--surveys)
  - [General Agent Surveys](#general-agent-surveys)
  - [Domain-Specific Application Surveys](#domain-specific-application-surveys)
  - [Foundation Models & Decision Making Surveys](#foundation-models--decision-making-surveys)
- [Anatomy of AI Agents: Core Architecture Blueprint](#anatomy-of-ai-agents-core-architecture-blueprint)
  - [Architecture Blueprint — Key Papers](#architecture-blueprint--key-papers)
- [Perception Module: Perceiving Digital and Physical Worlds](#perception-module-perceiving-digital-and-physical-worlds)
  - [Text Perception](#text-perception)
  - [Multimodal Perception & GUI Agents](#multimodal-perception--gui-agents)
  - [Core Tech: Vision-Language Models (VLMs)](#core-tech-vision-language-models-vlms)
  - [Key Challenges](#key-challenges)
  - [Related Papers & Resources](#related-papers--resources)
- [Planning & Reasoning Module: The Cognitive Core of Agents](#planning--reasoning-module-the-cognitive-core-of-agents)
  - [Base Reasoning Tech Evolution](#base-reasoning-tech-evolution)
  - [From thought search to feedback-guided action search](#from-thought-search-to-feedback-guided-action-search)
  - [Reasoning Tech Comparisons](#reasoning-tech-comparisons)
- [Memory Module: Enabling Learning and Context Awareness](#memory-module-enabling-learning-and-context-awareness)
  - [Memory Architecture](#memory-architecture)
  - [Core Mechanisms for Long-Term Memory](#core-mechanisms-for-long-term-memory)
  - [Related Papers & Resources](#related-papers--resources-1)
  - [From storing memory to influencing outcomes](#from-storing-memory-to-influencing-outcomes)
- [Action Module: Executing Tasks and Using Tools](#action-module-executing-tasks-and-using-tools)
  - [Tool Use Paradigms](#tool-use-paradigms)
  - [Tool Creation Paradigms](#tool-creation-paradigms)
  - [MCP: Model Context Protocol](#mcp-model-context-protocol)
  - [Related Papers & Resources](#related-papers--resources-2)
- [Agentic Coding: The Software Engineering Frontier](#agentic-coding-the-software-engineering-frontier)
  - [Key Systems & Benchmarks](#key-systems--benchmarks)
  - [Related Papers & Resources](#related-papers--resources-3)
- [Agent Development Frameworks: From Theory to Practice](#agent-development-frameworks-from-theory-to-practice)
  - [Deep Dive into Mainstream Frameworks](#deep-dive-into-mainstream-frameworks)
  - [Framework Comparisons](#framework-comparisons)
  - [Practice: Paper-Agent-Skills](#practice-paper-agent-skills)
- [Self-Evolving Agents: Self-Improvement and Adaptation Mechanisms](#self-evolving-agents-self-improvement-and-adaptation-mechanisms)
  - [Adaptation mechanisms and the RSI boundary](#adaptation-mechanisms-and-the-rsi-boundary)
  - [Related Papers & Resources](#related-papers--resources-4)
- [Multi-Agent Systems (MAS): Emergent Intelligence through Collaboration](#multi-agent-systems-mas-emergent-intelligence-through-collaboration)
  - [MAS Paradigm & Architectures](#mas-paradigm--architectures)
  - [Typical Applications](#typical-applications)
  - [Key Challenges](#key-challenges-1)
  - [Related Papers & Resources](#related-papers--resources-5)
- [Trustworthiness: Safety, Alignment, and Evaluation](#trustworthiness-safety-alignment-and-evaluation)
  - [Alignment Methodologies](#alignment-methodologies)
  - [From outcomes to evaluation protocols](#from-outcomes-to-evaluation-protocols)
  - [Context trust and execution permissions](#context-trust-and-execution-permissions)
  - [Evaluation & Benchmarks](#evaluation--benchmarks)
  - [Related Papers & Resources](#related-papers--resources-6)
- [2025–2026 Selected Research](#20252026-selected-research)
  - [Computer Vision & Multimodal (CV/Multimodal & GUI)](#computer-vision--multimodal-cvmultimodal--gui)
  - [NLP, Reasoning & Reinforcement Learning (NLP/Reasoning & RL)](#nlp-reasoning--reinforcement-learning-nlpreasoning--rl)
  - [Software Engineering & Systems (SE/Systems)](#software-engineering--systems-sesystems)
  - [Trustworthiness, Safety & Stress Analysis (Trustworthiness & Safety)](#trustworthiness-safety--stress-analysis-trustworthiness--safety)
- [How to Contribute](#how-to-contribute)
- [Citation](#citation)

---

## Foundational Overviews & Surveys

For any researcher looking to dive into the field of AI agents, starting with authoritative survey papers is essential. These documents provide a macro perspective, core concept definitions, and systematic technology classifications, serving as the cornerstone for building a knowledge framework. This section highlights high-quality survey papers covering topics from general agent architectures to specific domain applications.

### General Agent Surveys

- **A Survey on Large Language Model based Autonomous Agents** (Wang et al., 2023)

  This paper proposes a holistic framework for LLM-driven autonomous agents, systematically surveying existing research across three dimensions: construction, application, and evaluation. The proposed agent architecture (profile, memory, planning, and action modules) has become a widely-cited standard model in the field.

  [arXiv: 2308.11432](https://arxiv.org/abs/2308.11432)

- **Large Language Model Agent: A Survey on Methodology, Applications and Challenges** (Luo et al., 2025)

  This methodology-centric survey systematically deconstructs LLM agent systems, exploring architectural foundations, collaboration mechanisms, and evolution paths of agents. It unifies fragmented research threads and reveals connections between agent design principles and their emergent behaviors in complex environments.

  [arXiv: 2503.21460](https://arxiv.org/abs/2503.21460) / [GitHub](https://github.com/luo-junyu/Awesome-Agent-Papers)

- **Agentic Large Language Models, a Survey** (Plaat et al., 2025)

  This survey categorizes the core capabilities of Agentic LLMs into three aspects: reasoning, acting, and interacting. It clearly illustrates how different research domains reinforce one another—information retrieval empowers tool utilization, and reflection mechanisms enhance multi-agent collaboration.

  [arXiv: 2503.23037](https://arxiv.org/abs/2503.23037) / [Website](https://askeplaat.github.io/agentic-llm-survey-site/)

### Domain-Specific Application Surveys

- **A Survey of Large Language Model Agents for Question Answering** (2025)

  Focusing on agents in Question Answering tasks, this paper reviews LLM agent design covering planning, question comprehension, information retrieval, and answer generation, while discussing current challenges and future research directions.

  [arXiv: 2503.19213](https://arxiv.org/abs/2503.19213)

- **A Survey of Large Language Model Empowered Agents for Recommendation and Search** (Zhang et al., 2025)

  Explores the transformative potential of LLM agents in enhancing recommendation systems and search engines, offering the first systematic review and classification of LLM agent research in information retrieval.

  [arXiv: 2503.05659](https://arxiv.org/abs/2503.05659)

- **Large Language Model-based Data Science Agent: A Survey** (Wang et al., 2025)

  Comprehensively analyzes LLM agents designed for data science tasks, bridging general agent design principles with practical data science workflows (data preprocessing, model development, evaluation, and visualization).

  [arXiv: 2508.02744](https://arxiv.org/abs/2508.02744)

### Foundation Models & Decision Making Surveys

- **Foundation Models for Decision Making: Problems, Methods, and Opportunities** (Yang et al., 2023)

  Explores the application of foundation models in the broader field of decision-making, providing essential context for understanding agent behavior. Reviews how foundation models can be used in practical decision tasks through prompting, generative modeling, planning, optimal control, and reinforcement learning.

  [arXiv: 2303.04129](https://arxiv.org/abs/2303.04129)

---

## Anatomy of AI Agents: Core Architecture Blueprint

This guide uses four analytical views—perception, planning and reasoning, memory, and action—to explain a decision loop. They need not correspond to four independent implementation modules. Wang et al.'s survey uses profile, memory, planning, and action; this guide separately introduces input processing as perception. These are different taxonomies, rather than a single universal standard.

The LLM can propose decisions; the harness organizes context, executes tools, persists state, and applies stopping rules. For each module, ask how information reaches the model, who executes an action, and what evidence verifies its result.

The four core modules are:

- **Perception Module**: The entry point for environmental interaction. Receives and processes raw information—user instructions, API responses, webpage screenshots—transforming it into structured representations the agent can understand.

- **Planning & Reasoning Module**: The cognitive core. Receives processed information and conducts reasoning based on goals, breaking down complex objectives into specific, executable steps or subtasks.

- **Memory Module**: Enables learning and adaptation. Stores and retrieves information including short-term memory (current conversation context) and long-term memory (past experiences, user preferences, knowledge bases).

- **Action Module**: Translates planning decisions into actual environmental interactions by invoking external tools (code interpreters, search APIs, databases), enabling the agent to access real-time information and execute tasks.

Information flows in a dynamic cycle: Perception → Planning (with Memory) → Action → Environment → Perception, repeating until the task is complete.

These four modules describe the **agent's internal decision loop**. A runnable system also needs an explicit harness: tool interfaces, context and state management, execution permissions, verification and stopping rules, and human oversight. The harness can affect outcomes and resource use even when the model is held fixed, so model name alone is not a full system description. See [Code as Agent Harness](https://arxiv.org/abs/2605.18747) and [DAREBench](https://arxiv.org/abs/2609.06059). This extends the introductory blueprint; it does not imply a single standard implementation.

### Architecture Blueprint — Key Papers

- **Cognitive Architectures for Language Agents (CoALA)** (Sumers et al., 2023)

  Deeply integrates modern LLMs with classic cognitive science architectures (ACT-R, SOAR) to construct the highly influential CoALA standard. Rigorously defines the cyclical relationship between "internal actions" (procedure/memory modules) and the "external environment," deepening the theoretical foundation of general agent architecture design.

  [arXiv: 2309.02427](https://arxiv.org/abs/2309.02427)

- **OpenAgents: An Open Platform for Language Agents in the Wild** (Xie et al., 2023)

  Explores a unified design model from an engineering implementation perspective. Uses a highly standardized perception-planning-memory-execution framework to simultaneously incubate three complex specialized agent systems (data analysis, plugin, and web agents). A quintessential system engineering achievement validating complex multimodal modular architectures.

  [arXiv: 2310.10634](https://arxiv.org/abs/2310.10634) / [GitHub](https://github.com/xlang-ai/OpenAgents)

---

## Perception Module: Perceiving Digital and Physical Worlds

Perception is the bridge connecting agents to the world, and the foundation for all subsequent thinking and action. This module receives raw data from the environment and transforms it into structured information that the planning module can understand and utilize. The sophistication of perception capabilities directly determines the complexity of environments in which an agent can effectively operate.

### Text Perception

The most fundamental form of perception: agents understand their tasks and environment by processing pure text input. These inputs can come from many sources—user natural language instructions, document content read from files, or text results returned from API calls.

### Multimodal Perception & GUI Agents

As agent application scenarios expand from pure-text environments to graphical user interfaces (GUIs), web pages, and even the physical world, multimodal perception has become critical. It enables agents to "see" and understand visual information, allowing them to interact with systems designed for humans.

**Computer Use** represents a major frontier: agents that can directly control any application on a computer screen—clicking buttons, filling forms, navigating browsers—just like a human operator. This requires tight integration of vision, planning, and fine-grained action execution.

### Core Tech: Vision-Language Models (VLMs)

VLMs are the technical cornerstone of multimodal perception. These models combine visual encoders with language models to learn deep associations between visual data (images/video) and text. This enables agents to process not just text, but also understand visual elements in screenshots such as buttons, text boxes, and icons—a prerequisite for any GUI interaction.

### Key Challenges

Despite significant advances, several challenges remain in agent perception:

- **Element Grounding**: Precisely identifying and locating the coordinates of interactive elements (buttons, input fields) on GUI interfaces is extremely difficult. Even state-of-the-art VLMs often perform poorly here, as they are typically trained for image captioning or classification rather than pixel-level precise localization.

- **High-Resolution Input Processing**: GUI screenshots are typically high-resolution, producing extremely long token sequences when fed into VLMs, leading to high computational costs and inefficiency. Specialized optimization techniques are needed to handle redundancy and structural features in UI visual information.

- **Environmental Noise**: Real-world GUI environments are filled with visual information irrelevant to the core task—advertising pop-ups, promotional content, recommended content. Research shows that even top GUI agents can easily be distracted by these visual "distractors," deviating from the user's original intent.

### Related Papers & Resources

- **Survey: Agent AI: Surveying the Horizons of Multimodal Interaction** (Durante et al., 2024)

  Defines "Agent AI" as systems capable of perceiving visual stimuli and other grounded data to produce embodied actions, scoping the research domain for multimodal agents.

  [arXiv: 2401.03568](https://arxiv.org/abs/2401.03568)

- **OmniParser for Pure Vision Based GUI Agent** (Lu et al., 2024)

  Microsoft's OmniParser addresses the low precision of existing multimodal models when localizing GUI elements and their heavy reliance on DOM/XML structural trees. It is a pure-vision parsing system capable of precisely extracting and inferring interactive elements and their semantics on any screen, significantly improving GPT-4V's task success rate on real devices.

  [arXiv: 2408.00203](https://arxiv.org/abs/2408.00203) / [GitHub](https://github.com/microsoft/OmniParser)

- **Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception** (Wang et al., 2024)

  Introduces a pure-vision-driven mobile device agent that autonomously navigates and operates apps solely by analyzing screenshots, without relying on system-level metadata (XML layout files). Demonstrates the enormous potential of visual perception for cross-platform generality.

  [arXiv: 2401.16158](https://arxiv.org/abs/2401.16158) / [GitHub](https://github.com/X-PLUG/MobileAgent)

- **UI-TARS: Pioneering Automated GUI Interaction with Native Agents** (ByteDance, 2025)

  UI-TARS is an end-to-end GUI agent model that perceives screenshots and directly outputs precise actions (click coordinates, keyboard input). It achieves state-of-the-art performance on multiple GUI benchmarks (ScreenSpot, OSWorld, AndroidWorld) through large-scale GUI-specific training data and systematic reflection mechanisms.

  [arXiv: 2501.12326](https://arxiv.org/abs/2501.12326) / [GitHub](https://github.com/bytedance/UI-TARS)

- **ScreenSpot: A Grounding Benchmark for GUI Agents** (Cheng et al., 2024)

  Introduces a challenging benchmark for evaluating GUI element grounding, covering mobile, desktop, and web platforms. Reveals that even strong VLMs struggle significantly with fine-grained element localization.

  [arXiv: 2401.10935](https://arxiv.org/abs/2401.10935) / [GitHub](https://github.com/njucckevin/SeeClick)

The leap from text to vision is a critical step toward universal agents. However, current research clearly shows that reliable, faithful multimodal perception remains the primary bottleneck. The entire agent stack ultimately relies on the fidelity of its perception module.

---

## Planning & Reasoning Module: The Cognitive Core of Agents

The planning and reasoning module is the agent's "brain," responsible for formulating strategies to achieve goals. It receives information from the perception module and decomposes the core task—a high-level user goal—into a concrete, executable sequence of steps. The evolution of LLM reasoning capabilities is the core driver of agent capability development.


### Base Reasoning Tech Evolution

1. **Chain-of-Thought (CoT) & Self-Consistency**

   CoT is the foundational technique for unlocking complex reasoning in LLMs. By adding "Let's think step by step" instructions or examples to prompts, it guides the model to generate intermediate reasoning steps before giving a final answer. This approach mimics human problem-solving and significantly improves performance on arithmetic, commonsense, and symbolic reasoning tasks.

   Self-Consistency further enhances CoT by sampling the same problem multiple times, generating multiple different chains of thought, then selecting the most consistent answer through "voting," improving result robustness and accuracy.

   Foundational Papers:
   - **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (Wei et al., 2022) — [arXiv: 2201.11903](https://arxiv.org/abs/2201.11903)
   - **Self-Consistency Improves Chain of Thought Reasoning in Language Models** (Wang et al., 2022) — [arXiv: 2203.11171](https://arxiv.org/abs/2203.11171)

2. **ReAct: Synergizing Reasoning and Acting**

   ReAct is a paradigm shift, interleaving **Reasoning (Thought) and Action**. The agent first generates a "thought" analyzing the current situation and planning the next step, then executes an "action" (calling a search API to retrieve missing information). The action result is fed back as a new observation for the next reasoning cycle. This "Thought-Action-Observation" loop grounds the agent's reasoning in real-world information, effectively alleviating the knowledge hallucination problem of pure internal reasoning (like CoT).

   Foundational Paper: **ReAct: Synergizing Reasoning and Acting in Language Models** (Yao et al., 2022)

   [arXiv: 2210.03629](https://arxiv.org/abs/2210.03629) / [GitHub](https://github.com/ysymyth/ReAct)

3. **Tree of Thoughts (ToT)**

   ToT breaks the linear reasoning pattern of CoT and ReAct. When facing problems requiring exploration or deliberation, ToT allows the model to simultaneously explore multiple reasoning paths organized as a "thought tree." The LLM plays both "thinker" and "evaluator" roles: self-evaluating the value and prospects of each node (intermediate "thought") in the tree, then deciding whether to continue exploring a path (lookahead) or abandon it and backtrack to try other possibilities.

   Foundational Paper: **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (Yao et al., 2023)

   [arXiv: 2305.10601](https://arxiv.org/abs/2305.10601) / [GitHub](https://github.com/princeton-nlp/tree-of-thought-llm)

### From thought search to feedback-guided action search

[LATS](https://arxiv.org/abs/2310.04406) connects ReAct and ToT: MCTS selects and expands trajectories, estimates value after observing the environment, backpropagates terminal feedback, and retains failure reflections. Read it before SWE-Search to distinguish searching thoughts from searching executable actions.

These techniques are composable design choices. Report nodes, trajectories, tokens, and environment calls together. LATS uses correctness-oracle feedback for HotpotQA and assumes reversible states; backtracking in a benchmark does not authorize reversing real payments or production changes. See the [catalog record](docs/papers.md#paper-2310.04406).

### Reasoning Tech Comparisons

| Technique | Core Idea | Main Advantage | Best Use Case |
|:---|:---|:---|:---|
| Chain-of-Thought (CoT) | Decompose complex problems through intermediate steps | Significantly improves LLM performance on complex reasoning | Arithmetic, commonsense and symbolic reasoning |
| Self-Consistency | Multi-sample voting on CoT results | Higher answer accuracy and stability | Tasks requiring high result accuracy |
| ReAct | Interleaved "Think-Act-Observe" loop | Grounds reasoning in the external world, reduces hallucination | Tasks needing external tool interaction (search engines, APIs) |
| Tree of Thoughts (ToT) | Explore multiple reasoning paths, self-evaluate and backtrack | Handles complex problems requiring exploration and deliberation | Multi-step decisions with multiple possible paths |
| MCTS-based (SWE-Search) | Monte Carlo Tree Search over reasoning/action space | Systematic search with iterative refinement | Large search-space tasks like software bug fixing |

---

## Memory Module: Enabling Learning and Context Awareness

If planning and reasoning are the agent's "brain," memory is the foundation for gaining wisdom and enabling growth. The memory module allows agents to escape the limitations of "one-shot" tools, becoming stateful entities that can learn from experience and maintain context awareness in continuous interactions. Without memory, every interaction is a cold start.

### Memory Architecture

Agent memory systems are typically designed to mimic human cognitive architecture, divided into two main types:

- **Short-Term Memory**: Corresponds to the context window the LLM can process in a single interaction. Stores immediate information from the current conversation—fast to access but limited in capacity and temporary. Lost when the session ends or the context window fills up.

- **Long-Term Memory**: Enables cross-session knowledge retention and learning by storing information in external databases. Allows agents to persistently save and recall past interactions, user preferences, and successful or failed experiences. Critical for continuous learning and capability evolution.

### Core Mechanisms for Long-Term Memory

- **Retrieval-Augmented Generation (RAG)**: A mechanism for retrieving external knowledge or experience into the current context; a knowledge corpus, episodic memory, and visible context should be described separately. When responding to a user request, first retrieve the most relevant information from an external knowledge base (documents, databases), then augment the LLM's input with retrieved information as additional context. Its benefit depends on source quality, recall, and how the model uses the evidence; retrieval does not guarantee a correct answer.

- **Agentic RAG**: An evolution of standard RAG where one or more autonomous agents are integrated into the retrieval pipeline. These agents can dynamically manage retrieval strategies—reformulating queries through self-reflection, deciding when and from which data source to retrieve, or collaborating on complex multi-step queries—making the entire retrieval process more intelligent and flexible.

- **Vector Databases**: The underlying technical support for efficient RAG. Converts unstructured data (text, images) into high-dimensional vectors via embedding models for storage. During retrieval, the user query is also converted to a vector and semantic similarity search is performed to find the most conceptually related stored vectors. Compare semantic and keyword retrieval on task-specific recall, precision, and cost.

### Related Papers & Resources

- **Cognitive Memory in Large Language Models** (2025)

  Deeply explores memory mechanisms in LLMs and analyzes analogies between human cognitive memory architecture (sensory, short-term, long-term memory) and LLM memory systems.

  [arXiv: 2504.02441](https://arxiv.org/abs/2504.02441)

- **A-Mem: Agentic Memory for LLM Agents** (2025)

  Proposes a novel "agentic memory" system (A-Mem). Inspired by the Zettelkasten knowledge management method, this system allows agents to dynamically organize, link, and evolve their memories based on new experiences, rather than simply passively storing information.

  [arXiv: 2502.12110](https://arxiv.org/abs/2502.12110) / [GitHub](https://github.com/agiresearch/A-mem)

- **From Local to Global: A Graph RAG Approach to Query-Focused Summarization** (Edge et al., 2024)

  Microsoft's GraphRAG combines knowledge graphs with LLMs. By constructing a structured knowledge graph over the full text corpus, it captures global information across document collections and handles complex targeted summarization tasks, significantly improving RAG's ability to process massive interconnected information.

  [arXiv: 2404.16130](https://arxiv.org/abs/2404.16130) / [GitHub](https://github.com/microsoft/graphrag)

- **Survey: Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG** (Singh et al., 2025)

  A comprehensive survey on Agentic RAG, detailing various architectures, applications, and challenges of integrating agents into RAG pipelines.

  [arXiv: 2501.09136](https://arxiv.org/abs/2501.09136)

- **Vector Databases**: [Weaviate](https://weaviate.io/) · [Chroma](https://www.trychroma.com/) · [Qdrant](https://qdrant.tech/) · [Pinecone](https://www.pinecone.io/)

### From storing memory to influencing outcomes

Separate **storage → retrieval → visible context → task outcome → future retention**. [MemGPT](https://arxiv.org/abs/2310.08560) explains tiered storage, paging, and control flow; A-MEM explains organization. These address complementary questions.

[CMP](https://arxiv.org/abs/2610.02070) adds a measurement boundary: a memory never exposed in context has not been tested, so absent contribution does not establish uselessness. Random exposure improves identification, but the experimental pool uses relevance labels and future-query retention remains unresolved. Read it as an evaluation method, rather than a deployment-ready eviction policy.

---

## Action Module: Executing Tasks and Using Tools

The action module is the bridge translating the agent's internal decisions into actual effects on the external world. Through this module, agents transcend pure language generation—interacting with the environment by calling APIs, executing code, or operating software to become practical problem-solvers.

### Tool Use Paradigms

Empowering agents to use tools is key to improving their practical value. Current research focuses on two directions: teaching agents to use existing tools, and enabling agents to create new tools.

1. **Self-Supervised Tool Learning**

   Aims to enable LLMs to autonomously learn how to use external tools without large-scale human annotation.

   - **Toolformer**: A pioneering work. The model tries inserting API calls at various positions in text and observes whether doing so helps predict subsequent text. If an API call (and its returned result) significantly lowers the model's prediction difficulty, it is deemed beneficial and retained as new training data. Through fine-tuning on this self-generated data, the LLM learns to call the right API at the right time with the right parameters.

2. **Mastering Massive Real-World APIs**

   For agents to work in the real world, they must call thousands of real, diverse APIs.

   - **Gorilla**: Addresses LLM inaccuracy in generating API calls by fine-tuning LLaMA on a large-scale, high-quality API call dataset, surpassing GPT-4 in API call accuracy. Introduces "Retriever-Aware Training" to enable decisions based on up-to-date API documentation during inference.

   - **ToolLLM**: Bridges the gap between open-source and closed-source models in tool use capabilities. Constructs ToolBench, a massive instruction fine-tuning dataset containing 16,000+ real-world RESTful APIs. The resulting ToolLLaMA matches ChatGPT performance in handling complex instructions and generalizing to unseen APIs.

### Tool Creation Paradigms

This represents a new height of agent capability: from tool *user* to tool *creator*.

- **LLMs as Tool Makers (LATM)**: A two-stage process. In the "tool creation" phase, a powerful but expensive LLM (e.g., GPT-4) acts as the "tool creator," generating reusable Python functions as tools. In the "tool use" phase, a lighter, more economical LLM acts as the "tool user," directly calling the pre-generated tools to complete tasks. This division spreads one-time high creation costs across many low-cost uses.

### MCP: Model Context Protocol

The **Model Context Protocol (MCP)** standardizes interfaces for clients and servers to exchange tools, resources, and related information. Task state, business authorization, and execution outcomes remain implementation responsibilities.

Separate the protocol interface, server/downstream authentication and authorization, and harness/environment process, file, and network permissions. MCP support does not itself guarantee isolation. The official [security practices](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices) discuss token passthrough, confused-deputy risks, and scope minimization (checked 2026-10-05).

**Key Resources:**
- [Official MCP Specification](https://modelcontextprotocol.io/)
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) — Community-curated server list
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)

### Related Papers & Resources

- **Toolformer: Language Models Can Teach Themselves to Use Tools** (Schick et al., 2023)

  [arXiv: 2302.04761](https://arxiv.org/abs/2302.04761)

- **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering** (Jimenez et al., 2024)

  Proposes the SWE-agent system with a specialized "Agent-Computer Interface" (ACI) that dramatically improves LLM efficiency in navigating codebases, viewing, editing, and executing code, achieving outstanding performance on SWE-bench.

  [arXiv: 2405.15793](https://arxiv.org/abs/2405.15793) / [GitHub](https://github.com/princeton-nlp/SWE-agent)

- **Gorilla: Large Language Model Connected with Massive APIs** (Patil et al., 2023)

  [arXiv: 2305.15334](https://arxiv.org/abs/2305.15334) / [GitHub](https://github.com/ShishirPatil/gorilla)

- **ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs** (Qin et al., 2023)

  [arXiv: 2307.16789](https://arxiv.org/abs/2307.16789) / [GitHub](https://github.com/OpenBMB/ToolBench)

- **LLMs as Tool Makers** (Cai et al., 2023)

  [arXiv: 2305.17126](https://arxiv.org/abs/2305.17126)

---

## Agentic Coding: The Software Engineering Frontier

Agentic coding represents one of the most commercially impactful frontiers of AI agents. Rather than simple code completion, these agents operate over entire codebases—understanding complex software architectures, localizing bugs, writing multi-file patches, executing tests, and iterating until issues are resolved. This section covers the key benchmarks, systems, and research driving this field.

### Key Systems & Benchmarks

**Benchmarks:**

- **SWE-bench**: The standard benchmark for evaluating coding agents. Contains 2,294 real GitHub issues from popular Python repositories (Django, scikit-learn, etc.). An agent must analyze the codebase and submit a code patch that resolves the issue. SWE-bench Verified is a human-validated subset with more reliable ground truth.

  [Website](https://www.swebench.com/) / [arXiv: 2310.06770](https://arxiv.org/abs/2310.06770) / [GitHub](https://github.com/princeton-nlp/SWE-bench)

**Open-Source Agents:**

- **SWE-agent** (Princeton, 2024): Designs a specialized Agent-Computer Interface (ACI) for navigating and editing large codebases. The ACI provides tools like file viewer with line numbers, targeted search, and edit commands that are specifically optimized for LLM use patterns. Achieves strong performance on SWE-bench.

  [arXiv: 2405.15793](https://arxiv.org/abs/2405.15793) / [GitHub](https://github.com/princeton-nlp/SWE-agent)

- **OpenHands (formerly OpenDevin)**: An open-source platform for AI software development agents that can browse the web, write and execute code, and manage files. Supports multiple backend LLMs and is built for real-world software development workflows.

  [GitHub](https://github.com/All-Hands-AI/OpenHands)

- **SWE-Search** (2024): Enhances coding agents by integrating Monte Carlo Tree Search (MCTS) with LLM software agents. Enables systematic exploration of large code-action spaces with iterative refinement, achieving significant improvements on issue resolution tasks.

  [arXiv: 2410.20285](https://arxiv.org/abs/2410.20285) / [GitHub](https://github.com/aorwall/moatless-tools)

**Understanding delivery:** A generated patch, passing tests, human acceptance, post-merge maintenance, and live-service recovery are distinct observations. Use the [harness chapter](docs/harness.md) to separate interfaces, context, and verification, then [Who Finishes the Job?](https://arxiv.org/abs/2609.26847) for follow-up maintenance. [Incident-Arena](https://arxiv.org/abs/2610.00648) extends evaluation to recovery under sustained load and restart while preserving data and permitted change scope. Its limited tasks and model/harness pairs do not establish a commercial product ranking.

### Related Papers & Resources

- **SWE-bench: Can Language Models Resolve Real-world GitHub Issues?** (Jimenez et al., 2023)

  [arXiv: 2310.06770](https://arxiv.org/abs/2310.06770)

- **Devin: The First AI Software Engineer** (Cognition AI, 2024)

  [Blog Post](https://cognition.ai/blog/introducing-devin) / [Website](https://cognition.ai/)

- **SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search** (2024)

  [arXiv: 2410.20285](https://arxiv.org/abs/2410.20285)

- **AutoCodeRover: Autonomous Program Improvement** (Zhang et al., 2024)

  Combines code search with LLM reasoning for automated bug fixing, using program structure understanding to navigate repositories effectively.

  [arXiv: 2404.05427](https://arxiv.org/abs/2404.05427) / [GitHub](https://github.com/nus-apr/auto-code-rover)

---

## Agent Development Frameworks: From Theory to Practice

Understanding the modular architecture of agents is the theoretical foundation, but building a fully functional, reliable agent application from scratch remains a complex engineering challenge. Agent development frameworks dramatically simplify this process through high-level abstractions, rich integrations, and powerful toolsets, allowing developers to focus on business logic rather than low-level implementation.

### Deep Dive into Mainstream Frameworks

1. **LangChain & LangGraph**

   **Core Positioning**: A highly modular, general-purpose LLM application development framework.

   **Highlights**: LangChain's core idea is encapsulating each component of LLM applications (model calls, data connections, memory management) into interoperable "components," then flexibly combining them through "chains" or "graphs." Its greatest advantage is its vast integration ecosystem (supporting hundreds of LLMs, databases, APIs) and high flexibility, making it ideal for rapid prototyping and building diverse agent applications. LangGraph, its evolution, provides more fine-grained, explicit control over agent loops and state management, suitable for more complex, stateful agents.

   Repository: [LangChain GitHub](https://github.com/langchain-ai/langchain) / [LangGraph GitHub](https://github.com/langchain-ai/langgraph)

2. **LlamaIndex**

   **Core Positioning**: A data-centric RAG application development framework.

   **Highlights**: LlamaIndex's unique value proposition is providing an all-in-one solution for building LLM applications on private data. Its core functionality revolves around data ingestion, indexing, and querying. If your application's core need is enabling LLMs to efficiently and accurately query and understand your private knowledge bases (PDFs, databases, APIs), LlamaIndex provides the most optimized toolchain and abstraction layer.

   Repository: [LlamaIndex GitHub](https://github.com/run-llama/llama_index)

3. **AutoGen**

   **Core Positioning**: A framework focused on multi-agent conversation.

   **Highlights**: Microsoft Research's AutoGen is designed to simplify building multi-agent collaboration systems. It provides powerful abstractions for defining agents with different roles, capabilities, and conversation patterns, and coordinates their interactions to complete complex tasks. If you need to build a "virtual team" of expert agents ("programmer," "tester," "project manager"), AutoGen is a historical example of multi-agent orchestration. As of 2026-10-05, its [official repository](https://github.com/microsoft/autogen) states that it is in maintenance mode and directs new users to Microsoft Agent Framework; this does not establish the successor's performance.

   Repository: [AutoGen GitHub](https://github.com/microsoft/autogen)

4. **MS-Agent (ModelScope)**

   **Core Positioning**: A lightweight framework enabling agents to autonomously explore complex task scenarios.

   **Highlights**: MS-Agent provides a flexible and extensible architecture for creating agents capable of complex task handling—code generation, data analysis, and general tool calling with MCP (Model Context Protocol) support. Features include:
   - **Multi-Agent for General Purpose**: MCP-based tool calling capability
   - **Deep Research**: Autonomous exploration and complex research task execution
   - **Code Generation**: Code generation task support with artifact production
   - **Lightweight & Extensible**: Easy to extend and customize for various scenarios

   Repository: [MS-Agent GitHub](https://github.com/modelscope/ms-agent)

5. **CrewAI**

   **Core Positioning**: A role-playing multi-agent orchestration framework emphasizing team collaboration.

   **Highlights**: CrewAI organizes agents into "crews" with clearly defined roles, goals, and collaboration patterns. It emphasizes a simple, intuitive API while supporting both hierarchical and sequential task flows. Growing rapidly in the community for its ease of use in building collaborative agent workflows.

   Repository: [CrewAI GitHub](https://github.com/crewAIInc/crewAI)

### Framework Comparisons

| Framework | Core Abstraction | Primary Use Case | Key Advantage |
|:---|:---|:---|:---|
| LangChain | Component chains/graphs | Rapid prototyping of LLM apps | High modularity and vast integration ecosystem |
| LlamaIndex | Data index/query engine | Private data-based agents (RAG) | Data-centric indexing and retrieval optimization |
| AutoGen | Conversable agents | Multi-agent collaboration systems | Flexible multi-agent conversation orchestration |
| MS-Agent | Autonomous exploration, tool calling | Code generation, data analysis, general tool calling | Lightweight, multimodal, efficient, extensible |
| CrewAI | Role-based crews | Team simulation, collaborative workflows | Simple API, intuitive role-based design |

### Practice: Paper-Agent-Skills

To demonstrate how agents learn and execute complex vertical domain tasks, we provide a hands-on project: **[Paper-Agent-Skills](https://github.com/Scodive/Paper-Agent-Skills)**.

This project uses a **skill-based architecture**, encapsulating high-level academic research capabilities (paper writing, rebuttal strategy, slides generation) as reusable agent modules.

**Core Features:**
- **Pattern Extraction**: Extracts argumentation logic and rhetorical patterns from Best Papers at top venues (NeurIPS, ICLR, CVPR)
- **Interpretability**: Unlike black-box generation, agents demonstrate their reasoning through explicit "skill workflows"
- **Safety Alignment**: Built-in citation validation prevents academic hallucination

**Value**: Demonstrates how to transform LLM general reasoning into highly specialized research productivity tools.

---

---

## Self-Evolving Agents: Self-Improvement and Adaptation Mechanisms

Classify self-improvement by **the component changed, the feedback source, and the adaptation stage**. Experience accumulation, inference-time reflection, training-time weight updates, and recursive modification of an agent program involve different mechanisms and evidence. The label does not guarantee autonomy or sustained growth.

### Adaptation mechanisms and the RSI boundary

1. **Skills and memory**: Voyager stores reusable skills; A-MEM organizes experience. Neither guarantees avoiding repeated mistakes or exponential growth.
2. **Prompts and programs**: [GEPA](https://arxiv.org/abs/2507.19457) optimizes prompts; [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954) modifies agent code. Check whether accepted versions participate in further improvement, whether feedback is independent, and whether old tasks regress.
3. **Model training**: DeepSeek-R1 and Agent-R1 provide parameter-learning background. Reflection by a fixed trained model does not demonstrate runtime modification of its own improver; preference optimization such as DPO should not uniformly be described as online self-play.

The [RSI chapter](docs/rsi.md) compares GEPA, Gödel Agent, DGM, and AIDE² and separates AlphaEvolve's target-algorithm improvement. External validation, held-out tasks, and rollback conditions must be reported without assuming universal gains.

### Related Papers & Resources

- **Voyager: An Open-Ended Embodied Agent with Large Language Models** (Wang et al., 2023)

  A groundbreaking self-evolving embodied agent. Operating in Minecraft, Voyager introduces a tri-part architecture comprising an Automatic Curriculum, an Ever-Expanding Skill Library, and Iterative Self-Reflection, achieving lifelong learning without human supervision.

  [arXiv: 2305.16291](https://arxiv.org/abs/2305.16291) / [GitHub](https://github.com/MineDojo/Voyager)

- **A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence** (2025)

  This survey organizes self-evolving agents by evolving component, adaptation stage, and feedback mechanism; consult the paper for individual methods and evidence.

  [arXiv: 2507.21046](https://arxiv.org/abs/2507.21046)

- **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** (DeepSeek, 2025)

  Background on model reasoning training. R1-Zero studies pure RL without SFT; R1 uses cold-start data, SFT, and multi-stage RL. Neither directly establishes runtime RSI of an environment-interacting agent.

  [arXiv: 2501.12948](https://arxiv.org/abs/2501.12948) / [GitHub](https://github.com/deepseek-ai/DeepSeek-R1)

- **Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning** (2025)

  Studies end-to-end reinforcement learning of multi-step agents using environmental feedback; applicability depends on the training environments and rewards.

  [arXiv: 2511.14460](https://arxiv.org/abs/2511.14460) / [GitHub](https://github.com/AgentR1/Agent-R1)

## Multi-Agent Systems (MAS): Emergent Intelligence through Collaboration

Multi-agent systems organize tasks through division of labor, communication, and shared artifacts. Role design is a mechanism choice; gains over a single agent require comparisons under matched tasks, budgets, and tools, including handoff costs and error propagation.

[RAC](https://arxiv.org/abs/2610.00980) complements fixed-role examples with runtime selection. Selection has the highest observed mean in three research-agent hosts, while jointly adding contracts and verification reduces those means. This single-seed, small-sample result does not isolate either component or establish that collaboration is useless. Retain MetaGPT and ChatDev to study fixed workflows; use RAC to examine the cost of added coordination.

### MAS Paradigm & Architectures

- **Collaboration Patterns**: MAS agents can be organized into different topologies based on task needs:
  - **Pipeline**: Linear flow where each agent handles one stage
  - **Flat (Round Table)**: All agents debate and vote as equals
  - **Hierarchical**: A "manager" agent decomposes tasks and assigns subtasks to "worker" agents

- **Communication Mechanisms**: Communication is the lifeblood of MAS and the key to achieving collective intelligence. Agent interactions typically occur through structured natural language. Effective communication design—protocols, content formats, and interaction strategies—is critical for ensuring collaboration efficiency and avoiding confusion.

### Typical Applications

- **Collaborative Software Development (ChatDev)**: Builds a virtual software company with CEO, product manager, programmer, test engineer, and document engineer agents. When given a high-level requirement (e.g., "develop a Go game"), agents collaborate through a preset "Chat Chain" process following the waterfall model—design, coding, testing, documentation—ultimately delivering a complete software package. Demonstrates how to automate complex, creative workflows through structured multi-agent dialogue.

### Key Challenges

- **Task Allocation Optimization**: How to dynamically and optimally allocate tasks and subtasks based on each agent's expertise.
- **Context Management**: MAS context is multi-layered—global task context, each agent's own context, and shared local context between agents. Effectively managing these complex, hierarchical contexts is a major challenge.
- **Collective Memory**: Beyond individual agent memory, how to design a shared, consistent, updatable "collective memory" system for the entire agent team to support long-term collaboration and learning.

### Related Papers & Resources

- **Survey: A Communication-Centric Perspective on Large Language Model based Multi-Agent Systems** (2025)

  Analyzes MAS from the core perspective of "communication," providing a novel framework for understanding the internal mechanisms of multi-agent collaboration.

  [arXiv: 2502.14321](https://arxiv.org/abs/2502.14321)

- **MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework** (Hong et al., 2023)

  Uses Standard Operating Procedures (SOPs) to meta-program LLMs, integrating human workflows into multi-agent collaboration. Organizes requirements, design, and code through roles and structured artifacts; correctness still requires task verification and cannot be inferred from role count or document completeness.

  [arXiv: 2308.00352](https://arxiv.org/abs/2308.00352) / [GitHub](https://github.com/geekan/MetaGPT)

- **Generative Agents: Interactive Simulacra of Human Behavior** (Park et al., 2023)

  The famous "Stanford Town" research. Endows 25 virtual characters in a sandbox environment with individual memory streams; characters can observe, recall, reflect, and communicate naturally with others, demonstrating remarkable emergent social interaction capabilities and providing a pioneering paradigm for realistic social multi-agent systems.

  [arXiv: 2304.03442](https://arxiv.org/abs/2304.03442) / [GitHub](https://github.com/joonspk-research/generative_agents)

- **ChatDev: Communicative Agents for Software Development** (Qian et al., 2023)

  [arXiv: 2307.07924](https://arxiv.org/abs/2307.07924) / [GitHub](https://github.com/OpenBMB/ChatDev)

- **Development Framework**: AutoGen illustrates multi-agent conversation; see the framework section and [official repository](https://github.com/microsoft/autogen) for its maintenance status and successor.

---

## Trustworthiness: Safety, Alignment, and Evaluation

As agents become increasingly autonomous and are empowered to take actions in the real world, ensuring the trustworthiness of their behavior has become the most critical and urgent issue in the field. A powerful agent with unpredictable behavior, misalignment with human values, or security vulnerabilities poses risks far exceeding its benefits. Safety, Alignment with human values, and rigorous Evaluation form the three pillars of trustworthiness research.

### Alignment Methodologies

- **Constitutional AI (CAI)**: An innovative alignment technique from Anthropic. Rather than relying heavily on human annotators (like RLHF), CAI lets the AI "self-align" to a degree. First, a set of principles and values—a "Constitution"—is established. During training, the model not only generates responses but also self-critiques and revises them according to the Constitution through "Reinforcement Learning from AI Feedback" (RLAIF). This aims to make the alignment process more scalable, transparent, and consistent, reducing reliance on large-scale human annotation.

- **Defense Mechanisms**: Beyond training-time alignment, deployment-time defense is also needed. Researchers are exploring deploying external "guard" models before and after the agent's "brain" to filter malicious inputs and review unsafe outputs, or using multi-agent systems with debate and review mechanisms to collectively enhance decision robustness and safety.

### From outcomes to evaluation protocols

- **Who acts on the environment?** [τ²-Bench](https://arxiv.org/abs/2506.07982) gives both agents and simulated users tools in shared state. No-User/Oracle Plan comparisons separate reasoning and coordination. [τ^τ-Bench](https://arxiv.org/abs/2609.04611) evaluates constructing and delivering an agent; these are distinct benchmarks.
- **What counts as finished?** [Incident-Arena](https://arxiv.org/abs/2610.00648) checks recovery and safety under load and restart. Functional verifiers determine primary success; its separate reward-hacking analysis uses an LLM judge.
- **What are the denominator and budget?** Report task version, sample size, repetitions, tokens, latency, cost, permissions, and stopping rules. Consistent success in `pass^k` differs from at-least-one success in `pass@k`. Separate agent failures, tool/verifier faults, and missing results; report uncertainty and distinguish simulated from real users.

### Context trust and execution permissions

Training alignment, guards, context trust, and execution permissions constrain different stages. [CPE](https://arxiv.org/abs/2609.01222) studies lower-trust content promoted to higher-priority or more persistent context; the [harness chapter](docs/harness.md) separates this from configuration exposure. Findings on paper-era versions do not establish exploitability of current products; guards and multi-agent review do not replace permission isolation.

### Evaluation & Benchmarks

- **AgentBench**: A comprehensive evaluation benchmark for single-agent capabilities. Contains 8 carefully designed environments covering operating system interaction, database queries, web browsing, and other real-world tasks, comprehensively evaluating LLMs' reasoning and decision-making capabilities as agents.

- **MultiAgentBench**: A benchmark specifically designed for multi-agent systems. Unlike AgentBench, it focuses on evaluating interaction quality in collaborative and competitive scenarios, measuring collaboration efficiency and competition strategy effectiveness through novel milestone-based KPIs.

- **OSWorld**: The first benchmark for evaluating multimodal agents on open-ended tasks in real full-desktop OS environments, supporting cross-platform (Windows/Linux/macOS) evaluation with combined mouse and keyboard operations.

### Related Papers & Resources
- **Why Agents Compromise Safety Under Pressure** (Jiang et al., 2026)

    This work is the first to introduce the concept of "Agentic Pressure," exploring how interactions between agents and their environments affect accuracy under non-adversarial conditions. It provides a novel perspective on AI agent safety.

    [arXiv: 2603.14975](https://arxiv.org/abs/2603.14975)


- **Constitutional AI: Harmlessness from AI Feedback** (Bai et al., 2022)

  [arXiv: 2212.08073](https://arxiv.org/abs/2212.08073)

- **Survey: A Survey on Trustworthiness in LLM-based Agents** (2025)

  Proposes the TrustAgent framework, comprehensively studying all aspects of agent trustworthiness.

  [arXiv: 2503.09648](https://arxiv.org/abs/2503.09648)

- **OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments** (Xie et al., 2024)

  [arXiv: 2404.07972](https://arxiv.org/abs/2404.07972) / [GitHub](https://github.com/xlang-ai/OSWorld)

- **AgentBench: Evaluating LLMs as Agents** (Liu et al., 2023)

  [arXiv: 2308.03688](https://arxiv.org/abs/2308.03688) / [GitHub](https://github.com/THUDM/AgentBench)

- **MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents** (Zhu et al., 2025)

  [arXiv: 2503.01935](https://arxiv.org/abs/2503.01935) / [GitHub](https://github.com/THUDM/MultiAgentBench)

- **AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents** (2024)

  A benchmark directly addressing the pain points of agent safety and vulnerability, establishing the first robustness standard for evaluating defenses against adversarial and harmful sequential interaction tasks.

  [arXiv: 2410.09024](https://arxiv.org/abs/2410.09024)

The field is at a critical turning point: from "what can it do?" to "can we trust it?" How to build verifiable, safe, ethically-aligned agent systems has become the most core open problem in the field.

---

## 2025–2026 Selected Research

This section keeps a set of earlier further-reading items. See the [September 2026 picks](docs/monthly-picks.md) for recent work and its evidence limits; the items below are not a current leaderboard. Verify publication status and experimental claims on the original paper or official proceedings page.

### Computer Vision & Multimodal (CV/Multimodal & GUI)

- **UI-TARS: Pioneering Automated GUI Interaction with Native Agents** (ByteDance, 2025)

  An end-to-end native GUI agent model that perceives raw screenshots and directly outputs precise interaction coordinates and text actions. Achieves state-of-the-art results across major benchmarks including ScreenSpot, OSWorld, and AndroidWorld.

  [arXiv: 2501.12326](https://arxiv.org/abs/2501.12326) / [GitHub](https://github.com/bytedance/UI-TARS)

- **Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making** (NeurIPS 2024)

  Proposes the first LLM benchmark framework for embodied decision-making tasks, filling the gap in agent evaluation for complex 3D environment interaction and leading the next evaluation standard for embodied AI.

  [arXiv: 2410.07166](https://arxiv.org/abs/2410.07166) / [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=Embodied+Agent+Interface+Benchmarking+LLMs+Embodied+Decision+Making)

### NLP, Reasoning & Reinforcement Learning (NLP/Reasoning & RL)

- **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** (DeepSeek, 2025)

  Distinguish R1-Zero's pure RL from R1's multi-stage training. Longer inference traces, training-time weight updates, and agent-program self-modification are separate processes.

  [arXiv: 2501.12948](https://arxiv.org/abs/2501.12948) / [GitHub](https://github.com/deepseek-ai/DeepSeek-R1)

- **Large Language Model Agent: A Survey on Methodology, Applications and Challenges** (ACL 2025)

  Comprehensively surveys the development trajectory of LLM agents from foundational architecture to multi-agent system frontiers. A must-read overview of the field's latest state.

  [arXiv: 2503.21460](https://arxiv.org/abs/2503.21460) / [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=Large+Language+Model+Agent+Survey+Methodology+Applications+Challenges+2025)

- **Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents** (2024)

  Combines guided MCTS, self-critique, and off-policy DPO fine-tuning on interaction trajectories. Search and training are distinct stages; this is a historical method entry, with experimental numbers awaiting full-text verification.

  [arXiv: 2408.07199](https://arxiv.org/abs/2408.07199)

### Software Engineering & Systems (SE/Systems)

- **SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement** (ICLR 2025)

  Creatively integrates MCTS with LLM software development agents, achieving remarkable optimization in codebase navigation and issue resolution tasks.

  [arXiv: 2410.20285](https://arxiv.org/abs/2410.20285) / [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=SWE-Search+Software+Agents+Monte+Carlo+Tree+Search)

### Trustworthiness, Safety & Stress Analysis (Trustworthiness & Safety)

- **Why Agents Compromise Safety Under Pressure** (Jiang et al., 2026)

  Pioneers the concept of "Agent Pressure", investigating how environmental friction and task deadlines cause autonomous agents to compromise safety alignment under non-adversarial real-world conditions.

  [arXiv: 2603.14975](https://arxiv.org/abs/2603.14975)

- **AgentHarm: Benchmarking Robustness of LLM Agents on Harmful Tasks** (ICLR 2025)

  First robustness standard for evaluating defenses against adversarial and harmful sequential interaction tasks, directly addressing agent safety vulnerability pain points.

  [arXiv: 2410.09024](https://arxiv.org/abs/2410.09024) / [![Semantic Scholar](https://img.shields.io/badge/Semantic%20Scholar-View-blue)](https://api.semanticscholar.org/graph/v1/paper/search?query=AgentHarm+Benchmarking+Robustness+LLM+Agents+Harmful)

---

## How to Contribute

We warmly welcome community contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

**Quick start:**
- 📄 **Add a paper**: Open a PR with a new paper entry following our [paper template](CONTRIBUTING.md#submit-a-catalog-change)
- 🐛 **Report an issue**: Open a GitHub Issue for broken links, outdated info, or corrections
- 💡 **Suggest new sections**: Open a Discussion on GitHub

**Selection criteria:** A paper should directly inform agent mechanisms, systems, use, or evaluation; have a verifiable primary paper page; and support a concise account of its question, evidence, and limits. New preprints are eligible when their source status is labeled. Citation counts, GitHub stars, and venue names are not standalone thresholds. See the [selection criteria and weekly SOP](docs/update-sop.md).

---

## Citation

If you find this guide useful in your research, please consider citing the original papers referenced herein. This repository serves as a navigation and index, not a source of original research.

```bibtex
@misc{ai_agent_guide,
  title        = {{AI-Agent-Guide}: A Comprehensive Guide to LLM-based AI Agents},
  author       = {Scodive},
  year         = {2025},
  publisher    = {GitHub},
  journal      = {GitHub repository},
  howpublished = {\url{https://github.com/Scodive/AI-Agent-Guide}}
}
```

---

<p align="center">
  <sub>⭐ If this guide helped you, please consider starring the repository to help others discover it!</sub>
</p>

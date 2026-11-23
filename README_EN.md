# AI-Agent-Guide

[English](README_EN.md) | [中文](README.md)

[![GitHub Stars](https://img.shields.io/github/stars/Scodive/AI-Agent-Guide?style=social)](https://github.com/Scodive/AI-Agent-Guide/stargazers) [![Last Commit](https://img.shields.io/github/last-commit/Scodive/AI-Agent-Guide)](https://github.com/Scodive/AI-Agent-Guide/commits/main) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Scodive/AI-Agent-Guide/blob/main/CONTRIBUTING.md) [![License: MIT](https://img.shields.io/github/license/Scodive/AI-Agent-Guide)](https://github.com/Scodive/AI-Agent-Guide/blob/main/LICENSE) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Welcome to **AI-Agent-Guide**. This repository provides a structured, clear, and continuously updated research & engineering guide to AI Agents—helping you build a solid mental model and navigate foundational papers, core mechanisms, and open-source systems.

<p align="center">Read the guide · Explore structured courses · Run hands-on labs</p>

<p align="center">
  <a href="https://ai-notes-red-two.vercel.app/">
    <img src="assets/open-guide-en.svg" alt="Open website · Start learning" width="380" height="76">
  </a>
</p>

> **GitHub for the research map → Website for structured courses & labs:**
> Visit **[AI Notes (ai-notes)](https://ai-notes-red-two.vercel.app/)** for interactive learning paths across **AI Agents, RL & Post-Training, AI Infra Source Reading, and Engineering Interviews** (70 lessons + runnable code labs, currently in Chinese).

Quick links (Chinese docs): [Reading path](docs/reading-path.md) · [96-Paper catalog](docs/papers.md) · [Monthly picks](docs/monthly-picks.md) · [Harness & coding agents](docs/harness.md) · [RSI & self-improvement](docs/rsi.md) · [CSV data](data/papers.csv).

> Weekly review · 2026-11-23: added [intent contracts](docs/papers.md#paper-2611.24025), [prompt-update acceptance](docs/papers.md#paper-2611.23651), [memory deployment lessons](docs/papers.md#paper-2611.26361), and the older [Agent Meltdowns](docs/papers.md#paper-2605.19149), revised this week. H2E now follows v3. See the [review and evidence limits](data/weekly-reviews/2026-11-23.md).

## How to use this guide

Follow the Table of Contents below to build a conceptual foundation from scratch, or jump directly to active research questions in the table below (full 96-paper table and experiment metadata are in the [paper catalog](docs/papers.md)):

| Research Question | Start With | Where It Fits |
| --- | --- | --- |
| How can we verify that a proposed action is authorized? | [Intent Contracts](docs/papers.md#paper-2611.24025) · [Agent Meltdowns](docs/papers.md#paper-2605.19149) | [Harnesses and runtime](docs/harness.md#意图声明授权与环境证据) |
| How can we check whether an agent actually writes and reads its memory? | [How Much Should an Agent Remember?](docs/papers.md#paper-2611.26361) | Memory and retrieval |
| What checks should a reusable prompt update pass before adoption? | [Safe Personal RSI](docs/papers.md#paper-2611.23651) | [Self-improvement](docs/rsi.md#提示更新的接受门与静态规则对照) |
| Which experiences are worth carrying forward to an unknown next coding task? | [CoReMem](https://arxiv.org/abs/2611.17316) | Memory / Agentic Coding |
| How can we distill planning experience from a complex agent into a lightweight executor? | [H2E](https://arxiv.org/abs/2611.16246) | Perception & Embodied Training |
| Do harness improvements that win on dev screens hold up on unseen tasks? | [drydock-eval](https://arxiv.org/abs/2611.16485) | Harnesses & Evaluation |
| How are real-world coding agents built, configured, and supervised? | [τ^τ-Bench](https://arxiv.org/abs/2609.04611), [Scanning the Harness](https://arxiv.org/abs/2609.07360), [The Work Behind Delegation](https://arxiv.org/abs/2609.24234) | Agentic Coding / Security & Oversight |
| When goals change mid-run or UIs shift, how do we verify real completion? | [DynaRev](https://arxiv.org/abs/2610.40133), [VeriCUA](https://arxiv.org/abs/2610.40578), [Prefix Executability](https://arxiv.org/abs/2610.40444) | Planning, GUI & Process Verification |
| What reward-hacking shortcuts do RL tool-use policies learn? | [Spurious Tool Use](https://arxiv.org/abs/2609.16268) | Action & Tool Learning |
| How should we benchmark long-term memory and multi-agent coordination? | [DolphinBench](https://arxiv.org/abs/2609.24971), [CoCoBench](https://arxiv.org/abs/2608.28266) | Memory / Multi-Agent Systems |
| How do we measure real-world cost, reliability, and post-merge maintenance? | [DAREBench](https://arxiv.org/abs/2609.06059), [Are We There Yet?](https://arxiv.org/abs/2609.00524), [Who Finishes the Job?](https://arxiv.org/abs/2609.26847) | Evaluation, GUI & Agentic Coding |

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
- [Classical and Background Reading](#classical-and-background-reading)
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

  This foundational survey proposes a holistic framework for LLM-driven autonomous agents, systematically organizing early research across construction, application, and evaluation using a "Profile—Memory—Planning—Action" taxonomy.

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

A modern AI agent can be understood through four core functional views—**Perception, Planning & Reasoning, Memory, and Action**—forming a continuous decision loop with its environment:

- **Perception Module**: The entry point for environmental interaction. Receives and processes raw information—user instructions, API responses, webpage screenshots—transforming it into structured representations the agent can understand.

- **Planning & Reasoning Module**: The cognitive core. Receives processed information and breaks down complex objectives into concrete, executable steps or subtasks.

- **Memory Module**: Enables cross-step and cross-session learning by storing and retrieving short-term memory (current conversation context) and long-term memory (past experiences, user preferences, knowledge bases).

- **Action Module**: Translates internal decisions into real-world effects by invoking external tools (code interpreters, search APIs, databases, browsers).

Information flows in a dynamic cycle: **Perception → Planning (with Memory) → Action → Environment → Perception**, repeating until the task is complete.

In production engineering, an agent's performance depends heavily not just on the LLM itself, but also on its external **Agent Harness**—the runtime scaffolding that organizes context, enforces tool permissions, persists state, and checks completion criteria (see [Code as Agent Harness](https://arxiv.org/abs/2605.18747) and our [Harness guide](docs/harness.md)).

### Architecture Blueprint — Key Papers

- **Cognitive Architectures for Language Agents (CoALA)** (Sumers et al., 2023)

  Draws on cognitive science and symbolic AI to organize language agents around modular memory, internal/external action spaces, and a clear decision cycle—providing a shared vocabulary for comparing agent architectures.

  [arXiv: 2309.02427](https://arxiv.org/abs/2309.02427)

- **OpenAgents: An Open Platform for Language Agents in the Wild** (Xie et al., 2023)

  An open-source platform providing data, plugin, and web agents with an interactive UI—serving as a classic engineering reference for tool hosting and real-world user workflows.

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

  Microsoft's pure-vision UI parser combining interactable-region detection, icon descriptions, and OCR to generate structured element overlays for VLMs—significantly improving element selection accuracy on benchmarks such as ScreenSpot and Mind2Web.

  [arXiv: 2408.00203](https://arxiv.org/abs/2408.00203) / [GitHub](https://github.com/microsoft/OmniParser)

- **Mobile-Agent: Autonomous Multi-Modal Mobile Device Agent with Visual Perception** (Wang et al., 2024)

  Introduces a pure-vision-driven mobile device agent that autonomously navigates and operates apps solely by analyzing screenshots, without relying on system-level metadata (XML layout files). Demonstrates the enormous potential of visual perception for cross-platform generality.

  [arXiv: 2401.16158](https://arxiv.org/abs/2401.16158) / [GitHub](https://github.com/X-PLUG/MobileAgent)

- **UI-TARS: Pioneering Automated GUI Interaction with Native Agents** (ByteDance, 2025)

  An end-to-end native visual GUI agent mapping screenshots and interaction history directly to a unified action space via GUI-specific training, reflective traces, and DPO (note: the original repo was archived in Nov 2026).

  [arXiv: 2501.12326](https://arxiv.org/abs/2501.12326) / [GitHub](https://github.com/bytedance/UI-TARS)

- **ScreenSpot: A Grounding Benchmark for GUI Agents** (Cheng et al., 2024)

  Introduces a challenging benchmark for evaluating GUI element grounding, covering mobile, desktop, and web platforms. Reveals that even strong VLMs struggle significantly with fine-grained element localization.

  [arXiv: 2401.10935](https://arxiv.org/abs/2401.10935) / [GitHub](https://github.com/njucckevin/SeeClick)

**Post-action verification and executor distillation:**
In real GUI workflows, locating a button does not prove the task succeeded—the full pipeline is **element grounding → action execution → persisted state change → goal satisfaction**. [VeriCUA](https://arxiv.org/abs/2610.40578) inspects screenshots, action history, and underlying files/databases after execution to catch false-positive UI completions (see our [Harness guide](docs/harness.md#界面结果取证与模型接管)). For embodied navigation, [H2E](https://arxiv.org/abs/2611.16246) relabels LLM planner tool calls and VLA motions into unified task actions, trains a lightweight VLA executor, and removes the heavy planner at deployment.

H2E’s November 16–17 revisions add NavRAG-CE and a second training round using teacher recovery sessions from failed rollouts. The earlier v1-only scope should therefore be updated: recovery is measured, with a specific off-track definition, rather than universally solved. The 100-episode teacher comparison uses a different distillation recipe from the main benchmarks; these simulated navigation results are separate from GUI evidence. [Catalog details](docs/papers.md#paper-2611.16246).

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

- **Searching executable actions ([LATS](https://arxiv.org/abs/2310.04406))**: Combines ReAct and ToT using Monte Carlo Tree Search (MCTS) over live environmental feedback, backpropagating rewards and saving failure reflections. Best suited for reversible sandboxes (coding, web navigation); irreversible actions (payments, production writes) require sandboxing or explicit human confirmation.
- **Fixed pipelines vs. dynamic search**: In code repair, [Agentless](https://arxiv.org/abs/2407.01489) uses a deterministic three-stage pipeline (localize → sample → validate), SWE-agent lets the LLM choose tools dynamically, and SWE-Search adds branching search. Each trades off token cost against exploration freedom.
- **Plan first, fill evidence later ([ReWOO](https://arxiv.org/abs/2305.18323))**: A Planner drafts a dependency graph with placeholder variables, Workers run tool calls in parallel, and a Solver aggregates results—cutting repeated observation context overhead when tool dependencies are predictable.
- **Handling mid-run goal changes ([DynaRev](https://arxiv.org/abs/2610.40133))**: When users add or revise instructions mid-execution, DynaRev tracks active constraints, superseded requirements, and reusable progress before replanning—avoiding wasteful full resets.

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

Memory allows an agent to leverage past interactions and accumulated experience in future decisions. In practice, agent memory spans three substrates: **currently visible context, persistent external storage across sessions, and knowledge encoded in model weights**.

### Memory Architecture

- **Short-Term Memory**: The context visible to the model on its current call, bounded by the context window. Harnesses typically manage it via sliding windows, summarization, or selective reloading.

- **Long-Term Memory**: Facts, user preferences, and task experiences persisted across sessions in files, databases, or vector indexes and retrieved on demand.

### Core Mechanisms for Long-Term Memory

- **Retrieval-Augmented Generation (RAG)**: Retrieves relevant chunks from external knowledge bases or experience stores into the prompt before generating an answer, grounding outputs in verifiable sources and reducing hallucination.

- **Agentic RAG**: Integrates autonomous decision-making into retrieval—allowing agents to reformulate queries, pick data sources dynamically, or execute multi-hop retrieval loops for complex questions.

- **Vector Databases**: Infrastructure for semantic similarity search over embeddings; in production, vector retrieval is often paired with keyword search (BM25) for balanced recall and precision.

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

Turning stored records into real task gains requires five stages: **Storage → Retrieval → Context Injection → Decision Impact → Eviction & Revision**. Recent works tackle each bottleneck:

- **Tiered paging & control ([MemGPT](https://arxiv.org/abs/2310.08560))**: Borrows OS virtual-memory paging to swap data between bounded context windows and external storage via function calls (complementary to A-MEM's graph/Zettelkasten organization).
- **Verbal failure reflection ([Reflexion](https://arxiv.org/abs/2303.11366))**: Converts trial feedback into natural-language lessons stored in bounded memory so a fixed-weight model avoids repeating mistakes across retries.
- **Estimating untested memory utility ([CMP](https://arxiv.org/abs/2610.02070))**: A record never retrieved into context has not been tested yet; random exposure slots separate truly useless memories from unexposed ones.
- **Routing experience by substrate ([Component Routing](https://arxiv.org/abs/2610.01787))**: Splits GUI experience into locators, procedures, state facts, and lessons to test which belong in prompt context vs. fine-tuned weights.
- **Continual learning & fair comparisons ([MCCL](https://arxiv.org/abs/2610.29357) / [Harness the Memory](https://arxiv.org/abs/2608.15008))**: Benchmarks memory configurations under matched retrieval breadth and write/read overhead, distinguishing content updates from policy updates on unseen conversations.
- **Valuing memory for the next unknown task ([CoReMem](https://arxiv.org/abs/2611.17316))**: Runs paired next-task rollouts from the same inherited repo state (with vs. without memory) to keep only file locators and checks that actually help solve subsequent issues.

[How Much Should an Agent Remember?](https://arxiv.org/abs/2611.26361) follows the write path: mine lessons, consolidate them while retaining source/count metadata, then verify that the agent actually reads them. Frequent lessons can still be wrong. Test-set configuration selection and limited repeats constrain its model-dependent memory-dose observations. Separately, Safe Personal RSI’s single-entry deletion probe allowed re-extraction from retained sources; it did not test the distinct subject-level forgetting path. See [memory validation and forgetting](docs/rsi.md#单条删除与持续遗忘分开检验).

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

The **Model Context Protocol (MCP)** is an open standard introduced by Anthropic that acts like a "USB-C port for AI agents"—standardizing how clients and servers exchange tools, resources, and context without custom glue code.

When deploying MCP in production, focus on three engineering practices:
1. **Layered permissions & isolation**: MCP handles the communication protocol; authentication, downstream authorization, and OS/network sandboxing must still be enforced by servers and the host harness under least privilege (see official [MCP security practices](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices)).
2. **Error classification & timeout recovery**: The MCP [tool specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) separates protocol errors from tool execution errors (`isError`). On write timeouts, always query the operation receipt before retrying idempotently (see our [harness recovery flow](docs/harness.md#写入超时后先确认状态2026-10-19)).
3. **Process validity & synthetic environments**:
   - [AgentPerturb](https://arxiv.org/abs/2610.21624) evaluates robustness under missing, noisy, and corrupted tool/context inputs.
   - [Prefix Executability](https://arxiv.org/abs/2610.40444) pinpoints the first invalid tool step under contracts and visible state, separating step validity from final task recovery.
   - [ToolSpace](https://arxiv.org/abs/2611.05036) mines data/state dependencies across tool calls to synthesize replayable training environments.

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

**From patch generation to real-world delivery:**
Generating a passing patch is only part of software engineering. Real-world readiness requires examining **runtime harness design ([Harness guide](docs/harness.md)), post-merge follow-up fixes ([Who Finishes the Job?](https://arxiv.org/abs/2609.26847)), and live-service fault recovery under load and restarts ([Incident-Arena](https://arxiv.org/abs/2610.00648))**.

**Fixed-workflow baseline:** [Agentless](https://arxiv.org/abs/2407.01489) provides a clean non-agent baseline (localize → sample patches/tests → vote) without autonomous tool loops—a useful reference point for measuring whether extra agent autonomy pays for its token cost. ([GitHub](https://github.com/OpenAutoCoder/Agentless))

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

   **Highlights**: Microsoft Research's AutoGen provides abstractions for defining role-based conversable agents and coordinating multi-agent workflows (note: as of Oct 2026 its [official repository](https://github.com/microsoft/autogen) is in maintenance mode, pointing new projects to Microsoft Agent Framework).

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

## Self-Evolving Agents: Self-Improvement and Adaptation Mechanisms

"Self-evolving agents" span a spectrum from accumulating experience to rewriting their own source code. It helps to classify them along three axes: **what changes, where feedback comes from, and whether improvements persist across runs**.

### Adaptation mechanisms and the RSI boundary

1. **Skill & Memory Accumulation**: Voyager builds a reusable skill library, A-MEM links dynamic memory nodes, and [Reflexion](https://arxiv.org/abs/2303.11366) distills trial failures into verbal lessons. These grow external experience while keeping the core model and improver fixed.
2. **Prompt & Program Self-Modification (RSI)**: [GEPA](https://arxiv.org/abs/2507.19457) evolves prompts and workflows, while [Darwin Gödel Machine](https://arxiv.org/abs/2505.22954) lets an agent edit its own codebase and retain benchmark-verified descendants—true **Recursive Self-Improvement (RSI)**. The key test is whether accepted versions become the improver in the next round and generalize to held-out tasks.
   - [VERSE](https://arxiv.org/abs/2610.02616) separates inner executor-harness edits from outer optimizer-harness edits so accepted optimizer versions drive future rounds.
   - [Meta²](https://arxiv.org/abs/2611.05139) learns reusable `act/hold/avoid` guidance offline, freezes it at deployment, and resets per-task harness patches after each run to prevent cross-task regressions.
3. **Parametric Self-Evolution & Agentic RL**: DeepSeek-R1 and Agent-R1 train reasoning and tool-use policies via verifiable rewards; [MASS](https://arxiv.org/abs/2610.12176) alternates workflow search with shared-weight fine-tuning; [Terminal-RSI](https://arxiv.org/abs/2610.22192) combines verified-trajectory SFT with critic-inheriting policy optimization (see our [RSI guide](docs/rsi.md)).

[Safe Personal RSI](https://arxiv.org/abs/2611.23651) adds an acceptance gate for reusable prompt edits: compare the current and proposed versions, diagnose failures, repair, and keep the parent if no candidate passes. Weights and runtime stay fixed. Its known attack families and a matching broad handwritten rule limit claims of autonomous improvement; see [the RSI discussion](docs/rsi.md#提示更新的接受门与静态规则对照).

### Related Papers & Resources

- **Voyager: An Open-Ended Embodied Agent with Large Language Models** (Wang et al., 2023)

  A groundbreaking self-evolving embodied agent. Operating in Minecraft, Voyager introduces a tri-part architecture comprising an Automatic Curriculum, an Ever-Expanding Skill Library, and Iterative Self-Reflection, achieving lifelong learning without human supervision.

  [arXiv: 2305.16291](https://arxiv.org/abs/2305.16291) / [GitHub](https://github.com/MineDojo/Voyager)

- **A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence** (2025)

  Organizes self-evolving agent research by evolving component (model, memory, tools, architecture), adaptation stage, and feedback loop.

  [arXiv: 2507.21046](https://arxiv.org/abs/2507.21046)

- **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** (DeepSeek, 2025)

  Demonstrates how pure RL (R1-Zero) and cold-start multi-stage RL (R1) incentivize long-horizon reasoning and self-reflection in foundation models.

  [arXiv: 2501.12948](https://arxiv.org/abs/2501.12948) / [GitHub](https://github.com/deepseek-ai/DeepSeek-R1)

- **Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning** (2025)

  Applies end-to-end reinforcement learning with environmental feedback to optimize multi-step tool calling and planning.

  [arXiv: 2511.14460](https://arxiv.org/abs/2511.14460) / [GitHub](https://github.com/AgentR1/Agent-R1)

- **MOAE: Multi-Objective Agent Evolution with Pareto-Preserving Search** (2026)

  Mutates execution policies under a fixed model using multi-objective diagnostics (task success, trajectory quality, and safety), retaining Pareto-nondominated candidates on TravelPlanner and AgentDojo without weight updates.

  [arXiv: 2609.05992](https://arxiv.org/abs/2609.05992)

---

## Multi-Agent Systems (MAS): Emergent Intelligence through Collaboration

Multi-agent systems coordinate tasks through role division, communication, and shared artifacts. When designing MAS, compare against a strong single-agent baseline under matched budgets to ensure collaboration gains outweigh handoff overhead and error cascades.

Recent research highlights three architectural directions:
- **Runtime collaborator selection ([RAC](https://arxiv.org/abs/2610.00980))**: Dynamically picks the next collaborator based on execution state, showing that piling on heavy contracts and verification rules can actually hurt coordination efficiency.
- **Shared-weight training ([MASS](https://arxiv.org/abs/2610.12176))**: Feeds both orchestrator and worker traces into fine-tuning a single shared model across roles.
- **Asynchronous shared buffers ([Muffin](https://arxiv.org/abs/2610.31355))**: Keeps private chain-of-thought local while appending source-tagged intermediate findings to a shared buffer that peers read asynchronously without blocking for a full round.

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

- **Survey: Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems** (2025)

  Analyzes MAS from the core perspective of "communication," providing a novel framework for understanding the internal mechanisms of multi-agent collaboration.

  [arXiv: 2502.14321](https://arxiv.org/abs/2502.14321)

- **MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework** (Hong et al., 2023)

  Uses Standard Operating Procedures (SOPs) to meta-program LLMs, organizing requirements, design, and code generation through structured roles and artifacts.

  [arXiv: 2308.00352](https://arxiv.org/abs/2308.00352) / [GitHub](https://github.com/geekan/MetaGPT)

- **Generative Agents: Interactive Simulacra of Human Behavior** (Park et al., 2023)

  The famous "Stanford Town" research. Endows 25 virtual characters in a sandbox environment with individual memory streams; characters can observe, recall, reflect, and communicate naturally with others, demonstrating remarkable emergent social interaction capabilities and providing a pioneering paradigm for realistic social multi-agent systems.

  [arXiv: 2304.03442](https://arxiv.org/abs/2304.03442) / [GitHub](https://github.com/joonspk-research/generative_agents)

- **ChatDev: Communicative Agents for Software Development** (Qian et al., 2023)

  [arXiv: 2307.07924](https://arxiv.org/abs/2307.07924) / [GitHub](https://github.com/OpenBMB/ChatDev)

- **Development Frameworks**: AutoGen (maintenance mode) and CrewAI provide practical starting points for multi-agent conversation and crew orchestration (see the Frameworks section above).

---

## Trustworthiness: Safety, Alignment, and Evaluation

As agents become increasingly autonomous and are empowered to take actions in the real world, ensuring the trustworthiness of their behavior has become the most critical and urgent issue in the field. A powerful agent with unpredictable behavior, misalignment with human values, or security vulnerabilities poses risks far exceeding its benefits. Safety, Alignment with human values, and rigorous Evaluation form the three pillars of trustworthiness research.

### Alignment Methodologies

- **Constitutional AI (CAI)**: An innovative alignment technique from Anthropic. Rather than relying heavily on human annotators (like RLHF), CAI lets the AI "self-align" to a degree. First, a set of principles and values—a "Constitution"—is established. During training, the model not only generates responses but also self-critiques and revises them according to the Constitution through "Reinforcement Learning from AI Feedback" (RLAIF). This aims to make the alignment process more scalable, transparent, and consistent, reducing reliance on large-scale human annotation.

- **Defense Mechanisms**: Beyond training-time alignment, deployment-time defense is also needed. Researchers are exploring deploying external "guard" models before and after the agent's "brain" to filter malicious inputs and review unsafe outputs, or using multi-agent systems with debate and review mechanisms to collectively enhance decision robustness and safety.

### From outcomes to evaluation protocols

Modern agent evaluation goes beyond single-run accuracy to cover **interaction protocols, step validity, cost, and recovery**:

- **Interactive & end-to-end benchmarks**: [τ²-Bench](https://arxiv.org/abs/2506.07982) tests agents and users acting in shared state; [τ^τ-Bench](https://arxiv.org/abs/2609.04611) evaluates building and delivering an end-to-end service agent; [FDE-Gym](https://arxiv.org/abs/2610.22350) benchmarks requirement clarification under incomplete specs.
- **Process validity & outcome forensics**: [Prefix Executability](https://arxiv.org/abs/2610.40444) pinpoints the first invalid tool call under contracts, [VeriCUA](https://arxiv.org/abs/2610.40578) probes persisted files/databases after UI actions, and [Incident-Arena](https://arxiv.org/abs/2610.00648) tests fault recovery under load and restarts.
- **Reporting discipline & robustness**: Always report token/latency/call budgets alongside `pass@k` (at least one success) vs. `pass^k` (consistent success across k trials). For statistical horizon definitions ([METR audit](https://arxiv.org/abs/2610.12466)), input perturbations ([AgentPerturb](https://arxiv.org/abs/2610.21624)), evidence-seeking under missing facts ([EpiSEM-Bench](https://arxiv.org/abs/2610.31650)), and harness contract/holdout verification ([Doc2Harness](https://arxiv.org/abs/2610.20344) / [drydock-eval](https://arxiv.org/abs/2611.16485)), see our [Harness guide](docs/harness.md).

### Context trust and execution permissions

Trustworthy agents require **context trust boundaries** and **least-privilege execution isolation** in addition to model alignment:
- [CPE](https://arxiv.org/abs/2609.01222) analyzes how untrusted content can be promoted into high-priority or persistent context.
- [HarnessSecurity-Bench](https://arxiv.org/abs/2610.07639) evaluates legitimate-task utility and attack success side by side under matched models and harnesses (see [Harness security evaluation](docs/harness.md#保护是否有效同时测正常任务与攻击效果)).

[Intent Contracts](https://arxiv.org/abs/2611.24025) separates a planner’s declared goal from the executor’s command, but did not reduce unauthorized actions against blind review when the executor lacked environment evidence. [Agent Meltdowns](https://arxiv.org/abs/2605.19149) adds a complementary test: ordinary tool faults can prompt unsafe recovery without an attacker. Audit the actual target, permissions and effects separately from stated intent or task completion; see [the Harness discussion](docs/harness.md#意图声明授权与环境证据).

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

- **Survey: A Survey on Trustworthy LLM Agents: Threats and Countermeasures** (2025)

  Proposes the TrustAgent framework, comprehensively studying all aspects of agent trustworthiness.

  [arXiv: 2503.09648](https://arxiv.org/abs/2503.09648)

- **OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments** (Xie et al., 2024)

  [arXiv: 2404.07972](https://arxiv.org/abs/2404.07972) / [GitHub](https://github.com/xlang-ai/OSWorld)

- **AgentBench: Evaluating LLMs as Agents** (Liu et al., 2023)

  [arXiv: 2308.03688](https://arxiv.org/abs/2308.03688) / [GitHub](https://github.com/THUDM/AgentBench)

- **MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents** (Zhu et al., 2025)

  [arXiv: 2503.01935](https://arxiv.org/abs/2503.01935) / [GitHub](https://github.com/THUDM/MultiAgentBench)

- **AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents** (ICLR 2025)

  Evaluates tool-using agents on harmful multi-step tasks under refusal and adversarial attack conditions.

  [arXiv: 2410.09024](https://arxiv.org/abs/2410.09024)

---

<a name="20252026-selected-research"></a>

## Classical and Background Reading

This section highlights representative classical methods and background papers by topic; see the [paper catalog](docs/papers.md) and [monthly picks](docs/monthly-picks.md) for detailed metrics and recent updates.

### Computer Vision & Multimodal (CV/Multimodal & GUI)

- **UI-TARS: Pioneering Automated GUI Interaction with Native Agents** (ByteDance, 2025)

  An end-to-end native visual GUI agent mapping screenshots and history directly to a unified action space via GUI training, reflective traces, and DPO (original repo archived Nov 2026).

  [arXiv: 2501.12326](https://arxiv.org/abs/2501.12326) / [GitHub](https://github.com/bytedance/UI-TARS)

- **Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making** (NeurIPS 2024)

  Proposes the first LLM benchmark framework for embodied decision-making tasks, filling the gap in agent evaluation for complex 3D environment interaction.

  [arXiv: 2410.07166](https://arxiv.org/abs/2410.07166)

### NLP, Reasoning & Reinforcement Learning (NLP/Reasoning & RL)

- **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** (DeepSeek, 2025)

  Demonstrates how pure RL (R1-Zero) and cold-start multi-stage RL (R1) elicit long-horizon reasoning and self-reflection in foundation models.

  [arXiv: 2501.12948](https://arxiv.org/abs/2501.12948) / [GitHub](https://github.com/deepseek-ai/DeepSeek-R1)

- **Large Language Model Agent: A Survey on Methodology, Applications and Challenges** (2025)

  A broad survey organizing LLM agent methodologies, applications, and open challenges—useful for building an initial mental map.

  [arXiv: 2503.21460](https://arxiv.org/abs/2503.21460)

- **Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents** (2024)

  Combines guided MCTS, self-critique, and off-policy DPO fine-tuning on interaction trajectories to improve autonomous web agents.

  [arXiv: 2408.07199](https://arxiv.org/abs/2408.07199)

### Software Engineering & Systems (SE/Systems)

- **SWE-Search: Enhancing Software Agents with Monte Carlo Tree Search and Iterative Refinement** (ICLR 2025)

  Integrates MCTS with LLM software development agents to improve codebase navigation and issue resolution.

  [arXiv: 2410.20285](https://arxiv.org/abs/2410.20285)

### Trustworthiness, Safety & Stress Analysis (Trustworthiness & Safety)

- **Why Agents Compromise Safety Under Pressure** (Jiang et al., 2026)

  Pioneers the concept of "Agent Pressure", investigating how environmental friction and task deadlines cause autonomous agents to compromise safety alignment under non-adversarial conditions.

  [arXiv: 2603.14975](https://arxiv.org/abs/2603.14975)

- **AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents** (ICLR 2025)

  A benchmark evaluating tool-using agents on harmful multi-step tasks and adversarial robustness.

  [arXiv: 2410.09024](https://arxiv.org/abs/2410.09024)

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

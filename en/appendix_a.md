# Appendix A

Models, frameworks, toolchains, and Prompt templates — one table to settle every choice

The right tool makes the job easy. The world of Agent development is crowded with tools and frameworks vying for attention. This appendix collects the most common ones into a quick-reference table, so you can find the right "hammer" for your problem.

📋 Quick navigation

- A.1 Model selection
- A.2 Development frameworks
- A.3 Key toolchain
- A.4 Prompt templates

## A.1 Model selection at a glance

Picking the right LLM is the first step in Agent development. Think of it like choosing a car engine — more horsepower isn't automatically better; what matters is fit for your use case.

| Type | Representative products | Characteristics | Best for |
|-|-|-|-|
| General-purpose LLM | GPT-4 / Claude / Gemini | Well-rounded, strong reasoning, best overall performance | General Agents, complex tasks, multi-step reasoning |
| Code model | Codex / Claude Code / Cursor | Standout code comprehension and generation; knows coding conventions | Coding Agents, code review, automated testing |
| Open-source model | Llama / Qwen / Mistral | Private deployment, data security, controllable cost | Intranets, sensitive-data scenarios, customization |
| Multimodal model | GPT-4V / Claude 3 Opus / Gemini Pro | Understands images and text; reads pictures, charts, design drafts | Design Agents, visual recognition, UI reconstruction, screenshot analysis |
| Lightweight model | GPT-4o mini / Claude Haiku / Qwen-Turbo | Fast and cheap, suited to simple tasks | Classification, summarization, simple routing, batch processing |

**Selection advice**

Don't blindly chase the "strongest model." The best practice is **layered use**: lightweight models for simple tasks to save money and time, strong models for complex tasks to protect quality, and the strongest model at critical checkpoints to do the review. A good Agent system is usually the result of "multiple models working together."

## A.2 Agent development frameworks

If the model is the engine, the framework is the chassis and assembly line. Pick the right framework and you'll avoid a lot of dead ends.

| Framework | Language | Characteristics | Best for |
|-|-|-|-|
| **LangChain / LangGraph** | Python / JS | Richest ecosystem, largest community, most complete docs | Quick prototypes, learning, general scenarios |
| **AutoGPT** | Python | Highly autonomous, goal-driven, auto-decomposes tasks | Exploration, research, open-ended tasks |
| **CrewAI** | Python | Multi-Agent collaboration, clear role division | Team Agents, complex workflows, multi-role cooperation |
| **OpenAI Agents SDK** | Python | Native to OpenAI, deeply integrates GPT capabilities | OpenAI ecosystem, simple Agents, fast start |
| **Dify** | Visual / low-code | Drag-and-drop, usable by non-technical people | Non-technical users, business staff, quick idea validation |
| **LlamaIndex** | Python | Strong RAG, rich data connectors | Knowledge-base Agents, document Q&A, enterprise search |
| **AutoGen** | Python | From Microsoft, multi-Agent conversation framework | Research-oriented, multi-agent dialogue, complex collaboration |

🔬 Insider advice

For beginners, **LangChain** is the safe start — most tutorials, and easiest to find answers when you hit a wall. If you're building enterprise-grade applications, focus on **LangGraph**; its state-machine model fits building reliable Agent flows. Non-technical readers can begin with **Dify** and build a presentable Agent without writing code.

## A.3 Key toolchain

With a model and a framework, you still need a whole toolchain to support an Agent's development, operation, and monitoring — like a car needs gas stations, repair shops, and navigation systems.

🗄️

Vector database

Pinecone / Chroma / Weaviate / Milvus

Stores and retrieves vector embeddings; the core infrastructure of any RAG system. Use Chroma for lightweight scenarios, Pinecone or Milvus for enterprise scale.

🔌

MCP services

Official MCP Server / community MCP

Model Context Protocol — the standard protocol for Agents to connect to tools. Wire it up once, use it everywhere; it's becoming an industry standard.

💻

Code Agent

Claude Code / Codex / Cursor

AI coding assistants that understand project structure, write code, run tests, and fix bugs. The developer's "co-pilot" and a daily productivity booster.

📊

Observability platform

LangSmith / Langfuse / Helicone

The Agent's "dashcam." Records every call, tracks cost, debugs errors, and evaluates results. Essential in production.

🛡️

Sandbox environment

Docker / E2B / Firecracker

A safe, isolated environment where the Agent executes code — preventing it from running rogue commands, deleting files by mistake, or leaking data. The security floor.

📝

Prompt management

PromptLayer / Humanloop / Galileo

Centralized management of Prompt templates, A/B testing, and Prompt-effect tracking. You'll appreciate it once you have dozens or hundreds of Prompts.

**Note**

More tooling isn't better. Early on, start with **model + framework + one observability tool**. Once the Agent is running, fill in the rest as real pain points appear. Bringing in a complex toolchain too early just raises the learning cost and maintenance burden.

## A.4 Common Prompt templates

The Prompt is the Agent's "operator's manual." A good template lifts the Agent's performance a notch. Here are the five most-used templates from real practice — plug and play.

1. Role-setting template (essential baseline)

You are a [senior frontend engineer] with [8 years] of relevant experience. Your specialty is [React + TypeScript + performance optimization]. Working principles: - Code must be clean, readable, and maintainable - Prioritize performance and user experience - Every decision needs a rationale Answer with a professional, rigorous attitude, and give code examples when needed.

2. Task-decomposition template (complex tasks)

Task goal: [build a user login feature] Handle it in these steps: 1. Understand the requirements first; list the key points 2. Break the task into concrete subtasks (no more than 5) 3. Prioritize them and state each subtask's dependencies 4. Execute the subtasks one by one 5. Do an overall check when done Report progress and results after each subtask. Stop and ask me when something is unclear.

3. Reviewer template (quality assurance)

You are a strict code reviewer. Review the following code across these dimensions: 🔴 Critical issues (must fix): - Logic errors or security holes - Obvious performance problems - Violations of coding conventions 🟡 Suggestions (optional): - Places where readability could improve - More elegant implementations - Boundary conditions not fully considered 🟢 What's done well: - Implementations worth praising Give specific fix suggestions and code examples. Be concrete down to the line, not vague.

4. Structured-output template (format compliance)

Analyze the content below and output the result as JSON. Output format: ```json { "summary": "one-line summary", "key_points": ["point1", "point2", "point3"], "sentiment": "positive/neutral/negative", "action_items": [ { "task": "specific task", "priority": "high/medium/low", "deadline": "suggested completion time" } ] } ``` Requirements: - Output strictly as JSON, no extra text - key_points no more than 5 - action_items no more than 3

5. Risk-assessment template (decision support)

Assess the risk of the following plan/decision: Plan description: [build an enterprise Agent system with LangChain] Analyze from these dimensions: 1. Technical risk: Is the tech choice sound? Any pitfalls? 2. Cost risk: Rough dev and ops cost? Controllable? 3. Time risk: How long until launch? Likely causes of delay? 4. Security risk: Any data-security or permission issues? 5. Alternatives: If this fails, what's the backup? End with an overall verdict: ✅ Recommended / ⚠️ Use with caution / ❌ Not recommended, with reasons.

**Usage tips**

Prompt templates aren't set in stone. The advice is to **keep iterating** — note which Prompts work and which don't, and slowly polish your own "Prompt arsenal." Also, keep your common Prompts in `AGENTS.md` or a dedicated config file for easy reuse.

🏠 Back to contents [Appendix B: Learning roadmap →](appendix_b.md)

The Self-Driving Era: A Brief History of Agent Evolution © 2026

An evolutionary saga of AI Agents, from Prompt to self-evolving organizations

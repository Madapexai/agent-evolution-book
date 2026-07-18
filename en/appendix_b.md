# Appendix B

From zero to building your own Agent — a 12-week study plan

Many people want to learn Agents but don't know where to start. Online material is scattered every which way, and the more you read the more confused you get. This appendix lays out a clear 12-week path that takes you from scratch, step by step, to a real footing.

📋 Quick navigation

- B.1 Absolute beginner
- B.2 Moving up
- B.3 Hands-on practice
- B.4 The expert's path
- B.5 Recommended resources

2 weeks

Absolute beginner

2 weeks

Moving up

4 weeks

Hands-on practice

4 weeks

The expert's path

**Study advice**

The timeline here is a **reference**, not a hard requirement. If you have coding experience, skip stages. If you're a total beginner, slow down. The key is **hands-on practice** — reading without doing is just pretending; write code yourself for every concept you learn.

## B.1 Absolute beginner (Weeks 1-2)

Weeks 1-2 🚗 Meet AI, learn to use it

**Goal:** Understand what an LLM is, use AI tools fluently, and finish your first small project

- Grasp the basics of LLMs: what is an LLM, and why can it "talk"?
- Learn Prompt Engineering basics: role-setting, task description, output format
- Get on an AI coding assistant: Cursor or Claude Code, learn the basic operations
- Understand Token, context window, Temperature, and other fundamentals
- Try different Prompt techniques: Few-shot, CoT (Chain of Thought), role-play
- Finish your first small task: use AI to write a simple web page (a personal intro page)

**Deliverable:** A static web page built with AI help + your Prompt notes

🔑 Key mindset

What matters most at this stage isn't how much tech you learn, but building a **feel for AI**. Chat with AI more, try different phrasings, and sense where its abilities stop. Don't be afraid to ask "silly questions" — the more you talk with AI, the deeper your understanding gets.

## B.2 Moving up (Weeks 3-4)

Weeks 3-4 🧭 Give AI a map and a pair of eyes

**Goal:** Understand the core ideas of RAG and Agents, and write a simple Agent

- Learn RAG basics: what is a vector? What is an Embedding? Why do you need a vector database?
- Build the simplest RAG by hand: use Chroma + OpenAI API for document Q&A
- Understand the basic Agent architecture: the think → act → observe loop
- Learn the ReAct pattern: reasoning and acting in alternation
- Try writing a simple Agent: use LangChain to build a search-capable assistant
- Learn to manage projects with AGENTS.md: write a project description for the AI to read
- Understand Function Calling: how an LLM invokes external tools

**Deliverable:** A RAG app that answers document questions + a simple search Agent

**Caution**

This is the stage where "framework anxiety" hits hardest — learn LangChain today, hear CrewAI is hot tomorrow so chase it, then AutoGen the day after… Remember: frameworks are just tools, **core concepts are the foundation**. Mastering one framework beats dabbling in ten.

## B.3 Hands-on practice (Weeks 5-8)

Weeks 5-8 🛠️ From toy to product

**Goal:** Build a complete, usable Agent project on your own and understand the engineering essentials

- Go deep on Harness Engineering: permission control, validation, failure recovery
- Build your first complete Agent project: from requirements analysis to launch
- Learn observability: monitor Agent behavior with LangSmith or Langfuse
- Learn evaluation methods: how do you tell if an Agent is doing well?
- Try multi-Agent collaboration: use CrewAI or LangGraph for two-Agent cooperation
- Understand sandboxing: why does an Agent need a safe execution environment?
- Learn Prompt iteration: how to improve Agent performance systematically
- Write complete project docs: technical approach, pitfalls, optimization ideas

**Deliverable:** A complete, usable Agent project + project docs + observability dashboard

**Milestone**

Finishing this stage puts you **ahead of 80% of people who claim they "know Agents."** Many stall at "I can run a demo," but turning an Agent into a usable product takes far more than they imagine. If you get here, you can build Agent projects on your own.

## B.4 The expert's path (Weeks 9-12)

Weeks 9-12 🚀 From single unit to ecosystem

**Goal:** Master advanced Agent architectures and form your own methodology

- Study Loop Engineering: design patterns and best practices for Agent loops
- Design an Agent Mesh architecture: how to organize and coordinate a multi-Agent network
- Explore self-evolving system design: how does an Agent learn and improve from experience?
- Understand the MCP protocol deeply: the road to standardizing the tool ecosystem
- Study the Worktree mechanism: multi-workspace isolation and parallel development
- Learn cost optimization: how to cut Token consumption without hurting results
- Follow the frontier: World Model, Agentic AI, and other new directions
- Form your own methodology: summarize your personal Agent design principles

**Deliverable:** A multi-Agent collaboration system + your Agent methodology notes

🔬 Where to go next

Past this point there's no standard answer. Pick a direction by interest: architecture lovers dig into multi-Agent systems, product-minded people focus on Agent UX, algorithm types study Agent evaluation and optimization. **Find your niche and go deep** — that beats dabbling in everything.

## B.5 Recommended resources

Good resources save you detours. Below are vetted, high-quality picks, organized by category.

#### 📚 Books

- *The Self-Driving Era: A Brief History of Agent Evolution*
- The book you're reading! It explains where Agents came from using the self-driving metaphor
- *Deep Learning* (the "flower book")
- For those who want to understand LLM internals; has a real math prerequisite
- *Building Agentic Systems*
- From the LangChain team; a systematic take on building Agent systems, English original
- *Prompt Engineering for Generative AI*
- A classic entry point to Prompt Engineering; explains the basics clearly

#### 📝 Blogs / newsletters

- AI观察室 (WeChat account)
- The author's official account, with ongoing Agent tips and industry insight
- LangChain Blog
- LangChain's official blog; lots of Agent best practices and case studies
- Andrej Karpathy's Blog
- Posts from an AI heavyweight, clear and deep, worth rereading
- 机器之心 / 量子位 (WeChat accounts)
- Top domestic AI media; essential for tracking the industry
- Hugging Face Blog
- The compass of the open-source model ecosystem; latest models and trends

#### 💻 Open-source projects

- LangChain / LangGraph
- The most popular Agent frameworks; rich ecosystem, best for starting out
- CrewAI
- Multi-Agent collaboration framework; clear role division, easy to pick up
- AutoGPT
- The original autonomous-Agent project; may not suit production, but high learning value
- Dify
- A domestic low-code Agent platform; visual operation, usable by non-technical people
- MCP (Model Context Protocol)
- A tool-connection protocol from Anthropic, becoming an industry standard
- LlamaIndex
- A specialist RAG framework with very strong data-connector power

#### 🎓 Courses

- Andrew Ng's *Agentic AI* series
- From DeepLearning.AI; from Prompt to Agent systems; English with Chinese subtitles
- OpenAI Developer Tutorials
- OpenAI's official developer tutorials; official, quality guaranteed
- Harvard CS50 AI
- Harvard's AI intro course; beginner-friendly, systematic
- fast.ai courses
- Project-driven deep-learning courses; learn theory backward from projects

**How to use resources**

It's not about quantity but quality. Better to **finish one good blog** than collect a hundred accounts. Better to **complete one tutorial end to end** than watch ten. The worst habit is "saved means learned" — a bookmarks folder gathering dust beats writing one line of code right now.

[← Appendix A: Tools & frameworks quick reference](appendix_a.md) 🏠 Back to contents [Appendix C: Glossary →](appendix_c.md)

The Self-Driving Era: A Brief History of Agent Evolution © 2026

An evolutionary saga of AI Agents, from Prompt to self-evolving organizations

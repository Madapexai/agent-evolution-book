# Appendix C

Plain-language explanations of every technical term — look here when something's unclear

All key terms from the book, in alphabetical order. Each term comes with a plain-language explanation and a self-driving-car analogy, so even a beginner can follow. When you hit a word you don't know, flip to this section.

🔤 Alphabetical index

- A
- B
- C
- E
- F
- H
- I
- L
- M
- O
- P
- R
- S
- T
- V
- W

**33** key terms in total

A

- Agent
- An AI system that understands tasks on its own, makes plans, uses tools, and completes goals. The difference from a traditional Chatbot: a Chatbot just "answers questions," while an Agent "gets things done" — it actually rolls up its sleeves and acts. Like a self-driving car: tell it the destination and it plans the route, steers, avoids obstacles, and gets you there.
- Agent Mesh
- A decentralized collaboration network made of multiple Agents. Each Agent has its own specialty and role; they communicate, divide work, and cooperate to finish complex tasks. It's a flat, peer-to-peer web, not a top-down hierarchy. Like a convoy with vehicles that lead the way, haul cargo, and do repairs — they talk over the radio and team up automatically to move freight.
- Agent OS
- The base software platform that runs and manages Agents. Just as Windows is the OS for a computer, Agent OS handles an Agent's lifecycle, resource allocation, task scheduling, and security isolation. Like a car's whole-vehicle control system — it manages the engine, brakes, navigation, and entertainment, keeping every part working together.

B

- Builder / Reviewer
- A classic two-Agent collaboration pattern: the Builder produces content (code, docs) and the Reviewer checks and gives feedback. They alternate, raising quality through a generate → review → fix loop. Like a construction site — a worker lays bricks (Builder), an inspector checks quality (Reviewer); what fails gets torn down and redone, what passes keeps going up.

C

- Chain of Thought (CoT)
- A Prompt technique that makes an LLM "think step by step." Instead of demanding the answer, you have the model spell out its reasoning — what to think first, then next, then the conclusion. Accuracy goes up sharply. Like driving: you can't just stare at the destination, you go step by step — check the light, check cross traffic, press the gas, then change lanes… stepwise thinking avoids mistakes.
- Context
- All the information an LLM can "see" when making a decision — the current conversation, history, system prompt, retrieved documents, and so on. The quality and amount of context directly shape the AI's performance. Like the view through a car's windshield — how much road, how many cars, how many signs you can see sets how safely and accurately you drive.
- Context Engineering
- The engineering discipline of feeding the AI the most fitting context — how to organize information, filter what's relevant, and rank by priority, all to get the best result from a limited context window. Like designing the driver's dashboard and windshield — more information isn't better; what matters is seeing what you should, with nothing irrelevant getting in the way.
- Context Window
- The maximum number of Tokens an LLM can process at once. Like an "info backpack" with a finite capacity. A bigger window lets the AI "see" more, but costs more. Like the size of a car's windshield — bigger glass means a wider view, but a pricier car and more drag.

E

- Embedding
- The process of turning text, images, and such into a string of numbers (a vector). That string captures the content's "semantic features" — similar meanings sit close together in math space. It's the foundation of RAG. Like turning an address into latitude-longitude coordinates — how close two places are in meaning shows up as coordinate distance. A vector is semantics' "lat-long."

F

- Function Calling
- An LLM capability: rather than only outputting text, it can "decide" to call an external function/tool and produce the call arguments. This is what lets an Agent "act" — it turns AI from "talk only" into "talk and do." Like a driver who doesn't just say "I'm turning" but actually works the wheel and hits the brake — Function Calling is the AI's "hands and feet."

H

- Harness
- The engineering system that controls and constrains Agent behavior — permission control, behavior rules, validation, human-takeover points, failure recovery. The core aim is safe, reliable, controllable work. Like a car's brakes, steering wheel, seatbelt, airbags, and traffic laws — without them, the faster you go the more dangerous it gets.
- Harness Engineering
- The discipline of designing and building Harness systems. The core question: how do you let an Agent act without causing trouble? How do you balance autonomy and control? Like automotive safety engineering — designing brake systems, running crash tests, setting safety standards.
- Human in the Loop
- An Agent working mode where key decisions need human confirmation or intervention. You don't hand everything to the AI; the human guards the critical nodes — the AI executes, the human decides. Like Level 2/3 autonomy — the car can drive itself, but in tricky situations a human takes over and has the final say.

I

- In-Context Learning
- A remarkable LLM ability: without retraining, just give a few examples in the conversation and it learns the new task. All learning happens "in the context window" and is forgotten when the task ends. Like hailing a taxi and telling the driver "take this road today, the other one's under repair" — the driver gets it at once, no need to go back to driving school.

L

- Loop
- The basic mode an Agent runs in on its own: perceive → think → act → observe → think again → act again… looping until the task is done. With a Loop, the Agent "runs itself" instead of needing a push for every move. Like an engine's cycle — intake, compression, power, exhaust, repeating, so the car keeps moving. The Agent's Loop is its "engine."
- Loop Engineering
- The discipline of designing Agent loops. Core questions: what steps belong in the loop, when to keep looping and when to stop, how to avoid infinite loops, how to tune efficiency. Like powertrain engineering — designing the engine, matching the transmission, implementing cruise control, so the car goes fast and saves fuel.
- LLM (Large Language Model)
- A large neural-network model trained on massive text data. It understands and generates human language, and is the core technology of the current AI revolution. GPT, Claude, and Llama are all LLMs. Like a car's engine — the power core everything else is built around.

M

- MCP (Model Context Protocol)
- An open protocol from Anthropic that standardizes how AI models connect to external tools and data sources. With MCP, you wire a tool up once and use it in any MCP-compatible AI client. Like a car's OBD port (on-board diagnostics) — a standard interface where any compatible device plugs in to read vehicle data and control functions.
- Memory
- An Agent's ability to store and recall information. Usually split into short-term memory (the current conversation's context) and long-term memory (historical knowledge stored in an external database). Memory is the basis for an Agent to "learn" and "accumulate experience." Like a driver's memory — short-term is the current road (seconds to minutes), long-term is roads driven and rules learned (months to years).

O

- Observability
- The ability to see in real time what the Agent is doing, why, how much it costs, and what went wrong. Observability is the basis for debugging and operating an Agent system — you can't manage what you can't see. Like a car's dashboard and dashcam — the dashboard shows speed, RPM, fuel; the dashcam records the road taken, replayable after an incident.

P

- Prompt
- The text you give the AI. It can be a question, an instruction, a description, or a whole set of rules. Prompt quality directly drives output quality. Like what you say to a driver — "to the airport" is a simple prompt; "take the elevated road, avoid traffic, I'm in a hurry" is a more detailed one. The clearer you speak, the more accurately the driver drives.
- Prompt Engineering
- The technique and method of writing good Prompts. By designing the input carefully, you get better output from the AI. It's the first-generation paradigm of Agent evolution. Like studying how to talk to a driving instructor — phrasing so the instructor understands exactly what you mean and teaches better.

R

- RAG (Retrieval-Augmented Generation)
- A technique where, before answering, the AI first searches an external knowledge base, drops the results into context, then generates the answer from that information. This lets the AI cite the latest and private knowledge instead of relying only on what it memorized in training. Like a driver using navigation — not routes from memory but real-time retrieval of the latest map data to plan the way.
- ReAct
- Short for Reasoning + Acting. An Agent working mode: think (reason) first, then act, then observe the result, then think about the next step… reasoning and acting in alternation. It's the base pattern for many Agent frameworks. Like driving: read the road (think), then steer and accelerate (act), then see where the car is (observe), then adjust course (think and act again).

S

- Sandbox
- An isolated, safe execution environment. The Agent runs code and touches files inside it; even if it makes a mess, the real system outside stays untouched. A key piece of Agent security infrastructure. Like a driving school's practice lot — walled and dedicated, where a novice can crash without hurting pedestrians or public property.
- Skill
- A packaged, callable capability module an Agent can use — a "write email" skill, a "make a spreadsheet" skill, a "draw a chart" skill. Skills are reusable; different Agents can share one skill library. Like a car's function modules — A/C, audio, navigation, wipers… each independently packaged, switch on whichever you need.
- Sub-agent
- A small Agent dispatched by the main Agent to run a specific subtask. Like a boss sending an employee to do a job: the main Agent coordinates, the Sub-agent executes something concrete, then reports back. Like a support car in a convoy — the lead car (main Agent) plans overall and sends out a support car (Sub-agent) to scout, deliver, or check road conditions.

T

- Token
- The basic unit an LLM uses to process text. A Token can be a character, half a word, or a whole word. In English roughly 0.75 word per Token; in Chinese roughly 1-2 characters per Token. Token count drives both cost and context-window size. Like a car's "mileage" — the more kilometers you drive, the more fuel you pay for. Tokens are the AI's "mileage"; the more you use, the more you pay.

V

- Verification
- The process of checking whether an Agent's output is correct and meets requirements. It can be automatic (run tests, check format) or human (a person reviews). Verification is a core part of the Harness system. Like a car's annual inspection — checking the brakes, lights, and emissions. Without verification, you don't know if the car is safe to drive.
- Vector Database
- A database built to store and retrieve vectors (Embeddings). Its core power is "semantic search" — feed in a sentence and it finds the closest in meaning. A core component of any RAG system. Like a navigation database — it stores not plain-text addresses but lat-long coordinates, so it can quickly find "the gas station nearest me."

W

- World Model
- The AI's understanding and modeling of how the real world works. A good World Model lets an Agent predict "if I do this, what happens," so it can plan ahead and avoid errors. A key capability of advanced Agents. Like a veteran driver's experience — having driven many roads, they know what each condition brings and can foresee risk. The World Model is the AI's "driving experience."
- Workflow
- A series of steps run in a fixed order. What each step does, its inputs and outputs, and where to go next are all predefined. Reliable and controllable, but not flexible. Like a bus route — fixed stops and path, on time, but only the set line, with no flexible response to surprises.
- Worktree
- A Git feature that lets you open multiple branches in one repo, each with its own working directory. In Agent scenarios, Worktrees often give different Sub-agents isolated workspaces so they don't step on each other. Like each car in a convoy having its own lane and task — they work separately, then regroup at the finish.

**Tip for looking things up**

If you can't find the term you want here, try: **1.** the browser's find function (Ctrl+F / Cmd+F) to search keywords; **2.** going back to the main chapters to understand the term in context; **3.** following the "AI观察室" WeChat account and leaving a question.

## References and Further Reading

The main text weaves in recent frontier research on AI Agents. To go deeper, here are **verified primary sources** (papers / authoritative blogs). Note: web reposts of "surveys" often contain AI-generated content; for specific numbers, trust the original papers.

- **[1]** Hu, Y. et al. (2026). *Memory in the Age of AI Agents: A Survey*. arXiv:2512.13564. Fifty-plus authors; proposes a "form–function–dynamics" three-axis taxonomy of Agent memory. https://arxiv.org/abs/2512.13564
- **[2]** Weng, L. (2026-07-04). *Harness Engineering for Self-Improvement*. Lil'Log. Systematically describes three basic patterns of Harness engineering and their relation to Recursive Self-Improvement (RSI). https://lilianweng.github.io/posts/2026-07-04-harness/
- **[3]** Zhang, M. et al. (2025). *Darwin Gödel Machine: AI that can improve itself by editing its own code*. arXiv:2505.22954. With a fixed base model, lets a coding Agent evolve an editable harness codebase; SWE-bench Verified rises from 20% to 50%.
- **[4]** Novikov, A. et al. (2025). *AlphaEvolve*. arXiv:2506.13131. An evolutionary-search system built on coding Agents.
- **[5]** Zelikman, E. et al. (2023). *Self-Taught Optimizer (STOP)*. arXiv:2310.02304. An early Recursive Self-Improvement experiment; shows base-model capability is the precondition for iterative improvement.
- **[6]** Anthropic. *Agentic Misalignment* / *Sycophancy to Subterfuge* series. Focuses on reward hacking, deceptive compliance, and alignment risk (trust original papers for specific experimental numbers).
- **[7]** Yao, S. et al. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. arXiv:2210.03629. The "think–act" interleaving pattern that underpins virtually every tool-using Agent.
- **[8]** Wei, J. et al. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. arXiv:2201.11903. Systematically shows that "letting the model think step by step" reliably improves reasoning accuracy.
- **[9]** Lütke, T. (2025). *Context Engineering*. Popularized publicly by Shopify CEO Tobi Lütke in 2025, then adopted as a mainstream term — this book follows that usage.
- **[10]** Anthropic (2024-12). *Building Effective Agents*. https://www.anthropic.com/engineering/building-effective-agents . A foundational engineering reference for Agent design patterns and observability.

> Want to keep digging along this line? Start with the memory survey [1] and the Harness essay [2]; for hard proof that "an Agent rewrites itself," read [3] and [4] directly.

[← Appendix B: Learning roadmap](appendix_b.md) 🏠 Back to contents [Full table of contents →](../README.md)

The Self-Driving Era: A Brief History of Agent Evolution © 2026

![Figure: Triple Paradox - Three Reverse Questions](assets/figures/fig_triple_paradox.svg)

![Figure: Triple Paradox](assets/figures/fig_triple_paradox.svg)

An evolutionary saga of AI Agents, from Prompt to self-evolving organizations

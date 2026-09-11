---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 30 items, 22 important content pieces were selected

---

1. [Shopify Migrates Mobile Apps from React Native to Native Swift and Kotlin](#item-1) ⭐️ 9.0/10
2. [OpenAI Launches Managed Agents API for AI Agent Development](#item-2) ⭐️ 9.0/10
3. [Forgejo &lt;=16.0.3 Critical RCE via Template Expansion](#item-3) ⭐️ 9.0/10
4. [Microsoft Designates Rust as Tier-1 Language](#item-4) ⭐️ 9.0/10
5. [OpenAI Releases Lean 4 Formal Proof for Navier-Stokes Breakthrough](#item-5) ⭐️ 9.0/10
6. [Any Nix Package Runs Live in Browser via trynix.dev](#item-6) ⭐️ 9.0/10
7. [AI-Built Zero-Click WeChat Worm WeWorm Enables Cross-Platform RCE](#item-7) ⭐️ 9.0/10
8. [Researchers Question OpenAI&\#x27;s Use of Unpublished Math Ideas](#item-8) ⭐️ 8.0/10
9. [348M Model Trained on 22.7B Tokens Solves 14-Digit Arithmetic by Showing Work](#item-9) ⭐️ 8.0/10
10. [Fly Connectome Fails to Learn Pong, Bugs Found](#item-10) ⭐️ 8.0/10
11. [OpenAI Codex Python SDK v0.154.0 Adds Reasoning and Turn Features](#item-11) ⭐️ 7.0/10
12. [Cognition Launches SWE-2 Coding Model, Competing with Fable 5.1 and GPT-Astra](#item-12) ⭐️ 7.0/10
13. [Planetscale Launches Neki, a Sharded PostgreSQL Solution](#item-13) ⭐️ 7.0/10
14. [Stanford Launches &\#x27;Teach ML&\#x27; to Scale AI Education via Volunteers](#item-14) ⭐️ 7.0/10
15. [Sante&\#x27;s 83.83 on DiagnosisArena-MCQ Measures Constrained Diagnosis Selection](#item-15) ⭐️ 7.0/10
16. [uv 0.12.13 Released with GraalPy 3.13.0 Support and Performance Optimizations](#item-16) ⭐️ 6.0/10
17. [Neovim Releases v0.13.0-dev Nightly Build](#item-17) ⭐️ 6.0/10
18. [hunk v0.22.0 Released with Website VCS Pages and Pager Fixes](#item-18) ⭐️ 6.0/10
19. [OpenAI Releases Rust-Based Codex Alpha Version 0.155.0](#item-19) ⭐️ 6.0/10
20. [NASA Satellite Image Technique Reveals Hidden Ancient Rock Art](#item-20) ⭐️ 6.0/10
21. [Open-Access 21st-Century Music Theory Textbook Sparks Debate](#item-21) ⭐️ 6.0/10
22. [Simon Willison Builds .blend URL Viewer for AI-Generated Pluribus Fabergé Egg](#item-22) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Shopify Migrates Mobile Apps from React Native to Native Swift and Kotlin](https://shopify.engineering/back-to-native) ⭐️ 9.0/10

Shopify announced it is migrating its mobile applications from React Native back to native Swift and Kotlin codebases, citing debugging complexity and maintenance costs as primary drivers. The company detailed the technical challenges of debugging across JavaScript, C++, and native threads in a blog post. This reversal by a high-profile company like Shopify signals a shift in industry sentiment around cross-platform frameworks, particularly regarding long-term maintainability and performance. It may influence other large teams to reconsider their mobile architecture decisions. Shopify highlighted that debugging crashes spanning JS, C++, and native threads is more costly than maintaining two separate native codebases. Community comments noted that LLM-assisted tools like Codex enabled faster migrations, though some engineers disputed the extent of LLM involvement.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**Background**: React Native, developed by Meta, allows building mobile apps using JavaScript and React by bridging to native components. While it offers code reuse across platforms, it introduces complexity in debugging and performance due to the JavaScript-to-native bridge. The new React Native architecture replaces the legacy bridge with JSI and Turbo Modules, but many apps still rely on the older system.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@abbadmalikk/debugging-react-native-apps-in-expo-challenges-and-solutions-8237c367e190">Debugging React Native Apps in Expo: Challenges and Solutions | by Abbad Malik | Medium</a></li>
<li><a href="https://itsectr.com/en/knowledge/cross-platform/bridge/">Bridge — what it is, how it works, and JavaScript interaction with Native</a></li>
<li><a href="https://javascript.plainenglish.io/react-native-lag-explained-the-hidden-cost-of-the-bridge-5acbadc20d96">“ React Native Lag Explained: The Hidden Cost of the Bridge ”</a></li>

</ul>
</details>

**Discussion**: Community responses were mixed, with many engineers validating the move due to shared frustrations with React Native&\#x27;s debugging overhead. Some highlighted successful rapid migrations aided by LLMs, while others cautioned against overstating the role of AI in such transitions.

**Tags**: `#React Native`, `#Mobile Development`, `#Native iOS`, `#Native Android`, `#Software Architecture`

---

<a id="item-2"></a>
## [OpenAI Launches Managed Agents API for AI Agent Development](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 9.0/10

OpenAI has launched the Agents API, a managed service that allows developers to build and deploy AI agents with integrated tool support and state management. The API provides access to the Codex harness through an OpenAI-managed interface, handling sessions, orchestration, context compaction, and recovery while developers supply tools and select execution environments. This launch represents a significant platform-level move by OpenAI to standardize and simplify AI agent development, potentially reshaping how developers approach building autonomous systems. It introduces a managed abstraction layer that could accelerate adoption but also raises concerns about vendor lock-in compared to self-hosted alternatives. The Agents API supports automatic context compaction, multi-agent orchestration, programmatic tool calling, and integration with MCP servers. Developers can opt to self-host their sandbox environments, which eases transitions between providers and reduces lock-in risks.

hackernews · aquir · Sep 10, 19:43 · [Discussion](https://news.ycombinator.com/item?id=49649213)

**Background**: AI agents are autonomous software systems that use large language models \(LLMs\) to perceive environments, make decisions, and take actions through tools like APIs or web interfaces. Building such agents typically requires managing complex state, context windows, and tool integrations, which has led to the rise of frameworks like LangGraph, Crew AI, and AutoGen. OpenAI&\#x27;s new managed API aims to offload much of this complexity, offering a cloud-native solution similar to how serverless functions abstract infrastructure concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/agents-api/overview">Agents API | OpenAI API</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/agents">Agents SDK | OpenAI API</a></li>
<li><a href="https://openai.com/index/new-tools-for-building-agents/">New tools for building agents | OpenAI</a></li>

</ul>
</details>

**Discussion**: Community response on Hacker News reflects a mix of excitement and skepticism. Some users appreciate the convenience and self-hosting options, while others criticize the push for vendor lock-in and demand more transparency around reasoning tokens. There is also interest in how this could serve as a durable moat for OpenAI against open-source agent harnesses.

**Tags**: `#AI Agents`, `#API Design`, `#Platform Strategy`, `#Developer Tools`, `#Vendor Lock-in`

---

<a id="item-3"></a>
## [Forgejo &lt;=16.0.3 Critical RCE via Template Expansion](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md) ⭐️ 9.0/10

A critical remote code execution vulnerability in Forgejo versions up to 16.0.3 was patched in version 16.0.4, which prevents template expansion from interfering with git repository initialization. This vulnerability allows attackers to execute arbitrary code on self-hosted Git platforms by exploiting template repository expansion during repository creation, posing a severe risk to Forgejo users. The flaw occurs when Forgejo clones a template repository, removes the .git folder, expands variables in files under .forgejo/template, and initializes a new git repo, allowing malicious template content to execute code.

hackernews · weierstass · Sep 10, 15:57 · [Discussion](https://news.ycombinator.com/item?id=49645907)

**Background**: Forgejo is a self-hosted Git platform forked from Gitea, designed for collaborative software development. Template repositories allow users to generate new projects from predefined structures, but improper handling of file expansion can lead to security issues. Remote code execution vulnerabilities in such platforms can compromise entire server infrastructures.

<details><summary>References</summary>
<ul>
<li><a href="https://www.thehackerwire.com/vulnerability/CVE-2026-89094/">CVE-2026-89094 - Critical Vulnerability - TheHackerWire</a></li>
<li><a href="https://codeberg.org/forgejo/forgejo/milestone/27340">Forgejo v11.0.7 - forgejo/forgejo - Codeberg.org</a></li>
<li><a href="https://thehackernews.com/2026/07/new-gitea-rce-lets-repository-writers.html">New Gitea RCE Lets Repository Writers Plant a Git Hook to Run Shell Commands</a></li>

</ul>
</details>

**Discussion**: Community members confirmed that Gitea is not affected by this issue, and emphasized the importance of responsible vulnerability disclosure rather than shaming developers who report bugs.

**Tags**: `#security`, `#vulnerability`, `#rce`, `#forgejo`, `#git`

---

<a id="item-4"></a>
## [Microsoft Designates Rust as Tier-1 Language](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 9.0/10

Microsoft has officially elevated Rust to tier-1 language status, signaling strong enterprise commitment to the systems programming language for security-critical applications. This designation reflects Rust&\#x27;s growing maturity and enterprise readiness, positioning it as a serious competitor to C++ and C\# for systems programming and security-sensitive development. Microsoft&\#x27;s move aligns with broader industry trends, including a reported goal to convert 1 billion lines of code to Rust by 2030 using automated tooling, and ongoing DARPA efforts to automate C-to-Rust conversion.

hackernews · mmastrac · Sep 10, 13:39 · [Discussion](https://news.ycombinator.com/item?id=49643546)

**Background**: Rust is a systems programming language known for memory safety without garbage collection, making it ideal for performance-critical and security-sensitive applications. Tier-1 language status at Microsoft indicates first-class support, including integration with development tools like MSVC and prioritization for new projects.

**Discussion**: Community reactions highlight enthusiasm for Rust&\#x27;s enterprise validation, with discussions about its maturity compared to newer languages like Zig and Odin, and strategic benefits for reducing memory-safety vulnerabilities in Microsoft&\#x27;s codebase.

**Tags**: `#Rust`, `#Microsoft`, `#Systems Programming`, `#Language Adoption`, `#Enterprise Software`

---

<a id="item-5"></a>
## [OpenAI Releases Lean 4 Formal Proof for Navier-Stokes Breakthrough](https://www.johndcook.com/blog/2026/09/09/formal-method-revolution/) ⭐️ 9.0/10

OpenAI announced a formal proof in Lean 4 related to the Navier-Stokes equations, claiming a counterexample showing breakdown of smooth solutions in three-dimensional space. The proof was generated using approximately 10,000 AI agents running an internal frontier model, marking a significant milestone in AI-assisted mathematical verification. This development demonstrates that AI systems can now tackle extremely complex mathematical problems previously thought to require human intuition and creativity. It raises fundamental questions about the future of formal methods, automated theorem proving, and the role of AI in advancing mathematical knowledge. The counterexample resembles a spinning top that tightens to a singularity with diverging velocities, building upon methods developed by Diego Córdoba and Luis Martínez-Zoroa in 2023. OpenAI stated it would not claim the $1 million Clay Millennium Prize, and the result has not yet been verified by external mathematicians or the Clay Mathematics Institute.

hackernews · ibobev · Sep 10, 21:22 · [Discussion](https://news.ycombinator.com/item?id=49650326)

**Background**: The Navier-Stokes existence and smoothness problem is one of seven Millennium Prize Problems identified by the Clay Mathematics Institute in 2000, concerning whether solutions to these fluid dynamics equations remain smooth or can develop singularities. Lean is a free and open-source proof assistant based on dependent type theory, widely used for formal mathematical verification. Formal methods involve mathematically rigorous modeling and verification of systems, ensuring correctness beyond empirical testing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness_problem">Navier-Stokes existence and smoothness problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_methods">Formal methods - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members expressed amazement at AI solving such a magnitude problem in real time, while also debating the practicality of coordinating large-scale intellectual labor. Some noted that Lean verification is relatively slow compared to AI generation times, and questioned whether current proof automation is sufficient for broader mathematical adoption.

**Tags**: `#formal-methods`, `#lean-4`, `#automated-theorem-proving`, `#ai-research`, `#mathematical-verification`

---

<a id="item-6"></a>
## [Any Nix Package Runs Live in Browser via trynix.dev](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 9.0/10

Farid Zakaria launched trynix.dev, a service that boots any historical Nix package from the past 13 years inside an interactive x86\_64 Linux VM running entirely in the browser via QEMU compiled to WebAssembly. Users can navigate to URLs like https://trynix.dev/?pkg=python3%403.6.2 to instantly get a shell running Python 3.6.2 from 2017. This breakthrough combines WebAssembly, QEMU virtualization, and the Nix package manager to enable reproducible environments directly in the browser without servers, opening new workflows like reviewing pull requests by booting them. Simon Willison endorsed it as a &\#x27;magnum opus,&\#x27; highlighting its significance for developer tooling. The VM is powered by qemu-wasm, which translates each translation block \(TB\) into a WebAssembly module using browser APIs like WebAssembly.Module and WebAssembly.Instance. A GitHub Action called trynix-preview automatically comments a link on pull requests so reviewers can boot the PR’s build in the browser.

rss · Simon Willison · Sep 10, 23:44

**Background**: Nix is a purely functional package manager that installs each package into a unique directory named by a cryptographic hash of all its dependencies, ensuring reproducibility. QEMU is a generic open-source machine emulator and virtualizer. Compiling QEMU to WebAssembly allows full system emulation to run inside a browser, leveraging the browser&\#x27;s sandboxed execution environment.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/qemu-wasm: QEMU on browser · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nix_%28package_manager%29">Nix ( package manager ) - Wikipedia</a></li>
<li><a href="https://github.com/NixOS/nix">GitHub - NixOS/ nix : Nix , the purely functional package manager</a></li>

</ul>
</details>

**Tags**: `#WebAssembly`, `#Nix`, `#Virtualization`, `#Developer Tools`, `#Reproducible Builds`

---

<a id="item-7"></a>
## [AI-Built Zero-Click WeChat Worm WeWorm Enables Cross-Platform RCE](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research has released WeWorm, a zero-click worm that exploits WeChat voice calls to achieve remote code execution on both iOS and Android without user interaction. The team developed the exploit in about two days using AI assistance, and built the full worm in one additional week. This disclosure demonstrates that AI can dramatically accelerate exploit development, enabling small teams to build sophisticated cross-platform attacks in days rather than months. It highlights serious risks for billions of WeChat users and signals a shift in how quickly offensive capabilities can be developed. The exploit triggers during the ringing phase before the recipient answers or declines, leveraging a memory corruption bug in WeChat&\#x27;s VoIP stack. Even if answered, the victim hears nothing, and the compromise completes silently. Tencent confirmed the vulnerability on September 4, 2026.

rss · Simon Willison · Sep 10, 00:56

**Background**: Zero-click exploits are among the most powerful in cybersecurity because they require no user interaction, making them ideal for targeting high-value individuals. WeChat is one of the world&\#x27;s largest messaging platforms with over a billion users, making any vulnerability in its core features extremely impactful. AI-assisted development refers to using artificial intelligence tools to help write code, identify bugs, and automate parts of the software creation process.

<details><summary>References</summary>
<ul>
<li><a href="https://calif.io/research/weworm">The first zero-click worm to spread through WeChat calls across iOS...</a></li>
<li><a href="https://www.techtimes.com/articles/327153/20260910/wechat-zero-click-worm-built-ai-days-voip-bug-put-billion-accounts-risk.htm">WeChat Zero - Click Worm Built by AI in Days: VoIP Bug Put Billion...</a></li>
<li><a href="https://www.theregister.com/security/2026/09/09/wechat-worm-could-pwn-a-friend-before-they-even-answered-the-call/5295234">WeChat worm could pwn a friend before they even answered the call</a></li>

</ul>
</details>

**Tags**: `#ai-security-research`, `#mobile-security`, `#zero-click-exploit`, `#wechat`, `#ai-assisted-development`

---

<a id="item-8"></a>
## [Researchers Question OpenAI&\#x27;s Use of Unpublished Math Ideas](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

Researchers are raising ethical concerns about OpenAI using their unpublished mathematical ideas shared during collaborative interactions to train models that later publish related work without proper attribution. The controversy centers on whether OpenAI&\#x27;s models are benefiting from private researcher inputs in ways that blur the line between collaboration and exploitation. This issue strikes at the heart of research ethics and trust in AI collaboration, potentially reshaping how researchers engage with AI companies. If left unaddressed, it could undermine academic integrity and discourage open scientific exchange between researchers and AI developers. Commenters note that OpenAI has provided free access to over 100,000 researchers, yet some internal models are reportedly solving open problems at a rapid pace, raising suspicions about data usage. There are also concerns about OpenAI generating 300 billion output tokens from a model still in training shortly after learning a major math proof might be in its training data.

hackernews · pred\_ · Sep 10, 06:49 · [Discussion](https://news.ycombinator.com/item?id=49639408)

**Background**: OpenAI collaborates with researchers by offering access to its AI models, including through programs that provide free usage to a large number of academics. The controversy involves the use of conversational data—potentially including unpublished ideas—from these interactions to further train and improve AI systems, which may then produce outputs resembling the original research contributions.

**Discussion**: Community members express mixed sentiments, with some drawing parallels between OpenAI and a human collaborator who publishes related work without attribution. Others acknowledge that while chat data may enhance model intuition, AI systems can also independently discover novel techniques during training, complicating claims of direct idea theft.

**Tags**: `#AI Ethics`, `#Research Integrity`, `#OpenAI`, `#Machine Learning`, `#Academic Collaboration`

---

<a id="item-9"></a>
## [348M Model Trained on 22.7B Tokens Solves 14-Digit Arithmetic by Showing Work](https://www.reddit.com/r/MachineLearning/comments/1wc7hmu/i_trained_a_348m_model_trained_from_scratch_on/) ⭐️ 8.0/10

A 348M parameter language model trained from scratch on 22.7B tokens achieves 99.4% accuracy on GPT-3 arithmetic benchmarks by explicitly showing calculation steps like column addition and multiplication. The model also learned to extend its vocabulary beyond training data, inventing place names like &\#x27;millions&\#x27; and &\#x27;ten-millions&\#x27; to handle up to 14-digit arithmetic. This demonstrates that small models can outperform much larger ones like GPT-3 175B on arithmetic tasks when trained with explicit reasoning steps, advancing AI interpretability and reasoning research. The findings suggest that structured, step-by-step training may be more effective than scaling alone for certain logical tasks. The model uses greedy decoding and requires worked examples during training to maintain accuracy, as sampling corrupts the column-by-column routine. It fails on word problems \(GSM8K 4%\) due to operation selection errors, not arithmetic mistakes, and lacks division capability entirely.

reddit · r/MachineLearning · /u/nkthebass · Sep 10, 03:28

**Background**: Large language models like GPT-3 are typically evaluated on arithmetic benchmarks to assess their reasoning capabilities, often using few-shot learning where the model infers patterns from limited examples. Column addition with carries is a foundational arithmetic algorithm taught in schools, involving adding digits column by column and propagating carries to higher place values. Training models to show their work mimics human problem-solving strategies and can improve both accuracy and interpretability.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2305.14201">Goat: Fine-tuned LLaMA Outperforms GPT -4 on Arithmetic Tasks</a></li>
<li><a href="https://github.com/openai/gpt-3">GitHub - openai/ gpt - 3 : GPT - 3 : Language Models are Few-Shot Learners</a></li>
<li><a href="https://arxiv.org/abs/2005.14165">[2005.14165] Language Models are Few-Shot Learners - arXiv.org</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#language-models`, `#arithmetic-reasoning`, `#model-training`, `#ai-benchmark`

---

<a id="item-10"></a>
## [Fly Connectome Fails to Learn Pong, Bugs Found](https://www.reddit.com/r/MachineLearning/comments/1wc67ci/i_tried_to_make_a_real_fly_connectome_learn_to/) ⭐️ 8.0/10

An attempt to train a real fruit fly connectome subgraph \(from MaleCNS v1.0\) to play Pong using dopamine-style plasticity failed, revealing multiple bugs including a neuPrint regex issue that zeroed out neuron populations and incorrect neuron selection lacking photoreceptor-to-motion-detector pathways. This failure analysis provides valuable lessons for connectome-based ML research, showing that even with real biological data, subtle data parsing and connectivity errors can prevent learning, and highlighting the need for rigorous auditing of biological neural networks before training. The neuPrint regex bug used substring matching instead of full-match semantics, silently removing two neuron populations. Additionally, half of the motor neurons had zero synapses from sensory pathways due to coincidental array index assignment, and the original neuron selection lacked an intermediate layer between photoreceptors and motion detectors.

reddit · r/MachineLearning · /u/oPeraza2007 · Sep 10, 02:28

**Background**: The MaleCNS v1.0 connectome is a complete electron microscopy reconstruction of the Drosophila melanogaster male central nervous system containing 166k neurons, released by the FlyEM Project at HHMI-Janelia. neuPrint is a graph database tool built on Neo4j used to store and analyze such connectome data. Dopamine-modulated synaptic plasticity is a biologically-inspired learning rule where dopamine signals modulate synaptic strength based on spike timing and reward prediction errors.

<details><summary>References</summary>
<ul>
<li><a href="https://male-cns.janelia.org/">Male CNS Connectome - MaleCNS connectome</a></li>
<li><a href="https://github.com/connectome-neuprint/neuPrint">GitHub - connectome - neuprint / neuPrint : tools for importing...</a></li>
<li><a href="https://www.janelia.org/project-team/flyem/male-cns-connectome">Male CNS Connectome | Janelia Research Campus</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights strong engagement from ML and neuroscience researchers, with substantive comments around reproducibility challenges, tool limitations in connectome-based modeling, and interest in simulating the central complex and steering circuits properly. Users expressed curiosity about others&\#x27; experiences with MaleCNS v1.0 and similar auditing efforts.

**Tags**: `#neuroscience`, `#connectome`, `#reinforcement-learning`, `#biological-neural-networks`, `#debugging`

---

<a id="item-11"></a>
## [OpenAI Codex Python SDK v0.154.0 Adds Reasoning and Turn Features](https://github.com/openai/codex/releases/tag/python-v0.154.0) ⭐️ 7.0/10

OpenAI Codex Python SDK v0.154.0 introduces &\#x27;max&\#x27; and &\#x27;ultra&\#x27; reasoning-effort values, ExternalMessage support for run\(\) and turn\(\) calls, and enhanced turn management options including include\_turns and turn\_service\_tier. The release also includes matching CLI runtime updates and protocol model refreshes. These updates give developers more control over AI reasoning depth and turn-based interactions, improving flexibility for building AI-assisted coding tools. The coordinated CLI and protocol updates indicate ongoing refinement of the Codex platform. ExternalMessage allows external content to start or join turns with tool-level authority but does not grant user authorization. Custom codex\_bin overrides require CLI 0.151.0 or newer to use ExternalMessage and new history/per-turn options.

github · aibrahim-oai · Sep 10, 19:51

**Background**: OpenAI Codex is a lightweight coding agent that runs locally on a computer, offering CLI and SDK interfaces for AI-assisted development. The Python SDK enables developers to integrate Codex capabilities into their applications, while the CLI provides direct command-line access to the agent.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/codex">GitHub - openai / codex : Lightweight coding agent that runs in your...</a></li>
<li><a href="https://developers.openai.com/api/docs">Explore guides, API docs, and examples for the OpenAI API.</a></li>
<li><a href="https://openai.github.io/openai-agents-python/">OpenAI Agents SDK</a></li>

</ul>
</details>

**Tags**: `#openai-codex`, `#python-sdk`, `#ai-development`, `#api-release`, `#reasoning-models`

---

<a id="item-12"></a>
## [Cognition Launches SWE-2 Coding Model, Competing with Fable 5.1 and GPT-Astra](https://cognition.com/blog/swe-2) ⭐️ 7.0/10

Cognition has launched SWE-2, its most advanced coding model to date, which benchmarks competitively against established models like Fable 5.1 and GPT-Astra. The model is available today in Devin Desktop and CLI, with rollout planned for Devin Web and Fusion. SWE-2 represents a significant incremental advancement in specialized coding models, offering up to 70% lower cost while matching frontier coding performance. Its launch intensifies competition in the AI coding agent space and raises questions about the viability of closed-weight models. SWE-2 is post-trained from Kimi K3 and features effort levels, all trained in a single RL run with linear cost penalties. Cognition has not published SWE-2 weights, making it a closed-weight model with no downloadable version.

hackernews · seelos · Sep 10, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49645443)

**Background**: AI coding models are specialized large language models designed to assist with software development tasks, often integrated into coding assistants or autonomous agents. Closed-weight models restrict access to their internal parameters, contrasting with open-weight models that allow public inspection and modification. Benchmark generalization refers to how well a model performs on new, unseen tasks versus familiar ones.

<details><summary>References</summary>
<ul>
<li><a href="https://cognition.com/blog/swe-2">Introducing SWE - 2 : Pushing the Pareto Frontier | Cognition</a></li>
<li><a href="https://alphasignal.ai/news/cognition-s-swe-2-beats-gpt-5-6-sol-at-64-lower-cost">Cognition &#x27;s SWE - 2 Beats GPT-5.6 Sol at 64% Lower Cost | AlphaSignal</a></li>
<li><a href="https://platform.claude.com/docs/en/models/fable-5-1/overview">Claude Fable 5.1 - Claude Platform Docs</a></li>

</ul>
</details>

**Discussion**: Community members express skepticism about benchmark reliability, citing a large performance delta between Terminal Bench 2.1 \(92.8%\) and Terminal Bench 4 \(27.3%\) as evidence of overfitting. Some question the closed-weight approach and compare it unfavorably to open models like DeepSeek, while others note SWE-2 is post-trained from Kimi K3 and should be viewed with measured expectations.

**Tags**: `#AI`, `#Machine Learning`, `#Software Engineering`, `#Model Evaluation`, `#Coding Assistants`

---

<a id="item-13"></a>
## [Planetscale Launches Neki, a Sharded PostgreSQL Solution](https://planetscale.com/blog/introducing-neki) ⭐️ 7.0/10

Planetscale has introduced Neki, a sharded PostgreSQL solution designed to scale real Postgres to hundreds of millions of queries per second and petabytes of data with zero-downtime resharding. The product is now available in platform preview, built by the team behind Vitess. Neki represents a significant technical development in PostgreSQL sharding from a well-known database company, drawing high community engagement and substantive technical questions about consistency models and deployment. However, its closed-source nature and unclear launch messaging have sparked criticism regarding vendor lock-in and transparency. Neki is architected from first principles to bring Vitess-level scale and reliability to PostgreSQL workloads, supporting zero-downtime resharding. Despite its technical capabilities, the launch announcement lacks clarity about the product&\#x27;s purpose, and the CEO&\#x27;s public commentary about competitors has raised credibility concerns.

hackernews · simon\_weber · Sep 10, 15:43 · [Discussion](https://news.ycombinator.com/item?id=49645686)

**Background**: Database sharding is a horizontal partitioning technique used to distribute large datasets across multiple servers to improve scalability and performance in distributed systems. PostgreSQL is a popular open-source relational database, and sharding solutions like Neki aim to extend its capabilities to handle massive scale. Vitess, developed by YouTube, is a database clustering system for horizontal scaling of MySQL, and Neki&\#x27;s team leverages experience from Vitess to build PostgreSQL sharding technology.

<details><summary>References</summary>
<ul>
<li><a href="https://neki.dev/">Neki | Sharded Postgres by PlanetScale</a></li>
<li><a href="https://planetscale.com/neki">Neki — PlanetScale</a></li>
<li><a href="https://planetscale.com/blog/introducing-neki">Introducing Neki — PlanetScale</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion shows high engagement with substantive technical questions about consistency models and deployment, indicating genuine community interest. However, commenters criticized the launch post for not clearly describing what Neki is or its purpose, and some expressed concerns about the CEO&\#x27;s public commentary and the product not being open source.

**Tags**: `#PostgreSQL`, `#Database Sharding`, `#Distributed Systems`, `#Planetscale`, `#Database Architecture`

---

<a id="item-14"></a>
## [Stanford Launches &\#x27;Teach ML&\#x27; to Scale AI Education via Volunteers](https://www.reddit.com/r/MachineLearning/comments/1wbf3ox/teach_ml_community_service_project_from_stanford_n/) ⭐️ 7.0/10

Stanford professor Chris Piech announced &\#x27;Teach ML,&\#x27; a community service project that pairs volunteer teachers with students at a 1:10 ratio, with over 1,000 applicants already expressing interest in teaching. The project uses AI-assisted learning tools and offers free access supported by alumni funding. This initiative could significantly democratize AI education by making high-quality instruction accessible to more students through scalable volunteer models and AI tools. It reflects growing efforts to bridge the AI skills gap using community-driven and technology-enhanced approaches. The course, &\#x27;Probability for AI,&\#x27; begins October 9th with applications due by the end of September. Teachers receive training based on decades of Stanford experience and use AI coding agents to support student learning.

reddit · r/MachineLearning · /u/chrispiech · Sep 9, 07:54

**Background**: AI education has become increasingly vital as demand for machine learning expertise grows across industries. Stanford University has a strong history in AI research and education, including offerings like the Stanford Machine Learning Course and collaborations with DeepLearning.AI. Projects like Teach ML build on this legacy by leveraging both pedagogical innovation and AI tools to expand access.

<details><summary>References</summary>
<ul>
<li><a href="https://online.stanford.edu/courses/soe-ymls-machine-learning-specialization">Machine Learning Specialization I Stanford Online</a></li>
<li><a href="https://pit.stanford.edu/open-source/">Open Source - Public Interest Technology - Stanford University</a></li>
<li><a href="https://www.stanfordacm.org/mlab">MLab - stanfordacm.org</a></li>

</ul>
</details>

**Tags**: `#AI Education`, `#Community Service`, `#Machine Learning`, `#Stanford University`, `#Volunteer Teaching`

---

<a id="item-15"></a>
## [Sante&\#x27;s 83.83 on DiagnosisArena-MCQ Measures Constrained Diagnosis Selection](https://www.reddit.com/r/MachineLearning/comments/1wbkxsa/what_santes_8383_on_diagnosisarenamcq_actually/) ⭐️ 7.0/10

Ant Ling reported an 83.83 score for its Ling-3.0-flash-Sante medical reasoning model on DiagnosisArena-MCQ, a benchmark that provides case information and asks the model to choose from four candidate diagnoses. The analysis clarifies that this score reflects constrained multiple-choice selection rather than unrestricted diagnostic generation or clinical decision-making. This distinction is critical because multiple-choice performance with supplied options does not equate to real-world diagnostic capability, where models must generate differentials and decide on further investigations. Misinterpreting such scores could lead to overestimating model readiness for clinical use. The Sante release also includes MedXpertQA-Text \(53.88\) and HealthBench Professional \(45.73\), which together provide a broader evaluation profile. HealthBench Professional uses physician-written rubrics and is not scored as percentage accuracy, and the Sante chart lacks detail on whether scores are length-adjusted.

reddit · r/MachineLearning · /u/Expert\_Coffee\_203 · Sep 9, 13:01

**Background**: DiagnosisArena is a benchmark evaluating LLMs on 4,175 complex clinical case reports, with an MCQ variant that supplies candidate diagnoses for selection. HealthBench Professional, developed by OpenAI with 262 physicians, assesses open-ended clinical conversations using physician-authored rubrics across care consults, documentation, and research. MedXpertQA-Text is a board-level multiple-choice benchmark with 2,450 questions spanning medical specialties.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2505.14107">DiagnosisArena : Benchmarking Diagnostic Reasoningfor Large...</a></li>
<li><a href="https://openai.com/index/healthbench/">Introducing HealthBench - OpenAI</a></li>
<li><a href="https://www.emergentmind.com/topics/medxpertqa-text">MedXpertQA - Text : Medical QA Benchmark</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#medical-ai`, `#benchmarking`, `#evaluation`, `#ai-safety`

---

<a id="item-16"></a>
## [uv 0.12.13 Released with GraalPy 3.13.0 Support and Performance Optimizations](https://github.com/astral-sh/uv/releases/tag/0.12.13) ⭐️ 6.0/10

The uv package manager released version 0.12.13 on September 10, 2026, adding support for GraalPy 3.13.0 and introducing hash verification for PEP 658 metadata sidecars. The release also includes performance optimizations for wheel downloads and several bug fixes, such as improved Windows entry-point launcher handling. This release enhances uv&\#x27;s compatibility with alternative Python implementations like GraalPy and improves dependency resolution reliability through metadata hash verification. These changes benefit developers relying on uv for fast and secure Python environment management, especially in CI/CD pipelines. uv now verifies hashes when downloading PEP 658 metadata sidecars, ensuring integrity during dependency resolution. Additionally, it avoids full wheel downloads by reusing supported hashes from direct URL fragments when metadata is available separately, improving resolution speed.

github · astral-automations-bot\[bot\] · Sep 10, 19:27

**Background**: uv is a fast Python package and project manager written in Rust, designed as a drop-in replacement for pip and virtualenv. GraalPy is a high-performance Python implementation built on GraalVM, offering improved performance over CPython. PEP 658 defines a mechanism to serve distribution metadata via the simple repository API, allowing tools to fetch metadata without downloading entire wheels.

<details><summary>References</summary>
<ul>
<li><a href="https://www.graalvm.org/python/?ref=matt-rickard.com">GraalPy</a></li>
<li><a href="https://github.com/oracle/graalpython">GitHub - oracle/graalpython: GraalPy – A high-performance...</a></li>
<li><a href="https://peps.python.org/pep-0658/">PEP 658 – Serve Distribution Metadata in the... | peps .python.org</a></li>

</ul>
</details>

**Tags**: `#python`, `#package-manager`, `#uv`, `#graalpy`, `#performance-optimization`

---

<a id="item-17"></a>
## [Neovim Releases v0.13.0-dev Nightly Build](https://github.com/neovim/neovim/releases/tag/nightly) ⭐️ 6.0/10

The Neovim project released a new nightly build tagged as v0.13.0-dev-1583+gd039f19af5, compiled with RelWithDebInfo build type and LuaJIT 2.1.1788460057. The release includes a changelog, news documentation, and multi-platform installation packages for Windows, macOS, and Linux. This nightly release allows developers and early adopters to test upcoming features and fixes before the stable v0.13.0 release, helping identify bugs and gather feedback. It demonstrates the active development pace of Neovim, a popular modern text editor. The build uses RelWithDebInfo configuration, which optimizes performance like Release builds while retaining debugging information. It is powered by LuaJIT 2.1.1788460057, a high-performance Just-In-Time compiler for the Lua scripting language used for plugin development.

github · github-actions\[bot\] · Sep 10, 05:23

**Background**: Neovim is a modern fork of Vim, designed for extensibility and community-driven development, often used by programmers for code editing. Nightly builds are automatically generated from the latest source code commits and provide a snapshot of ongoing development work. RelWithDebInfo is a CMake build type that balances optimization and debuggability, commonly used during development phases. LuaJIT is a Just-In-Time compiler for Lua, known for its speed and used in applications like Neovim for efficient plugin execution.

<details><summary>References</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/48754619/what-are-cmake-build-type-debug-release-relwithdebinfo-and-minsizerel">cmake - What are CMAKE_BUILD_TYPE: Debug, Release ... Code sample</a></li>
<li><a href="https://cmake.org/cmake/help/latest/variable/CMAKE_BUILD_TYPE.html">CMAKE_BUILD_TYPE — CMake 4.4.3 Documentation</a></li>
<li><a href="https://gist.github.com/MangaD/475b8b413aff7682b803fb007083fb5c">Comprehensive Guide to `Release`, `Debug`, `RelWithDebInfo ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/LuaJIT">LuaJIT - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/LuaJIT">LuaJIT</a></li>
<li><a href="https://luajit.org/">The LuaJIT Project</a></li>

</ul>
</details>

**Tags**: `#neovim`, `#editor`, `#development`, `#release`

---

<a id="item-18"></a>
## [hunk v0.22.0 Released with Website VCS Pages and Pager Fixes](https://github.com/modem-dev/hunk/releases/tag/v0.22.0) ⭐️ 6.0/10

The hunk CLI tool released version 0.22.0, adding VCS landing pages and sitemap aliases to its website, introducing new extensions like hunk-gh and hunk-viewed to the marketplace, fixing pager performance issues that caused CPU pegging on large documents, and enabling static-first history browsing with responsive UI improvements. This release improves the usability and performance of hunk, a review-first terminal diff viewer designed for agent-authored changesets, making it more efficient for developers to review code changes and navigate version control history directly from the terminal. Key changes include upgrading the runtime to Bun 1.4.2, refactoring UI components to share renderers and session runtimes, adding support for replies to review comments, grouping history by day, and extracting bundled VCS providers for Git, Jujutsu, and Sapling into separate packages.

github · github-actions\[bot\] · Sep 10, 12:19

**Background**: Hunk is an open-source, review-first terminal diff viewer built for reading agent-authored changesets, leveraging OpenTUI and Pierre diffs. It is primarily written in TypeScript and licensed under the MIT License. The tool supports extensions via a community marketplace, allowing users to install panes, themes, and VCS backends with a single command.

<details><summary>References</summary>
<ul>
<li><a href="https://langlabs.io/modem-dev/hunk">hunk — install, API, examples, gotchas | modem - dev / hunk</a></li>
<li><a href="https://www.hunk.dev/extensions/">hunk extensions — the community directory</a></li>
<li><a href="https://github.com/modem-dev/hunk/">GitHub - modem-dev/hunk: Review-first terminal diff viewer ...</a></li>

</ul>
</details>

**Tags**: `#software-release`, `#cli-tool`, `#web-development`, `#performance-optimization`, `#feature-update`

---

<a id="item-19"></a>
## [OpenAI Releases Rust-Based Codex Alpha Version 0.155.0](https://github.com/openai/codex/releases/tag/rust-v0.155.0-alpha.1) ⭐️ 6.0/10

OpenAI has released an alpha version \(0.155.0-alpha.1\) of its Codex project, which has been rewritten in Rust. The release notes are extremely minimal, containing only the text &\#x27;Release 0.155.0-alpha.1&\#x27; with no further details about changes or features. This alpha release is notable because Codex is a significant AI model for code generation, and rewriting it in Rust could improve performance and memory safety. However, the lack of detailed release notes limits the immediate technical value of this announcement. The version number 0.155.0-alpha.1 suggests this is an early-stage release in the Rust rewrite of Codex. No specific features, bug fixes, or improvements are documented in the release notes.

github · github-actions\[bot\] · Sep 10, 11:53

**Background**: Codex is an AI system developed by OpenAI that powers GitHub Copilot, providing code suggestions based on natural language prompts. Rust is a systems programming language known for its focus on safety, concurrency, and performance. Rewriting AI tools in Rust can offer benefits like reduced memory usage and improved execution speed compared to higher-level languages.

**Tags**: `#openai`, `#codex`, `#rust`, `#alpha-release`, `#ai-coding`

---

<a id="item-20"></a>
## [NASA Satellite Image Technique Reveals Hidden Ancient Rock Art](https://spinoff.nasa.gov/Manipulating_Satellite_Photos_Now_Reveals_Ancient_Images) ⭐️ 6.0/10

NASA has adapted a satellite photo manipulation technique, originally developed for space imaging, to enhance subtle color variations in terrain and reveal hidden ancient rock art. The method, known as decorrelation stretch, amplifies differences between spectral bands to make faint markings visible to the human eye. This technique bridges space technology and archaeology, offering a non-invasive way to discover and study ancient rock art without disturbing the sites. It demonstrates how remote sensing innovations can have unexpected applications in cultural heritage preservation. The decorrelation stretch algorithm works by increasing contrast between spectral bands, particularly emphasizing chromatic differences that are otherwise imperceptible. Users have noted that similar effects can be achieved manually in tools like GIMP or ImageMagick by manipulating LAB color channels.

hackernews · gumby · Sep 10, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49645437)

**Background**: Remote sensing involves collecting information about Earth&\#x27;s surface using satellite or aerial sensors that detect electromagnetic radiation beyond what the human eye can see. Techniques like decorrelation stretch help analysts interpret multispectral data by enhancing subtle variations in reflected light. These methods were originally developed for analyzing geological features and land-use patterns from space. Their adaptation to archaeology shows how signal processing can uncover details invisible to standard photography.

**Discussion**: Commenters expressed enthusiasm for the technique, recalling their own experiences with false-color composites in GIS education. Some shared alternative workflows using GIMP and ImageMagick, while others joked about the effort behind ancient rock art. One user attempted similar methods at Angkor Wat but faced challenges with site guards.

**Tags**: `#remote sensing`, `#image processing`, `#satellite imagery`, `#archaeology`, `#signal processing`

---

<a id="item-21"></a>
## [Open-Access 21st-Century Music Theory Textbook Sparks Debate](https://musictheory.pugetsound.edu/mt21c/MusicTheory.html) ⭐️ 6.0/10

An open-access music theory textbook titled &\#x27;Music Theory for the 21st-Century Classroom&\#x27; has been published online, offering free self-study materials including homeworks and assignments. However, it has drawn criticism for its heavy focus on classical music theory while largely ignoring jazz, non-Western traditions, and contemporary popular music. This textbook represents a growing trend toward open educational resources in music education, making learning materials freely accessible to self-directed learners. However, the debate around its scope highlights ongoing tensions in music curricula about inclusivity and representation of diverse musical traditions. The textbook is hosted at musictheory.pugetsound.edu and includes interactive homework assignments suitable for autodidacts. Critics note that despite its &\#x27;21st-century&\#x27; branding, it lacks coverage of microtonal music, rhythmic theory, timbre, and theoretical frameworks from non-Western cultures.

hackernews · aanet · Sep 10, 17:14 · [Discussion](https://news.ycombinator.com/item?id=49647134)

**Background**: Open-access textbooks in music theory, such as Open Music Theory, have emerged as alternatives to traditional commercial texts, often incorporating interactive elements and multimedia. Traditional music education has historically centered Western classical traditions, leading to increasing calls for more inclusive curricula that reflect global musical diversity.

<details><summary>References</summary>
<ul>
<li><a href="https://openmusictheory.github.io/">Open Music Theory – Open Music Theory</a></li>
<li><a href="https://libguides.colorado.edu/oamusic/books">Books &amp; Textbooks - Open Access Music Resources - Research Guides at University of Colorado Boulder</a></li>
<li><a href="https://www.numberanalytics.com/blog/ultimate-guide-non-western-music-education">Exploring Non-Western Music in Education</a></li>

</ul>
</details>

**Discussion**: Commenters on Hacker News expressed skepticism about the &\#x27;21st-century&\#x27; label, arguing that the textbook overly emphasizes classical theory while neglecting jazz, non-Western traditions, and modern popular music. Some users appreciated the self-study resources but criticized the lack of context and motivation for theoretical concepts.

**Tags**: `#music theory`, `#education`, `#open source`, `#self-learning`, `#classical music`

---

<a id="item-22"></a>
## [Simon Willison Builds .blend URL Viewer for AI-Generated Pluribus Fabergé Egg](https://simonwillison.net/2026/Sep/9/blender-viewer/) ⭐️ 6.0/10

Simon Willison released a new tool called the .blend URL Viewer, which allows users to view Blender 3D model files directly in the browser by passing a GitHub URL. He created the viewer while experimenting with AI-generated Fabergé egg designs themed after the TV show Pluribus using ChatGPT Images 2.5 and GPT-6 Astra. This project demonstrates how AI tools like ChatGPT Images 2.5 and GPT-6 Astra can be integrated with creative software like Blender to enable rapid prototyping of 3D assets. It also highlights the growing trend of vibe coding, where developers use AI to generate functional code and models with minimal manual input. The .blend URL Viewer resolves GitHub URLs through jsDelivr and renders the 3D model using JavaScript, displaying metadata such as vertex count, materials, and mesh details. The tool was tested with a Pluribus-themed Fabergé egg model generated by GPT-6 Astra in 17 minutes and 51 seconds.

rss · Simon Willison · Sep 9, 23:58

**Background**: Blender is a free and open-source 3D creation suite used for modeling, animation, and rendering. The .blend file format is Blender&\#x27;s native format for storing 3D scenes. GPT-6 Astra is a large language model developed by OpenAI, released in September 2026, designed for advanced reasoning and coding tasks. ChatGPT Images 2.5 is an AI image generation model also released by OpenAI around the same time.

<details><summary>References</summary>
<ul>
<li><a href="https://chatgpt.com/images/">ChatGPT Images 2.5 | AI Image Generator</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT - 6 Astra : A new generation of intelligence | OpenAI</a></li>
<li><a href="https://muapi.ai/gpt-image-2.5">GPT Image 2.5 API (ChatGPT Images 2.5) — Upcoming OpenAI ...</a></li>

</ul>
</details>

**Tags**: `#AI Art`, `#Blender`, `#Creative Coding`, `#Personal Project`, `#Image Generation`

---
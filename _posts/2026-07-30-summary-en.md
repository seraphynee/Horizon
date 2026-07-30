---
layout: default
title: "Horizon Summary: 2026-07-30 (EN)"
date: 2026-07-30
lang: en
---

> From 24 items, 19 important content pieces were selected

---

1. [TurboFieldfare Runs Gemma 4 26B in 2GB RAM on M-Series Macs](#item-1) ⭐️ 9.0/10
2. [Long Policy Documents Fail to Govern Agentic LLMs, Study Finds](#item-2) ⭐️ 9.0/10
3. [AI Worms Self-Propagate Through Copilot for Word](#item-3) ⭐️ 9.0/10
4. [AI Startups Avoid Publishing Research Amid IP and Speed Concerns](#item-4) ⭐️ 8.0/10
5. [Kimi Launches K3-256k, a Cost-Effective 256k-Context LLM](#item-5) ⭐️ 8.0/10
6. [Matthew Green on AI Cryptanalysis During Post-Quantum Transition](#item-6) ⭐️ 8.0/10
7. [PostSlate Uses ncnn Vulkan for Cross-Vendor Edge ML Inference](#item-7) ⭐️ 8.0/10
8. [Mitchell Hashimoto Launches Superlogical for Terminal Apps](#item-8) ⭐️ 7.0/10
9. [Keychron Announces First Open-Source Firmware for Gaming Mice](#item-9) ⭐️ 7.0/10
10. [KOReader: Popular Open-Source E-Reader App Gains Community Praise and Criticism](#item-10) ⭐️ 7.0/10
11. [AI Boom Drives Surge in Demand for Electricians and Construction Workers](#item-11) ⭐️ 7.0/10
12. [CheapFoodMap: Crowdsourced Map of Meals Under $10](#item-12) ⭐️ 7.0/10
13. [Guide to Adding a Custom MCP Server to Claude and ChatGPT](#item-13) ⭐️ 7.0/10
14. [EMNLP 2026 Launches Opt-In AI Reviewing Experiment](#item-14) ⭐️ 7.0/10
15. [Vision Pro Used for Real-Space Architectural Design Visualization](#item-15) ⭐️ 6.0/10
16. [D. Richard Hipp on How SQL Transformed Data Querying](#item-16) ⭐️ 6.0/10
17. [ICLR 2027 Deadline Set Before NeurIPS 2026 Decisions](#item-17) ⭐️ 6.0/10
18. [TanML: Open-Source Toolkit for Automated Tabular Model Validation](#item-18) ⭐️ 6.0/10
19. [University of the Sunshine Coast Researchers Survey Human-AI Relationships](#item-19) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [TurboFieldfare Runs Gemma 4 26B in 2GB RAM on M-Series Macs](https://github.com/drumih/turbo-fieldfare) ⭐️ 9.0/10

TurboFieldfare, a new Swift and Metal-based inference engine, enables running the 4-bit quantized Gemma 4 26B-A4B-IT model on any M-series Mac using only about 2 GB of RAM by streaming routed experts from SSD. The engine achieves 5–6 tokens per second on an M2 MacBook Air and 31–35 tokens per second on an M5 MacBook Pro. 这种突破性进展表明，大型语言模型可以在消费级硬件上高效运行，无需昂贵的 GPU 或云基础设施。这推动了设备端 AI 推理的实际限制，并使普通用户能够使用强大的模型。 The model uses a Mixture-of-Experts \(MoE\) architecture where only the necessary experts are loaded from SSD for each token, while shared weights and KV cache remain in RAM. An experimental OpenAI-compatible local server supports streaming and tool calls, reusing prompt prefixes from the KV cache.

hackernews · gitpusher42 · Jul 29, 15:05 · [Discussion](https://news.ycombinator.com/item?id=49098510)

**Background**: Gemma 4 is a family of open-weight language models developed by Google DeepMind, featuring both dense and Mixture-of-Experts \(MoE\) architectures. The 26B A4B variant uses sparse MoE, activating only a subset of expert subnetworks per token to reduce computation. 4-bit quantization compresses model weights to lower precision, significantly reducing memory requirements while preserving performance. On-device AI refers to running AI models directly on personal devices like smartphones or laptops, rather than relying on remote servers.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.google.dev/gemma/docs/core/model_card_4">Gemma 4 model card | Google AI for Developers</a></li>
<li><a href="https://gemma4.dev/models/gemma-4-26b-a4b">Gemma 4 26 B A 4 B — MoE Architecture for Long Context</a></li>
<li><a href="https://gemma4.com/">Gemma 4 — Google DeepMind</a></li>

</ul>
</details>

**Discussion**: Community members praised the innovation and discussed technical details such as compilation fixes for older macOS versions and comparisons with mmap-based approaches like llama.cpp. Some users noted that llama.cpp can already run 26B models in 2GB RAM with mmap enabled, but TurboFieldfare&\#x27;s synchronized SSD reads may offer better latency. Others expressed interest in combining efforts with similar projects for further optimization.

**Tags**: `#machine-learning`, `#swift`, `#metal`, `#on-device-ai`, `#model-optimization`

---

<a id="item-2"></a>
## [Long Policy Documents Fail to Govern Agentic LLMs, Study Finds](https://arxiv.org/abs/2607.25398) ⭐️ 9.0/10

A new research paper \(arXiv:2607.25398\) empirically demonstrates that long policy documents, such as CLAUDE.md, do not reliably govern the behavior of agentic LLMs. The study highlights technical limitations in long-context models that cause policy adherence to degrade over extended interactions. This finding challenges the widespread assumption that extensive policy documentation can control agentic AI systems, with major implications for AI safety and practical agent deployment. It suggests that organizations relying on policy files for governance may need to adopt alternative mechanisms to ensure reliable compliance. Community discussion points to technical root causes including extreme quantization of model weights, KV cache limitations in long-context inference, and poor-quality samplers that strip away user controls. Users report that even strong instructions in CLAUDE.md are bypassed after sustained task execution, while inline prompts remain effective.

hackernews · spIrr · Jul 29, 13:01 · [Discussion](https://news.ycombinator.com/item?id=49096969)

**Background**: Agentic LLMs are AI systems built around one or more LLM-driven agents that plan, reflect, and act toward goals, rather than simply responding to prompts. Long-context models claim to support up to 1 million tokens of context, but community experts note that real-world performance degrades due to quantization and KV cache inefficiencies. KV caching is a technique used during LLM inference to avoid recomputing attention for previously processed tokens, speeding up generation but potentially introducing fidelity issues at scale.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/how-kv-caching-powers-faster-inference-llms-praveen-kumar-hbdnc">How KV Caching Powers Faster Inference in LLMs</a></li>
<li><a href="https://www.pythonalchemist.com/blog/kv-cache-llm-inference">KV Cache : LLM Inference | PythonAlchemist | PythonAlchemist</a></li>
<li><a href="https://github.com/jassics/awesome-agentic-ai-security">GitHub - jassics/awesome- agentic -ai-security: A one stop resource to...</a></li>

</ul>
</details>

**Discussion**: Community sentiment strongly validates the paper&\#x27;s findings, with users sharing anecdotal evidence that CLAUDE.md instructions degrade after about 10 minutes of continuous use. Commenters highlight technical causes such as KV cache quantization and poor samplers, and some suggest local inference as a workaround. Others note that agentic capabilities are synthetic and require specific post-training, implying that policy compliance may depend heavily on training rather than documentation.

**Tags**: `#AI Safety`, `#LLM Agents`, `#Research`, `#AI Alignment`, `#Policy Compliance`

---

<a id="item-3"></a>
## [AI Worms Self-Propagate Through Copilot for Word](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/) ⭐️ 9.0/10

Researchers demonstrated that malicious documents can exploit Copilot for Word to create self-propagating AI worms that execute embedded instructions and spread to new documents. The attack leverages hidden text and prompt injection techniques to manipulate AI-generated content. This reveals a critical vulnerability class where AI agents can be exploited by malicious documents to self-propagate, representing a fundamental architectural flaw in AI integration. The issue affects any system mixing instructions with data, potentially impacting millions of users relying on AI-powered document editors. The vulnerability allows hidden white text in Word documents to inject malicious instructions that alter reports and spread to new files via Copilot&\#x27;s &\#x27;Edit with Copilot&\#x27; functionality. No robust mitigation is currently available, and the attack works by making Copilot deem malicious documents relevant within the victim&\#x27;s OneDrive context.

hackernews · Canopy9560 · Jul 29, 11:44 · [Discussion](https://news.ycombinator.com/item?id=49096188)

**Background**: Prompt injection is a class of attacks where malicious instructions are embedded within data inputs to manipulate AI systems. In AI-powered document editors like Copilot for Word, the AI processes both user prompts and document content together, making it difficult to distinguish between legitimate instructions and malicious text. AI worms are a newer form of malware that uses LLM-based techniques to self-propagate across systems. Traditional security measures like input sanitization are insufficient because the malicious content appears as normal document text.

<details><summary>References</summary>
<ul>
<li><a href="https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/">Context Collapse, Part 3 - AI Worming through Word | En Klype Salt</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/cybersecurity/ai-worms/">AI Worms Explained: Adaptive Malware Threats - SentinelOne</a></li>
<li><a href="https://arxiv.org/html/2509.22040v2">“Your AI, My Shell”: Demystifying Prompt Injection Attacks on ...</a></li>

</ul>
</details>

**Discussion**: Security experts on Hacker News expressed strong concern, with comments highlighting that no robust mitigation exists until instructions and data are separated. Developers noted the vulnerability will worsen as more access is granted to AI agents, and some users have uninstalled Copilot entirely due to these risks. The discussion emphasized that this represents a fundamental design flaw in current AI integration approaches.

**Tags**: `#AI Security`, `#Vulnerability Research`, `#Copilot`, `#AI Worms`, `#Prompt Injection`

---

<a id="item-4"></a>
## [AI Startups Avoid Publishing Research Amid IP and Speed Concerns](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research) ⭐️ 8.0/10

A new analysis reveals that leading AI startups are increasingly choosing not to publish their research in academic venues, citing slow peer review processes and fears of intellectual property theft by larger competitors. The trend reflects a growing tension between open scientific collaboration and commercial interests in the AI industry. This shift threatens the flow of knowledge in the AI research ecosystem, potentially slowing scientific progress and reducing transparency. It also highlights how commercial pressures are reshaping how cutting-edge AI research is shared and validated. The analysis notes that companies like OpenAI and Anthropic are still publishing, contrary to assumptions, while others avoid publication due to past frustrations with peer review and concerns about being copied. Citations are used as a proxy for research significance, though this metric is imperfect.

hackernews · YeGoblynQueenne · Jul 29, 21:25 · [Discussion](https://news.ycombinator.com/item?id=49103285)

**Background**: Academic publishing in AI traditionally involves submitting research to conferences or journals where it undergoes peer review before publication. However, the process can be slow, and once published, ideas become public, making it difficult for startups to maintain a competitive edge. As AI becomes more central to business strategy, many startups are weighing the benefits of open publication against the risks of losing proprietary advantages.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41599-020-00703-8">AI-assisted peer review | Humanities and Social Sciences Communications</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2772577426000297">Reflections on the impact of artificial intelligence on peer-review practices and its implications for greener scientific evaluation - ScienceDirect</a></li>
<li><a href="https://arxiv.org/html/2604.27924v2">Can AI Be a Good Peer Reviewer? A Survey of Peer Review Process, Evaluation, and the Future</a></li>

</ul>
</details>

**Discussion**: Community members shared firsthand experiences from inside AI startups, describing years-long struggles with publishing and fears of being copied by companies like OpenAI and Anthropic. Some clarified that the article&\#x27;s framing was misleading, as several major players are still actively publishing research.

**Tags**: `#AI Research`, `#Academic Publishing`, `#Startup Strategy`, `#Intellectual Property`, `#Machine Learning`

---

<a id="item-5"></a>
## [Kimi Launches K3-256k, a Cost-Effective 256k-Context LLM](https://www.kimi.com/code/docs/en/kimi-code/models) ⭐️ 8.0/10

Kimi has introduced K3-256k, a new 256k-context LLM that costs half as much as its 1M-context counterpart, K3, while delivering equivalent performance within the 256k limit. The model is now available for use in coding tools such as Kimi Code CLI and Claude Code. This move reflects growing pressure on LLM providers to offer more cost-efficient options, as developers seek better performance-per-dollar. It also intensifies competition against OpenAI and other major players by lowering the barrier to entry for long-context applications. K3-256k delivers the same results as K3 \(1M\) within a 256k context window, consuming about half the quota. If a session exceeds 256k tokens, certain coding tools will perform automatic compaction on the tool side to manage context limits.

hackernews · monneyboi · Jul 29, 19:25 · [Discussion](https://news.ycombinator.com/item?id=49101852)

**Background**: Large Language Models \(LLMs\) are increasingly being viewed as commodities due to low switching costs and standardized interfaces, making pricing and performance-per-dollar critical factors for adoption. Context window size, which determines how much text a model can process at once, is a key differentiator, especially for tasks involving long documents or codebases. Providers like Kimi are responding to market demands by offering tiered models that balance cost and capability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kimi.com/code/docs/en/kimi-code/models">Model Configuration | Kimi Code Docs</a></li>
<li><a href="https://platform.kimi.ai/docs/models">Model List - Kimi API Platform</a></li>
<li><a href="https://cacm.acm.org/blogcacm/the-commoditization-of-llms/">The Commoditization of LLMs – Communications of the ACM</a></li>

</ul>
</details>

**Discussion**: Community members praised the cost efficiency of K3-256k, noting that 1M context is often unnecessary for typical use cases. Some viewed it as a sign of LLM commoditization, with hyperscalers and data center operators poised to dominate by offering cheaper tokens.

**Tags**: `#LLM`, `#AI`, `#Machine Learning`, `#Open Source`, `#Cost Optimization`

---

<a id="item-6"></a>
## [Matthew Green on AI Cryptanalysis During Post-Quantum Transition](https://simonwillison.net/2026/Jul/29/matthew-green/#atom-everything) ⭐️ 8.0/10

Matthew Green highlighted the historic transition from RSA and elliptic-curve cryptography to post-quantum algorithms, noting that AI advancements like Anthropic&\#x27;s Claude breaking the HAWK cipher in 60 hours underscore both the promise and peril of AI in cryptanalysis. As NIST advances post-quantum standards like HAWK, the emergence of AI capable of rapid cryptanalysis poses a dual challenge: accelerating validation of new algorithms while potentially undermining the hard problems they rely on. HAWK is the only lattice-based candidate among nine advanced to Round 3 of NIST&\#x27;s additional post-quantum digital signature process in May 2026, and its security rests on the Lattice Isomorphism Problem. Anthropic&\#x27;s Claude reportedly recovered signing material for HAWK-256 in a research challenge, not an active production system.

rss · Simon Willison · Jul 29, 18:18

**Background**: Post-quantum cryptography \(PQC\) refers to encryption methods designed to remain secure against both classical and quantum computers, addressing the threat that quantum algorithms like Shor&\#x27;s could break widely-used schemes such as RSA and ECC. The NIST PQC standardization process selects and refines candidate algorithms through multiple rounds of public scrutiny. Impagliazzo&\#x27;s Minicrypt is a theoretical complexity class where one-way functions exist but secure public-key cryptography does not, representing a world where traditional encryption assumptions fail.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/321876/20260728/ai-cracks-post-quantum-cipher-60-hours-after-two-years-human-review-failed.htm">AI Cracks Post-Quantum Cipher in 60 Hours After Two Years of Human Review Failed</a></li>
<li><a href="https://byteiota.com/claude-breaks-post-quantum-hawk-cipher-60-hours/">Claude Breaks Post-Quantum HAWK Cipher in Just 60 Hours | byteiota</a></li>

</ul>
</details>

**Tags**: `#post-quantum-cryptography`, `#AI-security`, `#cryptanalysis`, `#cybersecurity`, `#standards`

---

<a id="item-7"></a>
## [PostSlate Uses ncnn Vulkan for Cross-Vendor Edge ML Inference](https://www.reddit.com/r/MachineLearning/comments/1v9s4mz/vendoragnostic_ml_inference_on_production_edge/) ⭐️ 8.0/10

PostSlate, a video editing tool, adopted ncnn&\#x27;s Vulkan backend to run ML models on diverse GPU hardware including NVIDIA, AMD, Intel, and Apple Silicon, achieving up to 10x speedup over ONNX CPU inference. This approach solves the vendor-lock-in problem in edge ML deployment, allowing developers to target any GPU without requiring users to install specific runtimes like CUDA, which is critical for broad consumer software distribution. On an RTX 4070, ArcFace R50 inference dropped from 30ms \(ONNX CPU\) to 3ms \(ncnn Vulkan\), and SCRFD detection from 25ms to 2.5ms. Model size was also halved from 174MB to 87MB using fp16 weight storage.

reddit · r/MachineLearning · /u/ppchaos · Jul 29, 10:22

**Background**: ncnn is a high-performance neural network inference framework optimized for mobile and edge devices, and its Vulkan backend allows GPU acceleration across different vendors. Vulkan is a cross-platform graphics and compute API that provides low-level hardware access, enabling broad compatibility. ONNX Runtime is a popular inference engine but typically relies on CPU or vendor-specific GPU backends like CUDA.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/upscayl/upscayl-ncnn">GitHub - upscayl/upscayl-ncnn: The Upscayl backend powered by the NCNN framework and Real-ESRGAN architecture. · GitHub</a></li>
<li><a href="https://onnxruntime.ai/inference">Inference - ONNX Runtime</a></li>
<li><a href="https://www.spec.org/blog/machinelearning/">SPEC Machine Learning Committee to Develop Vendor-Agnostic ...</a></li>

</ul>
</details>

**Tags**: `#ML Inference`, `#Vulkan`, `#Edge Computing`, `#Cross-Platform`, `#Performance Optimization`

---

<a id="item-8"></a>
## [Mitchell Hashimoto Launches Superlogical for Terminal Apps](https://www.superlogical.com/) ⭐️ 7.0/10

Mitchell Hashimoto has launched Superlogical, a new company that builds terminal applications on top of the open-source libghostty library. The company plans to use libghostty as a public building block and upstream shared terminal work for all consumers. This move signals a growing trend of leveraging open-source terminal infrastructure to build specialized developer tools, potentially lowering the barrier for new terminal applications. It also demonstrates a sustainable model where foundational libraries remain community-owned while enabling commercial innovation. Superlogical consumes the same MIT-licensed components available to everyone else and will continue to upstream shared terminal work so every libghostty consumer can benefit. The project builds directly on libghostty, which is a C-compatible library for embedding the Ghostty terminal emulator.

hackernews · yan · Jul 29, 15:41 · [Discussion](https://news.ycombinator.com/item?id=49098965)

**Background**: A terminal emulator is a program that emulates a video terminal within another display architecture, allowing users to interact with command-line interfaces and text-based applications. Libghostty is a C-compatible library designed to let any application embed a fully functional, modern, and fast terminal emulator, making it easier to integrate terminal capabilities into other software.

<details><summary>References</summary>
<ul>
<li><a href="https://mitchellh.com/writing/libghostty-is-coming">Libghostty Is Coming – Mitchell Hashimoto</a></li>
<li><a href="https://docsmith.aigne.io/docs/ghostty/en/libghostty-ed730d">libghostty API - docsmith.aigne.io</a></li>
<li><a href="https://en.wikipedia.org/wiki/Terminal_application">Terminal application</a></li>

</ul>
</details>

**Discussion**: Community members praised Hashimoto&\#x27;s decision to transfer Ghostty ownership to a non-profit and build Superlogical on top of open-source components. Some users drew parallels to historical technologies like OLE and COM, while others shared related tools such as pi-web, herdr, and firstmate. A few commenters criticized enigmatic titles and clickbait-style naming conventions.

**Tags**: `#terminal`, `#open-source`, `#software-architecture`, `#developer-tools`, `#systems`

---

<a id="item-9"></a>
## [Keychron Announces First Open-Source Firmware for Gaming Mice](https://www.digitalfoundry.net/news/2026/07/keychron-announces-first-open-source-firmware-for-gaming-mice) ⭐️ 7.0/10

Keychron announced plans to release open-source firmware for gaming mice, named ZGM \(Zephyr Gaming Mouse\), with a targeted release in Q1 2027 for the G6 HE hybrid magnetic switch gaming mouse. While no source code is available yet, the project is built on the Zephyr RTOS and aims to bring customizable, low-latency input processing to gaming peripherals. This move represents a significant step toward transparency and community-driven development in the gaming hardware space, potentially enabling deeper customization and repairability for users. It also extends the open-source firmware culture that has long thrived in mechanical keyboards into the gaming mouse market. The firmware, called ZGM, is built on the Zephyr Real-Time Operating System \(RTOS\) and supports both wired and wireless gaming mice. Keychron has shared a GitHub repository \(github.com/Keychron/zgm\) and a project site \(zgm.gg\), but the repository currently contains no source code, leading to skepticism about the timeline.

hackernews · JLO64 · Jul 29, 16:36 · [Discussion](https://news.ycombinator.com/item?id=49099715)

**Background**: QMK \(Quantum Mechanical Keyboard\) is a well-established open-source firmware platform used primarily for mechanical keyboards, allowing users to customize key layouts, macros, and lighting. While open-source firmware has gained traction in the keyboard community, gaming mice have largely remained closed-source, with limited options for user modification or auditing.

<details><summary>References</summary>
<ul>
<li><a href="https://zgm.gg/">ZGM Firmware — Zephyr Gaming Mouse</a></li>
<li><a href="https://en.wikipedia.org/wiki/QMK">QMK - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members expressed cautious optimism but raised concerns about the lack of released code and the distant 2027 timeline, with some labeling the announcement as &\#x27;vaporware.&\#x27; Users noted existing open-source mouse projects like QMK on Ploopy devices and questioned what unique value ZGM would offer. Some also expressed disappointment that Keychron’s mice lack experimental form factors.

**Tags**: `#Open Source Hardware`, `#Gaming Peripherals`, `#Firmware Development`, `#QMK`, `#Hardware Hacking`

---

<a id="item-10"></a>
## [KOReader: Popular Open-Source E-Reader App Gains Community Praise and Criticism](https://koreader.rocks/) ⭐️ 7.0/10

KOReader, a widely-used open-source e-reader application, continues to gain traction across platforms like Kindle, Kobo, and Remarkable, with users sharing both positive experiences and constructive feedback in a recent Hacker News discussion. This reflects the growing influence of open-source software in shaping user hardware choices and reading habits, demonstrating how community-driven projects can impact real-world purchasing decisions and device usage. KOReader supports multiple formats including PDF, EPUB, FB2, and DjVu, and offers features like cross-device sync, customizable typesetting, and advanced PDF reflow via the built-in K2pdfopt library, though some users report UI unintuitiveness and performance issues.

hackernews · Cider9986 · Jul 29, 11:05 · [Discussion](https://news.ycombinator.com/item?id=49095865)

**Background**: KOReader is an open-source ebook reader application designed to enhance the reading experience on various devices such as e-ink readers, tablets, and smartphones. It is particularly popular among users who value free software and seek advanced customization options beyond what proprietary readers offer. The project supports a wide range of document formats and emphasizes flexibility, multilingual support, and integration with tools like Calibre.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/koreader/koreader">GitHub - koreader/koreader: An ebook reader application supporting PDF, DjVu, EPUB, FB2 and many more formats, running on Cervantes, Kindle, Kobo, PocketBook and Android devices · GitHub</a></li>
<li><a href="https://koreader.com/">KOReader – Free eBook Reader for PDF &amp; EPUB</a></li>
<li><a href="https://f-droid.org/en/packages/org.koreader.launcher.fdroid/">KOReader | F-Droid - Free and Open Source Android App Repository</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion reveals a mix of enthusiasm and constructive criticism, with users praising KOReader&\#x27;s enhanced reading experience and free software philosophy, while also noting issues with UI intuitiveness, performance lag, and gesture controls. Some users have even made purchasing decisions based on KOReader compatibility, highlighting its significant impact on user behavior.

**Tags**: `#open-source`, `#e-reader`, `#software`, `#mobile`, `#user-experience`

---

<a id="item-11"></a>
## [AI Boom Drives Surge in Demand for Electricians and Construction Workers](https://www.nytimes.com/2026/07/29/business/economy/data-center-electricians-training.html) ⭐️ 7.0/10

AI companies are hiring electricians, carpenters, and other skilled tradespeople by the thousands to construct and outfit new data centers, marking a major shift in labor market demand. This surge is driven by the rapid expansion of AI infrastructure, particularly for high-density computing and liquid cooling systems. The growing need for skilled tradespeople highlights how AI development is reshaping not just software and algorithms, but also physical infrastructure and the broader economy. It creates new career opportunities but also raises concerns about market volatility and boom-bust cycles in construction. The demand is especially high for electricians due to the massive power requirements of AI data centers, while plumbers are increasingly needed for liquid cooling systems. Commenters noted that wages can fluctuate dramatically, from $300k during construction booms to $30k during downturns.

hackernews · thm · Jul 29, 14:43 · [Discussion](https://news.ycombinator.com/item?id=49098198)

**Background**: Data centers are specialized facilities that house computer servers and networking equipment, requiring robust electrical, cooling, and structural systems. With the rise of generative AI and large language models, these facilities must support higher power densities and more advanced cooling technologies, increasing the complexity and cost of construction. This has led to a surge in demand for skilled tradespeople who can install and maintain such infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.blackridgeresearch.com/blog/data-center-construction-process">How to Build a Data Center ? 6 Steps You Need to Know</a></li>
<li><a href="https://www.techrepublic.com/article/news-ai-data-center-power-cooling-infrastructure-dcw/">AI Demand Is Forcing a Rethink of Data Center Power, Cooling</a></li>
<li><a href="https://blog.se.com/datacenter/2026/04/09/building-ai-factories-why-integrated-power-and-liquid-cooling-systems-are-critical-for-high-density-ai-data-centers/">AI factory liquid cooling &amp; power infrastructure - Schneider ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views, with some cautioning against basing career decisions on this trend due to its boom-bust nature, while others celebrated the high pay and job security for tradespeople. One user predicted growing demand for plumbers due to the shift toward liquid cooling systems in next-gen data centers.

**Tags**: `#AI Infrastructure`, `#Data Centers`, `#Workforce Development`, `#Labor Economics`, `#Tech Trends`

---

<a id="item-12"></a>
## [CheapFoodMap: Crowdsourced Map of Meals Under $10](https://cheapfoodmap.com/) ⭐️ 7.0/10

CheapFoodMap, a crowdsourced map of affordable local meals under $10, has launched with 1,200 meals across 15 U.S. cities, seeded from Google Reviews and inspired by Korea’s 거지맵 \(Begger’s Map\). Built during a 100-day post-layoff project, the platform invites community feedback on price freshness and trust models. As inflation drives up food prices, tools like CheapFoodMap help budget-conscious diners discover affordable meals without relying on franchises, potentially supporting local businesses and strengthening community engagement around cost-of-living challenges. Seed data was sourced from Google Reviews \(4.2+ stars, 500+ reviews, verified under $10 per item\), excluding franchises. The creator is seeking feedback on incentivizing price updates and improving trust, with heaviest coverage currently in Texas.

hackernews · jaep1 · Jul 29, 16:59 · [Discussion](https://news.ycombinator.com/item?id=49100043)

**Background**: Show HN is a Hacker News format where creators share projects they’ve built and invite community feedback. 거지맵 \(Begger’s Map\), a Korean crowdsourced tool for finding cheap eats, inspired this project and recently gained popularity amid rising dining costs in South Korea.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49100043">Show HN: CheapFoodMap – A map of good meals under $10 | Hacker News</a></li>
<li><a href="https://oneulkorea.com/articles/trends/geojimap-korea-viral-budget-food-map-2026">Geojimap: Korea&#x27;s Viral Budget Food Map That 400,000 Koreans Are Using Right Now | OneulKorea Articles</a></li>
<li><a href="https://www.koreatimes.co.kr/economy/20260401/map-for-beggars-goes-viral-as-koreans-seek-cheap-eats-amid-rising-prices">&#x27;Map for beggars&#x27; goes viral as Koreans seek cheap eats amid rising prices - The Korea Times</a></li>

</ul>
</details>

**Discussion**: Commenters praised the concept and compared it to GasBuddy, suggesting business incentives for price updates. Others noted regional affordability differences and proposed filters for even cheaper meals, while some highlighted the value of warehouse club options for families.

**Tags**: `#Show HN`, `#Crowdsourcing`, `#Web Application`, `#Community Feedback`, `#Local Search`

---

<a id="item-13"></a>
## [Guide to Adding a Custom MCP Server to Claude and ChatGPT](https://simonwillison.net/2026/Jul/29/mcp-in-claude-and-chatgpt/#atom-everything) ⭐️ 7.0/10

Simon Willison published a practical guide detailing the multi-step process of connecting a custom Model Context Protocol \(MCP\) server to both Claude and ChatGPT through their standard chat interfaces. As MCP adoption grows among major AI providers like Anthropic, OpenAI, and Google DeepMind, this guide helps developers extend the capabilities of popular AI assistants by integrating custom tools and data sources. The process involves multiple configuration steps and is described as non-trivial, highlighting the current complexity of integrating custom MCP servers with consumer-facing AI chat interfaces.

rss · Simon Willison · Jul 29, 00:13

**Background**: The Model Context Protocol \(MCP\) is an open standard introduced by Anthropic in November 2024 to standardize how AI systems integrate with external tools, systems, and data sources. It provides a standardized interface for reading files, executing functions, and handling contextual prompts. Major AI providers including OpenAI and Google DeepMind have adopted the protocol.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>

</ul>
</details>

**Tags**: `#ai`, `#generative-ai`, `#chatgpt`, `#claude`, `#model-context-protocol`

---

<a id="item-14"></a>
## [EMNLP 2026 Launches Opt-In AI Reviewing Experiment](https://www.reddit.com/r/MachineLearning/comments/1v9jfci/emnlp_2026_ai_reviewing_experiment_d/) ⭐️ 7.0/10

EMNLP 2026 has launched an opt-in AI Reviewing Experiment where AI-generated reviews are provided to authors for feedback, without influencing the actual peer review decisions. A Reddit user is asking whether AI review results are visible for ARR May 2026 submissions. This experiment represents a significant step in integrating AI into academic peer review, potentially reshaping how research is evaluated in the NLP and ML communities. It raises important questions about transparency, accountability, and the future role of AI in scientific publishing. The experiment is conducted under IRB approval and uses either open-weights models on in-house compute or closed models with zero-data retention guarantees. AI reviews are explicitly stated not to inform any part of the conference decision process.

reddit · r/MachineLearning · /u/Historical\_Pause247 · Jul 29, 02:44

**Background**: EMNLP \(Conference on Empirical Methods in Natural Language Processing\) is a leading venue for NLP research. ACL Rolling Review \(ARR\) is a peer review platform that allows researchers to submit papers multiple times per year. The integration of AI into peer review is a growing trend aimed at improving efficiency and consistency in evaluating research submissions.

<details><summary>References</summary>
<ul>
<li><a href="https://2026.emnlp.org/ai-reviewing-experiment/">EMNLP 2026 AI Reviewing Experiment - EMNLP 2026</a></li>
<li><a href="https://zplatform.ai/ai-event/emnlp-2026/">EMNLP 2026: Dates, Venue &amp; Program Guide | zPlatform.ai</a></li>
<li><a href="https://linguistlist.org/issues/37/972/">LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)</a></li>

</ul>
</details>

**Tags**: `#Machine Learning`, `#Academic Publishing`, `#AI Ethics`, `#Peer Review`, `#NLP`

---

<a id="item-15"></a>
## [Vision Pro Used for Real-Space Architectural Design Visualization](https://christianselig.com/2026/07/vision-pro-house/) ⭐️ 6.0/10

A developer demonstrated using the Apple Vision Pro to walk through and assess 3D home designs overlaid in the user&\#x27;s actual living space, showing how spatial computing can support architectural design review. This shows how the Vision Pro can move beyond novelty demos into practical architectural workflows, potentially letting clients experience and validate designs at human scale before construction begins. The demonstration relies on the Vision Pro&\#x27;s spatial tracking to anchor 3D models in real rooms, but commenters noted similar workflows already exist using Quest 3, HTC Vive with IrisVR Prospect, or even iPhone ARKit at far lower cost.

hackernews · robbiet480 · Jul 29, 20:39 · [Discussion](https://news.ycombinator.com/item?id=49102774)

**Background**: Architectural visualization converts CAD/BIM data into immersive visuals that help clients understand and validate designs before construction. AR and VR have already transformed this field by enabling real-time walkthroughs and spatial collaboration, with tools like Enscape, IrisVR Prospect, and Apple&\#x27;s ARKit supporting headset and mobile-based experiences.

<details><summary>References</summary>
<ul>
<li><a href="https://www.maxon.net/en/article/architectural-visualization-guide">What Is Architectural Visualization? A Complete Guide ... - Maxon</a></li>
<li><a href="https://www.augmentecture.com/blog/ar-in-architecture-designing-the-future-of-built-environments/">AR in Architecture: Designing the Future of Built Environments</a></li>
<li><a href="https://archint.org/the-evolution-of-architectural-visualization-how-vr-and-ar-are-changing-the-game/">Architectural Visualization: The Impact of VR &amp; AR – ArchInt</a></li>

</ul>
</details>

**Discussion**: Commenters were largely positive, sharing that their firms already use Quest 3 and HTC Vive with IrisVR Prospect for client walkthroughs and that the spatial feedback is valuable for proportion and planning. Some questioned the price premium of the Vision Pro versus iPhone ARKit, while others praised the developer&\#x27;s prior work on iOS apps.

**Tags**: `#AR/VR`, `#Vision Pro`, `#Architecture`, `#Design Technology`, `#Spatial Computing`

---

<a id="item-16"></a>
## [D. Richard Hipp on How SQL Transformed Data Querying](https://simonwillison.net/2026/Jul/29/d-richard-hipp/#atom-everything) ⭐️ 6.0/10

D. Richard Hipp reflected on how SQL replaced manual data querying code previously written by COBOL programmers, turning a specialized programming task into a simple declarative specification. This historical perspective illustrates how abstraction layers like SQL reshape job roles rather than eliminate them, a relevant insight as AI and automation continue to transform technical careers. Before SQL, COBOL programmers embedded SQL-like operations directly into code using host variables, cursors, and SQLCA for DB2 interaction. SQL introduced a declarative approach where users specify what they want rather than how to get it.

rss · Simon Willison · Jul 29, 21:15

**Background**: Before SQL, database interactions were performed using embedded SQL within host languages like COBOL, requiring detailed imperative programming. SQL introduced a declarative paradigm, allowing users to specify desired results without detailing the execution steps. This shift abstracted away low-level programming tasks, making data querying more accessible to non-specialists.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tutorialspoint.com/cobol/cobol_database_interface.htm">COBOL - Database Interface - Online Tutorials Library Code sample</a></li>
<li><a href="https://octopus.com/devops/infrastructure-as-code/declarative-vs-imperative-programming/">Declarative Vs. Imperative Programming: 4 Key Differences | Octopus Deploy</a></li>
<li><a href="https://www.educative.io/blog/declarative-vs-imperative-programming">Declarative vs imperative programming: 5 key differences</a></li>

</ul>
</details>

**Tags**: `#sql`, `#history`, `#programming-languages`, `#career-evolution`, `#d-richard-hipp`

---

<a id="item-17"></a>
## [ICLR 2027 Deadline Set Before NeurIPS 2026 Decisions](https://www.reddit.com/r/MachineLearning/comments/1v9v4e7/iclr_2027_deadline_is_before_neurips_2026/) ⭐️ 6.0/10

ICLR 2027 has set its full paper submission deadline for September 16, 2026, which falls 8 days before NeurIPS 2026 decisions are expected to be released. This creates a scheduling conflict for researchers who may want to revise or resubmit papers based on NeurIPS feedback. This scheduling conflict affects researchers&\#x27; submission strategies, as they cannot incorporate feedback from NeurIPS 2026 into their ICLR 2027 submissions. It raises concerns about coordination between major ML conferences and the impact on research workflow efficiency. The ICLR 2027 deadline is September 16, 2026, while NeurIPS 2026 decisions are expected around September 24, 2026. Researchers whose papers were rejected or improved since NeurIPS submission may be disadvantaged by this overlap.

reddit · r/MachineLearning · /u/1414vo · Jul 29, 12:43

**Background**: ICLR \(International Conference on Learning Representations\) and NeurIPS \(Conference on Neural Information Processing Systems\) are two of the most prestigious annual conferences in machine learning. Both conferences follow a cycle where papers are submitted, reviewed, and decisions are communicated to authors months before the actual conference. When deadlines overlap, researchers face difficult choices about where to submit their work and how to incorporate feedback from one conference into another.

<details><summary>References</summary>
<ul>
<li><a href="https://iclr.cc/Conferences/2027/AuthorGuidelines">ICLR 2027 Author Guidelines</a></li>
<li><a href="https://neurips.cc/Conferences/2026/CallForPapers">Call for Papers 2026</a></li>
<li><a href="https://huggingface.co/spaces/huggingface/ai-deadlines/commit/99f16a754ac0ed468034709b8cd393e594791a01">Update NeurIPS 2025 and 2026 conference data · huggingface/ai-deadlines at 99f16a7</a></li>

</ul>
</details>

**Discussion**: Community members expressed frustration with the scheduling conflict, agreeing that it disadvantages researchers who might benefit from NeurIPS feedback. Some speculated that ICLR may have intentionally moved the deadline earlier to reduce submission load, while others called for better coordination between major conferences.

**Tags**: `#machine-learning`, `#conference-scheduling`, `#research-workflow`, `#academic-publishing`

---

<a id="item-18"></a>
## [TanML: Open-Source Toolkit for Automated Tabular Model Validation](https://www.reddit.com/r/MachineLearning/comments/1va7w4p/opensource_tabular_model_validation_toolkit_tanml/) ⭐️ 6.0/10

TanML, an MIT-licensed open-source toolkit for validating tabular machine learning models, has been released and is seeking community feedback on its features and usability. It supports an end-to-end workflow including data profiling, drift analysis, SHAP explainability, and audit-ready reports. The toolkit addresses the growing need for model validation in regulated industries such as banking and insurance, where compliance with standards like SR 11-7 is critical. By automating documentation and validation steps, TanML could streamline model risk management workflows and reduce manual effort. TanML runs locally and integrates SHAP \(SHapley Additive exPlanations\) for model interpretability, along with drift analysis and stress testing. It generates audit-ready Word reports, aiming to bridge the gap between data science tools and governance requirements.

reddit · r/MachineLearning · /u/AccomplishedLeg1508 · Jul 29, 20:22

**Background**: Model Risk Management \(MRM\) refers to the processes used by financial institutions to ensure that models used for decision-making are reliable and compliant with regulatory standards such as SR 11-7. SHAP is a widely used method for explaining machine learning model predictions by assigning importance values to input features. Tools like TanML aim to combine data science workflows with governance requirements, automating validation and documentation for regulated environments.

<details><summary>References</summary>
<ul>
<li><a href="https://tdlabs-ai.github.io/tanml/">TanML: Automated Model Validation Toolkit for Tabular Machine ...</a></li>
<li><a href="https://github.com/tdlabs-ai/tanml">TanML: Automated Model Validation Toolkit for ... - GitHub</a></li>
<li><a href="https://pypi.org/project/tanml/">tanml · PyPI</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#model-validation`, `#open-source`, `#tabular-data`, `#model-risk-management`

---

<a id="item-19"></a>
## [University of the Sunshine Coast Researchers Survey Human-AI Relationships](https://www.reddit.com/r/MachineLearning/comments/1v9maa7/exploring_humanai_relationships_honours_thesis_r/) ⭐️ 6.0/10

Honours researchers at the University of the Sunshine Coast have launched an anonymous survey to explore human-AI relationships, targeting individuals aged 18 and over who have interacted with AI companions for friendship or romantic purposes within the past six months. The 25-30 minute survey is part of an ethics-approved study \(Approval S262259\) aimed at understanding evolving dynamics in human-AI interactions. As AI companions become increasingly sophisticated and socially integrated, understanding the emotional and relational dimensions of human-AI interactions is critical for guiding ethical development and policy. This research contributes to growing academic interest in how humans form attachments with AI systems. The survey is anonymous and designed to take approximately 25-30 minutes to complete, with no right or wrong answers. It is being conducted by three honours students under the supervision of the UniSC Human Research Ethics Committee, with full ethics approval \(S262259\).

reddit · r/MachineLearning · /u/Ok-Suggestion2488 · Jul 29, 05:02

**Background**: Human-AI interaction is a multidisciplinary field studied through social psychology, communications, and human-computer interaction frameworks. Recent research has focused on how individuals develop emotional attachments to AI, particularly in the context of companion apps like Replika and Character.AI. These platforms simulate intimacy and friendship, raising questions about authenticity, reciprocity, and the psychological impact of such relationships. The field is rapidly evolving, with increasing attention on the ethical implications of AI companionship.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Human%E2%80%93AI_interaction">Human – AI interaction - Wikipedia</a></li>
<li><a href="https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1723503/full">Frontiers | Human-AI attachment: how humans develop intimate relationships with AI</a></li>
<li><a href="https://justainews.com/blog/best-ai-companion-apps-and-ai-friends-2026/">Best AI Companion Apps &amp; AI Friends in 2026: Honest Reviews</a></li>

</ul>
</details>

**Tags**: `#human-ai-relationships`, `#academic-research`, `#survey-research`, `#ai-ethics`

---
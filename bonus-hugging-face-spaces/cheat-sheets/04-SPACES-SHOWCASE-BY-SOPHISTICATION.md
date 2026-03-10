# Hugging Face Spaces Showcase: From "Hello World" to Semi-Professional Apps

The point of this guide is simple: **you can build real, impressive, functional web apps on Hugging Face Spaces for free.** This is not just for toy demos. Companies like OpenAI, Tencent, NVIDIA, Qwen, and Black Forest Labs deploy production-quality interfaces here. Students can use Spaces to prototype ideas, build portfolio pieces, and test concepts before spending money on hosting.

Everything below is a **Gradio** Space unless noted otherwise. All links are live and explorable.

---

## Tier 1: The Basics — "My First Space"

These Spaces use the simplest Gradio patterns: a text input, a button, a text output. They prove that **a useful app can be 20 lines of Python.** Start here.

### What They Look Like
Standard Gradio interface: labeled input boxes, a submit button, output area. No custom styling, no JavaScript, no complex layout. The Gradio defaults do the visual work for you.

### Examples

| Space | What It Does | Why It's a Good Example | Link |
|-------|-------------|------------------------|------|
| **Zero-Shot Text Classification** | Enter text + candidate labels → get classification | Classic `gr.Interface` pattern: one function, two inputs, one output. ~50 lines of code. | [datasciencedojo/Zero-Shot-Text-Classification](https://hf.co/spaces/datasciencedojo/Zero-Shot-Text-Classification) |
| **GPT Detector** | Paste text → see if AI wrote it | Binary classification with a simple probability output. Minimal UI. | [rusen/gpt_detector](https://hf.co/spaces/rusen/gpt_detector) |
| **Text to Emotion Classifier** | Enter text → see emotion label | Single model, single output. As simple as it gets. | [Elegbede/Text_to_emotion_classifier](https://hf.co/spaces/Elegbede/Text_to_emotion_classifier) |
| **Emotions Classifier** | Enter text → emotion prediction | Another single-function demo. Good to compare approaches with the one above. | [Rahmat82/emotions_classifier](https://hf.co/spaces/Rahmat82/emotions_classifier) |
| **Skill Extraction** | Paste a job description → extract skills | Uses NER model, displays extracted entities. Clean, focused, useful. | [jjzha/skill_extraction_demo](https://hf.co/spaces/jjzha/skill_extraction_demo) |

### Gradio Patterns Used
- `gr.Interface(fn, inputs, outputs)` — the one-liner approach
- `gr.Textbox`, `gr.Label`, `gr.JSON` for simple I/O
- No `gr.Blocks`, no custom HTML, no JavaScript

### What Students Learn
- How to wrap a Hugging Face model in a web UI with minimal code
- How `requirements.txt` and `app.py` are all you need to deploy
- That "shipping something" is more valuable than perfecting it

---

## Tier 2: Structured Layouts — `gr.Blocks` and Multi-Component UIs

These Spaces go beyond single-function demos. They use `gr.Blocks()` to arrange multiple components, tabs, columns, and rows. The UI starts to feel like a real application.

### What They Look Like
Tabbed interfaces, side-by-side panels, multiple input types (text + audio + file upload), progress indicators, and conditional visibility.

### Examples

| Space | What It Does | Why It's a Good Example | Link |
|-------|-------------|------------------------|------|
| **OpenAI Whisper** | Upload audio or YouTube URL → transcription | Multi-input (mic, file, URL), tabbed output, language selection. 2,724 likes — one of the most popular Spaces ever. | [openai/whisper](https://hf.co/spaces/openai/whisper) |
| **GLiNER Multi v2.1** | Named entity recognition with custom labels | Dynamic label input, highlighted text output, good use of `gr.HighlightedText`. | [urchade/gliner_multiv2.1](https://hf.co/spaces/urchade/gliner_multiv2.1) |
| **AI Content Detector** | Paste text → AI vs. human score | Uses `gr.Blocks` for a cleaner layout than basic `Interface`, with a confidence meter display. | [PirateXX/AI-Content-Detector](https://hf.co/spaces/PirateXX/AI-Content-Detector) |
| **Qwen3 ASR Demo** | Audio speech recognition with timestamps | Multi-language support, structured output with word-level timestamps. Shows how audio + structured data can combine. | [Qwen/Qwen3-ASR](https://hf.co/spaces/Qwen/Qwen3-ASR) |
| **Multilingual TTS** | Type text → hear it spoken in many languages | Language selector, voice picker, audio output. Clean multi-step workflow. | [MohamedRashad/Multilingual-TTS](https://hf.co/spaces/MohamedRashad/Multilingual-TTS) |

### Gradio Patterns Used
- `gr.Blocks()` with `gr.Row()`, `gr.Column()`, `gr.Tab()`
- `gr.Audio`, `gr.File`, `gr.Dropdown` for richer input types
- `gr.HighlightedText`, `gr.Plot` for richer outputs
- Event chaining: one button triggers multiple updates
- `gr.Examples` for pre-loaded sample inputs

### What Students Learn
- How to move from `Interface` to `Blocks` for layout control
- How to combine multiple input types in a single app
- How tabs and columns create a more "app-like" experience

---

## Tier 3: Chatbot & Conversational UIs

Chat interfaces are one of the most common patterns on Spaces. Gradio's `gr.ChatInterface` makes this surprisingly easy, but some Spaces push it much further with streaming, multimodal input, and reasoning displays.

### What They Look Like
Chat bubbles, streaming token output, image/video upload into chat, collapsible "thinking" sections, model parameter controls in sidebars.

### Examples

| Space | What It Does | Why It's a Good Example | Link |
|-------|-------------|------------------------|------|
| **Qwen3 Demo** | Chat with Qwen3, see its reasoning chain | Streaming output with collapsible "thinking" panel. Shows how to expose model reasoning. 844 likes. | [Qwen/Qwen3-Demo](https://hf.co/spaces/Qwen/Qwen3-Demo) |
| **Qwen3 VL Demo** | Chat with text, images, and video | Multimodal chat: upload images/video alongside text. Shows the frontier of chat UIs. | [Qwen/Qwen3-VL-Demo](https://hf.co/spaces/Qwen/Qwen3-VL-Demo) |
| **DeepSeek VL2 Small** | Vision-language chat | Image understanding in a clean chat interface. Good example of a focused multimodal chat. | [deepseek-ai/deepseek-vl2-small](https://hf.co/spaces/deepseek-ai/deepseek-vl2-small) |
| **Groq Voice Assistant** | Voice-in, voice-out chat | Real-time audio conversation. Pushes Gradio into voice territory. | [Groq/groq-gradio-voice-assistant](https://hf.co/spaces/Groq/groq-gradio-voice-assistant) |
| **RWKV-Gradio-2** | Chat with the RWKV model | One of the early popular chat Spaces. 651 likes. Clean, focused implementation. | [BlinkDL/RWKV-Gradio-2](https://hf.co/spaces/BlinkDL/RWKV-Gradio-2) |

### Gradio Patterns Used
- `gr.ChatInterface` for quick chat UIs
- `gr.Chatbot` with streaming via generator functions (`yield`)
- Multimodal message objects (text + images in one message)
- Sidebar controls for temperature, max tokens, system prompts
- Custom CSS for chat bubble styling

### What Students Learn
- How `gr.ChatInterface` gets you to a working chatbot in ~10 lines
- How streaming works (Python generators + `yield`)
- How to add model parameter controls alongside a chat window

---

## Tier 4: Data Visualization & Leaderboards

These Spaces use Gradio as a data dashboard framework. They combine interactive tables, charts, filtering controls, and rich displays. Many are used by the research community as official benchmarks.

### What They Look Like
Sortable/filterable tables, bar charts, radar plots, comparison views, submission forms for new entries.

### Examples

| Space | What It Does | Why It's a Good Example | Link |
|-------|-------------|------------------------|------|
| **GAIA Leaderboard** | LLM agent benchmark with submission system | Full leaderboard with filtering, model submission, and comparison tools. 588 likes. Used by the research community. | [gaia-benchmark/leaderboard](https://hf.co/spaces/gaia-benchmark/leaderboard) |
| **Open ASR Leaderboard** | Compare speech recognition models across languages | Multi-dataset, multi-language comparison. 1,237 likes. One of the most polished leaderboards. | [hf-audio/open_asr_leaderboard](https://hf.co/spaces/hf-audio/open_asr_leaderboard) |
| **VBench Leaderboard** | Video model evaluation | Upload evaluation results, automated ranking. Shows how Spaces can be data collection + display tools. | [Vchitect/VBench_Leaderboard](https://hf.co/spaces/Vchitect/VBench_Leaderboard) |
| **TTS Spaces Arena** | Blind vote on text-to-speech models | ELO-style ranking from user votes. The "arena" pattern — interactive, crowd-sourced evaluation. 471 likes. | [Pendrokar/TTS-Spaces-Arena](https://hf.co/spaces/Pendrokar/TTS-Spaces-Arena) |
| **GIFT-Eval** | Time series forecasting benchmark | Salesforce-built dashboard with rich comparison views. Shows enterprise-quality data visualization. | [Salesforce/GIFT-Eval](https://hf.co/spaces/Salesforce/GIFT-Eval) |
| **Deep RL Leaderboard** | Reinforcement learning model comparison | Search, filter, sort across environments. Built by Hugging Face themselves. | [huggingface-projects/Deep-Reinforcement-Learning-Leaderboard](https://hf.co/spaces/huggingface-projects/Deep-Reinforcement-Learning-Leaderboard) |

### Gradio Patterns Used
- `gr.Dataframe` for interactive tables
- `gr.Plot` with Plotly for rich charts
- `gr.Dropdown` / `gr.CheckboxGroup` for filtering
- Custom CSS themes for branded looks
- File upload for benchmark submissions

### What Students Learn
- That Spaces aren't just for model demos — they're a dashboard platform
- How to build interactive data exploration tools
- That leaderboards/arenas are a powerful pattern for community engagement

---

## Tier 5: Professional-Grade Tools — Image, Video, 3D, and Document Processing

These are the Spaces that make people say "wait, this is free?" They handle complex media types — generating images, editing video, building 3D models, OCR on documents. Many are built by major companies and research labs.

### What They Look Like
Multi-step workflows, canvas/sketchpad inputs, side-by-side before/after views, 3D model viewers, progress bars for long-running tasks, gallery displays.

### Examples

| Space | What It Does | Why It's a Good Example | Link |
|-------|-------------|------------------------|------|
| **FLUX.2 [Klein] 9B** | Text-to-image generation + image editing | Black Forest Labs' flagship. Image gen + editing in one interface. Also an MCP server. 632 likes. | [black-forest-labs/FLUX.2-klein-9B](https://hf.co/spaces/black-forest-labs/FLUX.2-klein-9B) |
| **Z Image Turbo** | Ultra-fast text-to-image | Real-time generation as you type. Shows what's possible with optimized inference. 2,499 likes. | [mrfakename/Z-Image-Turbo](https://hf.co/spaces/mrfakename/Z-Image-Turbo) |
| **Hunyuan3D-2.1** | Image → 3D model generation | Tencent's 3D generator with an embedded 3D model viewer. 2,091 likes. The viewer alone is impressive. | [tencent/Hunyuan3D-2.1](https://hf.co/spaces/tencent/Hunyuan3D-2.1) |
| **TRELLIS.2** | Images → high-fidelity 3D models | Microsoft's 3D reconstruction. Interactive 3D viewer in the browser. 1,207 likes. | [microsoft/TRELLIS.2](https://hf.co/spaces/microsoft/TRELLIS.2) |
| **MinerU OCR** | PDF → Markdown/JSON extraction | Full document processing pipeline. Upload a PDF, get structured output. 549 likes. A real productivity tool. | [opendatalab/MinerU](https://hf.co/spaces/opendatalab/MinerU) |
| **DeepSeek OCR 2 Demo** | OCR on images and PDFs | Upload any document, extract text with layout preservation. Clean, functional, useful. | [merterbak/DeepSeek-OCR-Demo](https://hf.co/spaces/merterbak/DeepSeek-OCR-Demo) |
| **Roboflow Trackers** | Upload video → track objects across frames | Video processing with annotated output. Shows Gradio handling video workflows. | [Roboflow/Trackers](https://hf.co/spaces/Roboflow/Trackers) |
| **Qwen Image Edit LoRAs** | AI-powered image editing | Edit images with natural language instructions. Multiple LoRA models. 1,019 likes. | [prithivMLmods/Qwen-Image-Edit-2511-LoRAs-Fast](https://hf.co/spaces/prithivMLmods/Qwen-Image-Edit-2511-LoRAs-Fast) |
| **Wan2.2 Animate** | Image/text → video generation | Wan-AI's video generator. 4,898 likes — one of the highest-liked Spaces. | [Wan-AI/Wan2.2-Animate](https://hf.co/spaces/Wan-AI/Wan2.2-Animate) |

### Gradio Patterns Used
- `gr.Image`, `gr.Video`, `gr.Gallery` for rich media I/O
- `gr.Model3D` for interactive 3D viewer
- `gr.ImageEditor` / `gr.Sketchpad` for canvas-based input
- Custom Gradio components (e.g., PDF viewer, 3D viewer)
- GPU-accelerated inference via HF Spaces GPU options
- Progress indicators for long-running tasks

### What Students Learn
- That Spaces can handle heavy computational tasks (image gen, 3D, video)
- How professional teams structure complex multi-step workflows
- That the line between "demo" and "product" can be very thin

---

## Tier 6: Cutting-Edge — Custom HTML, Code Generation, and Full Web Apps

These Spaces push Gradio to its limits. They use Gradio 6's `gr.HTML` capabilities, custom components, or creative architecture to build things that don't look or feel like typical Gradio apps at all. Some generate entire applications. Others have custom JavaScript interactivity.

### What They Look Like
Custom-styled interfaces that break out of the standard Gradio look. Embedded code editors, live previews, workflow builders, arena-style voting, real-time WebRTC video.

### Examples

| Space | What It Does | Why It's a Good Example | Link |
|-------|-------------|------------------------|------|
| **Qwen2.5 Coder Artifacts** | Describe an app → get generated, runnable code with live preview | Like a mini Cursor/Replit in a Space. Code editor + live preview panel. 1,721 likes. | [Qwen/Qwen2.5-Coder-Artifacts](https://hf.co/spaces/Qwen/Qwen2.5-Coder-Artifacts) |
| **Gradio Canvas** | Draw/sketch-based interaction | Custom canvas component for freeform drawing input. Shows how to build non-standard input types. | [gabrielchua/gradio-canvas](https://hf.co/spaces/gabrielchua/gradio-canvas) |
| **Gradio Workflow Builder** | Visual node-based workflow editor | Drag-and-drop workflow creation inside Gradio. Custom component with complex JavaScript. | [Agents-MCP-Hackathon/gradio_workflowbuilder](https://hf.co/spaces/Agents-MCP-Hackathon/gradio_workflowbuilder) |
| **Gradio Playground Bot** | Describe a Gradio app → AI generates it | Meta: an AI that builds Gradio apps, running inside a Gradio app. Built by a Gradio core maintainer. | [abidlabs/gradio-playground-bot](https://hf.co/spaces/abidlabs/gradio-playground-bot) |
| **WebRTC YOLOv10n** | Live webcam object detection | Real-time video stream processing via WebRTC. No file upload — live camera feed. | [freddyaboulton/webrtc-yolov10n](https://hf.co/spaces/freddyaboulton/webrtc-yolov10n) |
| **LLaMA Mesh** | Chat → 3D mesh generation | Type a description, get a 3D model you can rotate and inspect. Chat + 3D viewer fusion. | [Zhengyi/LLaMA-Mesh](https://hf.co/spaces/Zhengyi/LLaMA-Mesh) |
| **Gradio-Blocks Story & Video Generation** | Story → illustration → video pipeline | Multi-model pipeline: text gen → image gen → video compilation. Early but influential example. | [Gradio-Blocks/Story_and_Video_Generation](https://hf.co/spaces/Gradio-Blocks/Story_and_Video_Generation) |
| **Text-guided Flux Inpainting** | Draw a mask → describe replacement → AI fills it in | Canvas-based mask drawing + text prompt + inpainting. Complex multi-step interaction. | [Gradio-Community/Text-guided-Flux-Inpainting](https://hf.co/spaces/Gradio-Community/Text-guided-Flux-Inpainting) |

### Gradio Patterns Used
- `gr.HTML` with `html_template`, `css_template`, `js_on_load` (Gradio 6)
- Custom Gradio components (built with `gradio cc create`)
- `gr.Code` for embedded code editors
- WebRTC integration for real-time video
- Complex event chains and state management
- `server_functions` for async Python ↔ JavaScript calls
- Custom themes and CSS overrides

### What Students Learn
- That Gradio 6's `gr.HTML` turns Spaces into a full web app platform
- How to combine multiple AI models in a single pipeline
- That "custom components" open up unlimited UI possibilities
- That real-time / streaming interfaces are achievable

---

## The Sophistication Spectrum — Summary

```
Tier 1: Basic Interface        → 20-50 lines, gr.Interface, zero JS
  ↓
Tier 2: Blocks Layout          → 50-200 lines, gr.Blocks, tabs/columns
  ↓
Tier 3: Chat UI                → gr.ChatInterface, streaming, multimodal
  ↓
Tier 4: Data Dashboards        → Tables, charts, filtering, submissions
  ↓
Tier 5: Pro Media Tools        → Image/video/3D/document processing
  ↓
Tier 6: Custom Web Apps        → gr.HTML, custom JS, real-time, pipelines
```

### Key Takeaway for Students

Every Space in this list is **free to deploy** on Hugging Face. The difference between Tier 1 and Tier 6 is not money — it's knowledge. You already know Python. Adding some HTML/CSS/JS (which Gradio 6 makes very approachable) takes you from "simple demo" to "impressive portfolio piece."

**The prototyping argument:** Before you spend $20/month on Vercel or $50/month on AWS, build it on Spaces first. Prove the idea works. Get user feedback. Then migrate to paid hosting only when you've validated the concept.

---

## Framework Quick Reference

While this guide focuses on Gradio (since it's what we use in our Spaces), HF Spaces also supports:

| Framework | Best For | Complexity |
|-----------|---------|------------|
| **Gradio** | ML demos, data tools, chatbots | Low–Medium |
| **Streamlit** | Data dashboards, quick prototypes | Low–Medium |
| **Docker** | Anything — full control, any language | High |
| **Static HTML** | Landing pages, documentation, portfolios | Low |

Gradio is the sweet spot for our course because it's Python-native, AI-model-friendly, and with Gradio 6's `gr.HTML`, it can produce genuinely polished interfaces.

---

## How This Connects to Our Course Spaces

Our five course Spaces sit in the **Tier 2–3 range** with Gradio 6 `gr.HTML` pushing them toward **Tier 6 visual quality**:

| Our Space | Base Tier | With gr.HTML |
|-----------|-----------|-------------|
| Image Color Mood Analyzer | Tier 2 (Blocks + image input) | Tier 5 look (custom color cards) |
| Emoji Mood Translator | Tier 2 (text → styled output) | Tier 6 look (custom emoji grid) |
| Audio Emotion Detector | Tier 2 (audio → classification) | Tier 4 look (custom visualization) |
| Headline Mood Dashboard | Tier 2 (multi-text analysis) | Tier 4 look (custom bar charts) |
| Story Emotion Arc | Tier 2 (text → chart) | Tier 5 look (SVG arc visualization) |

The message: **You don't need Tier 6 coding skills to get Tier 6 visual results.** Gradio 6's `gr.HTML` with `css_template` and `html_template` lets you write Python + a little HTML/CSS and produce something that looks far more sophisticated than the code complexity would suggest.

---

## Sources & Further Exploration

- [Hugging Face Spaces homepage](https://huggingface.co/spaces) — Browse trending and featured Spaces
- [Gradio Custom HTML Components Guide](https://gradio.app/guides/custom-HTML-components) — Official Gradio 6 `gr.HTML` documentation
- [One-Shot Any Web App with Gradio's gr.HTML](https://huggingface.co/blog/gradio-html-one-shot-apps) — The blog post that introduced the "vibe coding" approach
- [Gradio Quickstart](https://gradio.app/guides/quickstart) — Start from zero
- [Gradio Custom Components in Five Minutes](https://gradio.app/guides/custom-components-in-five-minutes) — Build your own reusable components

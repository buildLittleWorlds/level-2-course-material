# Build Guide 02: Emoji Mood Translator

**Complexity:** Low — single model, straightforward output
**Memory:** ~1.5GB (one transformer model + torch)
**Gradio 6 concepts introduced:** `gr.Blocks` layout, `html_template` with Handlebars, `css_template` together

---

## What This Space Does

Type any sentence and get back emojis that match its emotional content. Uses a 28-emotion model (GoEmotions) to detect feelings like joy, anger, curiosity, and gratitude, then maps each to its emoji.

## Why It's Second

This is your first Space with an ML model. One model, one text input, emoji output. The main new thing you're managing is model loading and memory.

## requirements.txt

```
gradio==6.9.0
transformers==4.48.0
torch
```

---

## Phase 1: Hello World with Text

```python
import gradio as gr

gr.Interface(
    fn=lambda text: f"You typed {len(text.split())} words.",
    inputs="text",
    outputs="text",
    title="Text Echo"
).launch()
```

**Deploy.** Confirm text input/output works.

---

## Phase 2: Add the Sentiment Model

Load the GoEmotions model with **lazy loading** — the model loads on first use, not at startup. This prevents crashes if the network hiccups during container boot.

```python
import gradio as gr
from transformers import pipeline

# Lazy loading: model loads on first call, not at startup
_classifier = None
def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "text-classification",
            model="SamLowe/roberta-base-go_emotions",
            top_k=None
        )
    return _classifier

def analyze(text):
    if not text.strip():
        return "Type something first."
    results = get_classifier()(text)[0]
    top = sorted(results, key=lambda x: x["score"], reverse=True)[:5]
    lines = [f'{r["label"]}: {r["score"]:.1%}' for r in top]
    return "\n".join(lines)

gr.Interface(fn=analyze, inputs="text", outputs="text",
             title="Emotion Detector").launch()
```

**Deploy.** Type "I'm so excited about this!" — you should see emotions like `excitement`, `joy`, `approval` with confidence scores. The first analysis will be slow (model downloading), subsequent ones fast.

> **Pattern: Lazy Loading**
> Always use `get_model()` with a global singleton instead of loading at module level. If the network fails during download, the Space shows an error page instead of crashing the whole container. Users can retry.

---

## Phase 3: Emoji Mapping + HTML Output

Map each of the 28 GoEmotions to an emoji and render styled HTML.

```python
import gradio as gr
from transformers import pipeline

EMOJI_MAP = {
    "admiration": "🤩", "amusement": "😄", "anger": "😠", "annoyance": "😤",
    "approval": "👍", "caring": "🤗", "confusion": "😕", "curiosity": "🤔",
    "desire": "😍", "disappointment": "😞", "disapproval": "👎", "disgust": "🤢",
    "embarrassment": "😳", "excitement": "🎉", "fear": "😨", "gratitude": "🙏",
    "grief": "😭", "joy": "😊", "love": "❤️", "nervousness": "😰",
    "neutral": "😐", "optimism": "🌟", "pride": "🏆", "realization": "💡",
    "relief": "😌", "remorse": "😔", "sadness": "😢", "surprise": "😲",
}

_classifier = None
def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "text-classification",
            model="SamLowe/roberta-base-go_emotions",
            top_k=None
        )
    return _classifier

def analyze(text):
    if not text.strip():
        return "<p style='color:#999;'>Type something to see its emoji mood.</p>"

    results = get_classifier()(text)[0]
    # Take emotions with score > 0.05, or at least top 3
    active = [r for r in results if r["score"] > 0.05]
    if len(active) < 3:
        active = sorted(results, key=lambda x: x["score"], reverse=True)[:3]
    active = sorted(active, key=lambda x: x["score"], reverse=True)[:8]

    # Big emoji row
    emojis = []
    for r in active:
        emoji = EMOJI_MAP.get(r["label"], "❓")
        size = int(36 + r["score"] * 50)
        emojis.append(f'<span style="font-size:{size}px;" title="{r["label"]}">{emoji}</span>')

    # Detail bars
    bars = []
    for r in active:
        emoji = EMOJI_MAP.get(r["label"], "❓")
        pct = r["score"] * 100
        bars.append(f"""
        <div style="display:flex; align-items:center; gap:8px; margin:4px 0;">
            <span style="width:24px;">{emoji}</span>
            <span style="width:100px; font-size:0.85em;">{r["label"]}</span>
            <div style="flex:1; background:#eee; border-radius:4px; height:16px;">
                <div style="width:{pct}%; background:#667eea; border-radius:4px;
                            height:100%; min-width:2px;"></div>
            </div>
            <span style="font-size:0.8em; color:#888; width:40px;">{pct:.0f}%</span>
        </div>""")

    return f"""
    <div style="font-family:system-ui;">
        <div style="text-align:center; padding:16px 0; letter-spacing:8px;">
            {"".join(emojis)}
        </div>
        <div style="margin-top:12px;">{"".join(bars)}</div>
    </div>"""

gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(label="Type anything", lines=2,
                      placeholder="I can't believe how amazing this turned out!"),
    outputs=gr.HTML(label="Emoji Mood"),
    title="Emoji Mood Translator",
    examples=[
        ["I'm so proud of what we accomplished together!"],
        ["This is confusing and frustrating."],
        ["I wonder what would happen if we tried something different."],
    ]
).launch()
```

**Deploy.** You should see large emojis scaled by confidence, with detail bars below. This is still the classic approach — Python returns an HTML string with inline styles.

---

## Phase 4: Gradio 6 — `html_template` + `css_template`

> **New Gradio 6 concept: `html_template` with data binding**
> Instead of building HTML strings in Python, you return structured data (a list of dicts) and let a template render it. When the `value` updates, the template re-renders automatically. This separates your data logic (Python) from your presentation (HTML/CSS).
>
> **Handlebars syntax:** Use `{{#each value}}` to loop over arrays and `{{this.field}}` to access properties.

```python
import gradio as gr
from transformers import pipeline

EMOJI_MAP = {
    "admiration": "🤩", "amusement": "😄", "anger": "😠", "annoyance": "😤",
    "approval": "👍", "caring": "🤗", "confusion": "😕", "curiosity": "🤔",
    "desire": "😍", "disappointment": "😞", "disapproval": "👎", "disgust": "🤢",
    "embarrassment": "😳", "excitement": "🎉", "fear": "😨", "gratitude": "🙏",
    "grief": "😭", "joy": "😊", "love": "❤️", "nervousness": "😰",
    "neutral": "😐", "optimism": "🌟", "pride": "🏆", "realization": "💡",
    "relief": "😌", "remorse": "😔", "sadness": "😢", "surprise": "😲",
}

_classifier = None
def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "text-classification",
            model="SamLowe/roberta-base-go_emotions",
            top_k=None
        )
    return _classifier

def analyze(text):
    if not text.strip():
        return []

    results = get_classifier()(text)[0]
    active = [r for r in results if r["score"] > 0.05]
    if len(active) < 3:
        active = sorted(results, key=lambda x: x["score"], reverse=True)[:3]
    active = sorted(active, key=lambda x: x["score"], reverse=True)[:8]

    # Return structured data — the template handles rendering
    return [
        {
            "emoji": EMOJI_MAP.get(r["label"], "❓"),
            "label": r["label"],
            "pct": round(r["score"] * 100),
        }
        for r in active
    ]

with gr.Blocks(title="Emoji Mood Translator") as demo:
    gr.Markdown("## Emoji Mood Translator\nType anything and see its emotional fingerprint as emojis.")

    text_input = gr.Textbox(label="Type anything", lines=2,
                            placeholder="I can't believe how amazing this turned out!")
    btn = gr.Button("Analyze")

    result = gr.HTML(
        value=[],
        html_template="""
            {{#if value.length}}
                <div class="emoji-row">
                    {{#each value}}
                        <span class="emoji" title="{{this.label}}: {{this.pct}}%">{{this.emoji}}</span>
                    {{/each}}
                </div>
                <div class="bars">
                    {{#each value}}
                        <div class="bar-row">
                            <span class="bar-emoji">{{this.emoji}}</span>
                            <span class="bar-label">{{this.label}}</span>
                            <div class="bar-track">
                                <div class="bar-fill" style="width:{{this.pct}}%"></div>
                            </div>
                            <span class="bar-pct">{{this.pct}}%</span>
                        </div>
                    {{/each}}
                </div>
            {{else}}
                <p class="empty">Type something to see its emoji mood.</p>
            {{/if}}
        """,
        css_template="""
            .emoji-row {
                text-align: center; padding: 20px 0;
                letter-spacing: 12px; line-height: 1.6;
            }
            .emoji { font-size: 42px; cursor: default; }
            .emoji:hover { transform: scale(1.3); display: inline-block; }
            .bars { margin-top: 12px; }
            .bar-row {
                display: flex; align-items: center; gap: 8px;
                margin: 5px 0;
            }
            .bar-emoji { width: 24px; text-align: center; }
            .bar-label {
                width: 110px; font-size: 0.85em; color: #555;
            }
            .bar-track {
                flex: 1; background: #f0f0f0; border-radius: 4px;
                height: 18px; overflow: hidden;
            }
            .bar-fill {
                height: 100%; background: linear-gradient(90deg, #667eea, #764ba2);
                border-radius: 4px; transition: width 0.4s ease;
                min-width: 3px;
            }
            .bar-pct {
                width: 36px; font-size: 0.8em; color: #999;
                text-align: right;
            }
            .empty { color: #aaa; text-align: center; padding: 40px; }
        """
    )

    btn.click(fn=analyze, inputs=text_input, outputs=result)

    gr.Examples(
        examples=[
            ["I'm so proud of what we accomplished together!"],
            ["This is confusing and frustrating."],
            ["I wonder what would happen if we tried something different."],
        ],
        inputs=text_input
    )

demo.launch()
```

**What changed from Phase 3:**
- `analyze()` now returns a **list of dicts** (data), not an HTML string
- The `html_template` uses **Handlebars** (`{{#each}}`, `{{this.label}}`) to loop and render
- All styling lives in `css_template` — scoped, clean, no inline styles
- The template automatically re-renders when new data arrives

**Deploy.** Visually similar to Phase 3, but the architecture is cleaner. Data and presentation are separated.

---

## What You Learned

| Concept | Where |
|---------|-------|
| Lazy model loading (`get_classifier()`) | Phase 2+ |
| `pipeline("text-classification", top_k=None)` | Phase 2+ |
| Classic HTML string output | Phase 3 |
| `html_template` with Handlebars loops | Phase 4 |
| `css_template` for scoped CSS | Phase 4 |
| Data/presentation separation | Phase 3 vs Phase 4 |

## Memory Notes

- GoEmotions (roberta-base) is ~500MB in memory
- With torch + Gradio, total is ~1.5GB — fits comfortably in free Spaces
- Lazy loading prevents startup crashes from network issues
- `top_k=None` returns all 28 emotions; we filter in Python

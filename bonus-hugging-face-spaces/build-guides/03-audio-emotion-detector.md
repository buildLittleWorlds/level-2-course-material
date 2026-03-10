# Build Guide 03: Audio Emotion Detector

**Complexity:** Low-medium — single model, new modality (audio)
**Memory:** ~1.5GB (one wav2vec2-base model + torch)
**Gradio 6 concepts introduced:** `gr.Audio` input, CSS animations in `css_template`, basic `js_on_load`

---

## What This Space Does

Record your voice or upload an audio clip, and see what emotion the AI detects — happy, sad, angry, or neutral. Uses a speech emotion recognition model trained on the IEMOCAP dataset.

## Why It's Third

Same complexity as the Emoji Translator (one model, one input), but introduces a new modality: audio. You'll learn how `gr.Audio` works, how audio classification pipelines differ from text, and how to add CSS animations.

## requirements.txt

```
gradio==6.8.0
transformers==4.48.0
torch==2.5.0
librosa==0.10.2
```

> `librosa` handles audio loading and resampling. The wav2vec2 model expects 16kHz audio — librosa handles this conversion automatically when the transformers pipeline processes the file.

---

## Phase 1: Audio Input Hello World

Prove `gr.Audio` works. Accept audio, report back what you received.

```python
import gradio as gr

def analyze(audio_path):
    if audio_path is None:
        return "Record or upload audio first."
    return f"Got audio file: {audio_path}"

gr.Interface(
    fn=analyze,
    inputs=gr.Audio(sources=["upload", "microphone"], type="filepath",
                    label="Record or upload audio"),
    outputs="text",
    title="Audio Test"
).launch()
```

**Deploy.** Record yourself saying something, or upload a WAV/MP3. You should see the file path.

> **Note on `type="filepath"`:** Gradio saves uploaded audio to a temp file and gives you the path. The transformers pipeline can read this directly.

---

## Phase 2: Add the Emotion Model

Load a speech emotion recognition model. `superb/wav2vec2-base-superb-er` is a base-sized model (~360MB) that classifies speech into 4 emotions.

```python
import gradio as gr
from transformers import pipeline

_classifier = None
def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "audio-classification",
            model="superb/wav2vec2-base-superb-er"
        )
    return _classifier

# Map abbreviated labels to readable names
LABEL_MAP = {
    "neu": "Neutral", "hap": "Happy", "sad": "Sad", "ang": "Angry",
    "neutral": "Neutral", "happy": "Happy", "sad": "Sad", "angry": "Angry",
}

def analyze(audio_path):
    if audio_path is None:
        return "Record or upload audio first."

    results = get_classifier()(audio_path)
    lines = []
    for r in results:
        label = LABEL_MAP.get(r["label"], r["label"])
        lines.append(f"{label}: {r['score']:.1%}")
    return "\n".join(lines)

gr.Interface(
    fn=analyze,
    inputs=gr.Audio(sources=["upload", "microphone"], type="filepath",
                    label="Record or upload audio"),
    outputs="text",
    title="Audio Emotion Detector"
).launch()
```

**Deploy.** Record yourself saying "I'm so happy!" in an excited voice, or "This is terrible" in a flat voice. You should see 4 emotion scores.

**Testing tip:** Try different vocal tones with the same words. The model listens to *how* you say it (pitch, energy, pace), not *what* you say.

---

## Phase 3: HTML Emotion Bars

Replace text output with styled HTML bars.

```python
import gradio as gr
from transformers import pipeline

_classifier = None
def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "audio-classification",
            model="superb/wav2vec2-base-superb-er"
        )
    return _classifier

LABEL_MAP = {
    "neu": "Neutral", "hap": "Happy", "sad": "Sad", "ang": "Angry",
    "neutral": "Neutral", "happy": "Happy", "sad": "Sad", "angry": "Angry",
}

EMOTION_STYLE = {
    "Happy":  {"emoji": "😊", "color": "#f1c40f"},
    "Sad":    {"emoji": "😢", "color": "#3498db"},
    "Angry":  {"emoji": "😠", "color": "#e74c3c"},
    "Neutral":{"emoji": "😐", "color": "#95a5a6"},
}

def analyze(audio_path):
    if audio_path is None:
        return "<p style='color:#999; text-align:center; padding:30px;'>Record or upload audio to detect its emotion.</p>"

    results = get_classifier()(audio_path)

    # Find the top emotion
    top = max(results, key=lambda x: x["score"])
    top_label = LABEL_MAP.get(top["label"], top["label"])
    top_style = EMOTION_STYLE.get(top_label, {"emoji": "❓", "color": "#999"})

    # Build bars
    bars = []
    for r in sorted(results, key=lambda x: x["score"], reverse=True):
        label = LABEL_MAP.get(r["label"], r["label"])
        style = EMOTION_STYLE.get(label, {"emoji": "❓", "color": "#999"})
        pct = r["score"] * 100
        bars.append(f"""
        <div style="display:flex; align-items:center; gap:10px; margin:8px 0;">
            <span style="font-size:24px;">{style["emoji"]}</span>
            <span style="width:70px; font-weight:600;">{label}</span>
            <div style="flex:1; background:#f0f0f0; border-radius:6px; height:24px; overflow:hidden;">
                <div style="width:{pct}%; background:{style["color"]}; height:100%;
                            border-radius:6px; min-width:3px;"></div>
            </div>
            <span style="width:45px; text-align:right; color:#888;">{pct:.0f}%</span>
        </div>""")

    return f"""
    <div style="font-family:system-ui; max-width:500px;">
        <div style="text-align:center; padding:20px 0;">
            <span style="font-size:64px;">{top_style["emoji"]}</span>
            <div style="font-size:1.2em; font-weight:700; margin-top:8px;
                        color:{top_style["color"]};">{top_label}</div>
        </div>
        {"".join(bars)}
    </div>"""

gr.Interface(
    fn=analyze,
    inputs=gr.Audio(sources=["upload", "microphone"], type="filepath",
                    label="Record or upload audio"),
    outputs=gr.HTML(label="Detected Emotion"),
    title="Audio Emotion Detector"
).launch()
```

**Deploy.** Big emoji for the dominant emotion, colored bars for all four.

---

## Phase 4: Gradio 6 — CSS Animations + `js_on_load`

> **New Gradio 6 concept: `js_on_load`**
> A JavaScript string that runs once when the component mounts. You get access to `element` (the DOM node), `props` (including `props.value`), and `trigger()` to send events back to Python. Use it for hover effects, animations, or any client-side interactivity.

```python
import gradio as gr
from transformers import pipeline

_classifier = None
def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "audio-classification",
            model="superb/wav2vec2-base-superb-er"
        )
    return _classifier

LABEL_MAP = {
    "neu": "Neutral", "hap": "Happy", "sad": "Sad", "ang": "Angry",
    "neutral": "Neutral", "happy": "Happy", "sad": "Sad", "angry": "Angry",
}

EMOTION_STYLE = {
    "Happy":  {"emoji": "😊", "color": "#f1c40f"},
    "Sad":    {"emoji": "😢", "color": "#3498db"},
    "Angry":  {"emoji": "😠", "color": "#e74c3c"},
    "Neutral":{"emoji": "😐", "color": "#95a5a6"},
}

def analyze(audio_path):
    if audio_path is None:
        return None

    results = get_classifier()(audio_path)
    top = max(results, key=lambda x: x["score"])
    top_label = LABEL_MAP.get(top["label"], top["label"])
    top_style = EMOTION_STYLE.get(top_label, {"emoji": "❓", "color": "#999"})

    emotions = []
    for r in sorted(results, key=lambda x: x["score"], reverse=True):
        label = LABEL_MAP.get(r["label"], r["label"])
        style = EMOTION_STYLE.get(label, {"emoji": "❓", "color": "#999"})
        emotions.append({
            "label": label,
            "emoji": style["emoji"],
            "color": style["color"],
            "pct": round(r["score"] * 100),
        })

    return {
        "top_emoji": top_style["emoji"],
        "top_label": top_label,
        "top_color": top_style["color"],
        "emotions": emotions,
    }

with gr.Blocks(title="Audio Emotion Detector") as demo:
    gr.Markdown("## Audio Emotion Detector\nRecord your voice or upload a clip to detect its emotional tone.")

    audio_input = gr.Audio(sources=["upload", "microphone"], type="filepath",
                           label="Record or upload audio")

    result = gr.HTML(
        value=None,
        html_template="""
            {{#if value}}
                <div class="hero">
                    <span class="hero-emoji">{{value.top_emoji}}</span>
                    <div class="hero-label" style="color:{{value.top_color}}">{{value.top_label}}</div>
                </div>
                <div class="bars">
                    {{#each value.emotions}}
                        <div class="bar-row">
                            <span class="emo">{{this.emoji}}</span>
                            <span class="name">{{this.label}}</span>
                            <div class="track">
                                <div class="fill" style="--target-width:{{this.pct}}%; background:{{this.color}}"></div>
                            </div>
                            <span class="pct">{{this.pct}}%</span>
                        </div>
                    {{/each}}
                </div>
            {{else}}
                <p class="empty">Record or upload audio to detect its emotion.</p>
            {{/if}}
        """,
        css_template="""
            .hero { text-align: center; padding: 16px 0; }
            .hero-emoji { font-size: 64px; display: block; }
            .hero-label { font-size: 1.3em; font-weight: 700; margin-top: 6px; }
            .bars { margin-top: 12px; }
            .bar-row {
                display: flex; align-items: center; gap: 8px; margin: 6px 0;
                padding: 4px 0;
            }
            .bar-row:hover { background: #f8f8f8; border-radius: 6px; }
            .emo { width: 28px; font-size: 20px; text-align: center; }
            .name { width: 70px; font-weight: 600; font-size: 0.9em; }
            .track {
                flex: 1; background: #f0f0f0; border-radius: 6px;
                height: 22px; overflow: hidden;
            }
            .fill {
                height: 100%; border-radius: 6px; min-width: 3px;
                width: 0%;
                animation: grow 0.6s ease-out forwards;
            }
            @keyframes grow {
                to { width: var(--target-width); }
            }
            .pct { width: 40px; text-align: right; color: #888; font-size: 0.85em; }
            .empty { color: #aaa; text-align: center; padding: 40px; }
        """,
        js_on_load="""
            // Re-trigger bar animations whenever new results appear
            const observer = new MutationObserver(() => {
                element.querySelectorAll('.fill').forEach(bar => {
                    bar.style.animation = 'none';
                    bar.offsetHeight;  // force reflow
                    bar.style.animation = '';
                });
            });
            observer.observe(element, { childList: true, subtree: true });
        """
    )

    audio_input.change(fn=analyze, inputs=audio_input, outputs=result)

demo.launch()
```

**What's new in Phase 4:**
- **CSS animations:** The `@keyframes grow` animation makes bars slide out from zero to their target width. The `--target-width` CSS variable is set per-bar via inline style.
- **`js_on_load`:** The MutationObserver watches for DOM changes (new results) and re-triggers the animation by resetting it. This runs client-side — no round-trip to Python.
- **Structured data:** `analyze()` returns a dict (or `None` for empty state) with `top_emoji`, `top_label`, and `emotions` list. The template uses `{{#if value}}` to switch between the results view and the empty prompt.

---

## Where to Get Audio Samples

- **Record yourself:** The Gradio microphone input is the easiest. Try saying the same sentence ("Hello, how are you?") in different emotional tones.
- **Free samples:** The [RAVDESS dataset](https://zenodo.org/records/1188976) has Creative Commons–licensed emotional speech recordings from actors.
- **Tip:** The model responds to vocal characteristics (pitch, energy, pace, breathiness) more than word content. A flat "I'm happy" might register as neutral.

---

## What You Learned

| Concept | Where |
|---------|-------|
| `gr.Audio(sources=["upload", "microphone"])` | Phase 1+ |
| `pipeline("audio-classification")` | Phase 2+ |
| CSS `@keyframes` in `css_template` | Phase 4 |
| CSS variables (`--target-width`) for dynamic animation | Phase 4 |
| `js_on_load` with MutationObserver | Phase 4 |

## Memory Notes

- wav2vec2-base is ~360MB (smaller than most text models)
- `librosa` adds ~50MB for audio processing
- Total with torch: ~1.5GB — fits in free Spaces
- Lazy loading prevents startup crashes
- Audio files are small (a 10-second clip is ~300KB) so no upload size concerns

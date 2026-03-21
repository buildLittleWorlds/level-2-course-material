# Build Guide 01: Image Color Mood Analyzer

**Complexity:** Lowest — no ML model, just image processing
**Memory:** ~150MB (no torch, no transformers)
**Gradio 6 concepts introduced:** `gr.Image`, `gr.HTML`, `css_template` for scoped styling

---

## What This Space Does

Upload any image and get its dominant color palette with emotional associations based on color psychology. Warm reds suggest passion, cool blues suggest calm, bright yellows suggest joy.

## Why It's First

No transformer model. No torch. Just PIL and KMeans clustering. Instant startup, tiny memory, zero chance of model-loading errors. If this Space has problems, the issue is your HF account setup, not your code.

## requirements.txt

```
gradio==6.9.0
Pillow==11.1.0
scikit-learn==1.6.1
numpy==2.2.3
```

---

## Phase 1: Hello World

Prove Gradio works with an image input. Three lines.

```python
import gradio as gr

gr.Interface(
    fn=lambda img: f"Got a {img.size[0]}x{img.size[1]} image!",
    inputs=gr.Image(type="pil"),
    outputs="text"
).launch()
```

**Deploy this first.** Upload any image. You should see its dimensions. If this doesn't work, fix your Space setup before going further.

> **Why `type="pil"`?** By default, Gradio passes uploaded images as numpy arrays. A numpy array's `.size` is a single number (total pixels), not dimensions — so `img.size[0]` crashes. Setting `type="pil"` tells Gradio to pass a PIL Image instead, where `.size` gives you `(width, height)`.

---

## Phase 2: Extract Dominant Colors

Add KMeans clustering to find the 5 most common colors.

```python
import gradio as gr
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

def analyze(image):
    if image is None:
        return "Upload an image first."

    # Resize small for speed
    img = image.resize((100, 100)).convert("RGB")
    pixels = np.array(img).reshape(-1, 3).astype(float)

    # Filter out near-black and near-white (uninteresting)
    mask = (pixels.sum(axis=1) > 50) & (pixels.sum(axis=1) < 700)
    pixels = pixels[mask] if mask.sum() > 10 else pixels

    km = KMeans(n_clusters=5, n_init=10, random_state=42)
    km.fit(pixels)

    colors = km.cluster_centers_.astype(int)
    counts = np.bincount(km.labels_)
    order = counts.argsort()[::-1]

    lines = []
    for i in order:
        r, g, b = colors[i]
        pct = counts[i] / counts.sum() * 100
        lines.append(f"RGB({r}, {g}, {b}) — {pct:.0f}%")

    return "\n".join(lines)

gr.Interface(fn=analyze, inputs=gr.Image(type="pil"), outputs="text",
             title="Color Analyzer").launch()
```

**Deploy.** Upload a photo — you should see 5 dominant colors with percentages.

---

## Phase 3: Add Mood Mapping + HTML Output

Map colors to emotions using HSL color psychology, then output styled HTML.

```python
import gradio as gr
import numpy as np
import colorsys
from PIL import Image
from sklearn.cluster import KMeans

def color_to_mood(r, g, b):
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    hue = h * 360

    if s < 0.15:
        return "Neutral"

    if hue < 15 or hue >= 345:
        mood = "Passionate"
    elif hue < 45:
        mood = "Warm"
    elif hue < 75:
        mood = "Joyful"
    elif hue < 160:
        mood = "Harmonious"
    elif hue < 200:
        mood = "Tranquil"
    elif hue < 260:
        mood = "Calm"
    elif hue < 290:
        mood = "Mysterious"
    else:
        mood = "Romantic"

    if l < 0.25:
        mood = "Deep " + mood
    elif l > 0.75:
        mood = "Light " + mood
    return mood

def analyze(image):
    if image is None:
        return "<p>Upload an image to analyze its color mood.</p>"

    img = image.resize((100, 100)).convert("RGB")
    pixels = np.array(img).reshape(-1, 3).astype(float)
    mask = (pixels.sum(axis=1) > 50) & (pixels.sum(axis=1) < 700)
    pixels = pixels[mask] if mask.sum() > 10 else pixels

    km = KMeans(n_clusters=5, n_init=10, random_state=42)
    km.fit(pixels)
    colors = km.cluster_centers_.astype(int)
    counts = np.bincount(km.labels_)
    order = counts.argsort()[::-1]

    cards = []
    for i in order:
        r, g, b = colors[i]
        pct = counts[i] / counts.sum() * 100
        mood = color_to_mood(r, g, b)
        cards.append(f"""
        <div style="display:flex; align-items:center; gap:12px; margin:8px 0;">
            <div style="width:50px; height:50px; border-radius:8px;
                        background:rgb({r},{g},{b}); border:1px solid #ddd;"></div>
            <div>
                <div style="font-weight:600;">{mood}</div>
                <div style="color:#888; font-size:0.85em;">rgb({r},{g},{b}) — {pct:.0f}%</div>
            </div>
        </div>""")

    return f'<div style="font-family:system-ui;">{"".join(cards)}</div>'

gr.Interface(
    fn=analyze,
    inputs=gr.Image(type="pil", label="Upload an image"),
    outputs=gr.HTML(label="Color Mood"),
    title="Image Color Mood Analyzer"
).launch()
```

**Deploy.** Now you get colored swatches with mood labels. This is the classic Gradio approach — Python returns an HTML string with inline styles.

---

## Phase 4: Gradio 6 — `gr.Blocks` + `css_template`

> **New Gradio 6 concept: `css_template`**
> Instead of inline styles scattered through your HTML string, you define scoped CSS in `css_template`. The styles are automatically scoped to your component — they won't leak into the rest of the page. This keeps your HTML clean and your styles organized.

Switch to `gr.Blocks` for layout control and use `css_template` for polished, scoped styling.

```python
import gradio as gr
import numpy as np
import colorsys
from PIL import Image
from sklearn.cluster import KMeans

MOOD_TABLE = [
    (15,  "Passionate", "Fiery energy and intensity"),
    (45,  "Warm",       "Comfort and enthusiasm"),
    (75,  "Joyful",     "Optimism and brightness"),
    (160, "Harmonious", "Growth and balance"),
    (200, "Tranquil",   "Clarity and peace"),
    (260, "Calm",       "Depth and trust"),
    (290, "Mysterious", "Intrigue and spirituality"),
    (345, "Romantic",   "Tenderness and playfulness"),
    (361, "Passionate", "Fiery energy and intensity"),
]

def color_to_mood(r, g, b):
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    hue = h * 360
    if s < 0.15:
        return ("Neutral", "Understated and balanced")
    for threshold, mood, desc in MOOD_TABLE:
        if hue < threshold:
            if l < 0.25:
                mood = "Deep " + mood
            elif l > 0.75:
                mood = "Light " + mood
            return (mood, desc)
    return ("Neutral", "Balanced tone")

def analyze(image):
    if image is None:
        return "<p class='empty'>Upload an image to see its emotional color palette.</p>"

    img = image.resize((100, 100)).convert("RGB")
    pixels = np.array(img).reshape(-1, 3).astype(float)
    mask = (pixels.sum(axis=1) > 50) & (pixels.sum(axis=1) < 700)
    pixels = pixels[mask] if mask.sum() > 10 else pixels

    km = KMeans(n_clusters=5, n_init=10, random_state=42)
    km.fit(pixels)
    colors = km.cluster_centers_.astype(int)
    counts = np.bincount(km.labels_)
    order = counts.argsort()[::-1]

    # Palette bar (proportional color strips)
    bar = []
    for i in order:
        r, g, b = colors[i]
        pct = counts[i] / counts.sum() * 100
        bar.append(f'<div class="seg" style="width:{pct}%;background:rgb({r},{g},{b})"></div>')

    # Color cards
    cards = []
    for i in order:
        r, g, b = colors[i]
        pct = counts[i] / counts.sum() * 100
        mood, desc = color_to_mood(r, g, b)
        cards.append(f"""
        <div class="card">
            <div class="swatch" style="background:rgb({r},{g},{b})"></div>
            <div class="info">
                <div class="mood">{mood}</div>
                <div class="desc">{desc}</div>
                <div class="meta">rgb({r},{g},{b}) · {pct:.0f}%</div>
            </div>
        </div>""")

    return f"""
    <div class="bar">{"".join(bar)}</div>
    <div class="cards">{"".join(cards)}</div>
    """

with gr.Blocks(title="Image Color Mood Analyzer") as demo:
    gr.Markdown("## Image Color Mood Analyzer\nUpload any image to reveal its emotional color palette.")

    with gr.Row():
        img_input = gr.Image(type="pil", label="Upload an image")
        result = gr.HTML(
            value="<p class='empty'>Your color mood palette will appear here.</p>",
            css_template="""
                .bar {
                    display: flex; height: 28px; border-radius: 8px;
                    overflow: hidden; margin-bottom: 16px;
                    border: 1px solid #e0e0e0;
                }
                .seg { min-width: 4px; }
                .cards { display: flex; flex-direction: column; gap: 8px; }
                .card {
                    display: flex; align-items: center; gap: 14px;
                    padding: 10px 14px; border-radius: 10px;
                    background: #fafafa; border: 1px solid #eee;
                }
                .swatch {
                    width: 48px; height: 48px; border-radius: 8px;
                    border: 1px solid rgba(0,0,0,0.08); flex-shrink: 0;
                }
                .mood { font-weight: 700; font-size: 1.05em; }
                .desc { color: #666; font-size: 0.85em; margin-top: 2px; }
                .meta { color: #aaa; font-size: 0.78em; margin-top: 3px; font-family: monospace; }
                .empty { color: #999; text-align: center; padding: 40px 20px; }
            """
        )

    img_input.change(fn=analyze, inputs=img_input, outputs=result)

demo.launch()
```

**Deploy.** The output now has:
- A proportional palette bar across the top
- Clean cards with scoped CSS (no inline styles cluttering the HTML)
- Styles that won't interfere with the rest of the Gradio page

---

## What You Learned

| Concept | Where |
|---------|-------|
| `gr.Interface` (simplest Gradio app) | Phase 1-3 |
| `gr.Image(type="pil")` | Phase 2+ |
| `gr.HTML` with returned HTML strings | Phase 3 |
| `gr.Blocks` for layout control | Phase 4 |
| `css_template` for scoped CSS (Gradio 6) | Phase 4 |

## Memory Notes

This Space uses **no ML model**, so memory is never a concern:
- PIL + scikit-learn + numpy total ~150MB
- No torch, no transformers — starts in seconds
- If this Space crashes, the problem is your HF account, not your code
- Use this as your baseline: if this works, your environment is healthy

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

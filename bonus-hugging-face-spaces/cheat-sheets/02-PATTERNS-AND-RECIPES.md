# Gradio `gr.HTML` Patterns & Recipes

## Pattern 1: Dynamic Visualization (No JS Framework Needed)

Use `html_template` with JavaScript template literals to generate SVG or styled HTML from data.

```python
gr.HTML(
    value={"joy": 0.8, "sadness": 0.1, "anger": 0.05, "neutral": 0.05},
    html_template="""
        <div class="bars">
        ${Object.entries(value).map(([k,v]) => `
            <div class="bar-row">
                <span class="label">${k}</span>
                <div class="bar" style="width:${v*100}%">${(v*100).toFixed(0)}%</div>
            </div>
        `).join('')}
        </div>
    """,
    css_template="""
        .bar-row { display: flex; align-items: center; margin: 4px 0; }
        .label { width: 80px; font-weight: bold; }
        .bar { background: #3b82f6; color: white; padding: 4px 8px;
               border-radius: 4px; min-width: 30px; transition: width 0.3s; }
    """
)
```

**Why this matters for our Spaces:** Every sentiment result can be visualized as colored bars, radar charts, or gauges without importing matplotlib or plotly.

## Pattern 2: Color-Coding Text by Sentiment

Break text into segments and color each one based on model output.

```python
# In your Python function, return a list of (text, color) tuples:
def colorize(text, results):
    segments = []
    for sent, result in zip(sentences, results):
        color = {"joy": "#fef3c7", "sadness": "#dbeafe", "anger": "#fee2e2"}
        segments.append({"text": sent, "bg": color.get(result["label"], "#f3f4f6")})
    return segments

gr.HTML(
    value=[],
    html_template="""
        <div class="colored-text">
        ${value.map(seg => `<span style="background:${seg.bg}; padding:2px 4px; border-radius:3px;">${seg.text}</span> `).join('')}
        </div>
    """
)
```

## Pattern 3: Interactive Click-to-Select (with `js_on_load`)

Let users click on elements to make selections, then send the result to Python.

```python
gr.HTML(
    value=None,
    emotions=["joy","sadness","anger","fear","surprise","disgust","neutral"],
    html_template="""
        <div class="grid">
        ${emotions.map(e => `<button class="emotion-btn" data-emotion="${e}">${e}</button>`).join('')}
        </div>
        <p>Selected: <strong>${value || 'none'}</strong></p>
    """,
    css_template="""
        .grid { display: flex; flex-wrap: wrap; gap: 8px; }
        .emotion-btn { padding: 8px 16px; border: 2px solid #ddd; border-radius: 8px;
                       cursor: pointer; font-size: 14px; }
        .emotion-btn:hover { border-color: #3b82f6; }
    """,
    js_on_load="""
        element.addEventListener('click', (e) => {
            if (e.target.matches('.emotion-btn')) {
                props.value = e.target.dataset.emotion;
                trigger('change');
            }
        });
    """
)
```

## Pattern 4: Animated Score Gauge

A circular gauge that fills based on a 0–1 score.

```python
gr.HTML(
    value=0.75,
    html_template="""
        <div class="gauge-container">
            <svg viewBox="0 0 100 50" class="gauge">
                <path d="M 10 45 A 35 35 0 0 1 90 45" fill="none" stroke="#e5e7eb" stroke-width="8"/>
                <path d="M 10 45 A 35 35 0 0 1 90 45" fill="none" stroke="#3b82f6" stroke-width="8"
                      stroke-dasharray="${value * 110} 110"/>
            </svg>
            <div class="score">${(value * 100).toFixed(0)}%</div>
        </div>
    """,
    css_template="""
        .gauge-container { text-align: center; width: 200px; }
        .gauge { width: 100%; }
        .score { font-size: 24px; font-weight: bold; margin-top: -20px; }
    """
)
```

## Pattern 5: Card Grid Layout

Display multiple results as a grid of cards.

```python
gr.HTML(
    value=[
        {"model": "VADER", "label": "POS", "score": 0.87},
        {"model": "Binary", "label": "POSITIVE", "score": 0.99},
        {"model": "Emotion", "label": "joy", "score": 0.72},
    ],
    html_template="""
        <div class="card-grid">
        ${value.map(r => `
            <div class="card">
                <div class="model-name">${r.model}</div>
                <div class="result-label">${r.label}</div>
                <div class="result-score">${(r.score*100).toFixed(0)}%</div>
            </div>
        `).join('')}
        </div>
    """,
    css_template="""
        .card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; }
        .card { background: white; border: 1px solid #e5e7eb; border-radius: 12px;
                padding: 16px; text-align: center; }
        .model-name { font-size: 12px; color: #6b7280; text-transform: uppercase; }
        .result-label { font-size: 20px; font-weight: bold; margin: 8px 0; }
        .result-score { font-size: 14px; color: #3b82f6; }
    """
)
```

## Pattern 6: Server Functions for On-Demand Analysis

Run Python model inference from a button click without a full Gradio event round-trip.

```python
from transformers import pipeline
clf = pipeline("sentiment-analysis", model="...", device=-1)

def analyze_text(text):
    result = clf(text)[0]
    return {"label": result["label"], "score": round(result["score"], 4)}

gr.HTML(
    value="",
    html_template="""
        <input type="text" id="input" placeholder="Type something..." />
        <button id="go">Analyze</button>
        <div id="result"></div>
    """,
    js_on_load="""
        const input = element.querySelector('#input');
        const btn = element.querySelector('#go');
        const result = element.querySelector('#result');
        btn.addEventListener('click', async () => {
            result.textContent = 'Analyzing...';
            const res = await server.analyze_text(input.value);
            result.textContent = res.label + ' (' + (res.score * 100).toFixed(1) + '%)';
        });
    """,
    server_functions=[analyze_text]
)
```

## Pattern 7: Combining Traditional Gradio + gr.HTML

You don't have to go all-in on `gr.HTML`. Mix standard components with custom HTML output:

```python
with gr.Blocks() as demo:
    text_input = gr.Textbox(label="Enter text")
    analyze_btn = gr.Button("Analyze")

    # Standard Gradio input, custom HTML output
    result_display = gr.HTML(
        value=None,
        html_template="""
            ${value ? `<div class="result">${value.label}: ${value.score}</div>` : '<p>Enter text above</p>'}
        """
    )

    analyze_btn.click(fn=my_analysis_fn, inputs=text_input, outputs=result_display)
```

**This is the recommended pattern for our Spaces:** Use standard `gr.Textbox` and `gr.Button` for inputs, and `gr.HTML` for rich custom output displays.

## Sources

- [Gradio Custom HTML Components Guide](https://gradio.app/guides/custom-HTML-components)
- [One-Shot Any Web App with Gradio's gr.HTML](https://huggingface.co/blog/gradio-html-one-shot-apps)

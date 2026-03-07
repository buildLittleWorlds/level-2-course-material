# Gradio 6 `gr.HTML` vs. Classic Gradio: When to Use What

## The Decision Framework

When building a Hugging Face Space, you now have two approaches for displaying results:

| | Classic Gradio Components | Gradio 6 `gr.HTML` |
|---|---|---|
| **Use when** | Standard inputs/outputs are sufficient | You need custom visual design |
| **Learning curve** | Low — just wire Python functions | Medium — need HTML/CSS/JS basics |
| **Interactivity** | Built-in (sliders, buttons, etc.) | Custom (write your own JS) |
| **Styling control** | Limited to themes | Complete control |
| **Best for students** | First Spaces, learning the pipeline | After they understand the basics |

## The Hybrid Approach (Recommended for Our Spaces)

**Use classic Gradio for inputs, `gr.HTML` for outputs.**

This gives students familiar input controls while letting you create visually impressive result displays.

```python
import gradio as gr

with gr.Blocks() as demo:
    # CLASSIC: Standard input components
    text = gr.Textbox(label="Enter text to analyze", lines=3)
    btn = gr.Button("Analyze", variant="primary")

    # CUSTOM: Rich HTML output
    output = gr.HTML(
        value=None,
        html_template="""...""",  # your custom visualization
        css_template="""..."""
    )

    # Wire them together normally
    btn.click(fn=analyze, inputs=text, outputs=output)

demo.launch()
```

## What Classic Gradio Components Can't Do (That `gr.HTML` Can)

1. **Color-coded text rendering** — `gr.HighlightedText` exists but is limited; `gr.HTML` gives you full control over colors, fonts, layout
2. **Custom animations** — CSS transitions and keyframes for score reveals, gauge fills, etc.
3. **Side-by-side card layouts** — CSS Grid / Flexbox for comparing multiple model outputs
4. **Interactive elements without Python round-trips** — Click-to-select, hover effects, expand/collapse via pure JS
5. **Emoji rendering with custom sizing** — Full control over how emojis display
6. **SVG-based charts** — Lightweight inline visualizations without matplotlib

## What `gr.HTML` Can't Do (Where Classic Components Win)

1. **File uploads** — Use `gr.File` or `gr.UploadButton` (though `gr.HTML` can do this with `upload()` in `js_on_load`, it's harder)
2. **Built-in accessibility** — Classic components have ARIA labels, keyboard nav, etc.
3. **Gradio API compatibility** — Classic components work automatically with the Gradio API/MCP; `gr.HTML` needs `api_info()` defined
4. **Zero JS knowledge required** — Classic components need only Python

## Mapping Our Five Spaces to the Spectrum

| Space | Inputs | Outputs | Why |
|-------|--------|---------|-----|
| Sentiment Battle Arena | `gr.Textbox` | `gr.HTML` cards | Need custom side-by-side card layout |
| Story Emotion Arc | `gr.Textbox` (multiline) | `gr.Plot` or `gr.HTML` SVG | Could go either way; `gr.Plot` is simpler |
| Emoji Mood Translator | `gr.Textbox` | `gr.HTML` with emojis | Need custom emoji sizing and layout |
| Review Star Guesser | `gr.HTML` buttons | `gr.HTML` reveal | Need game state and interactive clicking |
| Headline Dashboard | `gr.Textbox` (multiline) | `gr.HTML` bars or `gr.Plot` | Custom bars look better in HTML |

## `gr.HTML` Requirements Checklist

Before using `gr.HTML`, make sure the Space needs at least one of:

- [ ] Custom visual layout (cards, grids, non-standard arrangements)
- [ ] Color-coding or conditional styling based on data
- [ ] Client-side interactivity (clicks, hovers) that don't need Python
- [ ] Animations or transitions
- [ ] Inline SVG or canvas-based visualizations
- [ ] Rich emoji or icon rendering

If none of these apply, stick with classic Gradio components — they're simpler and more maintainable.

## Gradio 6 Compatibility Note

The `html_template`, `css_template`, `js_on_load`, and `server_functions` parameters require **Gradio 6+**. Make sure your `requirements.txt` specifies:

```
gradio>=6.0
```

On Hugging Face Spaces, you can set the Gradio version in the Space's `README.md` metadata or `requirements.txt`.

## Sources

- [Gradio Custom HTML Components Guide](https://gradio.app/guides/custom-HTML-components)
- [Gradio HTML Component Docs](https://gradio.app/docs/gradio/html)
- [One-Shot Any Web App with Gradio's gr.HTML](https://huggingface.co/blog/gradio-html-one-shot-apps)

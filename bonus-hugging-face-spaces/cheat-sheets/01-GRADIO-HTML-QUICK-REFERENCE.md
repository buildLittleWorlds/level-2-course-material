# Gradio `gr.HTML` Quick Reference

## What Changed in Gradio 6

`gr.HTML` is no longer just a static display component. It now supports **templates**, **scoped CSS**, **JavaScript interactivity**, and **server function calls** — meaning you can build complete custom interactive components in a single Python file with no build step.

## The Four Key Parameters

### 1. `html_template` — Your HTML Structure

A string of HTML that gets rendered. Supports two templating syntaxes:

```python
# JavaScript template literals: ${expression}
gr.HTML(value="world", html_template="<h1>Hello, ${value}!</h1>")

# Handlebars: {{value}} and {{#each}}, {{#if}}
gr.HTML(value=["a","b","c"], html_template="""
    <ul>
      {{#each value}}
        <li>{{this}}</li>
      {{/each}}
    </ul>
""")
```

**When to use which:**
- `${}` — for JavaScript logic (Array.from, ternary operators, .map(), .join())
- `{{}}` — for loops and conditionals ({{#each}}, {{#if}})

### 2. `css_template` — Scoped Styles

CSS that is **automatically scoped** to your component. Rules outside a block target the root element.

```python
gr.HTML(
    value="Hello",
    html_template="<div class='card'><p>${value}</p></div>",
    css_template="""
        .card {
            background: #f0f0f0;
            padding: 20px;
            border-radius: 12px;
        }
        .card p { color: #333; font-size: 18px; }
    """
)
```

**Key detail:** `css_template` also supports `${}` for dynamic values:
```python
css_template="img { height: ${size}px; }"
```

### 3. `js_on_load` — JavaScript Interactivity

JavaScript that runs when the component loads. Has access to:

| Variable | What it does |
|----------|-------------|
| `element` | The DOM element of this component |
| `props` | All component props; set `props.value = x` to update and re-render |
| `trigger(name)` | Fire a Gradio event (e.g. `trigger('submit')`, `trigger('click')`) |
| `trigger(name, data)` | Fire event with data: `trigger('click', {index: 3})` |
| `upload(file)` | Upload a JS File object; returns `{path, url}` |
| `server` | Object with async methods for each `server_functions` entry |

```python
gr.HTML(
    value=0,
    html_template="<button id='btn'>Clicked ${value} times</button>",
    js_on_load="""
        element.querySelector('#btn').addEventListener('click', () => {
            props.value = props.value + 1;
        });
    """
)
```

**Critical rule:** Event listeners in `js_on_load` attach **once** at load time. For dynamically created elements, use event delegation:
```javascript
element.addEventListener('click', (e) => {
    if (e.target && e.target.matches('.dynamic-item')) {
        props.value = e.target.dataset.value;
    }
});
```

### 4. `server_functions` — Call Python from JavaScript

Pass Python functions that become async methods on the `server` object in `js_on_load`:

```python
def analyze(text):
    return {"score": 0.95, "label": "positive"}

gr.HTML(
    html_template="...",
    js_on_load="""
        const btn = element.querySelector('#go');
        btn.addEventListener('click', async () => {
            const result = await server.analyze(props.value);
            // use result...
        });
    """,
    server_functions=[analyze]
)
```

## Extra Props

Pass any keyword argument beyond the standard ones, and it becomes available in templates:

```python
gr.HTML(
    value=3,
    max_stars=5,        # custom prop
    color="gold",       # custom prop
    html_template="<div>Rating: ${value}/${max_stars}</div>",
    css_template=".star { color: ${color}; }"
)
```

Update extra props from event listeners:
```python
slider.change(fn=lambda x: gr.HTML(size=x), inputs=slider, outputs=html_component)
```

## `@children` — Embed Gradio Components Inside HTML

Use `@children` as a placeholder in `html_template` to nest standard Gradio components inside custom HTML:

```python
with gr.HTML(html_template="""
    <div class="custom-card">
        <h2>My Form</h2>
        @children
    </div>
""", css_template="...") as card:
    name = gr.Textbox(label="Name")
    email = gr.Textbox(label="Email")
```

**Constraint:** `@children` must be at the top level of the template (not nested inside other HTML tags).

## Reusable Component Classes

Subclass `gr.HTML` to create reusable components:

```python
class EmotionBadge(gr.HTML):
    def __init__(self, value="neutral", **kwargs):
        super().__init__(
            value=value,
            html_template="""<span class='badge ${value}'>${value}</span>""",
            css_template="""
                .badge { padding: 4px 12px; border-radius: 12px; font-weight: bold; }
                .joy { background: #fef3c7; color: #92400e; }
                .sadness { background: #dbeafe; color: #1e40af; }
                .anger { background: #fee2e2; color: #991b1b; }
            """,
            **kwargs
        )
```

## Other Useful Parameters

| Parameter | Default | Purpose |
|-----------|---------|---------|
| `apply_default_css` | `True` | Set `False` to remove Gradio's default theme styles |
| `container` | `False` | Set `True` to wrap in a standard Gradio container |
| `padding` | `False` | Set `True` to add standard Gradio padding |
| `min_height` | `None` | Minimum height in pixels |
| `max_height` | `None` | Maximum height with scroll |
| `autoscroll` | `False` | Auto-scroll to bottom on content change |

## Sources

- [Gradio Custom HTML Components Guide](https://gradio.app/guides/custom-HTML-components)
- [Gradio HTML Component Docs](https://gradio.app/docs/gradio/html)
- [One-Shot Any Web App with Gradio's gr.HTML](https://huggingface.co/blog/gradio-html-one-shot-apps)

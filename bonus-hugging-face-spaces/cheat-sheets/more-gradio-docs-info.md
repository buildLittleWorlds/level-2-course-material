Here is a comprehensive specification and detailed technical guide for building Hugging Face Spaces using the new **Gradio 6 HTML/One-Shot Apps functionality**.

This document is structured to serve as both a conceptual reference and a practical "copy-paste" repository for building highly interactive, custom web components within a single Python file.

---

# 🚀 The Gradio 6 HTML Specification: Building One-Shot Web Apps

Gradio 6 introduced a major upgrade to the `gr.HTML` component. It is no longer just for displaying static markup; it is now a fully-fledged engine for creating custom, interactive frontend components with scoped CSS, templating, JavaScript interactivity, and seamless two-way state binding with Python—all without needing a separate frontend build step (like React or Vue).

Because everything is contained in a single Python file, this architecture is perfect for **"Vibe Coding"**—generating complete web apps in one shot using LLMs and deploying them instantly to Hugging Face Spaces.

---

## 1. The Core Anatomy of `gr.HTML`

The new `gr.HTML` takes three primary templates to define the structure, style, and behavior of your component:

```python
import gradio as gr

my_component = gr.HTML(
    value={"count": 0},  # The initial state/data
    html_template="""...""", # HTML structure with template tags
    css_template="""...""",  # Scoped CSS styles
    js_on_load="""...""",    # JavaScript executed on mount
    apply_default_css=False  # Optional: disable default Gradio styling
)

```

### 1.1 `html_template` (Structure)

Supports two types of templating syntax, which can be mixed:

* **JavaScript Expressions (`${...}`)**: Used for executing arbitrary JS, injecting props, or evaluating logic directly. Example: `<p>${value.length} items</p>`
* **Handlebars (`{{...}}`)**: Best for structured logic like loops and conditionals. Example: `{{#each value}} <li>{{this}}</li> {{/each}}`

### 1.2 `css_template` (Styling)

CSS provided here is **automatically scoped** to the component. You don't need to worry about polluting the rest of your Gradio app's CSS. Rules written outside a specific block target the component's root wrapper element. You can also inject dynamic CSS using `${}` notation.

### 1.3 `js_on_load` (Interactivity)

A string of JavaScript that runs exactly once when the component mounts. This script operates within a specific scope that provides several powerful variables:

* `element`: Refers to the root HTML element of the component (use `element.querySelector` to find children).
* `props`: An object containing all properties passed to the component, including `props.value`. **Updating a prop (e.g., `props.value = new_val`) automatically re-renders the HTML template.**
* `trigger('event_name', payload)`: A function to dispatch events from JavaScript to Gradio Python event listeners.
* `server`: An object containing async representations of any Python functions passed to the `server_functions` argument.
* `upload(file)`: An async function to upload File objects to the Gradio server.

---

## 2. Copy-Paste Boilerplates

Below are modular templates you can drop directly into your Hugging Face Space `app.py` files.

### Boilerplate A: Basic Two-Way State Binding (Counter)

This shows how to update state from JS and trigger a Gradio Python function.

```python
import gradio as gr

with gr.Blocks() as demo:
    counter = gr.HTML(
        value=0,
        html_template="""
            <div class="container">
                <h2>Count: ${value}</h2>
                <button id="increment-btn">+1</button>
            </div>
        """,
        css_template="""
            .container { padding: 20px; border: 2px solid #ccc; border-radius: 8px; text-align: center; }
            button { background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
            button:hover { background: #0056b3; }
        """,
        js_on_load="""
            const btn = element.querySelector('#increment-btn');
            btn.addEventListener('click', () => {
                // Update local state (triggers re-render automatically)
                props.value = props.value + 1;
                // Notify Python backend (triggers Gradio .change listener)
                trigger('change'); 
            });
        """
    )
    
    # Python can listen to the change event
    output_text = gr.Textbox(label="Python Backend Log")
    counter.change(fn=lambda val: f"Python received: {val}", inputs=counter, outputs=output_text)

demo.launch()

```

### Boilerplate B: Custom Triggers and EventData

Instead of just relying on the built-in `.change()` or `.click()`, you can create custom triggers that pass complex JSON payloads back to Python.

```python
import gradio as gr

with gr.Blocks() as demo:
    interactive_list = gr.HTML(
        value=["Apple", "Banana", "Cherry"],
        html_template="""
            <ul>
                {{#each value}}
                    <li data-item="{{this}}" class="list-item">Click me: {{this}}</li>
                {{/each}}
            </ul>
        """,
        css_template="""
            .list-item { cursor: pointer; padding: 8px; margin: 4px; background: #eee; border-radius: 4px; }
            .list-item:hover { background: #ddd; }
        """,
        js_on_load="""
            // Attach listener to parent for event delegation (best practice for templated lists)
            element.addEventListener('click', (e) => {
                if (e.target && e.target.matches('.list-item')) {
                    const clickedItem = e.target.dataset.item;
                    // Trigger a custom event named 'item_clicked' with a payload
                    trigger('item_clicked', { item: clickedItem, timestamp: Date.now() });
                }
            });
        """
    )

    selection_output = gr.JSON(label="Clicked Data")

    # Handle the custom trigger in Python using gr.EventData
    def handle_click(evt: gr.EventData):
        # evt._data contains the JS object payload
        return {"selected": evt._data["item"], "time": evt._data["timestamp"]}

    interactive_list.event(fn=handle_click, inputs=[], outputs=[selection_output])

demo.launch()

```

---

## 3. Advanced Integrations

### 3.1 Server Functions (Calling Python Directly from JS)

Sometimes you don't want to rely on Gradio's standard event queue; you just want to query the backend asynchronously from your frontend script. You can pass Python functions to the `server_functions` parameter.

```python
import gradio as gr
import os

def list_files(path):
    try:
        return os.listdir(path)
    except Exception as e:
        return [str(e)]

with gr.Blocks() as demo:
    file_explorer = gr.HTML(
        value=".",  # Start directory
        server_functions=[list_files], # Register Python function
        html_template="""
            <div>
                <input type="text" id="path-input" value="${value}" />
                <button id="load-btn">Load</button>
                <ul id="file-list"></ul>
            </div>
        """,
        js_on_load="""
            const btn = element.querySelector('#load-btn');
            const input = element.querySelector('#path-input');
            const list = element.querySelector('#file-list');

            btn.addEventListener('click', async () => {
                list.innerHTML = '<li>Loading...</li>';
                // Call the Python function as an async JS method!
                const files = await server.list_files(input.value);
                
                list.innerHTML = '';
                files.forEach(file => {
                    const li = document.createElement('li');
                    li.textContent = file;
                    list.appendChild(li);
                });
            });
        """
    )

demo.launch()

```

### 3.2 HTML Children (Nesting standard Gradio Components)

You can use your custom HTML as a wrapper/layout engine for standard Gradio components by using the `@children` placeholder.
*Note: `@children` must be at the top level of the `html_template` and cannot be nested inside inner HTML tags. You must style the parent container via CSS to layout the children.*

```python
import gradio as gr

with gr.Blocks() as demo:
    with gr.HTML(
        html_template="""
            <div class="custom-card">
                <h2>Custom AI Form Wrapper</h2>
                @children
            </div>
        """,
        css_template="""
            /* Target the component's root to style the @children wrapper */
            border: 2px solid purple; 
            border-radius: 12px;
            padding: 20px;
            background: #f9f9f9;
            
            h2 { color: purple; margin-top: 0; }
        """
    ):
        # These standard Gradio components will be injected at @children
        text_in = gr.Textbox(label="Input")
        btn = gr.Button("Submit")
        text_out = gr.Textbox(label="Output")
        btn.click(lambda x: x.upper(), text_in, text_out)

demo.launch()

```

### 3.3 Reusable Subclasses (Creating a Python Library of Components)

If you want to create a clean API for yourself or others, wrap `gr.HTML` in a custom Python class. This allows you to hide the HTML/CSS/JS strings and expose a clean Python interface.

To support APIs or MCP (Model Context Protocol), you should define the data format using a Pydantic model (`GradioModel` or `GradioRootModel`).

```python
import gradio as gr
from gradio.data_classes import GradioModel
from typing import List

# 1. Define the API Data Model
class KanbanData(GradioModel):
    todo: List[str]
    done: List[str]

# 2. Subclass gr.HTML
class KanbanBoard(gr.HTML):
    data_model = KanbanData  # Ensures API/MCP compatibility

    def __init__(self, value=None, theme_color="#333", **kwargs):
        html_template = """
            <div class="board" style="--theme: ${theme_color}">
                <div class="column">
                    <h3>To Do</h3>
                    {{#each value.todo}} <div class="card">{{this}}</div> {{/each}}
                </div>
                <div class="column">
                    <h3>Done</h3>
                    {{#each value.done}} <div class="card">{{this}}</div> {{/each}}
                </div>
            </div>
        """
        
        css_template = """
            .board { display: flex; gap: 20px; }
            .column { flex: 1; padding: 10px; background: #f0f0f0; border-radius: 8px; }
            h3 { color: var(--theme); }
            .card { background: white; padding: 10px; margin-bottom: 8px; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        """
        
        # Pass **kwargs to ensure Gradio's internal props (like 'render') are handled
        super().__init__(
            value=value or {"todo": [], "done": []},
            theme_color=theme_color,
            html_template=html_template,
            css_template=css_template,
            **kwargs
        )

# 3. Use it exactly like a built-in component!
with gr.Blocks() as demo:
    board = KanbanBoard(
        value={"todo": ["Build app", "Write docs"], "done": ["Read Gradio updates"]},
        theme_color="#008080"
    )

demo.launch()

```

---

## 4. Key Rules and Best Practices for AI/LLM Prompting

If you are using an LLM (like Claude or Gemini) to generate these components for you, include these strict rules in your prompt:

1. **Single File Output:** Ensure the LLM outputs exactly one Python script. No separate HTML/CSS/JS files. Everything goes into `gr.HTML()` strings.
2. **Event Delegation:** Tell the LLM to use event delegation in `js_on_load` for dynamic content. (e.g., attach listeners to `element`, not to individual dynamically generated `<li>` tags).
3. **Props Updating:** Remind the LLM that changing `props.value = newValue` automatically updates the UI. There is no need for manual DOM manipulation (like `element.innerHTML = ...`) if `html_template` Handlebars logic handles it.
4. **Trigger Sync:** Instruct the LLM to call `trigger('change')` or `trigger('custom_event', payload)` when Python needs to be informed of state changes.
5. **Security Check:** Avoid passing untrusted user input directly into `html_template` tags without sanitization if the app will be public, as raw HTML injection can lead to XSS.
This file was changed

# Writing in Markdown

What it is, why it matters, and the formatting you need to know for your research journal.

## What Is Markdown?

Markdown is a lightweight way to format plain text. You write in a regular text file using simple symbols — `#` for headings, `**` for bold, `-` for bullet points — and any Markdown-aware tool renders it into clean, readable formatting.

John Gruber created Markdown in 2004 with a simple goal: let people write for the web without learning HTML. The idea was that the raw text should be just as readable as the formatted version. Two decades later, Markdown has become far more than a blogging shortcut. It's the default writing format across most of the tools you'll encounter in technical and creative work.

## Why Markdown Is Everywhere Now

Three developments made Markdown ubiquitous.

**GitHub adopted it as its native language.** Every README file on GitHub is written in Markdown. Every issue, pull request comment, and wiki page uses Markdown. When you look at a project on GitHub and see nicely formatted documentation with headings, code blocks, and links — that's Markdown being rendered. Your research journal lives in a GitHub repository, which means it's a `.md` file that GitHub will automatically display as a formatted document.

**AI tools speak Markdown natively.** When you interact with ChatGPT, Claude, Gemini, or any other LLM, the responses come back formatted in Markdown. Those bold headings, numbered lists, and code blocks you see in AI output? That's Markdown. When you write prompts that include structured formatting, you're writing Markdown whether you realize it or not. Understanding Markdown means you understand the formatting language that LLMs use to communicate with you — and that you can use to communicate more effectively with them.

**Documentation moved to plain text.** Across software development, data science, and increasingly in publishing and academia, people write in Markdown because it's portable. A `.md` file works everywhere. It doesn't require Microsoft Word or Google Docs. It doesn't break when you open it on a different computer. It versions cleanly in Git, which means you can track every change you've ever made. It converts easily to HTML, PDF, slides, or almost any other format.

The practical upshot: if you're going to work with AI tools, contribute to open-source projects, write technical documentation, or publish on platforms like GitHub, Notion, Obsidian, or Substack — you're going to write in Markdown.

## Markdown for Your Research Journal

Your research journal is a file called `research-journal.md` that lives in your GitHub repository. You'll write it in Markdown using the weekly template from the Research Journal guide.

Here's what that means in practice: you open a plain text file, you type using the formatting symbols described below, and when you push your file to GitHub, it renders into a clean, readable document that anyone can view in a browser.

You don't need a special editor. You can write Markdown in any text editor — VS Code, Notepad, TextEdit, or directly in GitHub's browser editor. What matters is that you know the handful of formatting conventions that make your journal readable.

## The Six Things You Need to Know

These six formatting elements cover everything you'll need for your research journal and most other Markdown writing.

### 1. Headings

Use `#` symbols at the start of a line. More `#` signs mean smaller headings.

```markdown
# Main Title
## Section Heading
### Subsection
```

In your journal, each weekly entry starts with `##` (a section heading), and each part of the template — Method, What I Found, etc. — uses `###` (a subsection). This creates a clear hierarchy that's easy to scan.

### 2. Bold and Italic

Wrap text in asterisks to emphasize it.

```markdown
**bold text**
*italic text*
***bold and italic***
```

Use bold sparingly for key terms or important findings. Use italic for titles of things or for emphasis within a sentence. If everything is bold, nothing stands out.

### 3. Lists

Start lines with `-` or `*` for bullet points, or with numbers for ordered lists.

```markdown
- first item
- second item
- third item

1. first step
2. second step
3. third step
```

Bullet lists work well for observations and findings. Numbered lists work well for steps or ranked items.

### 4. Links

Put the display text in square brackets, followed immediately by the URL in parentheses.

```markdown
[Hugging Face](https://huggingface.co)
```

This renders as a clickable link. You'll use this to link to models, Spaces, datasets, and articles in your journal entries. Linking to your sources makes your journal entries verifiable.

### 5. Code and Code Blocks

Use single backticks for inline code and triple backticks for blocks of code.

```markdown
The model name is `distilbert-base-uncased`.
```

For longer code or model outputs, use a fenced code block with triple backticks on their own lines:

````markdown
```
Output: POSITIVE (confidence: 0.94)
```
````

You can also specify a language after the opening backticks for syntax highlighting:

````markdown
```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
```
````

Use inline code for model names, file names, and short technical terms. Use code blocks for model outputs, error messages, and code snippets.

### 6. Tables

Use pipes `|` and hyphens `-` to create tables.

```markdown
| Model | Input | Result | Confidence |
|---|---|---|---|
| distilbert-sst-2 | "I love this" | POSITIVE | 0.99 |
| distilbert-sst-2 | "meh" | POSITIVE | 0.58 |
```

Tables are especially useful for side-by-side model comparisons in your journal. When you test the same input across multiple models, a table makes the differences visible at a glance.

## A Quick Reference

| What you want | What you type | What it looks like |
|---|---|---|
| Heading | `## My Heading` | **My Heading** (rendered large) |
| Bold | `**important**` | **important** |
| Italic | `*emphasis*` | *emphasis* |
| Bullet list | `- item` | • item |
| Numbered list | `1. step` | 1. step |
| Link | `[text](url)` | [text](url) |
| Inline code | `` `model-name` `` | `model-name` |
| Code block | ` ``` code ``` ` | (formatted code block) |
| Table | `\| A \| B \|` | (formatted table) |

## One More Thing

Markdown is forgiving. If you forget a `#` or misplace an asterisk, your file won't break — it just won't format that part. You can always preview how your Markdown looks by pushing to GitHub and viewing the file there, or by using the preview mode in VS Code or GitHub's browser editor.

The best way to learn Markdown is to write in it. Your research journal gives you weekly practice. By mid-semester, this formatting will be automatic.

---

AI + Research Level 2 • Session 2: Data Collection and Representation

# Designing Your GitHub Profile README

A guide to the design space, written for students in *AI + Research Level 2*. The Session 8 guide covered the **structure** of a profile README — what sections to include and what to put in them. This guide covers the **design** — the visual and rhetorical choices that turn a generic README into something that fits the specific reader you want it to fit.

---

## Start with the audience, not the techniques

Every other guide on this topic starts with "10 cool things you can put on your GitHub profile." That order is wrong. The technique inventory only matters once you know who you're trying to reach.

Spend ten minutes writing one sentence about each of these:

1. **Who is the most important reader of this page?** Not "everyone." One specific person. A college admissions officer reading 200 applications today. A grad-school faculty member checking whether you're a serious applicant for their lab. A startup CTO deciding whether to invite you to a weekend-trial interview. A peer in your major you want to collaborate with. A future you, six years from now, looking at your own undergraduate portfolio.
2. **What are they hoping to find in the first five seconds?** Different readers want different things. The admissions officer wants to know you've actually done something concrete and you can describe it without jargon. The CTO wants to see code that ships. The peer wants to know if you have shared interests.
3. **What signal would make them close the tab?** Animated typing text, on most academic readers. A wall of unstyled paragraphs, on most industry readers. A list of fifty technology badges on essentially everyone above the entry-level audience. Knowing what *won't* work for your audience is as useful as knowing what will.

Your visual register — restrained, distinctive, dynamic — is downstream of these answers. Three students with three different audiences should land on three different designs, even if they're using identical Hugging Face Spaces and the same paper-template.

---

## Three legitimate registers

There is no single "best" GitHub profile README. There are three distinct registers, each appropriate for a different audience. Every other choice — banner or no banner, badges or sentence-about-skills, stats card or no stats card — follows from which register fits your reader.

### Register 1 — Restrained

> **For:** academic readers, fellowship committees, faculty mentors, grad-school applications.
>
> **Looks like:** typography only. No banner. Section heads, horizontal rules, and disciplined whitespace do all the visual work. Maybe one diagram. Maybe one consistent badge style for publications.
>
> **Models:**
> - **[github.com/rougier](https://github.com/rougier)** — the canonical academic profile. A reverse-chronological publication list with right-aligned DOI badges. No imagery. Reads like a CV that learned to be a webpage.
> - **[github.com/karpathy](https://github.com/karpathy)** — one sentence. Then the pinned repos do the work.
>
> **Why it works:** it doesn't fight the reader. Every line is content. Nothing animates. The credibility-per-pixel is high because the page trusts its own substance to carry the meeting.
>
> **Failure mode:** if your substance is thin, this register exposes it. There is no decoration to hide behind.

### Register 2 — Distinctive

> **For:** mixed audiences. A reader you cannot fully anticipate — some peers, some industry, some teachers, some strangers who arrived via a public talk.
>
> **Looks like:** one carefully chosen visual element at the top (a hand-authored banner, or a distinctive piece of typography), a clear position statement, a *Now* line that signals the page is alive, two or three anchor projects with a paragraph each, then a clean list of everything else. One Mermaid diagram earns its space if it communicates something a paragraph couldn't.
>
> **Models:**
> - **[github.com/anuraghazra](https://github.com/anuraghazra)** — author of the most-used GitHub stats widget; uses one banner, brief about-me bullets, and his stats card. Restrained for someone whose tool *is* maximalist decoration.
> - **[github.com/maxwelljoslyn](https://github.com/maxwelljoslyn)** — a grad-student profile that picks three projects and writes a real paragraph about each, with screenshots. The most directly imitable model for current students.
>
> **Why it works:** reads as designed without reading as decorated. Most academic visitors find it credible; most non-academic visitors find it visually distinct from the dozens of identical developer profiles they see in a row.
>
> **Failure mode:** the banner. A banner that looks generic — a stock gradient with your name in white sans-serif — actively hurts the page. If you can't make a banner that adds something, skip it and lean on typography.

### Register 3 — Dynamic

> **For:** a reader you want to convince that you're *currently active*. Often a hiring audience, sometimes a peer audience, occasionally a researcher whose calling card is being plugged into many ongoing public projects at once.
>
> **Looks like:** a multi-column dashboard near the top — recent posts, recent commits, recent talks — each driven by a scheduled GitHub Action that pulls from a feed and rewrites the README every few hours. Most readers don't notice the columns are auto-generated; the page just feels fresh every time they visit.
>
> **Models:**
> - **[github.com/simonw](https://github.com/simonw)** — Simon Willison's three-column self-updating page is the canonical example. Built by his own GitHub Action, which is itself one of his projects. The page demonstrates the kind of practitioner he is.
> - **[github.com/Platane](https://github.com/Platane)** — a single dynamic element (a snake game that "eats" his contribution graph), generated by a scheduled action that commits the regenerated SVG back to his profile repo. One decision, well executed.
>
> **Why it works:** it earns the impression of activity by actually being active.
>
> **Failure mode:** the maintenance bill. A scheduled Action that silently breaks turns the page into a lie — last-week's freshness frozen forever. If you're not going to monitor it, don't build it. Register 2 with a hand-edited *Now* line gets you 80% of the same effect with none of the maintenance.

---

## How the registers map to your specific audience

| If your audience is... | The register that usually fits |
|---|---|
| College admissions officer | Restrained, with one **distinctive** project paragraph that lets your voice through. |
| Grad-school application reader | Restrained. They want a CV-like artifact, not a personality. |
| Faculty researcher in your field | Restrained or distinctive. Lead with the work, let one design choice (the diagram, the dated *Now* line) signal taste. |
| Peer collaborator at your level | Distinctive. They want to know what kind of person they'd be working with. |
| Industry recruiter, technical role | Distinctive or dynamic. They are skimming many pages; one or two visual anchors help. |
| Industry recruiter, non-technical role | Distinctive. The dynamic dashboard pattern is read as "developer signaling," which can backfire outside CS. |
| Future-you, looking back in five years | Whichever register makes you proud now. There is no reader except you. Be brave. |

---

## The technique inventory

Once your register is chosen, the technique question is "which of these earn their place on this specific page?" — not "how many can I fit?" The categories below cover what is actually possible. Use them as a menu, not a checklist.

### Markdown-only (always available, never breaks)

- **HTML inside Markdown for layout.** `<div align="center">` for centered banners; `<table>` for two- or three-column layouts; `<sub>` and `<sup>` for small text and superscripts; `<details>` and `<summary>` for collapsible sections; `<picture>` and `<source>` with `prefers-color-scheme` for light/dark image swaps.
- **GitHub callouts.** `> [!NOTE]`, `> [!TIP]`, `> [!WARNING]`, `> [!IMPORTANT]`, `> [!CAUTION]` render as colored boxes. Useful for one-or-two-line emphasis without an image.
- **Mermaid diagrams.** Fenced code blocks with `mermaid` render as actual diagrams. Useful in a researcher profile to show how the parts of your work connect. One diagram, well placed, communicates more than a paragraph.
- **LaTeX math.** `$inline$` and `$$display$$` work natively. If you do ML or any quantitative work, a single equation that captures the kind of work you do can be a strong visual anchor.
- **Footnotes** (`[^1]`) and **task lists** (`- [x]`) for substance and structure.
- **Anchored TOCs.** Auto-generated header anchors. Useful in long profiles, unnecessary in short ones.

### Badges (use sparingly, one consistent style)

- **Shields.io** is the dominant service. The pattern is `https://img.shields.io/badge/<label>-<message>-<color>?style=flat-square&logo=<simpleicon>`. Used carefully (a single repeated style for publication links, or one ORCID badge under your name), badges create a useful scan-rhythm. Used badly (a wall of fifteen language badges next to a wall of fifteen framework badges), they signal early-career and undermine the rest of the page.
- **The skill-matrix antipattern.** A row of forty technology badges is the most-used and most-counterproductive pattern on student profile READMEs. A sentence — *"I write Python and TypeScript every day; I read Rust and Go; I'm fluent in PyTorch"* — is more informative, harder to fake, and easier on the reader.

### Dynamic widgets (interesting, but read the caveat)

- **`github-readme-stats`** — the colored stats card most developer profiles have. Customizable themes. Approximately neutral — using one doesn't hurt, doesn't help.
- **`github-readme-streak-stats`** — current/longest streak, total contributions.
- **Snake-game contribution graph** ([Platane/snk](https://github.com/Platane/snk)) — animated SVG of a snake eating your contribution squares. Generated by a GitHub Action that commits the SVG to your own profile repo, so it remains stable over time.
- **Typing SVGs** ([DenverCoder1/readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg)) — typing-then-deleting animated text. Very common on student profiles. Almost never on senior profiles. Read whatever signal that gives you.
- **WakaTime / activity graphs** — code-time and contribution-pattern visualizations. Useful if your audience is a hiring manager who values evidence of consistent practice; not useful for an academic audience.

> **Caveat that matters:** every dynamic widget is an `<img>` element pointing at a third-party server. If that server goes quiet (rate-limited, deprecated, abandoned by maintainer), your profile breaks silently. Design choices that depend on third-party services have a half-life. The author of `github-readme-stats` himself recommends self-hosting the service if your profile needs to render reliably in 18 months. For an undergraduate or graduate profile that has to survive a job search or an admissions cycle, prefer assets you commit to your own profile repo (the snake-game pattern is good for this — the SVG is regenerated by an Action and pushed to your `output` branch, so it keeps working even if the upstream tool changes).

### Custom assets

- **Banners.** Figma is the most-used tool, with a free tier. Canva for templates. Photopea for browser-Photoshop. Excalidraw for the sketch aesthetic. Sized at roughly 1280×320 pixels with a transparent background. Always commit two variants (light / dark) and use `<picture>` to swap.
- **Animated SVGs.** Hand-authored SMIL animations work in GitHub's image proxy. Tedious for anything complex. Don't pursue this unless you know why you want it.
- **`capsule-render`** — the gradient banner with a wave at the bottom that you've seen on hundreds of profiles. Wide range of types and animations. Note the same caveat as above: the public service is best-effort.

### Information-architecture moves

- **The "Now" line.** A dated paragraph that says what you're working on this month. Borrowed from [nownownow.com](https://nownownow.com). Lower-maintenance than a scheduled-Action dashboard; updates only when the answer changes. The freshness signal is in the date.
- **The "Currently / Previously / Building" temporal triple.** A compressed CV format that fits the README form well.
- **Pinned repos as portfolio.** GitHub allows six pins above your README. They act as a six-tile gallery of your output. Pin one repo per *kind* of work, not six versions of the same thing.
- **Linked papers, talks, posts.** For an academic profile: flat reverse-chronological list with venue and year. For a non-academic profile: topic clusters often work better.

---

## How to pick

The decision tree:

1. Write the one-sentence answers for **audience**, **first-five-seconds**, **closing-signal**. (See the top of this guide.)
2. Match your audience to a **register** in the table above.
3. Pick **one** distinctive design move that fits the register. *One.* (A single banner, or a single Mermaid diagram, or a single Now line. Not all three.)
4. Write the **structure** the Session 8 guide covers — research, projects, paper, what you're building now.
5. Run the page on **mobile** at ~380px viewport width. If multi-column tables wrap badly, fix or remove them.
6. Run the page in **dark mode**. If any image looks wrong, author a dark variant and use `<picture>`.
7. Pick **one external dependency** (a stats card, a typing SVG, a banner from `capsule-render`) at most. Every external dependency is a potential silent break in 18 months.

If your draft has more than one external dependency, more than one big visual element, or more than one badge style, simplify it. The strongest profiles in any register are the ones whose decisions are visible — *they chose this, on purpose, instead of those other things.*

---

## Three variants of the same researcher

The course repository contains three complete worked examples, all describing the same researcher (Daniel Plate's profile, redesigned three different ways) so you can see what changes when the register changes:

- **[`README-variant-A-restrained-academic.md`](./README-variant-A-restrained-academic.md)** — Register 1. Typography only. One Mermaid diagram. Ready to commit as-is.
- **[`README-variant-B-mid-distinctive.md`](./README-variant-B-mid-distinctive.md)** — Register 2. One banner, one diagram, one *Now* line, two anchor-project paragraphs. The recommended starting point for most students.
- **[`README-variant-C-self-updating-builder.md`](./README-variant-C-self-updating-builder.md)** — Register 3. Three-column dashboard driven by a scheduled GitHub Action. Includes the full workflow YAML in the file's comment block.

Each file is self-contained. The differences between them are the design decisions to study.

---

## Common student traps

A short list of the patterns we see most often on first drafts:

- **The wall of badges.** Forty technology badges in three rows. Communicates nothing specific. Replace with one sentence.
- **The default stats card.** The exact same `github-readme-stats` card that 200,000 other developers use. Approximately neutral; not the worst thing, but not doing work for you. If you keep it, customize the theme to match a personal palette.
- **The animated typing banner.** Cute the first time, friction every time after. Almost universally read as early-career. Skip it.
- **The visitor counter.** Counts loads of an image, not unique visitors. Trivially gameable. Reads as decorative rather than informative.
- **The half-finished anchor.** A README that says "Currently working on [project name]" with a link to a repo whose latest commit was eight months ago. The dated *Now* line is much harder to fake than an undated "currently working on" — it forces honesty.
- **The maximalist trap.** Adding the snake game and the streak card and the WakaTime block and the trophy widget *and* the typing banner, hoping that more decoration will read as more substance. It doesn't. The strongest profiles in any register are the ones with fewer elements, each chosen on purpose.

---

## What success looks like

When your README is finished, a stranger landing on your page should be able to answer these in roughly five seconds, before they've decided to read further:

- *What field does this person work in?*
- *What is one specific thing they have made or are making?*
- *Are they currently active?*
- *Where would I click to find out more?*

If your page answers all four, the register doesn't matter. If your page answers none, the register doesn't matter — no amount of decoration fixes the underlying problem.

---

## Further reading

- The companion research dossier: [`readme-research-dossier.md`](./readme-research-dossier.md) — the full technique inventory with verified exemplar profiles, code snippets for the load-bearing techniques, and the failure-mode catalog.
- GitHub's own accessibility guidance: [5 tips for making your GitHub profile page accessible](https://github.blog/developer-skills/github/5-tips-for-making-your-github-profile-page-accessible/).
- Simon Willison's post on how his self-updating profile works: [How my self-updating profile README works](https://simonwillison.net/2020/Jul/10/self-updating-profile-readme/).
- The Session 8 guide on README **structure**: [`session-08/GUIDE-github-profile-readme.md`](./session-08/GUIDE-github-profile-readme.md).

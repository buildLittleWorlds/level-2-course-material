# Google Classroom Build Status

Last updated: 2026-02-24

## Classroom Details

- **Class name**: AI + Research Level 2 Class 1
- **Section**: 2026 Spring Term
- **Subject**: Level 2
- **Room field**: Every Saturday @ 8-10 pm EST
- **Class code**: vw7jbsfo
- **URL**: https://classroom.google.com/c/ODI1ODUxNDgwOTQ1
- **Classwork page**: https://classroom.google.com/w/ODI1ODUxNDgwOTQ1/t/all
- **Admin**: Bing (Youth Horizons Learning) — Daniel is a co-teacher but does not have admin/Workspace permissions (e.g., cannot enable Meet links)
- **Settings**: Students can post and comment; No overall grade calculation; No Meet link (admin-controlled)

## What Has Been Built

### Topics (13 total)

All topics were created successfully. They currently appear in reverse order on the Classwork page (Google Classroom puts newest at top). They need to be reordered so START HERE is first, then Sessions 1-12 in order.

| Topic Name | Arc |
|---|---|
| START HERE - Course Info & Tools | (intro) |
| Exploration - Session 1: Your First Space | Exploration |
| Exploration - Session 2: Swap the Engine | Exploration |
| Exploration - Session 3: Break It on Purpose | Exploration |
| Evaluation - Session 4: Sentiment Showdown | Evaluation |
| Evaluation - Session 5: Text Playground | Evaluation |
| Evaluation - Session 6: Domain Safari | Evaluation |
| Advanced - Session 7: Bias Tester | Advanced |
| Advanced - Session 8: Image Pipeline | Advanced |
| Project - Session 9: Make It Useful | Project |
| Project - Session 10: Build Your Own | Project |
| Project - Session 11: Iterate and Polish | Project |
| Project - Session 12: Demo Day | Project |

### Session 1: Fully Populated

Under **Exploration - Session 1: Your First Space**:

1. **Material**: "Session 1 Notebook: Your First Space"
   - Description: Companion notebook for Session 1 explaining INPUT --> MODEL --> OUTPUT pipeline and zero-shot classification
   - Link: https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-01/notebook.ipynb

2. **Assignment** (Ungraded): "Between Sessions: Duplicate & Customize the Silly Phrase Finder"
   - Full instructions adapted from session-01/BETWEEN-SESSION.md
   - Steps: Go to profplate/silly-phrase-finder on Hugging Face, Duplicate Space, edit app.py labels, commit changes
   - Also includes: Create a GitHub account before Session 2
   - Submission type: Link submission (students paste their HF Space URL)

### Sessions 2-12: Notebook Materials Only

Each session has one **Material** post containing:
- Title: "Session N Notebook: [Session Name]"
- Description: 1-2 sentence summary of what students will do + the ML concept
- Link: Colab notebook URL

| Session | Title | Concept in Description |
|---|---|---|
| 2 | Swap the Engine | Training Data & Representation |
| 3 | Break It on Purpose | Data Cleaning & Feature Engineering |
| 4 | Sentiment Showdown | Model Evaluation |
| 5 | Text Playground | Hyperparameters |
| 6 | Domain Safari | Overfitting & Domain Shift |
| 7 | Bias Tester | Bias in AI |
| 8 | Image Pipeline | Multi-Model Systems & Error Cascades |
| 9 | Make It Useful | Prompt Engineering & Human-AI Interaction |
| 10 | Build Your Own | Supervised Learning & Task Design |
| 11 | Iterate and Polish | The Experimentation Loop |
| 12 | Demo Day | Reflection & Portfolio |

Colab URLs follow the pattern:
```
https://colab.research.google.com/github/buildLittleWorlds/level-2-course-material/blob/main/session-{XX}/notebook.ipynb
```
Where `{XX}` is the zero-padded session number (01, 02, ... 12).

## What Has NOT Been Built Yet

### 1. Between-Session Assignments (Sessions 2-11)

Session 1's between-session assignment was created as an **Ungraded Assignment** (not a Material) so it appears on students' To-Do lists. The same pattern should be used for Sessions 2-11. Session 12 has no between-session challenge.

Each session folder has a `BETWEEN-SESSION.md` file with the challenge details. These need to be read and adapted into Google Classroom Assignment posts, following the pattern established for Session 1:
- Type: Assignment (not Material)
- Points: Ungraded
- Topic: Assigned to the corresponding session topic
- Description: Adapted from the BETWEEN-SESSION.md content
- Submission: Link submission where appropriate

**Note**: Daniel indicated he wants to review the material first and think about what should be done with the between-session files before we create these assignments.

### 2. START HERE Topic Content

The "START HERE - Course Info & Tools" topic is empty. It should contain:

- **Material: Course Overview** — What the course is, the four arcs, what students will build
- **Material: Account Setup** — Links to create accounts on:
  - Hugging Face (https://huggingface.co/)
  - Google Colab (https://colab.research.google.com/)
  - GitHub (https://github.com/)
- **Material: Zoom Link** — Placeholder for the Zoom meeting link (Daniel may not have this yet; Bing controls the Zoom account)
- Possibly a visual or overview of how the platforms connect

### 3. Topic Reordering

Topics are currently in reverse creation order (Session 12 at top, START HERE at bottom). They need to be dragged into the correct order:
1. START HERE - Course Info & Tools
2. Exploration - Session 1: Your First Space
3. Exploration - Session 2: Swap the Engine
4. ... (Sessions 3-11 in order)
5. Project - Session 12: Demo Day

This is done by dragging topics on the Classwork page using the three-dot menu or drag handles.

### 4. Final Review

After all content is added and topics are reordered, do a full scroll-through of the Classwork page to verify everything looks correct.

## Technical Notes for Future Sessions

### Browser Automation Details
- **Tab ID**: 1121197660 (will change in new sessions — navigate to the Classwork URL above)
- The Google Classroom is accessed through Chrome browser automation (Claude in Chrome MCP tools)
- Daniel is logged into Google Classroom as a co-teacher on Bing's Workspace account

### Creating Materials (pattern)
1. Click "+ Create" → Material
2. Type title in Title field
3. Type description in Description field
4. Click Topic dropdown (click the arrow on the right side of the "No topic" button, or use `find` tool to locate the combobox element)
5. Topics are listed **alphabetically** in the dropdown — scroll to find the right one
6. Click the correct topic
7. Click "Link" icon in the Attach section
8. Paste the Colab URL in the Add link dialog
9. Click "Add link"
10. Wait for the link preview to load
11. Click "Post"

### Creating Assignments (pattern)
1. Click "+ Create" → Assignment
2. Type title
3. Type instructions in the Instructions field
4. Set Points to "Ungraded" (triple-click the points field to select "100", type "Ungraded")
5. Set Topic from dropdown (same alphabetical scrolling as Materials)
6. Click "Assign" (or use the dropdown arrow next to Assign for scheduling)

### Known Quirks
- The Points dropdown in Assignments is finicky — sometimes need to use `find` tool to locate the combobox element, triple-click to select, then type "Ungraded"
- Topics dropdown lists alphabetically, not in creation/display order
- A popup about scheduling across classes may appear on first Material/Assignment creation — dismiss it
- New topics appear at the top of the Classwork page, not the bottom

## Context

This classroom is for a 12-week hands-on AI course called "Roots: Iterative Space Building" for grades 7-11, delivered through Youth Horizons Learning (YHL). 5-6 students meet Saturday evenings 8-10pm EST via Zoom. Daniel (Dr. Plate) is the instructor; Bing (YHL) handles operational support including Google Classroom admin. The course teaches ML concepts through building Hugging Face Spaces, with companion Colab notebooks and progressive GitHub skills. See README.md in this folder for full course details and correspondence-and-research/ for program context.

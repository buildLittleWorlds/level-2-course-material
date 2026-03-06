# Between Sessions 3 & 4

## Your Challenge

**Find a text where the model completely misreads the tone.**

### Steps

1. Open your Space (the Mood Meter or Sarcasm Breaker — whichever you have)
2. Try to find text where the model's reading of the feeling is clearly wrong — not because the text is messy, but because the *tone* doesn't match the words
3. Some ideas to try:
   - A sarcastic text you'd send to a friend
   - A passive-aggressive email ("As per my previous message...")
   - A song lyric that sounds happy but is actually sad (or vice versa)
   - Something you'd say that means the opposite of what it literally says
4. Describe the failure to Claude or ChatGPT using the CLEAR framework:
   - **C**ontext: What does your Space do?
   - **L**anguage: What's it built with? (Python, Gradio, Transformers)
   - **E**xplain: What goes wrong? What input causes the tone misread?
   - **A**sk: What do you want the AI to do?
   - **R**equirements: Any specific constraints? (Must work on free CPU, must stay simple)
5. Try applying the AI's suggestion to your Space

### What to Notice

- Did the AI understand why the model misread the tone?
- Did the fix actually help, or is sarcasm just too hard?
- What's the difference between fixing noise (emoji, caps) and fixing meaning (sarcasm, irony)?

### Bring It Back

Next session, be ready to share: what text broke the model, and was it a noise problem or a tone problem?

---

## Notebook

Finish the experiments in today's notebook. Try editing the `clean_text()` function to add your own cleaning step — the notebook has a cell ready for you to experiment with.

The key question: **What can cleaning fix, and what is beyond its reach?**

## GitHub

Upload this notebook to your `my-ai-portfolio` repo:
1. Go to your repo on github.com
2. Click **Add file** → **Upload files**
3. Drag the `.ipynb` file and click **Commit changes**

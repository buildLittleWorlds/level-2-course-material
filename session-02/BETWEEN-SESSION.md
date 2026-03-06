# Between Sessions 2 & 3

## Your Challenge

**Find a model on the Hub that recognizes feelings the current ones miss.**

### Steps

1. Go to [huggingface.co/models](https://huggingface.co/models)
2. Browse or search for a model that detects emotions or feelings. Some ideas:
   - Search for "emotion" to find models that label text with feelings
   - Search for "sentiment" to find more binary models
   - Search for "text-classification" and browse for interesting tasks
   - Look at the "Most downloaded" tab for popular models
3. Click on a model and **read its model card**. Answer these questions:
   - What was it trained on?
   - What emotion labels does it use?
   - What feelings are missing from its categories?
4. Try swapping it into your Space:
   - Open your Space's `app.py` in the Files tab
   - Change the model name in the `pipeline()` line
   - You might need to change the pipeline task too (e.g., `"text-classification"`, `"sentiment-analysis"`)
5. If it breaks, that's totally fine! Note what happened.

### What to Notice

- Does the new model use different feeling categories than the ones we tried tonight?
- Does it recognize any emotions that our three models couldn't see?
- Did it need different inputs to work well?
- What kind of training data was it built on? How does that change what it "understands"?

### Bring It Back

Next session, be ready to share: what model did you try, and what feelings could it see that ours couldn't?

---

## Notebook

Finish the experiments in today's notebook. The key question for each experiment: **which model do you agree with most, and why?**

Try to find:
- Text where all three models agree about the feeling
- Text where they completely disagree
- A feeling you've had that none of the three models can name

## GitHub

1. Create a new repository called `my-ai-portfolio`
2. On github.com, click the **+** in the top right, then **New repository**
3. Name: `my-ai-portfolio`, keep it Public, add a README
4. Upload today's notebook: go to your repo, click **Add file**, then **Upload files**, and drag the `.ipynb` file

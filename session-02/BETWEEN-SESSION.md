# Between Sessions 2 & 3

## Your Challenge

**Find a model on the Hub and try swapping it into your Space.**

### Steps

1. Go to [huggingface.co/models](https://huggingface.co/models)
2. Browse or search for a model that does something interesting. Some ideas:
   - Search for "text-classification" to find models that label text
   - Search for "zero-shot" to find models like our original one
   - Look at the "Most downloaded" tab for popular models
3. Click on a model and **read its model card**. Answer these questions:
   - What was it trained on?
   - What task does it do?
   - What labels/categories does it output?
4. Try swapping it into your Space:
   - Open your Space's `app.py` in the Files tab
   - Change the model name in the `pipeline()` line
   - You might need to change the pipeline task too (e.g., `"text-classification"`, `"zero-shot-classification"`, `"sentiment-analysis"`)
5. If it breaks, that's totally fine! Note what happened.

### What to Notice

- Did the new model work with your existing code, or did you need to change things?
- What kind of output did it give? Same format as before, or different?
- Did it need different inputs to work well?

### Bring It Back

Next session, be ready to share: what model did you try, and what happened?

---

## Notebook

Finish the experiments in today's notebook. See if you can find text that makes all three models agree — and text that makes them all disagree.

## GitHub

1. Create a new repository called `my-ai-portfolio`
2. On github.com → click the **+** in the top right → **New repository**
3. Name: `my-ai-portfolio`, keep it Public, add a README
4. Upload today's notebook: go to your repo → **Add file** → **Upload files** → drag the `.ipynb` file

# Bonus Fine-Tuning: Nostalgia Demo

This folder contains a standalone classroom fine-tuning example built around the Hugging Face dataset [`Senem/Nostalgic_Sentiment_Analysis_of_YouTube_Comments_Data`](https://huggingface.co/datasets/Senem/Nostalgic_Sentiment_Analysis_of_YouTube_Comments_Data).

Files:

- `nostalgia_finetune_colab.ipynb` — the Colab notebook students can run
- `../scripts/build_nostalgia_finetune_notebook.py` — the small generator script used to build the notebook

What this experiment does:

- loads the nostalgia dataset
- creates a stratified train/test split from the single `train` split
- maps the string labels to numeric ids
- fine-tunes `distilbert-base-uncased` for binary text classification
- evaluates with accuracy, precision, recall, F1, and a confusion matrix
- optionally pushes the final model to `profplate/distilbert-nostalgia-youtube-comments`

Why this version is safer than the pasted draft:

- it uses the dataset's real columns: `comment` and `sentiment`
- it does not assume a pre-made test split
- it keeps Hub upload optional so the training section can finish even if login is skipped

Suggested sharing flow:

1. Run the notebook in Colab with a GPU runtime.
2. Push the trained model to your Hugging Face profile.
3. Edit the model card on Hugging Face and add:
   - a 2-3 sentence summary of the experiment
   - the dataset link
   - the Colab notebook link
   - a few sample comments and predictions
4. Pin the model repo on your profile so students can find it quickly.

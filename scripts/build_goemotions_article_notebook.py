import json
from pathlib import Path
from textwrap import dedent


NOTEBOOK_PATH = Path("_archive/articles/goemotions-paper-explorer.ipynb")


def md(text: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": dedent(text).strip("\n").splitlines(keepends=True),
    }


def code(text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": dedent(text).strip("\n").splitlines(keepends=True),
    }


EMOTION_NAMES = [
    "admiration",
    "amusement",
    "anger",
    "annoyance",
    "approval",
    "caring",
    "confusion",
    "curiosity",
    "desire",
    "disappointment",
    "disapproval",
    "disgust",
    "embarrassment",
    "excitement",
    "fear",
    "gratitude",
    "grief",
    "joy",
    "love",
    "nervousness",
    "optimism",
    "pride",
    "realization",
    "relief",
    "remorse",
    "sadness",
    "surprise",
    "neutral",
]


cells = [
    md(
        f"""
        # Exploring The GoEmotions Paper In Colab

        ## Fine-Grained Emotion Detection on GoEmotions

        This notebook is built around the article **"Fine-Grained Emotion Detection on GoEmotions: Experimental Comparison of Classical Machine Learning, BiLSTM, and Transformer Models"** by Ani Harutyunyan and Sachin Kumar (arXiv preprint, January 26, 2026).

        Source article in this repo:
        - `_archive/articles/fine-grained-emotion-detection-on-goEmtions.pdf`

        The goal is not just to run code. The goal is to **read the paper through experiments**:

        - understand what question the paper asks
        - summarize its method in plain language
        - test some of its core claims with runnable code
        - inspect where simple models succeed and where they fail
        - try one of the paper's proposed future directions: **threshold tuning**

        This notebook is intentionally long and structured like a guided lab.
        """
    ),
    md(
        """
        ## What The Paper Studies

        The paper focuses on **fine-grained emotion classification** rather than simple positive/negative sentiment. Instead of asking "is this text positive or negative?", the task is to predict one or more labels from the GoEmotions label set, including emotions such as:

        - admiration
        - annoyance
        - grief
        - curiosity
        - excitement
        - neutral

        The challenge is that this is a **multi-label** problem:

        - one comment can have more than one emotion
        - some labels are common and some are rare
        - some labels overlap semantically
        - lexical cues can be helpful, but context also matters

        The paper compares three model families:

        1. **TF-IDF + Logistic Regression**
        2. **BiLSTM + Attention**
        3. **BERT fine-tuning**

        The paper evaluates them with:

        - Micro-F1
        - Macro-F1
        - Hamming Loss
        - Subset Accuracy
        """
    ),
    md(
        """
        ## The Paper's Main Findings

        The article reports these headline conclusions:

        | Model | What the paper says |
        |---|---|
        | Logistic Regression | Surprisingly strong baseline; best reported Micro-F1 in the paper's experiments |
        | BiLSTM + Attention | Better than a trivial baseline, but weaker than the other two model families |
        | BERT | Best overall balance, especially on rarer or more ambiguous emotions |

        The paper's interpretation is important:

        - **Frequent emotions** often align with direct lexical clues, which helps TF-IDF + logistic regression.
        - **Rarer or more context-sensitive emotions** benefit from contextual embeddings, which helps BERT.
        - **Class imbalance** makes Macro-F1 and per-label analysis essential, because Micro-F1 can hide weak performance on rare emotions.

        We will test each of those ideas below.
        """
    ),
    md(
        """
        ## How This Notebook Connects To The Paper

        This notebook is inspired by the paper, but it is not a perfect reproduction of every training detail. That is deliberate.

        The article uses:

        - official train / validation / test splits
        - TF-IDF logistic regression with binary relevance
        - BiLSTM with attention and GloVe embeddings
        - BERT fine-tuning
        - imbalance handling and discussion of focal loss

        In this notebook we do four practical things:

        1. **Recreate the dataset story** with EDA
        2. **Train a lexical baseline** close to the paper's logistic regression setup
        3. **Train a lightweight transformer proxy** to test the paper's contextual-model claim in a Colab-friendly way
        4. **Tune thresholds per label**, which the paper specifically suggests as future work

        We do **not** fully implement the BiLSTM section here because it adds substantial code and runtime cost while contributing less insight than the lexical-vs-contextual comparison. Instead, we leave a clear extension path at the end.
        """
    ),
    code(
        """
        !pip install -q datasets transformers accelerate evaluate scikit-learn seaborn matplotlib pandas
        """
    ),
    code(
        """
        import math
        import random
        import warnings
        from dataclasses import dataclass

        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns
        import torch
        from IPython.display import display

        from datasets import load_dataset
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import (
            accuracy_score,
            classification_report,
            f1_score,
            hamming_loss,
            precision_recall_fscore_support,
        )
        from sklearn.multiclass import OneVsRestClassifier
        from sklearn.preprocessing import MultiLabelBinarizer

        from transformers import (
            AutoModelForSequenceClassification,
            AutoTokenizer,
            DataCollatorWithPadding,
            Trainer,
            TrainingArguments,
        )

        warnings.filterwarnings("ignore")

        sns.set_theme(style="whitegrid")
        plt.rcParams["figure.figsize"] = (12, 6)

        SEED = 42
        random.seed(SEED)
        np.random.seed(SEED)
        torch.manual_seed(SEED)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(SEED)

        print("Torch:", torch.__version__)
        print("CUDA available:", torch.cuda.is_available())
        """
    ),
    md(
        """
        ## Runtime And Scope Controls

        The paper trains full models. In a free Colab session, full reproduction can be slow.

        This notebook therefore supports two modes:

        - `QUICK_MODE = True`: lighter experiments, faster iteration
        - `QUICK_MODE = False`: larger slices of the official splits, closer to a serious reproduction

        The paper's claims are qualitative enough that even quick mode can still be informative.
        """
    ),
    code(
        """
        QUICK_MODE = True

        LOGREG_TRAIN_LIMIT = 12000 if QUICK_MODE else None
        LOGREG_VAL_LIMIT = 2000 if QUICK_MODE else None
        LOGREG_TEST_LIMIT = 3000 if QUICK_MODE else None

        RUN_TRANSFORMER = torch.cuda.is_available()
        TRANSFORMER_MODEL_NAME = "distilbert-base-uncased"
        TRANSFORMER_TRAIN_LIMIT = 6000 if QUICK_MODE else 20000
        TRANSFORMER_VAL_LIMIT = 1000 if QUICK_MODE else 3000
        TRANSFORMER_TEST_LIMIT = 2000 if QUICK_MODE else 5000
        MAX_LENGTH = 96
        NUM_EPOCHS = 1 if QUICK_MODE else 2

        print("QUICK_MODE:", QUICK_MODE)
        print("RUN_TRANSFORMER:", RUN_TRANSFORMER)
        print("Transformer model:", TRANSFORMER_MODEL_NAME)
        """
    ),
    md(
        """
        ## Load The GoEmotions Dataset

        The paper uses the official GoEmotions train / validation / test split.

        Below we try a few Hugging Face dataset loading paths because the exact configuration name can vary across environments. We also keep a fixed fallback list of label names from the paper so the notebook stays readable even if feature metadata is slightly different.
        """
    ),
    code(
        f"""
        EMOTION_NAMES = {EMOTION_NAMES}

        DATASET_CANDIDATES = [
            ("go_emotions", None),
            ("go_emotions", "raw"),
            ("google-research-datasets/go_emotions", None),
            ("google-research-datasets/go_emotions", "raw"),
        ]

        goemotions = None
        last_error = None

        for path, config in DATASET_CANDIDATES:
            try:
                if config is None:
                    goemotions = load_dataset(path)
                else:
                    goemotions = load_dataset(path, config)
                print(f"Loaded dataset from path={{path!r}}, config={{config!r}}")
                break
            except Exception as exc:
                last_error = exc

        if goemotions is None:
            raise RuntimeError(f"Could not load GoEmotions. Last error: {{last_error}}")

        print(goemotions)
        """
    ),
    code(
        """
        def normalize_labels(label_list):
            return [int(x) for x in label_list]

        def split_to_frame(ds):
            return pd.DataFrame(
                {
                    "text": ds["text"],
                    "labels": [normalize_labels(x) for x in ds["labels"]],
                }
            )

        train_df_full = split_to_frame(goemotions["train"])
        val_df_full = split_to_frame(goemotions["validation"])
        test_df_full = split_to_frame(goemotions["test"])

        print("Train size:", len(train_df_full))
        print("Validation size:", len(val_df_full))
        print("Test size:", len(test_df_full))

        train_df_full.head()
        """
    ),
    md(
        """
        ## Paper Summary: Why The Dataset Matters

        One of the strongest sections of the article is the dataset discussion.

        The paper highlights that GoEmotions is hard because:

        - it has **28 labels** including `neutral`
        - comments can have **multiple labels**
        - the label distribution is **highly imbalanced**
        - some labels are semantically close, such as `sadness` vs `grief`

        The next few sections recreate that argument visually.
        """
    ),
    code(
        """
        def label_count_series(df):
            counts = np.zeros(len(EMOTION_NAMES), dtype=int)
            for labels in df["labels"]:
                counts[labels] += 1
            return pd.Series(counts, index=EMOTION_NAMES).sort_values(ascending=False)

        train_label_counts = label_count_series(train_df_full)

        display(train_label_counts.to_frame("train_count").head(10))

        plt.figure(figsize=(14, 8))
        sns.barplot(x=train_label_counts.values, y=train_label_counts.index, palette="viridis")
        plt.title("GoEmotions label frequency in the training split")
        plt.xlabel("Count")
        plt.ylabel("Emotion")
        plt.show()
        """
    ),
    code(
        """
        train_num_labels = train_df_full["labels"].apply(len).value_counts().sort_index()
        train_num_labels_pct = (train_num_labels / train_num_labels.sum() * 100).round(2)

        label_count_table = pd.DataFrame(
            {"count": train_num_labels, "percent": train_num_labels_pct}
        )
        display(label_count_table)

        plt.figure(figsize=(8, 4))
        sns.barplot(x=label_count_table.index, y=label_count_table["percent"], color="#4c72b0")
        plt.title("How many emotion labels each training example has")
        plt.xlabel("Number of labels on a comment")
        plt.ylabel("Percent of training examples")
        plt.show()
        """
    ),
    code(
        """
        cooc = np.zeros((len(EMOTION_NAMES), len(EMOTION_NAMES)), dtype=int)
        for labels in train_df_full["labels"]:
            for i in labels:
                for j in labels:
                    cooc[i, j] += 1

        top_labels = train_label_counts.head(12).index.tolist()
        top_idx = [EMOTION_NAMES.index(label) for label in top_labels]
        cooc_top = pd.DataFrame(
            cooc[np.ix_(top_idx, top_idx)],
            index=top_labels,
            columns=top_labels,
        )

        plt.figure(figsize=(10, 8))
        sns.heatmap(cooc_top, cmap="mako", annot=False)
        plt.title("Label co-occurrence among the 12 most frequent emotions")
        plt.show()
        """
    ),
    md(
        """
        ## Reading The EDA Through The Paper's Lens

        The paper argues that these patterns create different kinds of difficulty:

        - **Imbalance** makes it easy for a model to look strong on common labels while failing on rare ones.
        - **Multi-label overlap** means independent predictions are imperfect, because some emotions appear together.
        - **Fine-grained semantic boundaries** make this more than a keyword lookup problem.

        That is exactly why the paper reports both **Micro-F1** and **Macro-F1**:

        - **Micro-F1** rewards overall correctness and is influenced heavily by common labels.
        - **Macro-F1** averages across labels equally, so weak rare-label performance hurts more.
        """
    ),
    md(
        """
        # Part 1: Test The Paper's Lexical-Cue Claim

        The paper reports that TF-IDF + logistic regression achieved the strongest **Micro-F1** in its experiments. That is surprising if you assume the most modern model must always win.

        The paper's explanation is:

        > frequent emotions often rely on surface lexical cues

        This section tests that idea directly.

        We will:

        1. train a one-vs-rest logistic regression baseline
        2. inspect Micro-F1 vs Macro-F1
        3. examine the highest-weighted n-grams for selected labels
        """
    ),
    code(
        """
        def maybe_limit_df(df, limit):
            if limit is None or limit >= len(df):
                return df.copy()
            return df.sample(n=limit, random_state=SEED).reset_index(drop=True)

        train_df = maybe_limit_df(train_df_full, LOGREG_TRAIN_LIMIT)
        val_df = maybe_limit_df(val_df_full, LOGREG_VAL_LIMIT)
        test_df = maybe_limit_df(test_df_full, LOGREG_TEST_LIMIT)

        mlb = MultiLabelBinarizer(classes=list(range(len(EMOTION_NAMES))))
        y_train = mlb.fit_transform(train_df["labels"])
        y_val = mlb.transform(val_df["labels"])
        y_test = mlb.transform(test_df["labels"])

        print("Logistic train shape:", y_train.shape)
        print("Logistic val shape:", y_val.shape)
        print("Logistic test shape:", y_test.shape)
        """
    ),
    code(
        """
        tfidf = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            min_df=3,
            max_features=50000,
        )

        X_train = tfidf.fit_transform(train_df["text"])
        X_val = tfidf.transform(val_df["text"])
        X_test = tfidf.transform(test_df["text"])

        logreg = OneVsRestClassifier(
            LogisticRegression(
                solver="liblinear",
                max_iter=1000,
                class_weight="balanced",
            ),
            n_jobs=-1,
        )

        logreg.fit(X_train, y_train)
        logreg_val_probs = logreg.predict_proba(X_val)
        logreg_test_probs = logreg.predict_proba(X_test)

        print("TF-IDF matrix shape:", X_train.shape)
        """
    ),
    code(
        """
        def multilabel_metrics(y_true, y_pred):
            return {
                "subset_accuracy": accuracy_score(y_true, y_pred),
                "micro_f1": f1_score(y_true, y_pred, average="micro", zero_division=0),
                "macro_f1": f1_score(y_true, y_pred, average="macro", zero_division=0),
                "hamming_loss": hamming_loss(y_true, y_pred),
            }

        def metrics_frame(result_dict):
            return (
                pd.DataFrame(result_dict)
                .T.reset_index()
                .rename(columns={"index": "split"})
                .round(4)
            )

        def per_label_frame(y_true, y_pred):
            precision, recall, f1, support = precision_recall_fscore_support(
                y_true,
                y_pred,
                average=None,
                zero_division=0,
            )
            return pd.DataFrame(
                {
                    "label": EMOTION_NAMES,
                    "precision": precision,
                    "recall": recall,
                    "f1": f1,
                    "support": support,
                }
            ).sort_values("f1", ascending=False)

        default_thresholds = np.full(len(EMOTION_NAMES), 0.5)
        logreg_val_pred_default = (logreg_val_probs >= default_thresholds).astype(int)
        logreg_test_pred_default = (logreg_test_probs >= default_thresholds).astype(int)

        logreg_results_default = {
            "validation": multilabel_metrics(y_val, logreg_val_pred_default),
            "test": multilabel_metrics(y_test, logreg_test_pred_default),
        }

        display(metrics_frame(logreg_results_default))
        """
    ),
    md(
        """
        ## What To Look For In The Baseline Results

        Compare the validation and test scores with the paper's interpretation:

        - If **Micro-F1** is meaningfully stronger than **Macro-F1**, that supports the paper's argument that the model handles common labels better than rare ones.
        - If **Subset Accuracy** is much lower than the F1 scores, that is normal in multi-label tasks because exact-set prediction is strict.
        - If **Hamming Loss** looks reasonably small while Macro-F1 is mediocre, that tells you many binary decisions are fine even though rare-label balance is still hard.
        """
    ),
    code(
        """
        feature_names = np.array(tfidf.get_feature_names_out())

        def top_ngrams_for_label(label_name, n=15):
            idx = EMOTION_NAMES.index(label_name)
            estimator = logreg.estimators_[idx]
            coefs = estimator.coef_[0]
            top_idx = np.argsort(coefs)[-n:][::-1]
            return pd.DataFrame(
                {
                    "ngram": feature_names[top_idx],
                    "weight": coefs[top_idx],
                }
            )

        for label in ["gratitude", "grief", "admiration", "anger"]:
            print(f"Top n-grams for {label}")
            display(top_ngrams_for_label(label))
        """
    ),
    md(
        """
        ## Why The Top N-Grams Matter

        This is one of the clearest ways to test the paper's lexical-cue story.

        If the top weighted n-grams for labels like `gratitude`, `grief`, or `anger` look intuitively emotion-bearing, then the baseline is doing something real, not just getting lucky.

        You should expect many strong lexical cues such as:

        - gratitude words for `gratitude`
        - loss or condolence language for `grief`
        - praise-related phrases for `admiration`
        - explicit negative wording for `anger`

        That is the exact mechanism the paper suggests when it says logistic regression can perform surprisingly well on frequent labels.
        """
    ),
    code(
        """
        USER_TEXTS = [
            "Thank you so much, this was exactly what I needed.",
            "I still cannot believe he is gone. Rest in peace.",
            "This made me laugh way harder than it should have.",
            "I am furious that they ignored the warning signs.",
            "I did not expect that ending at all, but now it makes sense.",
        ]

        def decode_predictions(prob_row, thresholds, top_k=5):
            pairs = [
                (EMOTION_NAMES[i], float(prob_row[i]))
                for i in range(len(EMOTION_NAMES))
                if prob_row[i] >= thresholds[i]
            ]
            pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
            return pairs[:top_k]

        X_user = tfidf.transform(USER_TEXTS)
        user_probs = logreg.predict_proba(X_user)

        for text, probs in zip(USER_TEXTS, user_probs):
            print("TEXT:", text)
            print("Predicted labels:", decode_predictions(probs, default_thresholds))
            print()
        """
    ),
    md(
        """
        # Part 2: Test The Paper's Future-Work Idea On Threshold Tuning

        Near the end, the paper suggests that **per-label threshold calibration** could improve the balance between precision and recall.

        That idea is important because a single default threshold of `0.5` assumes every label behaves the same way. But in an imbalanced multi-label problem:

        - some labels are common
        - some labels are rare
        - probability calibration is uneven across labels

        So this section asks:

        **Can we improve Macro-F1 by choosing a separate threshold for each emotion on the validation split?**
        """
    ),
    code(
        """
        def find_best_thresholds(y_true, probs, grid=None):
            if grid is None:
                grid = np.linspace(0.1, 0.9, 17)

            best_thresholds = np.full(probs.shape[1], 0.5)
            best_scores = np.zeros(probs.shape[1])

            for label_idx in range(probs.shape[1]):
                label_true = y_true[:, label_idx]
                label_probs = probs[:, label_idx]
                best_f1 = -1.0
                best_t = 0.5

                for t in grid:
                    label_pred = (label_probs >= t).astype(int)
                    score = f1_score(label_true, label_pred, zero_division=0)
                    if score > best_f1:
                        best_f1 = score
                        best_t = t

                best_thresholds[label_idx] = best_t
                best_scores[label_idx] = best_f1

            return best_thresholds, best_scores

        tuned_thresholds_logreg, tuned_label_f1_logreg = find_best_thresholds(y_val, logreg_val_probs)
        logreg_val_pred_tuned = (logreg_val_probs >= tuned_thresholds_logreg).astype(int)
        logreg_test_pred_tuned = (logreg_test_probs >= tuned_thresholds_logreg).astype(int)

        logreg_results_tuned = {
            "validation_default": multilabel_metrics(y_val, logreg_val_pred_default),
            "validation_tuned": multilabel_metrics(y_val, logreg_val_pred_tuned),
            "test_default": multilabel_metrics(y_test, logreg_test_pred_default),
            "test_tuned": multilabel_metrics(y_test, logreg_test_pred_tuned),
        }

        display(metrics_frame(logreg_results_tuned))
        """
    ),
    code(
        """
        threshold_table = pd.DataFrame(
            {
                "label": EMOTION_NAMES,
                "threshold": tuned_thresholds_logreg,
                "val_label_f1_at_best_threshold": tuned_label_f1_logreg,
                "train_support": [train_label_counts[label] for label in EMOTION_NAMES],
            }
        ).sort_values("threshold")

        display(threshold_table.head(12))
        display(threshold_table.tail(12))
        """
    ),
    md(
        """
        ## How To Interpret Threshold Tuning

        If tuned thresholds improve **Macro-F1** more than **Micro-F1**, that strongly supports the paper's future-work suggestion.

        Why?

        - Micro-F1 is already helped by common labels.
        - Rare labels often need thresholds below or above `0.5`.
        - Per-label tuning is a cheap way to handle imbalance better without changing the model architecture.

        This section is especially useful because it moves beyond "what the paper reported" into "what the paper suggested next."
        """
    ),
    code(
        """
        logreg_label_default = per_label_frame(y_test, logreg_test_pred_default).rename(
            columns={"precision": "precision_default", "recall": "recall_default", "f1": "f1_default"}
        )
        logreg_label_tuned = per_label_frame(y_test, logreg_test_pred_tuned).rename(
            columns={"precision": "precision_tuned", "recall": "recall_tuned", "f1": "f1_tuned"}
        )

        logreg_label_compare = logreg_label_default.merge(
            logreg_label_tuned[["label", "precision_tuned", "recall_tuned", "f1_tuned"]],
            on="label",
        )
        logreg_label_compare["f1_gain"] = (
            logreg_label_compare["f1_tuned"] - logreg_label_compare["f1_default"]
        )
        logreg_label_compare["support"] = [
            train_label_counts[label] for label in logreg_label_compare["label"]
        ]

        display(logreg_label_compare.sort_values("f1_gain", ascending=False).head(12))
        """
    ),
    md(
        """
        # Part 3: Test The Paper's Contextual-Model Claim

        The paper's strongest claim is not that BERT wins every metric. It is more nuanced:

        - lexical models can be very strong on obvious cues
        - contextual models do better overall, especially on rarer and more ambiguous emotions

        A full BERT reproduction can be heavy in Colab, so this notebook uses **DistilBERT** as a practical proxy. That means:

        - it is **not** a byte-for-byte reproduction of the paper
        - it **is** a good test of the paper's broader hypothesis about contextual representations

        If you have no GPU, you can skip this section and still learn a lot from the notebook.
        """
    ),
    code(
        """
        def maybe_limit_hf_split(ds, limit):
            if limit is None or limit >= len(ds):
                return ds
            return ds.shuffle(seed=SEED).select(range(limit))

        transformer_train_ds = maybe_limit_hf_split(goemotions["train"], TRANSFORMER_TRAIN_LIMIT)
        transformer_val_ds = maybe_limit_hf_split(goemotions["validation"], TRANSFORMER_VAL_LIMIT)
        transformer_test_ds = maybe_limit_hf_split(goemotions["test"], TRANSFORMER_TEST_LIMIT)

        tokenizer = AutoTokenizer.from_pretrained(TRANSFORMER_MODEL_NAME)

        def encode_batch(batch):
            encoded = tokenizer(
                batch["text"],
                truncation=True,
                max_length=MAX_LENGTH,
            )

            labels = np.zeros((len(batch["labels"]), len(EMOTION_NAMES)), dtype=np.float32)
            for row_idx, label_ids in enumerate(batch["labels"]):
                labels[row_idx, [int(x) for x in label_ids]] = 1.0

            encoded["labels"] = labels.tolist()
            return encoded

        tokenized_train = transformer_train_ds.map(
            encode_batch,
            batched=True,
            remove_columns=transformer_train_ds.column_names,
        )
        tokenized_val = transformer_val_ds.map(
            encode_batch,
            batched=True,
            remove_columns=transformer_val_ds.column_names,
        )
        tokenized_test = transformer_test_ds.map(
            encode_batch,
            batched=True,
            remove_columns=transformer_test_ds.column_names,
        )

        data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

        print(tokenized_train)
        """
    ),
    code(
        """
        def sigmoid(x):
            return 1 / (1 + np.exp(-x))

        def compute_metrics_transformer(eval_pred):
            logits, labels = eval_pred
            probs = sigmoid(logits)
            preds = (probs >= 0.5).astype(int)
            metrics = multilabel_metrics(labels, preds)
            return {k: float(v) for k, v in metrics.items()}

        model = AutoModelForSequenceClassification.from_pretrained(
            TRANSFORMER_MODEL_NAME,
            num_labels=len(EMOTION_NAMES),
            problem_type="multi_label_classification",
        )

        training_args = TrainingArguments(
            output_dir="tmp_goemotions_transformer",
            learning_rate=2e-5,
            per_device_train_batch_size=16,
            per_device_eval_batch_size=32,
            num_train_epochs=NUM_EPOCHS,
            weight_decay=0.01,
            evaluation_strategy="epoch",
            save_strategy="no",
            logging_steps=50,
            report_to="none",
            fp16=torch.cuda.is_available(),
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=tokenized_train,
            eval_dataset=tokenized_val,
            tokenizer=tokenizer,
            data_collator=data_collator,
            compute_metrics=compute_metrics_transformer,
        )
        """
    ),
    code(
        """
        if RUN_TRANSFORMER:
            trainer.train()
            transformer_val_output = trainer.predict(tokenized_val)
            transformer_test_output = trainer.predict(tokenized_test)

            transformer_val_probs = sigmoid(transformer_val_output.predictions)
            transformer_test_probs = sigmoid(transformer_test_output.predictions)
            transformer_y_val = transformer_val_output.label_ids.astype(int)
            transformer_y_test = transformer_test_output.label_ids.astype(int)

            transformer_val_pred_default = (transformer_val_probs >= 0.5).astype(int)
            transformer_test_pred_default = (transformer_test_probs >= 0.5).astype(int)

            transformer_results_default = {
                "validation": multilabel_metrics(transformer_y_val, transformer_val_pred_default),
                "test": multilabel_metrics(transformer_y_test, transformer_test_pred_default),
            }

            display(metrics_frame(transformer_results_default))
        else:
            print("Skipping transformer training because RUN_TRANSFORMER is False.")
        """
    ),
    md(
        """
        ## Why The Transformer Section Matters

        This section tests the paper's second big claim:

        **Contextual models should be better balanced across labels, especially rare or ambiguous ones.**

        In practical terms, here are the questions to ask:

        - Does the transformer close the gap between Micro-F1 and Macro-F1?
        - Does it improve per-label F1 for rare emotions?
        - Does it make fewer "keyword-only" mistakes?

        Even if the transformer does not dominate every metric in your run, that does not refute the paper. Small-sample Colab experiments have more variance. What matters is the **pattern**.
        """
    ),
    code(
        """
        if RUN_TRANSFORMER:
            tuned_thresholds_transformer, tuned_label_f1_transformer = find_best_thresholds(
                transformer_y_val,
                transformer_val_probs,
            )

            transformer_test_pred_tuned = (
                transformer_test_probs >= tuned_thresholds_transformer
            ).astype(int)

            transformer_results_compare = {
                "test_default": multilabel_metrics(transformer_y_test, transformer_test_pred_default),
                "test_tuned": multilabel_metrics(transformer_y_test, transformer_test_pred_tuned),
            }

            display(metrics_frame(transformer_results_compare))
        else:
            print("Transformer threshold tuning skipped.")
        """
    ),
    code(
        """
        if RUN_TRANSFORMER:
            transformer_test_raw_df = pd.DataFrame(
                {
                    "text": transformer_test_ds["text"],
                    "labels": [normalize_labels(x) for x in transformer_test_ds["labels"]],
                }
            )

            shared_y_test = mlb.transform(transformer_test_raw_df["labels"])
            X_test_shared = tfidf.transform(transformer_test_raw_df["text"])
            logreg_shared_probs = logreg.predict_proba(X_test_shared)
            logreg_shared_pred_tuned = (logreg_shared_probs >= tuned_thresholds_logreg).astype(int)

            shared_metrics = {
                "logreg_on_transformer_test_subset": multilabel_metrics(shared_y_test, logreg_shared_pred_tuned),
                "transformer_on_same_subset": multilabel_metrics(transformer_y_test, transformer_test_pred_tuned),
            }
            display(metrics_frame(shared_metrics))

            comparison_df = per_label_frame(shared_y_test, logreg_shared_pred_tuned)[
                ["label", "f1", "support"]
            ].rename(columns={"f1": "logreg_f1"})

            transformer_label_frame = per_label_frame(transformer_y_test, transformer_test_pred_tuned)[
                ["label", "f1", "support"]
            ].rename(columns={"f1": "transformer_f1", "support": "transformer_support"})
            comparison_df = comparison_df.merge(transformer_label_frame[["label", "transformer_f1"]], on="label")
        else:
            comparison_df = per_label_frame(y_test, logreg_test_pred_tuned)[
                ["label", "f1", "support"]
            ].rename(columns={"f1": "logreg_f1"})

        comparison_df = comparison_df.sort_values("support", ascending=False)
        display(comparison_df.head(15))
        """
    ),
    code(
        """
        plot_df = comparison_df.copy()

        plt.figure(figsize=(12, 7))
        plt.scatter(
            plot_df["support"],
            plot_df["logreg_f1"],
            label="LogReg (tuned thresholds)",
            s=80,
            alpha=0.8,
        )

        if "transformer_f1" in plot_df.columns:
            plt.scatter(
                plot_df["support"],
                plot_df["transformer_f1"],
                label="Transformer (tuned thresholds)",
                s=80,
                alpha=0.8,
            )

        for _, row in plot_df.iterrows():
            plt.text(row["support"], row["logreg_f1"] + 0.01, row["label"], fontsize=9)

        plt.xscale("log")
        plt.xlabel("Training support (log scale)")
        plt.ylabel("Per-label F1")
        plt.title("How label frequency relates to F1")
        plt.legend()
        plt.show()
        """
    ),
    md(
        """
        ## Reading The Frequency-vs-F1 Plot

        This visualization goes straight at one of the paper's central claims:

        - common labels are easier
        - rare labels are harder
        - contextual models should help more on the harder tail

        If you see the transformer curve pulling upward on lower-support labels, that is the paper's argument in picture form.
        """
    ),
    code(
        """
        RARE_LABELS = ["grief", "relief", "pride", "embarrassment", "nervousness"]
        display(
            comparison_df[comparison_df["label"].isin(RARE_LABELS)].sort_values("label")
        )
        """
    ),
    code(
        """
        if RUN_TRANSFORMER:
            def labels_from_binary_row(row):
                return [EMOTION_NAMES[i] for i, v in enumerate(row) if v == 1]

            disagreements = []
            shared_n = min(len(transformer_test_raw_df), len(transformer_y_test))

            for i in range(shared_n):
                if not np.array_equal(logreg_shared_pred_tuned[i], transformer_test_pred_tuned[i]):
                    disagreements.append(
                        {
                            "text": transformer_test_raw_df.iloc[i]["text"],
                            "gold": labels_from_binary_row(transformer_y_test[i]),
                            "logreg": labels_from_binary_row(logreg_shared_pred_tuned[i]),
                            "transformer": labels_from_binary_row(transformer_test_pred_tuned[i]),
                        }
                    )

            disagreement_df = pd.DataFrame(disagreements)
            display(disagreement_df.head(10))
        else:
            print("Disagreement analysis requires transformer predictions.")
        """
    ),
    md(
        """
        # Part 4: What We Learned Relative To The Paper

        At this point you should be able to answer the paper's main questions from your own run:

        1. **Are lexical cues enough to get a strong baseline?**
        2. **Does Macro-F1 reveal weaknesses hidden by Micro-F1?**
        3. **Do contextual models help on difficult or rare labels?**
        4. **Does threshold tuning improve balance across labels?**

        This is the core difference between a passive reading of the article and an experimental reading of the article.
        """
    ),
    md(
        """
        ## Optional Extension: Add The Missing BiLSTM Section

        The original paper includes a BiLSTM + attention model. This notebook omits that implementation to stay practical in Colab, but if you want to extend the notebook toward a fuller reproduction, this is the natural next step.

        A good BiLSTM extension would:

        - tokenize the text at the word level
        - initialize embeddings with GloVe or a lighter pretrained matrix
        - use a bidirectional LSTM encoder
        - add an attention pooling layer
        - predict a 28-dimensional multi-label output with sigmoid activations

        That extension would help answer a sharper question:

        **Was the paper's BiLSTM underperformance caused by the recurrent architecture itself, or by the use of static word embeddings?**
        """
    ),
    md(
        """
        ## Suggested Follow-Up Experiments

        If you want to keep exploring the paper, these are the best next experiments:

        1. Use the full official splits instead of quick mode.
        2. Swap `distilbert-base-uncased` for `bert-base-uncased`.
        3. Add a BiLSTM baseline.
        4. Compare `0.5` thresholds, tuned thresholds, and class-dependent heuristics.
        5. Build a classifier-chain baseline to test the paper's label-dependency suggestion.
        6. Add qualitative analysis for pairs like `sadness` vs `grief` or `approval` vs `admiration`.
        7. Test the models on your own Reddit-style or journaling text.
        """
    ),
    md(
        """
        ## Reflection Questions

        Use these after you run the notebook:

        - Which emotions seem to be almost keyword-driven?
        - Which emotions seem to require broader context?
        - Where does Micro-F1 give a misleadingly optimistic picture?
        - Did threshold tuning help mostly frequent labels, rare labels, or both?
        - If the transformer wins, *why* does it win?
        - If the transformer does not clearly win in your run, is that because the paper is wrong, or because your Colab setup is a smaller, noisier experiment?
        """
    ),
]


notebook = {
    "cells": cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "name": "python",
            "version": "3.11",
        },
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}


NOTEBOOK_PATH.parent.mkdir(parents=True, exist_ok=True)
NOTEBOOK_PATH.write_text(json.dumps(notebook, indent=2) + "\n")
print(f"Wrote {NOTEBOOK_PATH}")

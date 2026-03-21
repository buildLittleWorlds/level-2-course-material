import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "bonus-fine-tuning" / "nostalgia_finetune_colab.ipynb"


def lines(text: str) -> list[str]:
    text = dedent(text).strip("\n")
    return [line + "\n" for line in text.splitlines()]


def markdown_cell(text: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": lines(text),
    }


def code_cell(text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": lines(text),
    }


NOTEBOOK = {
    "cells": [
        markdown_cell(
            """
            # Nostalgia Comment Classifier: Colab Fine-Tuning Demo

            [Dataset](https://huggingface.co/datasets/Senem/Nostalgic_Sentiment_Analysis_of_YouTube_Comments_Data) |
            [Base model](https://huggingface.co/distilbert-base-uncased) |
            [Your HF profile](https://huggingface.co/profplate)

            This notebook fine-tunes a small text classifier on nostalgic vs. non-nostalgic YouTube comments, then optionally pushes the trained model to your Hugging Face profile.
            """
        ),
        markdown_cell(
            """
            ## Why this version should work

            The pasted draft was close, but it made a few assumptions that are risky in class:

            - The dataset text column is `comment`, not `text`.
            - The labels are strings in a single `train` split, so we create a stratified train/test split ourselves.
            - We map labels explicitly so `not nostalgia = 0` and `nostalgia = 1`.
            - The Hub upload is optional, so training can still succeed even if you skip login.

            Recommended runtime:

            - GPU runtime in Colab: usually about 3-6 minutes for training
            - CPU runtime: usually about 20-30 minutes
            """
        ),
        code_cell(
            """
            # Setup - run this first
            !pip install -q -U transformers datasets accelerate scikit-learn huggingface_hub
            """
        ),
        code_cell(
            """
            import numpy as np
            import pandas as pd
            import torch

            from datasets import DatasetDict, load_dataset
            from huggingface_hub import login
            from sklearn.metrics import (
                accuracy_score,
                classification_report,
                confusion_matrix,
                precision_recall_fscore_support,
            )
            from sklearn.model_selection import train_test_split
            from transformers import (
                AutoModelForSequenceClassification,
                AutoTokenizer,
                DataCollatorWithPadding,
                Trainer,
                TrainingArguments,
                pipeline,
                set_seed,
            )

            set_seed(42)

            DATASET_ID = "Senem/Nostalgic_Sentiment_Analysis_of_YouTube_Comments_Data"
            BASE_MODEL = "distilbert-base-uncased"
            REPO_ID = "profplate/distilbert-nostalgia-youtube-comments"
            OUTPUT_DIR = "nostalgia-distilbert-checkpoints"
            FINAL_DIR = "final_nostalgia_model"
            MAX_LENGTH = 128
            TEST_SIZE = 0.2

            LABEL2ID = {
                "not nostalgia": 0,
                "nostalgia": 1,
            }
            ID2LABEL = {idx: label for label, idx in LABEL2ID.items()}

            device = "cuda" if torch.cuda.is_available() else "cpu"
            print(f"Using device: {device}")
            print(f"Model will be pushed to: https://huggingface.co/{REPO_ID}")
            """
        ),
        markdown_cell(
            """
            ## Load the dataset and inspect it

            This dataset has one split with 1,500 rows and two columns:

            - `comment`
            - `sentiment`
            """
        ),
        code_cell(
            """
            raw_train = load_dataset(DATASET_ID, split="train")
            print(raw_train)

            df = raw_train.to_pandas()
            display(df["sentiment"].value_counts().rename("count").to_frame())
            display(df.sample(5, random_state=42))
            """
        ),
        markdown_cell(
            """
            ## Build a train/test split

            We stratify on the string labels so both classes stay balanced across train and test.
            """
        ),
        code_cell(
            """
            indices = np.arange(len(raw_train))
            train_idx, test_idx = train_test_split(
                indices,
                test_size=TEST_SIZE,
                random_state=42,
                stratify=raw_train["sentiment"],
            )

            splits = DatasetDict(
                {
                    "train": raw_train.select(train_idx),
                    "test": raw_train.select(test_idx),
                }
            )

            def add_numeric_label(example):
                example["labels"] = LABEL2ID[example["sentiment"]]
                return example

            splits = splits.map(add_numeric_label)

            for split_name in splits:
                split_df = splits[split_name].to_pandas()
                print(f"\\n{split_name.upper()} label counts")
                print(split_df["sentiment"].value_counts())
            """
        ),
        markdown_cell(
            """
            ## Tokenize the comments
            """
        ),
        code_cell(
            """
            tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)

            def tokenize_batch(batch):
                return tokenizer(
                    batch["comment"],
                    truncation=True,
                    max_length=MAX_LENGTH,
                )

            tokenized_splits = splits.map(tokenize_batch, batched=True)
            data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
            tokenized_splits
            """
        ),
        markdown_cell(
            """
            ## Load the model and define evaluation metrics
            """
        ),
        code_cell(
            """
            model = AutoModelForSequenceClassification.from_pretrained(
                BASE_MODEL,
                num_labels=2,
                id2label=ID2LABEL,
                label2id=LABEL2ID,
            )

            def compute_metrics(eval_pred):
                logits, labels = eval_pred
                predictions = np.argmax(logits, axis=-1)
                precision, recall, f1, _ = precision_recall_fscore_support(
                    labels,
                    predictions,
                    average="binary",
                )
                accuracy = accuracy_score(labels, predictions)
                return {
                    "accuracy": accuracy,
                    "precision": precision,
                    "recall": recall,
                    "f1": f1,
                }
            """
        ),
        markdown_cell(
            """
            ## Train

            This is a baseline classroom setup: lightweight model, short sequence length, small number of epochs.
            """
        ),
        code_cell(
            """
            training_args = TrainingArguments(
                output_dir=OUTPUT_DIR,
                learning_rate=2e-5,
                per_device_train_batch_size=16,
                per_device_eval_batch_size=16,
                num_train_epochs=3,
                weight_decay=0.01,
                evaluation_strategy="epoch",
                save_strategy="epoch",
                load_best_model_at_end=True,
                metric_for_best_model="f1",
                greater_is_better=True,
                save_total_limit=1,
                fp16=torch.cuda.is_available(),
                push_to_hub=False,
                hub_model_id=REPO_ID,
                report_to="none",
            )

            trainer = Trainer(
                model=model,
                args=training_args,
                train_dataset=tokenized_splits["train"],
                eval_dataset=tokenized_splits["test"],
                tokenizer=tokenizer,
                data_collator=data_collator,
                compute_metrics=compute_metrics,
            )

            trainer
            """
        ),
        code_cell(
            """
            train_result = trainer.train()
            eval_metrics = trainer.evaluate()

            trainer.save_model(FINAL_DIR)
            tokenizer.save_pretrained(FINAL_DIR)

            print("Training finished.")
            print(eval_metrics)
            """
        ),
        markdown_cell(
            """
            ## Look at the results more closely
            """
        ),
        code_cell(
            """
            prediction_output = trainer.predict(tokenized_splits["test"])
            predicted_ids = np.argmax(prediction_output.predictions, axis=-1)
            true_ids = prediction_output.label_ids

            print(classification_report(true_ids, predicted_ids, target_names=[ID2LABEL[0], ID2LABEL[1]]))
            print("Confusion matrix:")
            print(confusion_matrix(true_ids, predicted_ids))
            """
        ),
        markdown_cell(
            """
            ## Try the model on fresh comments

            Edit these examples or add your own.
            """
        ),
        code_cell(
            """
            classifier = pipeline(
                "text-classification",
                model=trainer.model,
                tokenizer=tokenizer,
                truncation=True,
            )

            sample_comments = [
                "This song takes me right back to riding in my dad's truck in the summer.",
                "I just found this track today and the guitar solo is incredible.",
                "Hearing this again reminds me of my grandmother's kitchen when I was little.",
                "The production is clean, but the chorus feels repetitive to me.",
            ]

            for text in sample_comments:
                prediction = classifier(text)[0]
                print(f"Comment: {text}")
                print(f"Prediction: {prediction['label']} ({prediction['score']:.3f})")
                print("-" * 80)
            """
        ),
        markdown_cell(
            """
            ## Optional: push the model to your Hugging Face profile

            Before you run the next cells:

            1. Create a **write** token at https://huggingface.co/settings/tokens
            2. Log in below
            3. Run the push cell

            Your model repo will be:

            `https://huggingface.co/profplate/distilbert-nostalgia-youtube-comments`
            """
        ),
        code_cell(
            """
            login()
            """
        ),
        code_cell(
            """
            trainer.create_model_card(
                model_name=REPO_ID.split("/")[-1],
                language="en",
                tags=[
                    "text-classification",
                    "distilbert",
                    "education",
                    "nostalgia",
                    "youtube-comments",
                ],
                finetuned_from=BASE_MODEL,
                tasks="text-classification",
                dataset_tags=DATASET_ID,
                dataset=DATASET_ID,
            )

            hub_url = trainer.push_to_hub(
                commit_message="Add classroom nostalgia fine-tuning demo"
            )

            print(f"Model pushed to https://huggingface.co/{REPO_ID}")
            print(hub_url)
            """
        ),
        markdown_cell(
            """
            ## Share it with students

            Good sharing pattern:

            - Share the model repo on Hugging Face
            - Add a short note in the model card explaining the experiment
            - Link back to the Colab notebook from the model card
            - If you want a clickable demo, build a tiny Gradio Space that loads this model
            """
        ),
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "name": "python",
            "version": "3.10.0",
        },
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(NOTEBOOK, indent=2) + "\n")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

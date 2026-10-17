# Fintech Sentiment Analysis Thesis

## Folder Guide

- `Dataset/dataset/` contains the raw review exports.
- `Functions/` contains numbered processing notebooks and helper scripts.
- `Normalize/` contains `02_combined_data.csv`, the combined input for normalization and preprocessing.
- `Prepro/` contains the numbered normalization and preprocessing notebooks.
- `Normalized_Done/`, `CombinedLabelled/`, and `NormLabelled/` contain source batches and numbered combined handoffs.
- `Verified/` and `Sentiment/` contain the other labeling handoffs.
- `Model/` contains numbered training and comparison notebooks.
- `Output/` is the single collection point for numbered exports and deliverables. Archived duplicate/revision copies are under `Output/Archive/`; the old-order normalized CSV is under `Archive/pre_reorganization/`.

## Processing Flow

1. `Dataset/dataset.py` filters raw reviews into `Output/01_hasil_filter_*.csv`.
2. `Functions/02_combine_filtered_reviews.py` combines filtered reviews into `Normalize/02_combined_data.csv`.
3. `Functions/03_normalize_reviews.ipynb` writes normalized batches into `Normalized_Done/`; the combined result is `Normalized_Done/03_combined_normalized_done.csv`.
4. `Functions/04_preprocess_reviews.ipynb` writes the preprocessing workbooks to `Output/03_*`.
5. `Functions/05_label_reviews.ipynb` and `Functions/06_assign_sentiment.ipynb` handle the labeling workflows. Combined files are `CombinedLabelled/05_combined_labelled_all.csv` and `NormLabelled/05_combined_normlabelled.csv`.
6. `Output/04_final_preprocessed.xlsx` and `Output/04_final_normalized_preprocessed.xlsx` are the final model datasets.
7. `Model/09` through `Model/15` contain training overviews and Naive Bayes, SVM, and IndoBERT variants; `Model/16` compares precision-recall results.

The normalization notebook reads its API credential from the `OPENAI_API_KEY` environment variable.

## Numbered Output Files

`Output/01` contains filtered exports; `02` contains combined normalized data; `03` contains preprocessing workbooks; `04` contains final model datasets; `05` contains reproduction/validation exports. Model notebooks load the final workbooks from `Thesis/Output/` in Google Drive.

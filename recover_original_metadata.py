from pathlib import Path

import pandas as pd
from pandas.errors import EmptyDataError


ROOT = Path(__file__).resolve().parent
PREPROCESSED_FILE = ROOT / "final_normalized_preprocessed.xlsx"
RAW_DATA_DIR = ROOT / "Dataset" / "dataset"
FILTERED_DATA_DIR = ROOT / "Output"
OUTPUT_FILE = ROOT / "recovered_original_metadata.xlsx"


def load_original_reviews() -> pd.DataFrame:
    frames = []
    for path in sorted(RAW_DATA_DIR.glob("*.csv")):
        try:
            frame = pd.read_csv(path, encoding="utf-8-sig")
        except EmptyDataError:
            continue
        frame["application"] = path.name.split("_googleplay_", 1)[0]
        frames.append(
            frame[["reviewId", "content", "application"]].rename(
                columns={"content": "original_review"}
            )
        )

    if not frames:
        raise FileNotFoundError(f"No raw CSV files found in {RAW_DATA_DIR}")

    return (
        pd.concat(frames, ignore_index=True)
        .drop_duplicates(subset="reviewId", keep="first")
    )


def load_keywords() -> pd.DataFrame:
    frames = []
    for path in sorted(FILTERED_DATA_DIR.glob("hasil_filter_*.csv")):
        try:
            frame = pd.read_csv(path, encoding="utf-8-sig")
        except EmptyDataError:
            continue
        if {"reviewId", "keyword"}.issubset(frame.columns):
            frames.append(frame[["reviewId", "keyword"]])

    if not frames:
        raise FileNotFoundError(
            f"No filtered CSV files with reviewId and keyword found in {FILTERED_DATA_DIR}"
        )

    return (
        pd.concat(frames, ignore_index=True)
        .drop_duplicates(subset="reviewId", keep="first")
    )


def main() -> None:
    preprocessed = pd.read_excel(PREPROCESSED_FILE)
    original = load_original_reviews()
    keywords = load_keywords()

    result = (
        preprocessed.merge(original, on="reviewId", how="left", validate="one_to_one")
        .merge(keywords, on="reviewId", how="left", validate="one_to_one")
    )

    result.insert(0, "reviewId", result.pop("reviewId"))
    result.insert(1, "application", result.pop("application"))
    result.insert(2, "keyword", result.pop("keyword"))
    result.insert(3, "original_review", result.pop("original_review"))
    result.to_excel(OUTPUT_FILE, index=False)

    missing_original = result["original_review"].isna().sum()
    missing_keyword = result["keyword"].isna().sum()
    print(f"Saved {len(result)} rows to {OUTPUT_FILE}")
    print(f"Missing original reviews: {missing_original}")
    print(f"Missing keywords: {missing_keyword}")


if __name__ == "__main__":
    main()
import pandas as pd
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Read both datasets
combined_df = pd.read_csv(os.path.join(current_dir, "combined_data.csv"))
data_vermuk = pd.read_csv(os.path.join(current_dir, "Dataset/sample.csv"))

# Rename sample.csv to data_vermuk and save it
data_vermuk.to_csv(os.path.join(current_dir, "data_vermuk.csv"), index=False)

# Find reviewIds in data_vermuk that are NOT in combined_data
# Using reviewId as the key identifier
missing_review_ids = data_vermuk[~data_vermuk['reviewId'].isin(combined_df['reviewId'])][['reviewId']]

# Save to duplicate_vermuk.csv
missing_review_ids.to_csv(os.path.join(current_dir, "duplicate_vermuk.csv"), index=False)

# Display statistics
print(f"Records in data_vermuk: {len(data_vermuk)}")
print(f"Records in combined_data: {len(combined_df)}")
print(f"Missing reviewIds (not in combined_data): {len(missing_review_ids)}")
print(f"\nFiles saved:")
print(f"  - data_vermuk.csv")
print(f"  - duplicate_vermuk.csv (contains only missing reviewIds)")

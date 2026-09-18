import pandas as pd
import glob
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Find all CSV files with "hasil_filter_" pattern
csv_files = glob.glob(os.path.join(current_dir, "Output/hasil_filter_*.csv"))

# Debug: print found files
print(f"Current directory: {current_dir}")
print(f"Looking for files in: {os.path.join(current_dir, 'Output')}")
print(f"Found files: {csv_files}")

# Read and combine all CSV files
dfs = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(dfs, ignore_index=True)

# Remove duplicate data based on reviewId column
combined_df = combined_df.drop_duplicates(subset=['reviewId'], keep='first')

# Randomize the order of data
combined_df = combined_df.sample(frac=1).reset_index(drop=True)

# Display information
print(f"\nCombined DataFrame shape: {combined_df.shape}") #6028 rows
print(f"\nFirst few rows:\n{combined_df.head()}")

# Print frequency of each unique value in keyword column
print(f"\nKeyword frequency:\n{combined_df['keyword'].value_counts()}")

combined_df.to_csv("combined_data.csv", index=False)

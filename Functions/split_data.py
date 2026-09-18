import openpyxl
import pandas as pd
import os
import math

# Get the current directory
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Read the file
df = pd.read_csv(os.path.join(current_dir, "sentiment_combined_labelled_data.csv"))

# Define chunk size
chunk_size = 200

# Calculate number of chunks needed
num_chunks = math.ceil(len(df) / chunk_size)

print(f"Total records: {len(df)}")
print(f"Chunk size: {chunk_size}")
print(f"Number of files to create: {num_chunks}\n")

# Split and save each chunk
for i in range(num_chunks):
    start_idx = i * chunk_size
    end_idx = start_idx + chunk_size
    
    chunk_df = df[start_idx:end_idx]
    
    # Create filename with numerical suffix
    filename = f"combined_labelled{i + 1}.xlsx"
    filepath = os.path.join(current_dir, filename)
    
    chunk_df.to_excel(filepath, index=False)
    
    print(f"File {i + 1}: {filename} ({len(chunk_df)} rows)")

print(f"\nAll files saved successfully!")

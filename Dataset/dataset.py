import pandas as pd
import glob

import re
import nltk
from nltk.corpus import stopwords

# ============================================================
#                           LOAD DATA
# ============================================================

all_files = glob.glob("Dataset/dataset/*.csv")
# print("File ditemukan:", all_files)

df_list = []

for file in all_files:
    try:
        df_temp = pd.read_csv(file, encoding="utf-8-sig")
        df_temp["source"] = file  # tracking asal data
        df_list.append(df_temp)
        print(f"Successfully loaded: {file}")
    except pd.errors.EmptyDataError:
        print(f"Skipping empty or malformed file: {file}")
    except Exception as e:
        print(f"Error Loading {file}: {e}")

# CEK DAN GABUNGKAN FILE
if len(df_list) == 0:
    print("ERROR: Tidak ada file terbaca")
else:
    df = pd.concat(df_list, ignore_index=True)
    print("Berhasil! Shape:", df.shape)


# ============================================================
#                           FILTERING
# ============================================================

text_column = "content"
# pattern = r"\b(qris|top up|topup|verif|muka|wajah|transfer|trf|tf|login)\b"

#qris
# pattern = r"\b(qris)\b"
# kword = "qris"

#topup
# pattern = r"\b(top up|topup)\b"
# kword = "topup"

#vermuk
# pattern = r"\b(verif|muka|wajah)\b"
# kword = "vermuk"

#transfer
pattern = r"\b(transfer|trf|tf)\b"
kword = "transfer"

#login
pattern = r"\b(login)\b"
kword = "login"

df_qr = df[df[text_column].str.lower().str.contains(pattern, regex=True, na=False)]
df_qr['keyword'] = kword


print("Jumlah data:", len(df_qr))

df_qr.to_csv("Output/hasil_filter_login.csv", index=False)

# # ============================================================
# #                   TRADITIONAL PREPROCESSING
# # ============================================================

# nltk.download('stopwords')

# stop_words = set(stopwords.words('indonesian'))

# # CLEANING
# def clean_text(text):
#     text = str(text)

#     # 1. Hapus URL
#     text = re.sub(r'http\S+|www\S+', '', text)

#     # 2. Hapus mention (@username)
#     text = re.sub(r'@\w+', '', text)

#     # 3. Hapus hashtag (#)
#     text = re.sub(r'#', '', text)

#     # 4. Hapus angka
#     text = re.sub(r'\d+', '', text)

#     # 5. Hapus emoji & karakter non-ASCII
#     text = re.sub(r'[^\x00-\x7F]+', '', text)

#     # 6. Hapus tanda baca & karakter khusus
#     text = re.sub(r'[^\w\s]', '', text)

#     # 7. Rapikan spasi
#     text = re.sub(r'\s+', ' ', text).strip()

#     return text

# def preprocessing_traditional(text):
#     # Cleaning
#     text = clean_text(text)

#     # Case folding (lowercase)
#     text = text.lower()

#     # Tokenization
#     tokens = text.split()

#     # Stopword removal
#     tokens = [word for word in tokens if word not in stop_words]

#     return " ".join(tokens)

# df_qr["clean_text_traditional"] = df_qr[text_column].apply(preprocessing_traditional)

# df_qr.to_csv("Output/qris_traditional_preprocessing.csv", index=False)
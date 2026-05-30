import os
from kaggle.api.kaggle_api_extended import KaggleApi

# 1. 初始化 Kaggle API (它會去讀取我們等一下設定的環境變數)
api = KaggleApi()
api.authenticate()

# 2. 設定你要下載的資料集名稱（已根據你的截圖填入正確名稱）
dataset_name = 'sujaykapadnis/vehicle-type-image-dataset' 

print(f"🚀 開始下載資料集: {dataset_name} ...")

# 3. 下載並自動解壓縮到 data 資料夾
api.dataset_download_files(dataset_name, path='./data', unzip=True)

print("✨ 下載並解壓縮完成！照片已經乖乖躺在 data/ 資料夾底下了。")
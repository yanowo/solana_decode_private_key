import os
import base58
import json
from dotenv import load_dotenv

# 載入.env檔案中的環境變量
load_dotenv()

# 從環境變數讀取Base58編碼的私鑰
base58_encoded_private_key = os.getenv("PRIVATE_KEY")

# 確保私鑰已經提供
if base58_encoded_private_key is None:
    raise ValueError("私鑰未在.env檔中設定")

# 解碼Base58編碼的私鑰
decoded_private_key = base58.b58decode(base58_encoded_private_key)

# 將位元組序列轉換為數字數組
private_key_array = list(decoded_private_key)

# 建立包含私鑰的JSON對象
private_key_json = json.dumps(private_key_array, separators=(",", ":"))

# 將JSON物件寫入文件
with open("id.json", "w") as key_file:
    key_file.write(private_key_json)

print("私鑰已儲存為 id.json")

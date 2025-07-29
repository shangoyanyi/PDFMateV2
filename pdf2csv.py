import os
import re
import sys
import pandas as pd
from PyPDF2 import PdfReader
from datetime import datetime

def write_log(log_path, message):
    """將訊息寫入 log 檔案"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def pdf_to_csv(pdf_path):
    log_path = os.path.splitext(pdf_path)[0] + ".log"

    if not os.path.isfile(pdf_path):
        write_log(log_path, f"❌ 找不到檔案: {pdf_path}")
        return

    try:
        write_log(log_path, f"🚀 開始轉換: {pdf_path}")

        reader = PdfReader(pdf_path)
        all_data = []
        columns = ["商品料號", "商品名稱", "出貨數", "退貨數", "進出貨數"]

        for page_num, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            rows = re.findall(r'(\d{8,})\s+([\w\W]+?)\s+(\d+)\s+(\d+)\s+(-?\d+)', text)
            write_log(log_path, f"📄 第 {page_num} 頁擷取到 {len(rows)} 筆資料")
            all_data.extend(rows)

        if not all_data:
            write_log(log_path, "⚠️ 沒有擷取到任何資料，請確認 PDF 格式是否符合規則")
        else:
            df = pd.DataFrame(all_data, columns=columns)
            csv_path = os.path.splitext(pdf_path)[0] + ".csv"
            df.to_csv(csv_path, index=False, encoding="utf-8-sig")
            write_log(log_path, f"✅ 轉換完成，CSV 檔案已產生：{csv_path}")

    except Exception as e:
        write_log(log_path, f"❌ 發生錯誤：{e}")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        pdf_to_csv(sys.argv[1])

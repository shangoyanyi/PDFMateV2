# PDFMate

**PDFMate** 是一款輕量化的 Windows 工具，讓使用者可以直接在檔案總管中使用右鍵功能來完成兩項常用操作：

1. 將 PDF 月結表 **轉換為 CSV**  
2. 對資料夾內的 PDF 進行 **自動配對整理**

---

## 🔧 功能特色

- 在 PDF 檔案上 **按右鍵 → 將月結表 PDF 轉換為 CSV 檔**
- 在資料夾空白處 **按右鍵 → PDF 配對整理**，會自動建立資料夾並將成對的 PDF 搬移進去
- 轉換結果會在同資料夾下產生：
  - 同名的 `.csv` 檔案
  - 同名的 `.log` 紀錄檔案
- PDF 配對整理功能也會產生 `pdfs_to_folders.log`，記錄每次的搬移結果
- 免管理員權限安裝（使用 HKCU 註冊表）
- 不需額外 GUI，適合搭配既有檔案管理流程使用

---

## 📁 專案檔案說明

| 檔案名稱           | 功能說明                                                |
|--------------------|-------------------------------------------------------|
| `pdf2csv.py`       | 將 PDF 月結表轉換為 CSV，並輸出 log                   |
| `pdf2folders.py`   | 將資料夾內 PDF 自動配對並整理到子資料夾              |
| `requirements.txt` | 套件清單（需包含 `pandas`、`PyPDF2`、`pymupdf`）      |
| `install.bat`      | 安裝工具：複製檔案並註冊右鍵選單功能                   |
| `uninstall.bat`    | 解除安裝工具：移除右鍵選單並刪除安裝檔案               |
| `README.md`        | 使用說明文件                                          |

---

## 🛠 安裝方式

1. **第一次使用**
   - 下載並安裝 python
   - 更新 install.bat 內 PYEXE 路徑指向的 python
   - 確認 requirements.txt 內的套件已安裝，或直接執行 install.bat 自動安裝

2. **執行 `install.bat`**
   - 會將檔案複製到 `%LOCALAPPDATA%\Programs\PDFMate\`
   - 會自動下載並安裝 `requirements.txt` 中的套件
   - 註冊右鍵選單功能

---

## 🧼 移除方式

1. 執行 `uninstall.bat`  
2. （選用）手動刪除 `%LOCALAPPDATA%\Programs\PDFMate\` 資料夾

---

## 🧠 注意事項

- 轉換及配對整理都會產生 `.log` 檔案記錄執行結果。
- 目前僅支援特定格式的 PDF 月結表，若無法擷取資料，請確認 PDF 是否為文字型檔案。

---

## 🔍 範例

### PDF 轉 CSV
```bash
python pdf2csv.py "D:\報表\測試月結表.pdf"
```

### PDF 配對整理
```bash
python pdf2folders.py "D:\報表\"
```

---

## 📎 授權
MIT — 可自由用於個人與商業用途。

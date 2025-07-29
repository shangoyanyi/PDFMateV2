# PDFMate

**PDFMate** 是一款輕量化的 Windows 工具，可讓你在檔案總管中直接透過右鍵功能，將 **PDF 月結表快速轉換為 CSV 檔案**。

這個工具特別適合需要頻繁將 PDF 表格資料轉換成 CSV 以供後續整理、比對或上傳的使用者，不需手動開啟 Python 或額外工具，直接在 PDF 上按右鍵即可完成。

---

## 🔧 功能特色

- 在 PDF 檔案上 **按右鍵 → 轉換 PDF → CSV**
- 會在 **同路徑下產生同名的 `.csv` 檔案**
- 同時會產生 **同名 `.log` 檔案**，記錄轉換過程與錯誤訊息
- 免管理員權限安裝（使用使用者層級註冊表 `HKCU`）
- 不需額外 GUI，適合搭配既有檔案管理流程使用

---

## 📁 專案檔案說明

| 檔案名稱           | 功能說明                                                |
|--------------------|-------------------------------------------------------|
| `pdf2csv.py`       | 核心 Python 腳本，負責解析 PDF 並輸出 CSV 與 log      |
| `requirements.txt` | 需安裝的套件清單（包含 `pandas`、`PyPDF2`）           |
| `install.bat`      | 安裝工具：複製檔案並註冊右鍵選單功能                   |
| `uninstall.bat`    | 解除安裝工具：移除右鍵選單並刪除安裝檔案               |
| `README.md`        | 使用說明文件                                          |

---

## 🛠 安裝方式

1. **確認已安裝 Python**，且路徑為：
   ```
   %LOCALAPPDATA%\Programs\Python\Python312\python.exe
   ```
   若路徑不同，請修改 `install.bat` 內的 `PYEXE` 變數。

2. 執行 `install.bat`  
   - 會將檔案複製到 `%LOCALAPPDATA%\Programs\PDFMate\`
   - 並自動安裝套件 (`requirements.txt`)

3. 在任意 PDF 檔案上 **按右鍵 → 轉換 PDF → CSV**  
   - 會在相同資料夾產生同名 `.csv` 與 `.log`。

---

## 🧼 移除方式

1. 執行 `uninstall.bat`  
2. （選用）手動刪除 `%LOCALAPPDATA%\Programs\PDFMate\` 資料夾

---

## 🧠 注意事項

- 轉換過程會在 **同資料夾下產生 `.log` 檔案**，記錄每次執行狀態與錯誤訊息。
- 目前僅支援特定格式的 PDF 月結表，若無法擷取資料，請檢查 PDF 是否為文字型檔案。
- 需安裝 `pandas` 與 `PyPDF2` 套件，`install.bat` 會自動處理。

---

## 🔍 範例（CLI 使用）

```bash
python pdf2csv.py "D:\報表\測試月結表.pdf"
```

執行後會在同資料夾產生：

- `測試月結表.csv`
- `測試月結表.log`

---

## 📎 授權
MIT — 可自由用於個人與商業用途。

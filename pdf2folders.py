import os
import shutil
import sys
import fitz  # pip install pymupdf
from datetime import datetime

def write_log(log_path, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def pt_to_mm(pt):
    return round(pt * 25.4 / 72, 1)

def is_scan_version(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        page = doc[0]
        width_mm = pt_to_mm(page.rect.width)
        height_mm = pt_to_mm(page.rect.height)
        return (width_mm, height_mm) == (210.1, 297.2) or (width_mm, height_mm) == (297.2, 210.1)
    except Exception:
        return False

def process_folder(folder_path):
    log_path = os.path.join(folder_path, "pdfs_to_folders.log")
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".pdf")]
    processed = set()

    for file in pdf_files:
        if file in processed:
            continue

        if "黏" in file or "粘" in file:
            base_name = file.replace("黏", "月").replace("粘", "月")
            match_file = base_name if base_name in pdf_files else None

            if match_file:
                scan_flag = is_scan_version(os.path.join(folder_path, file))
                folder_name = os.path.splitext(file)[0]
                if scan_flag:
                    folder_name += "_掃描檔"

                new_folder_path = os.path.join(folder_path, folder_name)
                os.makedirs(new_folder_path, exist_ok=True)

                shutil.move(os.path.join(folder_path, file), os.path.join(new_folder_path, file))
                shutil.move(os.path.join(folder_path, match_file), os.path.join(new_folder_path, match_file))

                write_log(log_path, f"✅ 已移動：{file} & {match_file} → {folder_name}")
                processed.update({file, match_file})

    write_log(log_path, "📦 所有配對完成。")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        process_folder(sys.argv[1])

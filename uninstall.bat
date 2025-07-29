@echo off
chcp 65001 >nul
setlocal

set "TARGETDIR=%LOCALAPPDATA%\Programs\PDFMate"

REM 移除右鍵選單：將月結表 PDF 轉換為 CSV 檔
reg delete "HKCU\Software\Classes\SystemFileAssociations\.pdf\shell\月結表PDF轉換為CSV檔" /f

REM 移除右鍵選單：PDF 配對整理
reg delete "HKCU\Software\Classes\Directory\Background\shell\月結表與黏存單PDF配對整理" /f

REM 刪除安裝目錄
if exist "%TARGETDIR%" (
    rmdir /S /Q "%TARGETDIR%"
    echo [OK] 已刪除安裝資料夾：%TARGETDIR%
) else (
    echo [INFO] 找不到安裝資料夾：%TARGETDIR%
)

echo [OK] PDFMate 已移除。
pause

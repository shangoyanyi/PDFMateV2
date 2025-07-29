@echo off
chcp 65001 >nul
setlocal

set "TARGETDIR=%LOCALAPPDATA%\Programs\PDFMate"

REM 移除右鍵選單
reg delete "HKCU\Software\Classes\SystemFileAssociations\.pdf\shell\PDF2CSV" /f

REM 刪除安裝目錄
if exist "%TARGETDIR%" (
    rmdir /S /Q "%TARGETDIR%"
    echo [OK] 已刪除安裝資料夾：%TARGETDIR%
) else (
    echo [INFO] 找不到安裝資料夾：%TARGETDIR%
)

echo [OK] PDFMate 已移除。
pause

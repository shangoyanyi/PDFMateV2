@echo off
chcp 65001 >nul
setlocal

REM 設定目標資料夾與 Python 執行檔
set "BASEDIR=%~dp0"
set "TARGETDIR=%LOCALAPPDATA%\Programs\PDFMate"
set "PYEXE=%LOCALAPPDATA%\Programs\Python\Python312\pythonw.exe"

REM 建立目標資料夾
if not exist "%TARGETDIR%" (
    mkdir "%TARGETDIR%"
)

REM 複製檔案到目標資料夾
xcopy /E /Y "%BASEDIR%*" "%TARGETDIR%" >nul


REM 安裝python依賴套件
echo [INFO] Installing dependencies...
:: "%PYEXE%" -m pip install --upgrade pip
"%PYEXE%" -m pip install -r "%TARGETDIR%\requirements.txt"


REM 註冊右鍵選單 (只針對 PDF 檔案)
reg add "HKCU\Software\Classes\SystemFileAssociations\.pdf\shell\PDF2CSV" /ve /d "將月結表 PDF 轉換為 CSV 檔" /f
reg add "HKCU\Software\Classes\SystemFileAssociations\.pdf\shell\PDF2CSV\command" /ve /d "\"%PYEXE%\" \"%TARGETDIR%\pdf2csv.py\" \"%%1\"" /f

echo.
echo [OK] PDFMate 安裝完成並已新增右鍵功能！
echo [PATH] 腳本安裝路徑: %TARGETDIR%
echo [PYTHON] 使用的 Python 執行檔: %PYEXE%
pause

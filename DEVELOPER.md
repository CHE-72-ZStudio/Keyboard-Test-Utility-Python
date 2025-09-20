# 「鍵盤檢測工具程式（Python）」的開發手冊
## Developer Manual for Keyboard Test Utility (Python)

## 0. 目錄

1. [環境需求 Environment Requirements](#1-環境需求-environment-requirements)
2. [安裝配置 Installation & Configuration](#2-安裝配置-installation--configuration)
3. [基本使用 Basic Usage](#3-基本使用-basic-usage)
4. [專案結構 Project Structure](#4-專案結構-project-structure)

---

## 1. 環境需求 Environment Requirements
- **作業系統**：
    - Microsoft Windows Vista+  
    - Apple macOS 10.9+  
    - Linux  
- **依賴套件**：  
    - Python 3.6+  
    - 本專案的 Python 模組需求已在 `Requirements.txt` 文件中列出。您可以使用 pip 安裝所有模組依賴： `pip install -r Requirements.txt`  

## 2. 安裝配置 Installation & Configuration
1. 從 GitHub 上的 [Releases](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/releases) 頁面下載本程式檔案的壓縮檔 `Source Code`，解壓縮後放置於適當的位置  
2. 確認解壓縮後的 `Main.py` 與程式運行時的其他必備檔案放置於同一文件夾路徑下  
3. 請確認您的電腦中已安裝 Python (>=3.6)，若是尚未安裝，可至 [Download Python](https://www.python.org/downloads/) 網頁下載安裝適合您作業系統的 Python 版本  
    > （若您已安裝完成合乎此程式要求的 Python 版本，可忽略這步驟）  
4. 在此文件夾路徑下開啟終端輸出程式，輸入 `pip install -r Requirements.txt`  
    >（若您已安裝完成此程式的必備模組依賴項，可忽略這步驟）  
5. 在該文件夾路徑中的終端窗口中輸入 `python Main.py` 以執行 `Main.py`  
6. 在 CLI 介面輸出必要資訊後會另外打開一個 GUI 視窗，將視窗焦點放在該 GUI 視窗上即可開始測試鍵盤按鍵  

## 3. 基本使用 Basic Usage
請參照 [USER.md](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/blob/main/USER.md) 文件中的第 3 章  

## 4. 專案結構 Project Structure
- `Main.py`：本程式的唯一入口與運行核心，處理視窗渲染、CLI 輸出、檔案寫入  
- `Studio.py`：存放簡短開源資訊與工作室 ASCII 藝術宣告  
- `NotoSansRegular.otf`：視窗文字顯示所使用的思源黑體繁體中文字型檔案，增強跨系統顯示能力  


### 鍵盤檢測工具程式（Python），著作權所有 (C) 2024-現在 CHE_72 ZStudio<br>鍵盤檢測工具程式（Python），著作權所有 (C) 2022-2023 CHE72
#### Keyboard Test Utility (Python), Copyright (C) 2024-present CHE_72 ZStudio.<br>Keyboard Test Utility (Python), Copyright (C) 2022-2023 CHE72.
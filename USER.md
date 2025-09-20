# 「鍵盤檢測工具程式（Python）」的用戶手冊
## User Manual for Keyboard Test Utility (Python)

## 0. 目錄

1. [環境需求](#1-環境需求)
2. [安裝配置](#2-安裝配置)
3. [基本使用](#3-基本使用)

---

## 1. 環境需求
- **作業系統**：
    - Microsoft Windows 7+ 64位元
    - Apple macOS 10.9+
    - Linux
- **系統/軟體解析度 > 1600×900**：
    - 1920×1080 125%: 1920÷1.25=1536, 1080÷1.25=864 ❌  
    - 2560×1440 150%: 2560÷1.5=1706.7, 1440÷1.5=960 ⭕  
    - 8192×4320 320%: 8192÷3.2=2560, 4320÷3.2=1350 ⭕  

## 2. 安裝配置
1. 從 GitHub 上的 [Releases](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/releases) 頁面下載對應系統的壓縮包 `KTUP-OS-X.Y.ZZ.zip`  
2. 將下載的壓縮包解壓縮後放置於適當的位置，**請不要任意編輯、刪除解壓縮後的檔案**  
3. 雙擊打開本程式的可執行二進制檔案 `KTUP-X.Y.ZZ-OS`，即可開始使用本程式  

## 3. 基本使用
1. 按照上方步驟開啟本程式的執行檔  
2. 程式在 CLI 介面輸出必要資訊後會另外打開一個 GUI 視窗  
3. 將視窗焦點放在該 GUI 視窗上，按下您想測試的鍵盤按鍵，此時視窗中應當出現您目前按下的按鍵名稱與累計按下次數  
    * 程式同時會將當下的日期、時間與按下的按鍵名稱、累積次數儲存在與主程式同資料夾下的 `KTUP_Records.log` 中，方便您日後可以隨時查詢之前的測試紀錄  
4. 如果測試完成，想要離開本程序，只需按下 GUI 視窗上的關閉按鈕即可  
5. 這時程式會在 CLI 介面中輸出一些資訊，在 CLI 介面中按下鍵盤上的任意按鍵即可完全結束運行並退出程式  


### 鍵盤檢測工具程式（Python），著作權所有 (C) 2024-現在 CHE_72 ZStudio<br>鍵盤檢測工具程式（Python），著作權所有 (C) 2022-2023 CHE72
#### Keyboard Test Utility (Python), Copyright (C) 2024-present CHE_72 ZStudio.<br>Keyboard Test Utility (Python), Copyright (C) 2022-2023 CHE72.
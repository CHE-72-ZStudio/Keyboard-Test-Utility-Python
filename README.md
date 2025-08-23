# 鍵盤檢測工具程式（Python）
## Keyboard Test Utility (Python) Made by CHE_72 ZStudio

## 狀態徽章 (Badges)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python)
    [![GitHub Release](https://img.shields.io/github/v/release/CHE-72-ZStudio/Keyboard-Test-Utility-Python)](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/releases)
    [![GitHub License](https://img.shields.io/github/license/CHE-72-ZStudio/Keyboard-Test-Utility-Python)](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/blob/main/LICENSE)
    [![GitHub Last Commit](https://img.shields.io/github/last-commit/CHE-72-ZStudio/Keyboard-Test-Utility-Python)](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/commits)
    [![Python 3.6+](https://img.shields.io/badge/Python%203.6+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org)
    [![PyCharm](https://img.shields.io/badge/PyCharm-000000.svg?logo=PyCharm&logoColor=white)](https://www.jetbrains.com/pycharm/)  
> 「Ask DeepWiki」功能為由 Devin AI 生成的 Wiki 文檔，每週自動刷新一次，內容可能與最新版程式有所差異  
> 該 AI 生成的 Wiki 文檔與回覆內容僅供參考，我們對其不負任何擔保責任，實際情形請依本儲存庫最新提交為準  

## 程式介紹 (Description)
「鍵盤檢測工具程式（Python）」是一款 GUI 程式，可以協助您判斷您鍵盤的健康情形。  
本檢測程式同時支援多媒體按鍵如音量增減、播放暫停的檢測，讓您可以檢測鍵盤是否能夠正確發送多媒體組合鍵的訊號。  

## 程式功能 (Features)
* 🖥 **易用的圖形介面**：透過 GUI 即時顯示按鍵名稱與按壓次數，協助您確認電腦是否有成功收到按鍵訊號，幫助您快速分析鍵盤按鍵的健康情形。
* ⌨ **按鍵顯示名稱**：以清晰的格式區分不同區域的鍵盤，像是可以區分您按下的 `Enter/Return` 訊號是來自於英文字母區還是數字小鍵盤區，協助您檢測不同區域的按鍵情形。
* ➕ **按壓次數計數**：可以檢查電腦是否有正確偵測到按鍵按下的事件，協助您判斷鍵盤是否出現無反應、雙擊或是連擊等故障情形。
* 💾 **儲存計算結果**：程式會自動將每次按壓的日期、時間、按鍵名稱與累積次數儲存至 `KTUP_Records.log` 檔案中，您可以在日後直接該開啟檔案回顧之前的測試紀錄。

## 環境需求 (Requirements)
+ 本程式發行 `.zip` 壓縮檔，需要系統中具備可以解壓縮 `.zip` 格式檔案的軟體 

- Microsfoft Windows
    * 對於一般使用者，建議使用 Microsoft Windows 7 64位元 或更新版本的 Microsoft Windows 作業系統
- Apple macOS 10.9+  
- Linux
> 一般的 Windows 使用者可以直接從 [Releases](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/releases) 頁面直接下載 `KTUP-Win-X.Y.ZZ.zip`  
> 目前僅建議專業開發者直接在 Apple macOS / Linux 編譯運行本程式，我們預計會在未來發行可供一般使用者執行的可執行二進制檔，詳情可見「未來功能」區塊

## 使用說明 (Instructions)
1. 從 GitHub 上的 [Releases](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/releases) 頁面下載對應系統的壓縮包 `KTUP-OS-X.Y.ZZ.zip`，解壓縮後放置於適當的位置
2. 雙擊打開本程式的可執行二進制檔案 `KTUP-X.Y.ZZ-OS`，即可開始使用本程式  
3. 按下你想測試的鍵盤按鍵，此時視窗中應當出現您目前按下的按鍵內容與按下次數
4. 如果測試完成，要關閉本程序，只需按下右上角的關閉按鈕即可
> 詳細的 用戶手冊可以參考 [USER.md](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/blob/main/USER.md) 文件；開發手冊可以參考 [DEVELOPER.md](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/blob/main/DEVELOPER.md) 文件

## V1.0.6 更新日誌 (Changes in V1.0.6)
* 首次正式版本發佈 First Release
    - 使用 `pygame` 顯示結果視窗與讀取鍵盤按鍵輸入
    - 具備基礎的鍵盤按鍵檢測與按壓次數功能
> 所有更新紀錄可參閱 [CHANGELOG.md](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/blob/main/CHANGELOG.md) 文件  

## V1.0.6 已知問題 (Known Issues in V1.0.6)
| 問題編號 (Issues Num) | 錯誤標題 (Issues Title) | 影響程度 (Priority) | 修復狀態 (Status)        | 替代方案(Workaround)                                                    | 詳細內容 (Datails)                                          | 
|-------------------|---------------------|-----------------|----------------------|---------------------------------------------------------------------|---------------------------------------------------------|
| *None*            | 部分情形下無法讀取按鍵輸入       | 部分 (Major)      | 正在調查 (Investigating) | 使用 Windows 上的英文輸入法，如 `ㄅ英` 或 `EN` 進行檢測，避免在運行本程式時使用 `ㄅ中` 輸入法或其他非英文輸入法 | 在 Windows 上，按下 `Shift` 使輸入模式變成「中文模式」時，程式無法正常接收與檢測字母區的信號 |
| *None*            | 部分鍵位顯示文字錯誤          | 部分 (Major)      | 正在調查 (Investigating) | 使用 macOS 上的英文輸入法，如 `ABC` 進行檢測，避免在運行本程式時使用 `繁體注音` 輸入法或其他非英文輸入法       | 在 macOS 上，使用 `繁體注音` 輸入法進行測試時，部分鍵位的映射、對照與顯示文字會出現問題       |
> 如果您有發現任何其他這裡未列出的問題，歡迎向本存儲庫提出問題 (Issues) 與程式建議 (PR)  

## 未來功能 (Future Features)
| 未來版本        | 增加功能                                                   | 開發狀態              | 優先順序     | 預定發布          |
|-------------|--------------------------------------------------------|-------------------|----------|---------------|
| ***1.1.8*** | 增加可以寫入鍵盤按鍵按壓紀錄 `Record.log` 日誌檔案的功能                    | 正在開發 (Developing) | 高 (High) | ***2025-08*** |
| ***1.1.8*** | 新增支援多個多媒體與軟體開啟的鍵盤按鍵按鍵                                  | 準備發布 (Completed)  | 高 (High) | ***2025-08*** |
| ***1.1.8*** | 增加在 CLI 介面中輸出版權宣告的功能與開源協議的功能                           | 準備發布 (Completed)  | 高 (High) | ***2025-08*** |
| ***1.1.8*** | 優化視窗標題列的內容文字，現在會顯示完整的程式版本號與作者訊息                        | 準備發布 (Completed)  | 高 (High) | ***2025-08*** |
| ***1.1.8*** | 修改 `README.md` 中的描述說明，使其更為完整清晰                         | 準備發布 (Completed)  | 高 (High) | ***2025-08*** |
| ***1.1.8*** | 新增 `CHANGELOG.md`、`USER.md`、`DEVELOPER.md`，讓整體專案更為清晰易用 | 正在設計 (Designing)  | 高 (High) | ***2025-08*** |
| ***1.1.8*** | 移除 `EN_README.md`                                      | 準備發布 (Completed)  | 高 (High) | ***2025-08*** |
| 1.1.9       | 提升跨系統顯示相容性，並開始發行 macOS/Linux 可執行檔                      | 正在設計 (Planning)   | 低 (Low)  | 2026-??       |
> 實際發布時間可能會因為當下開發情形而有所提前或延後，敬請耐心等候  
> 如果您有其他的功能需求或建議，歡迎向本存儲庫提出問題 (Issues) 與程式建議 (PR)  

## 貢獻清單 (Contributors)
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者  

## 授權許可 (License)
本專案使用 GNU General Public License v3 開源許可，詳細開源授權許可內容可參閱 [LICENSE](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/blob/main/LICENSE) 文件  
> 注意：所有對此程式碼的修改與衍生版本，都必須以 GNU GPLv3 授權釋出。  

### 鍵盤檢測工具程式（Python），著作權所有 (C) 2024-現在 CHE_72 ZStudio<br>鍵盤檢測工具程式（Python），著作權所有 (C) 2022-2023 CHE72
#### Keyboard Test Utility (Python), Copyright (C) 2024-present CHE_72 ZStudio.<br>Keyboard Test Utility (Python), Copyright (C) 2022-2023 CHE72.

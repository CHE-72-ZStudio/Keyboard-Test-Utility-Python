# 「鍵盤檢測工具程式（Python）」
## Keyboard Test Utility (Python) Made by CHE_72 ZStudio

## 狀態徽章 (Badges)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python)
    [![GitHub Release](https://img.shields.io/github/v/release/CHE-72-ZStudio/Keyboard-Test-Utility-Python)](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/releases)
    [![GitHub License](https://img.shields.io/github/license/CHE-72-ZStudio/Keyboard-Test-Utility-Python)](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/blob/main/LICENSE)
    [![GitHub Last Commit](https://img.shields.io/github/last-commit/CHE-72-ZStudio/Keyboard-Test-Utility-Python)](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/commits)
    [![Python 3](https://img.shields.io/badge/Python%203-3776AB.svg?logo=python&logoColor=white)](https://www.python.org)
    [![PyCharm](https://img.shields.io/badge/PyCharm-000000.svg?logo=PyCharm&logoColor=white)](https://www.jetbrains.com/pycharm/)  

## 程式介紹 (Description)
本程式可以協助您判斷您鍵盤的健康情形

## 程式功能 (Features)
1. 偵測您按下的按鍵內容，並且即時顯示，協助您確認電腦是否有成功收到按鍵內容訊號。
2. 本程式附帶有計數器功能，您可以檢查電腦是否有偵測到按鍵按下的事件。每當按鍵按下時，計數器的數值應當 + 1。
3. 計數器功能亦可協助您判斷鍵盤是否出現無反應、雙擊或是連擊等故障情形。

## 環境需求 (Requirements)
+ 本程式發行 .zip 壓縮檔，需要系統具備可以解壓縮 .zip 格式檔案的軟體 

- Microsfoft Windows
  * 對於一般使用者，建議使用 Microsoft Windows 7 或更新版本的 Microsoft Windows 作業系統
- Apple macOS / Linux  
    * 本程式尚未完全進行關於 macOS / Linux 的相容性測試  
    * 您可以先為此程式的相容性進行測試，若使用中遇到任何問題，歡迎向本存儲庫提出問題 (Issues) 與建議 (PR)  
    > 我們預計會在未來增加對這些系統的兼容，並發行可執行二進制檔，詳情可見「未來功能」區塊  

## 使用說明 (Instructions)
1. 將從 Realease 下載出來的壓縮包解壓縮。
2. 執行解壓縮後的 KTU_CHE72_ZStudio.exe。
3. 按下你想測試的鍵盤按鍵，此時視窗中應當出現您目前按下的按鍵內容與按下次數。
4. 如果測試完成，要關閉本程序，只需按下右上角的關閉按鈕即可。 
> 更為詳細的用戶使用說明可以參考 [USER.md](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/blob/main/MANUAL.md) 文件  
> 更為詳細的開發使用說明可以參考 [DEVELOPER.md](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/blob/main/MANUAL.md) 文件  

## V1.0.6 已知問題 (Known Issues in V1.0.6)
| 問題編號 (Issues Num) | 錯誤標題 (Issues Title) | 影響程度 (Priority) | 修復狀態 (Status)        | 替代方案(Workaround)                      | 詳細內容 (Datails)                 | 
|-------------------|---------------------|-----------------|----------------------|---------------------------------------|--------------------------------|
| *None*            | 部分鍵位顯示文字錯誤          | 邊緣 (Major)      | 正在調查 (Investigating) | 使用`ABC`英文輸入法進行檢測，避免在運行本程式時使用`繁體注音`輸入法 | 在 macOS 上，部分鍵位的映射、對照與顯示文字會出現問題 |
> 如果您有發現任何其他這裡未列出的問題，歡迎向本存儲庫提出問題 (Issues) 與程式建議 (PR)  

## 未來功能 (Future Features)
| 未來版本        | 增加功能                              | 開發狀態            | 優先順序     | 預定發布          |
|-------------|-----------------------------------|-----------------|----------|---------------|
| ***1.1.0*** | 增加可以寫入鍵盤按鍵按壓紀錄 Record.log 日誌檔案的功能 | 功能規劃 (Planning) | 高 (High) | ***2025-??*** |
> 實際發布時間可能會因為當下開發情形而有所提前或延後，敬請耐心等候  
> 如果您有其他的功能需求或建議，歡迎向本存儲庫提出問題 (Issues) 與程式建議 (PR)  

## 貢獻清單 (Contributors)
- [![CHE72](https://img.shields.io/badge/CHE72-181717.svg?logo=github&logoColor=white)](https://github.com/CHE72): 專案發起人／項目**唯一**貢獻者／項目**唯一**維護者  

## 授權許可 (License)
本專案使用 GNU General Public License v3 開源許可，詳細開源授權許可內容可參閱 [LICENSE](https://github.com/CHE-72-ZStudio/Keyboard-Test-Utility-Python/blob/main/LICENSE) 文件  
> 注意：所有對此程式碼的修改與衍生版本，都必須以 GNU GPLv3 授權釋出。  

### 「鍵盤檢測工具程式（Python）」 Ver1.0.6，著作權所有 (C) 2024-現在 CHE_72 ZStudio.
#### Keyboard Test Utility (Python) Ver1.0.6, Copyright (C) 2024-present CHE_72 ZStudio.
#### 著作權所有 (C) 2022-2023 CHE72 / Copyright (C) 2022-2023 CHE72.

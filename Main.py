"""
Main.py
此模組為「鍵盤檢測工具程式」的唯一入口

* update_display：
* record：
"""

# TODO: rename variables
# TODO: update comments

import pygame  # 載入pygame模組
import sys
import datetime

from Studio import *


def update_display():  # 定義更新畫面的函式
    background.blit(instruction_text1, (0, 0))  # 繪製左上角第一行的文字
    background.blit(instruction_text2, (0, 75))  # 繪製左上角第二行的文字
    background.blit(instruction_text3, (0, 150))  # 繪製左上角第三行的文字
    background.blit(numbers_display, (1000, 800))  # 繪製計數器的文字
    background.blit(key_display, (50, 400))  # 繪製按鍵內容的文字
    screen.blit(background, (0, 0))  # 在繪圖視窗繪製畫布
    pygame.display.update()  # 更新繪圖視窗

def record(count, id, name):
    # 嘗試開啟 KTUP_Records.log 為 file 句柄後，將 時間戳記、計算結果、程式版本、分隔符號 寫入檔案中，方便使用者日後查詢
    try:
        # 由 Gemini Code Assist 建議使用 datetime.datetime.now() 取代 time.localtime()，以便取得毫秒的方法
        # 參考來源：https://docs.python.org/zh-cn/3.13/library/datetime.html
        with open("KTUP_Records.log", "a+", encoding="UTF-8") as file:
            stamp = datetime.datetime.now()
            file.write("{:03d}.\t".format(count))
            file.write(stamp.strftime("%Y-%m-%d %H:%M:%S") + ".{:03d}\t".format(stamp.microsecond // 1000))
            file.write("{}: ({})\n".format(name, id))
    # TODO 增加磁碟空間已滿，無法寫入的專用 except 提示
    except PermissionError:  # 如果文件系統的存取權限不足
        print("\033[38;5;197m因為程式對於文件系統的存取權限不足，無法將結果寫入至檔案內\033[0m\a")  # 輸出檔案權限不足訊息與通知聲音
    except Exception:
        print("\033[38;5;197m程式遇到不明原因的錯誤，無法將結果寫入至檔案內\033[0m\a")  # 輸出檔案無法寫入訊息與通知聲音
    else:
        print("\033[38;5;47m成功將計算結果寫入至 \"KTUP_Records.log\"，可於日後開啟該檔案檢視結果\033[0m")  # 輸出檔案成功寫入訊息


if __name__ == "__main__":
    # 定義 中／英 程式名稱、程式版本號，如果日後有需要更新時，更改此處即可避免缺失遺漏
    program_zh = "鍵盤檢測工具程式（Python）"
    program_en = "Keyboard Test Utility (Python)"
    version = "1.1.7"

    pygame.init()  # 啟動pygame
    screen = pygame.display.set_mode((1600, 900))  # 建立繪圖視窗（寬1600，高900）  # TODO: 是否可以讀取系統的解析度以決定視窗大小？
    pygame.display.set_caption("「{}」Ver{}，著作權所有 (C) 2025-現在 CHE_72 ZStudio".format(program_zh, version))  # 設定視窗的標題
    background = pygame.Surface(screen.get_size())  # 建立畫布
    background = background.convert()
    background.fill((31, 31, 31))  # 設定畫布顏色(31, 31, 31)
    default_font = pygame.font.Font("NotoSansRegular.otf", 54)  # 設定預設文字字型及大小
    key_font = pygame.font.Font("NotoSansRegular.otf", 100)  # 設定鍵盤顯示文字字型及大小
    # TODO: split instruction_text1 to 2 lines
    instruction_text1 = default_font.render("歡迎您使用「{}」Ver{}，本程式由 CHE_72 ZStudio 製作".format(program_zh, version), True, (191, 191, 191))  # 設定左上角第一行的文字內容
    instruction_text2 = default_font.render("按下鍵盤上的任意按鍵即可開始檢測", True, (191, 191, 191))  # 設定左上角第二行的文字內容
    instruction_text3 = default_font.render("程式尚未收到您按下任何按鍵的訊號！", True, (191, 191, 191))  # 設定左上角第三行的文字內容
    numbers = 0  # 設定按鍵次數計數器
    numbers_text = ("目前已按下鍵盤 {} 次".format(numbers))  # 設定計數器的顯示文字內容
    numbers_display = default_font.render(numbers_text, True, (191, 191, 191))  # 設定計數器文字的顏色
    key_text = ""  # 設定按鍵文字內容 為空白
    key_display = key_font.render(key_text, True, (191, 191, 191))  # 設定按鍵文字的顏色
    update_display()  # 使用更新畫面的函式

    clock = pygame.time.Clock()  # 建立時間元件
    running = True  # 設定當前迴圈運行狀態為啟動
    while running:  # 無窮迴圈
        clock.tick(120)  # 每秒執行120次
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # 如果鍵盤按鍵被按下
                try:  # TODO: use match/case or dict() here?
                    if event.key == 8:
                        key_text = "< BACKSPACE >"
                    elif event.key == 9:
                        key_text = "< TAB >"
                    elif event.key == 13:
                        key_text = "< ENTER >"
                    elif event.key == 27:
                        key_text = "< ESC >"
                    elif event.key == 32:
                        key_text = "< SPACE >"
                    elif event.key == 127:
                        key_text = "< DELETE >"
                    elif event.key == 1073741881:
                        key_text = "< CAPS_LOCK >"
                    elif 1073741882 <= event.key <= 1073741893:
                        key_text = "< F_{} >".format(event.key % 1073741881)  # 前面的 F 表示為上方功能區的按鍵
                    elif event.key == 1073741894:
                        key_text = "< PrintScreen / SystemRequest >"
                    elif event.key == 1073741895:
                        key_text = "< SCROLL_LOCK >"
                    elif event.key == 1073741896:
                        key_text = "< PAUSE / BREAK >"
                    elif event.key == 1073741897:
                        key_text = "< INSERT >"
                    elif event.key == 1073741898:
                        key_text = "< HOME >"
                    elif event.key == 1073741899:
                        key_text = "< PAGE_UP >"
                    elif event.key == 1073741901:
                        key_text = "< END >"
                    elif event.key == 1073741902:
                        key_text = "< PAGE_DOWN >"
                    elif event.key == 1073741903:
                        key_text = "< ARROW_RIGHT >"  # 方向鍵的 向右 鍵
                    elif event.key == 1073741904:
                        key_text = "< ARROW_LEFT >"  # 方向鍵的 向左 鍵
                    elif event.key == 1073741905:
                        key_text = "< ARROW_DOWN >"  # 方向鍵的 向下 鍵
                    elif event.key == 1073741906:
                        key_text = "< ARROW_UP >"  # 方向鍵的 向上 鍵
                    elif event.key == 1073741907:
                        key_text = "< NUM_LOCK >"
                    elif event.key == 1073741908:
                        key_text = "< NUM_/ >"  # 數字區小鍵盤的 / 鍵
                    elif event.key == 1073741909:
                        key_text = "< NUM_* >"  # 數字區小鍵盤的 * 鍵
                    elif event.key == 1073741910:
                        key_text = "< NUM_- >"  # 數字區小鍵盤的 - 鍵
                    elif event.key == 1073741911:
                        key_text = "< NUM_+ >"  # 數字區小鍵盤的 + 鍵
                    elif event.key == 1073741912:
                        key_text = "< NUM_ENTER >"  # 數字區小鍵盤的 ENTER 鍵
                    elif 1073741913 <= event.key <= 1073741921:
                        key_text = "< NUM_{} >".format(event.key % 1073741912)  # 前面的 NUM 表示為數字區小鍵盤的按鍵
                    elif event.key == 1073741922:
                        key_text = "< NUM_0 >"  # 數字區小鍵盤的 0 鍵
                    elif event.key == 1073741923:
                        key_text = "< NUM_. >"  # 數字區小鍵盤的 . 鍵
                    elif event.key == 1073741925:
                        key_text = "< MENU >"
                    elif event.key == 1073742048:
                        key_text = "< LEFT_CTRL >"
                    elif event.key == 1073742049:
                        key_text = "< LEFT_SHIFT >"
                    elif event.key == 1073742050:
                        key_text = "< LEFT_ALT >"
                    elif event.key == 1073742051:
                        key_text = "< WINDOWS >"
                    elif event.key == 1073742052:
                        key_text = "< RIGHT_CTRL >"
                    elif event.key == 1073742053:
                        key_text = "< RIGHT_SHIFT >"
                    elif event.key == 1073742054:
                        key_text = "< RIGHT_ALT >"
                    elif event.key == 1073742086:
                        key_text = "< VOL_MUTE >"  # 多媒體鍵的 靜音 鍵
                    elif event.key == 1073741953:
                        key_text = "< VOL_DOWN >"  # 多媒體鍵的 音量減小 鍵
                    elif event.key == 1073741952:
                        key_text = "< VOL_UP >"  # 多媒體鍵的 音量增大 鍵
                    elif event.key == 1073742082:
                        key_text = "< MEDIA_NEXT_TRACK >"  # 多媒體鍵的 下一首 鍵
                    elif event.key == 1073742083:
                        key_text = "< MEDIA_PREV_TRACK >"  # 多媒體鍵的 上一首 鍵
                    elif event.key == 1073742084:
                        key_text = "< MEDIA_STOP >"  # 多媒體鍵的 停止 鍵
                    elif event.key == 1073742085:
                        key_text = "< MEDIA_PLAY/PAUSE >"  # 多媒體鍵的 播放/暫停 鍵
                    elif event.key == 1073742087:
                        key_text = "< OPEN_MEDIA_PLAYER >"  # 開啟 多媒體播放軟體
                    elif event.key == 1073742089:
                        key_text = "< OPEN_E-MAIL >"  # 開啟 電子郵件軟體
                    elif event.key == 1073742092:
                        key_text = "< OPEN_SEARCH >"  # 開啟 搜尋輸入框
                    elif event.key == 1073742093:
                        key_text = "< OPEN_INTERNET_BROWSER >"  # 開啟 網路瀏覽器軟體
                    elif event.key == 1073742107:
                        key_text = "< OPEN_EXPLORER/THIS PC >"  # 開啟 檔案總管/本機
                    elif event.key == 1073742108:
                        key_text = "< OPEN_CALCULATOR >"  # 開啟 小算盤軟體
                    elif 97 <= event.key <= 122:
                        key_text = "< {} >".format(chr(event.key - 32))  # 這些按鍵是英文按鍵
                    elif (44 <= event.key <= 57) or (91 <= event.key <= 93) or (event.key == 39 or 59 or 61):
                        key_text = "< {} >".format(chr(event.key))  # 這些按鍵是上排數字鍵及標點符號
                except:  # 如果按鍵不符合以上內容
                    key_text = "< UNKNOWN : {} >".format(event.key)  # 輸出：未知的按鍵
                finally:  # 無論是否為例外事件
                    numbers = numbers + 1  # 計數器 + 1
                    record(numbers, event.key, key_text)  # TODO: write some comments here
            if event.type == pygame.QUIT:  # 如果使用者按關閉鈕
                running = False  # 設定當前迴圈運行狀態為停止
            if numbers != 0:  # 如果計數器不為0
                instruction_text3 = default_font.render("您剛剛按下的按鍵為︰", True, (191, 191, 191))  # 更改左上角第三行的文字
        key_display = key_font.render(key_text, True, (191, 191, 191))  # 更改按鍵文字內容
        numbers_text = ("目前已按下鍵盤 {} 次".format(numbers))  # 更新計數器的文字內容
        numbers_display = default_font.render(numbers_text, True, (191, 191, 191))  # 更新計數器的文字顯示
        background.fill((31, 31, 31))  # 重新填充畫布
        update_display()  # 使用更新畫面的函式
    pygame.quit()  # 關閉視窗

    # 嘗試開啟 KTUP_Records.log 為 file 句柄後，將 時間戳記、計算結果、程式版本、分隔符號 寫入檔案中，方便使用者日後查詢
    try:
        # 由 Gemini Code Assist 提供可以在時間戳記的缺位中自動補 0 的方法
        with open("KTUP_Records.log", "a+", encoding="UTF-8") as file:
            file.write("「{}」Ver{}\n".format(program_zh, version))
            file.write("{}\n".format("=" * 36))
    # TODO 增加磁碟空間已滿，無法寫入的專用 except 提示
    except PermissionError:  # 如果文件系統的存取權限不足
        print("\n\033[38;5;197m因為程式對於文件系統的存取權限不足，無法將結果寫入至檔案內\033[0m\a")  # 輸出檔案權限不足訊息與通知聲音
    except Exception:
        print("\n\033[38;5;197m程式遇到不明原因的錯誤，無法將結果寫入至檔案內\033[0m\a")  # 輸出檔案無法寫入訊息與通知聲音
    else:
        print("\n\033[38;5;47m成功將程式資訊寫入至 \"KTUP_Records.log\"，可於日後開啟該檔案檢視結果\033[0m")  # 輸出檔案成功寫入訊息
    finally:
        print()
        print("「{}」Ver{}，著作權所有 (C) 2025-現在 CHE_72 ZStudio".format(program_zh, version))
        print("{} Ver{} , Copyright (C) 2025-present CHE_72 ZStudio".format(program_en, version))
        print(Studio_ZH)  # Studio.py 中的中文版工作室宣告
else:  # 如果使用者誤將本程式作為模組引用
    print("\033[38;5;197m本程式為「鍵盤檢測工具程式」的主入口\n請直接運行 Main.py，而非透過其他模組引入本程式\033[0m\a\n")  # 輸出提示訊息提醒使用者正確使用方式
    sys.exit(1)  # 呼叫系統結束本程式運行，原因為"Operation not permitted"
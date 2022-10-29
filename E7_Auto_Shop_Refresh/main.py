##from asyncio.windows_events import NULL
from time import sleep
import datetime
import keyboard
from numpy import datetime_as_string
import pyautogui

#counters
covenant_count = 0
covenant_bought = False
mystic_count = 0
mystic_bought = False
refresh_count = 0
ss_used = 0
current_ss = 33651
current_gold = 509850721
gold_used = 0
refresh_failed = 0
date_str = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
date_file_name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
start_time = datetime.datetime.now().strftime("%H:%M:%S")
start_time1 = datetime.datetime.now()


def shopRefresh():
    global refresh_count, ss_used, covenant_bought, mystic_bought, current_ss, refresh_failed
    covenant_bought = False
    mystic_bought = False
    sleep(0.5)
    refresh_cords = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\shop_refresh.png")
    print(refresh_cords)
    if refresh_cords:
        pyautogui.click(refresh_cords)
        sleep(0.5)
        doublecheck_refresh = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\shop_refresh.png")
        if doublecheck_refresh:
            print("Shop refresh Unsuccessful -- Refresh still on screen")
            refresh_failed = refresh_failed + 1
            return False
        sleep(0.5)
        confirm_cords = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\confirm.png")
        if confirm_cords:
            print(confirm_cords)
            pyautogui.click(confirm_cords)
            sleep(0.5)
            doublecheck_confirm = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\confirm.png")
            print("Double Check Confirm: ", doublecheck_confirm)
            if doublecheck_confirm:
                print("Shop refresh Unsuccessful -- Confirm still on screen")
                refresh_failed = refresh_failed + 1
                return False
            else:
                print("Shop refreshed Successful")
                refresh_count = refresh_count + 1
                ss_used = ss_used + 3
                current_ss = current_ss - 3
                return True
    else:
        print("Shop refreshed Unsuccessful-- Other Reason")
        refresh_failed = refresh_failed + 1
        return False
    

def searchConvenant():
    global covenant_count, covenant_bought, current_gold, gold_used
    covenant_cords = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\covenant_bookmark.png", confidence=.90)
    if covenant_cords:
        print("-Convenant Bookmarks found")
        sleep(.25)
        covenant_cords_x, covenant_cords_y = covenant_cords
        pyautogui.click(int(covenant_cords_x) + 565, int(covenant_cords_y) + 25, 2)
        print(covenant_cords)
        #covenant_buy_cords = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\covenant_bookmark_buy.png", confidence=.95)
        #print("Convenant Bookmark Button")
        #print(covenant_buy_cords)
        #covenant_buy_cords_x, covenant_buy_cords_y = covenant_buy_cords
        #pyautogui.click(int(covenant_buy_cords_x), int(covenant_buy_cords_y) + 25)
        sleep(.5)
        buyConvenant()
    else:
        print("-No Convenant Bookmarks found")


def buyConvenant():
    global covenant_count, covenant_bought, current_gold, gold_used
    covenant_buy_confirm_cords = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\covenant_bookmark_buy_confirm.png", confidence=.90)
    print("Convenant Bookmark Button Buy")
    print(covenant_buy_confirm_cords)
    if covenant_buy_confirm_cords:
        pyautogui.click(covenant_buy_confirm_cords)
        sleep(.25)
        doublecheck_c_confirm = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\covenant_bookmark_buy_confirm.png", confidence=.90)
        print("-Double Check Confirm: ", doublecheck_c_confirm)
        if doublecheck_c_confirm:
            print("---Covenant Buy Confirm still on screen")
            pyautogui.click(doublecheck_c_confirm)
            doublecheck_c_confirm = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\covenant_bookmark_buy_confirm.png", confidence=.90)
            if doublecheck_c_confirm:
                print("-Double Check Confirm: ", doublecheck_c_confirm)
                input("Click Confirm on screen. Then press <Enter> to continue...")
        print("--Covenant Bookmark Bought")
        covenant_bought = True
        covenant_count = covenant_count + 1
        gold_used = gold_used + 184000
        current_gold = current_gold - 184000
    else:
        print("--Problem with clicking covenant confirm buy. Click on Buy.")
        input("Please press <Enter> to continue...")
        buyConvenant()

def searchMystic():
    global mystic_count, mystic_bought, current_gold, gold_used
    mystic_cords = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\mystic_bookmark.png", confidence=.90)
    if mystic_cords:
        print("-Mystic Bookmarks found")
        sleep(.25)
        mystic_cords_x, mystic_cords_y = mystic_cords
        pyautogui.click(int(mystic_cords_x) + 565, int(mystic_cords_y) + 25, 2)
        print(mystic_cords)
        #mystic_buy_cords = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\mystic_bookmark_buy.png", confidence=.95)
        print("Mystic Bookmark Button")
        #print(mystic_buy_cords)
        #mystic_buy_cords_x, mystic_buy_cords_y = mystic_buy_cords
        #pyautogui.click(int(mystic_buy_cords_x), int(mystic_buy_cords_y) + 25)
        sleep(.5)
        buyMystic()
    else:
        print("-No Mystic Bookmarks found")

def buyMystic():
    global mystic_count, mystic_bought, current_gold, gold_used
    mystic_buy_confirm_cords = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\mystic_bookmark_buy_confirm.png", confidence=.90)
    #print("Mystic Bookmark Button Buy")
    #print(mystic_buy_confirm_cords)
    if mystic_buy_confirm_cords:
        pyautogui.click(mystic_buy_confirm_cords)
        sleep(.25)
        doublecheck_m_confirm = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\mystic_bookmark_buy_confirm.png", confidence=.90)
        print("-Double Check Confirm: ", doublecheck_m_confirm)
        if doublecheck_m_confirm:
            print("---Mystic Buy Confirm still on screen")
            pyautogui.click(doublecheck_m_confirm)
            doublecheck_m_confirm = pyautogui.locateCenterOnScreen("E7_Auto_Shop_Refresh\Images\mystic_bookmark_buy_confirm.png", confidence=.90)
            if doublecheck_m_confirm:
                print("-Double Check Confirm: ", doublecheck_m_confirm)
                input("Click Confirm on screen. Then press <Enter> to continue...")
        print("--Mystic Bookmark Bought")
        mystic_bought = True
        mystic_count = mystic_count + 1
        gold_used = gold_used + 280000
        current_gold = current_gold - 280000
    else:
        print("--Problem with clicking covenant confirm buy. Click on Buy")
        input("Please press <Enter> to continue...")
        buyMystic()

def checkShop():
    if not covenant_bought:
        searchConvenant()
    sleep(0.5)
    if not mystic_bought:
        searchMystic()

a = input("Enter current Skystones: ")
current_ss = int(a)
b = input("Enter current Gold: ")
current_gold = int(b)
input("Press Enter to Start...")
print("Script started at: ", start_time)
print("Shop refresh Starting... Current SS: ", current_ss, "Current SS Spent: ", ss_used, " Current Gold: ", current_gold, " Current Gold Spent: ", gold_used)
while not keyboard.is_pressed('q'):
    if keyboard.is_pressed(' '):
        input("PAUSED. Press <Enter> to continue...")
    print("Shop refresh # ", int(refresh_count) + 1, " Current SS: ", int(current_ss) - 3, "Current SS Spent: ", ss_used, " Current Gold: ", current_gold, " Current Gold Spent: ", gold_used)
    print("Covenants found: ", covenant_count, " Mystics found ", mystic_count)
    x = shopRefresh()
    sleep(0.5)
    if x:
        checkShop()
        sleep(0.1)  
        pyautogui.scroll(-5000)
        sleep(0.65)
        checkShop()
    sleep(0.25)

try:
    ss_per_c = ss_used / covenant_count
except ZeroDivisionError:
    ss_per_c = 0

try:
    ss_per_m = ss_used / mystic_count
except ZeroDivisionError:
    ss_per_m = 0

end_time = datetime.datetime.now().strftime("%H:%M:%S")
end_time1 = datetime.datetime.now()
time_diff = end_time1 - start_time1

print("===========SHOP REFRESH RESULTS===========")
print("Started: ", start_time, " Ended: ", end_time, " Delta: ", time_diff)
print("Covenants Bought: ", covenant_count, " Equals ", covenant_count * 5)
print("Mystics Bought: ", mystic_count, " Equals ", mystic_count * 50)
print("Shop Refreshes: ", refresh_count)
print("Failed Shop Refreshes: ", refresh_failed)
print("Skystones used: ", ss_used)
print("Skystones should be ", current_ss)
print("Gold used: ", gold_used)
print("Gold should be ", current_gold)
print("Covenants %: ", covenant_count / refresh_count * 100)
print("Skystones per Covenant: ", ss_per_c)
print("Mystics %: ", mystic_count / refresh_count * 100)
print("Skystones per Mystic: ", ss_per_m)
print("==========================================")

file_name = "Shop_Refresh_" + date_file_name + ".txt"

log_text = ''
log_text = date_str
log_text += '\n'
log_text += "Started: " + str(start_time) + " Ended: " + str(end_time) + " Delta: " + str(time_diff)
log_text += '\n'
log_text += "===========SHOP REFRESH RESULTS==========="
log_text += '\n'
log_text += "Covenants Bought: " + str(covenant_count) + " Equals " + str(covenant_count * 5)
log_text += '\n'
log_text += "Mystics Bought: " + str(mystic_count) + " Equals " + str(mystic_count * 50)
log_text += '\n'
log_text += "Shop Refreshes: " + str(refresh_count)
log_text += '\n'
log_text += "Failed Shop Refreshes: " + str(refresh_failed)
log_text += '\n'
log_text += "Skystones used: " + str(ss_used)
log_text += '\n'
log_text += "Skystones should be " + str(current_ss)
log_text += '\n'
log_text += "Gold used: " + str(gold_used)
log_text += '\n'
log_text += "Gold should be " + str(current_gold)
log_text += '\n'
log_text += "Covenants %: " + str(covenant_count / refresh_count * 100)
log_text += '\n'
log_text += "Skystones per Covenant: " + str(ss_per_c)
log_text += '\n'
log_text += "Mystics %: " + str(mystic_count / refresh_count * 100)
log_text += '\n'
log_text += "Skystones per Mystic: " + str(ss_per_m)
log_text += '\n'
log_text += "=========================================="
with open( file_name, 'w') as f:
    f.write(log_text)
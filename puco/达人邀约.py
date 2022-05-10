import pyautogui
import time
import pyperclip
import json
# 921.6

url_list=[]
news_urls = []

def pyautogui_action(action):
    if action["name"] in ["move_to_click"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')

    elif action["name"] in ["select_all_and_copy"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")

    elif action["name"] in ["select_all_and_paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "v")

    elif action["name"] in ["select_all_and_copy_and_paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        write_content = action.get("content","")
        pyperclip.copy(write_content)
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')

    elif action["name"] in ["open_console"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("f12")
    print(action.get("action_name"))
    action_sleep = action.get("sleep",0)
    time.sleep(action_sleep)

for n in range(0,1):
    for i in range(0,20):
        pyautogui.moveTo(x=1209,y=178,duration=0.3)
        pyautogui.click(x=1209,y=178, button='left')
        pyautogui.moveTo(x=1209,y=178,duration=0.3)
        pyautogui.click(x=1209,y=178,button='left')
        pyautogui.moveTo(x=1324,y=819,duration=0.3)
        pyautogui.click(x=1324,y=819,button='left')
        pyperclip.copy('document.getElementsByClassName("daren-card")[%s].click()'%(i))
        pyautogui.hotkey('ctrl','v')
        pyautogui.keyDown('enter')
        time.sleep(2)
        pyautogui.hotkey('f12')
        time.sleep(1)
        pyautogui.moveTo(x=1209,y=178,duration=0.3)
        pyautogui.click(x=1209,y=178, button='left')
        pyautogui.moveTo(x=1209,y=178,duration=0.3)
        pyautogui.click(x=1209,y=178,button='left')
        pyautogui.moveTo(x=1324,y=819,duration=0.3)
        pyautogui.click(x=1324,y=819,button='left')
        pyperclip.copy('''
if (document.getElementsByClassName("contact-btn-text sp-tooltip")[0].innerText=="发送邀约"){
    document.getElementsByClassName("contact-btn-text sp-tooltip")[0].click()
    document.getElementsByClassName("add-product-last-operate")[0].click()
    setTimeout(function(){
    document.getElementsByClassName("drawer-footer-default")[0].getElementsByClassName("ant-btn ant-btn-primary")[0].click()
                        },1000)
                    }
        '''
        )
        pyautogui.hotkey('ctrl','v')
        pyautogui.keyDown('enter')
        time.sleep(8)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(0.5)
    pyautogui.moveTo(x=1209, y=178, duration=0.3)
    pyautogui.click(x=1209, y=178, button='left')
    pyautogui.moveTo(x=1209, y=178, duration=0.3)
    pyautogui.click(x=1209, y=178, button='left')
    pyautogui.moveTo(x=1324, y=819, duration=0.3)
    pyautogui.click(x=1324, y=819, button='left')
    pyperclip.copy('document.getElementsByClassName("ant-pagination-item-link")[2].click()')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.keyDown('enter')
    time.time(1)

'''
result=[]
result.push($(".daren-overview-base-nameblock").innerText)
result.push($(".daren-overview-base-traitblock").innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[0].innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[1].innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[2].innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[3].innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[4].innerText)
result.push(document.getElementsByClassName("data-overview-dashboard-items-item__value")[6].innerText)
result_info = {
    "name":result[0],
    "traitblock":result[1],
    "frequency":result[2],
    "days":result[3],
    "promote":result[4],
    "cooperation":result[5],
    "people":result[6],
    "sales":result[7],
}
'''
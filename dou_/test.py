import sys
import os
import pyautogui
import time
import pyperclip

page_num = 0
page_num_end = 3
# SK-II 从第二页开始
page_with_items = [13,13,13,13,8]
t=21
action_list = [
    {
        "x": 127,
        "y": 17,
        "sleep": 1,
        "name": "move_to_click",
        "content": "",
        "action_name": "切换pgy页面",
    },
]
def pyautogui_action(action):
    if action["name"] in ["move_to_click"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
    elif action["name"] in ["select_all_and_write"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        write_content = action.get("content", "")
        pyautogui.typewrite(write_content)
        pyautogui.press('enter')
    elif action["name"] in ["select_all_and_js_latest"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press('backspace')
        pyautogui.press('up')
        pyautogui.press('enter')
    elif action["name"] in ["select_all_and_copy"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "c")
    elif action["name"] in ["select_all_and_paste"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "v")
    elif action["name"] in ["select_item_and_close_tab"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        pyautogui.hotkey("ctrl", "w")
    elif action["name"] in ["select_all_and_copy_and_paste"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        write_content = action.get("content", "")
        pyperclip.copy(write_content)
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
    elif action["name"] in ["open_console"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        pyautogui.hotkey("f12")
    elif action["name"] in ["esc"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        pyautogui.hotkey("esc")
    print(action.get("action_name"))
    action_sleep = action.get("sleep", 0)
    time.sleep(action_sleep)
for page in page_with_items:
    for item in range(3,page):
        action_item_click_list=[
            {
                "x": 1377,
                "y": 147,
                "sleep": 0.5,
                "name": "move_to_click",
                "content": "",
                "action_name": "切换console",
            },
            {
                "x": 1204,
                "y": 172,
                "sleep": 0.5,
                "name": "move_to_click",
                "content": "",
                "action_name": "清空信息console",
            },
            {
                "x": 1282,
                "y": 995,
                "sleep": 0.5,
                "name": "select_all_and_copy_and_paste",
                "content": '$("#wlb_cover").remove()',
                "action_name": "获取商品信息"
            },
            {
                "x": 1282,
                "y": 995,
                "sleep": 2,
                "name": "select_all_and_copy_and_paste",
                "content": r'''
result=[]
result.push(document.getElementsByClassName("card--1fmeJ")[%s].getElementsByClassName("name--3OXp2")[0].innerText)
result.push(document.getElementsByClassName("card--1fmeJ")[%s].getElementsByClassName("time--1J-Ei")[0].innerText)
result.push(document.getElementsByClassName("card--1fmeJ")[%s].getElementsByClassName("valueWrapper--3jbBR")[0].innerText)
result.push(document.getElementsByClassName("card--1fmeJ")[%s].getElementsByClassName("valueWrapper--3jbBR")[1].innerText)
result.push(document.getElementsByClassName("card--1fmeJ")[%s].getElementsByClassName("valueWrapper--3jbBR")[2].innerText)
result_info={
    "date":"1月%s日",
    "name":result[0],
    "time":result[1],
    "clinch":result[2],
    "number":result[3],
    "thousands":result[4],
}
dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+JSON.stringify(result_info)+"</textarea>"
document.body.append(dom)
                '''%(item,item,item,item,item,t),
                "action_name": "get_info",
            },
            {
                "x": 1023,
                "y": 152,
                "sleep": 0.5,
                "name": "select_all_and_copy",
                "content": "",
                "action_name": "copy"
            },
            {
                "x": 455,
                "y": 13,
                "sleep": 0.5,
                "name": "move_to_click",
                "content": "",
                "action_name": "点击选项卡",
            },
            {
                "x": 455,
                "y": 13,
                "sleep": 0.5,
                "name": "esc",
                "content": "",
                "action_name": "esc",
            },
            {
                "x":440,
                "y":210,
                "sleep": 0.5,
                "name": "select_all_and_paste",
                "content": "",
                "action_name": "提交",
            },
            {
                "x": 429,
                "y": 282,
                "sleep": 0.5,
                "name": "move_to_click",
                "content": "",
                "action_name": "submit",
            },
            {
                "x": 131,
                "y": 17,
                "sleep": 0.5,
                "name": "move_to_click",
                "content": "",
                "action_name": "点击选项卡",

            },
        ]
        for action_page_change in action_item_click_list:
            pyautogui_action(action_page_change)
    next=[
        {
            "x": 1377,
            "y": 147,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "切换console",
        },
        {
            "x": 1204,
            "y": 172,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "清空信息console",
        },
        {
            "x": 1282,
            "y": 995,
            "sleep": 1,
            "name": "select_all_and_copy_and_paste",
            "content": '''
document.getElementsByClassName("ecom-pagination-item-link")[1].click()
                    ''',
            "action_name": "nexit",
        },
    ]
    for action_page_change in next:
        pyautogui_action(action_page_change)


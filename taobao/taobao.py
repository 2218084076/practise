import pyautogui
import time
import pyperclip

def pyautogui_action(action):
    if action["name"] in ["move_to_click"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
    elif action["name"] in ["select_all_and_write"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        write_content = action.get("content","")
        pyautogui.typewrite(write_content)
        pyautogui.press('enter')
    elif action["name"] in ["select_all_and_js_latest"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press('backspace')
        pyautogui.press('up')
        pyautogui.press('enter')
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

    elif action["name"] in ["paste"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
    elif action["name"] in ["select_item_and_close_tab"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("ctrl", "w")
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

for i in range(1,101):
    print(i)
    print(i)
    print(i)
    print(i)
    action_item_click_list =[
        {
            "x": 1367,
            "y": 149,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "切换console",
        },
        {
            "x": 1204,
            "y": 177,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "清空信息console",
        },
        {
            "x": 1198,
            "y": 993,
            "sleep": 1,
            "name": "select_all_and_copy_and_paste",
            "content": 'document.getElementById("wlb_cover").remove()',
            "action_name": "清空dom",
        },
        {
            "x": 1198,
            "y": 993,
            "sleep": 1,
            "name": "select_all_and_copy_and_paste",
            "content":
                '''
url_list=[]
items = document.getElementsByClassName("item J_MouserOnverReq")
for(i=0;i<items.length;i++){
    url_list.push(items[i].getElementsByTagName("a")[0].href)
}
dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
            ''',
            "action_name": "get_urls_list",
        },
        {
            "x": 1198,
            "y": 993,
            "sleep": 0.5,
            "name": "select_all_and_copy_and_paste",
            "content": '''
document.getElementsByClassName("modal-dialog-el")[0].remove()
document.getElementById("J_advice2snapshot").remove()
''',
            "action_name": "",
        },
        {
            "x": 1198,
            "y": 993,
            "sleep": 0.5,
            "name": "select_all_and_copy_and_paste",
            "content": rf'dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+url_list+"</textarea>"',
            "action_name": "",
        },
        {
            "x": 1198,
            "y": 993,
            "sleep": 0.5,
            "name": "select_all_and_copy_and_paste",
            "content": "document.body.append(dom)",
            "action_name": "展示文本框",
        },
        {
            "x": 1053,
            "y": 163,
            "sleep": 1,
            "name": "select_all_and_copy",
            "content": "",
            "action_name": "copy"
        },
        # {
        #     "x": 931,
        #     "y": 1049,
        #     "sleep": 1,
        #     "name": "move_to_click",
        #     "content": "",
        #     "action_name": "切换笔记",
        # },
        {
            "x": 1067,
            "y": 1048,
            "sleep": 3,
            "name": "paste",
            "content": "",
            "action_name": "提交",
        },
        {
            "x": 961,
            "y": 1041,
            "sleep": 1,
            "name": "move_to_click",
            "content": "",
            "action_name": "切换到浏览器",
        },
        {
            "x": 1204,
            "y": 177,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "清空信息console",
        },
        {
            "x": 1198,
            "y": 993,
            "sleep": 5,
            "name": "select_all_and_copy_and_paste",
            "content": '''
scroll(0,4000)
document.getElementsByClassName("J_Ajax num icon-tag")[1].click()
            ''',
            "action_name": "滚动到下一页位置",
        },
    ]
    for action_item_click in action_item_click_list:
        pyautogui_action(action_item_click)


'''
url_list=[]
items = document.getElementsByClassName("item J_MouserOnverReq")
for(i=0;i<items.length;i++){
    url_list.push(items[i].getElementsByTagName("a")[0].href)
}
dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+url_list+"</textarea>"
'''
import random
import time

import pyautogui
import pyperclip

# Chrome打开浏览器 https://pgy.xiaohongshu.com/solar/advertiser/patterns/kol
# 选择分类
# 打开审查元素工具 位置1160px
# 滚动屏幕至全部右下角
page_num = 0
page_num_end = 3

page_with_items = [19]
action_list = [
    {
        "x": 118,
        "y": 15,
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
    elif action["name"] in ["f5"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        pyautogui.hotkey("f5")
    elif action["name"] in ["select_all_and_copy"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "x")
    elif action["name"] in ["select_all_and_paste"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("ctrl", "v")
    elif action["name"] in ["select_item_and_close_tab"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        pyautogui.hotkey("ctrl", "w")
    elif action["name"] in ["esc"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        pyautogui.hotkey("esc")
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
    print(action.get("action_name"))
    action_sleep = action.get("sleep", 0)
    time.sleep(action_sleep)


for page in page_with_items:
    action_page_change = {
        "x": 118,
        "y": 15,
        "sleep": 1,
        "name": "move_to_click",
        "content": "",
        "action_name": "点击选项卡",

    }
    pyautogui_action(action_page_change)
    for item in range(0, page):
        action_item_click_list = [
            {
                "x": 1380,
                "y": 107,
                "sleep": random.randint(1, 3),
                "name": "move_to_click",
                "content": "",
                "action_name": "切换console",
            },
            {
                "x": 1230,
                "y": 140,
                "sleep": random.randint(1, 3),
                "name": "move_to_click",
                "content": "",
                "action_name": "清空信息console",
            },
            {
                "x": 1302,
                "y": 980,
                "sleep": random.randint(2, 5),
                "name": "select_all_and_copy_and_paste",
                "content": "document.getElementsByClassName(\"product-item-default\")[%s].children[1].click()" % item,
                "action_name": "切换产品",
            },
            {
                "x": 437,
                "y": 18,
                "sleep": random.randint(1, 3),
                "name": "f5",
                "content": "",
                "action_name": "f5",
            },
            {
                "x": 437,
                "y": 17,
                "sleep": random.randint(1, 3),
                "name": "open_console",
                "content": "",
                "action_name": "打开控制台",
            },
            {
                "x": 1380,
                "y": 107,
                "sleep": random.randint(1, 3),
                "name": "select_all_and_copy_and_paste",
                "content": "",
                "action_name": "选择console",
            },
            {
                "x": 1230,
                "y": 140,
                "sleep": random.randint(1, 3),
                "name": "move_to_click",
                "content": "",
                "action_name": "清空信息console",
            },
            {
                "x": 1302,
                "y": 980,
                "sleep": random.randint(1, 3),
                "name": "select_all_and_copy_and_paste",
                "content": r"""
result=[]
result.push(document.getElementsByClassName("detail-box-title")[0].innerText)
result.push(document.getElementsByClassName("product-name")[0].innerText)
result.push(document.getElementsByClassName("product-code-value")[0].innerText)
result.push(document.getElementsByClassName("price-now")[0].innerText)

cxs=document.getElementsByClassName("promotion-item")
cxs_info = []
for (i=0;i<cxs.length;i++){
    cxs_info.push(cxs[i].innerText)
}
ths=document.getElementsByClassName("property-item-title")
tds=document.getElementsByClassName("property-item-value")
kv={}
for (i=0;i<ths.length;i++){
    kv[ths[i].innerText]=tds[i].innerText
}

result_info = {
    "detail-box-title":result[0],
    "product-name":result[1],
    "product-code-value":result[2],
    "price-now":result[3],
    "promotion-item":cxs_info,
    "property-item":kv,
}
console.log(result_info)

dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+JSON.stringify(result_info)+"</textarea>"
document.body.append(dom)
                """,
                "action_name": "执行获取内容的JS",
            },
            {
                "x": 1302,
                "y": 980,
                "sleep": 1,
                "name": "select_all_and_copy_and_paste",
                "content": '',
                "action_name": "获取商品信息"
            },
            {
                "x": 1033,
                "y": 109,
                "sleep": random.randint(1, 3),
                "name": "select_all_and_copy",
                "content": "",
                "action_name": "copy"
            },
            {
                "x": 357,
                "y": 16,
                "sleep": random.randint(1, 2),
                "name": "select_item_and_close_tab",
                "content": "",
                "action_name": "关闭选项卡",
            },
            {
                "x": 437,
                "y": 18,
                "sleep": random.randint(1, 3),
                "name": "move_to_click",
                "content": "",
                "action_name": "点击选项卡",
            },
            {
                "x": 437,
                "y": 18,
                "sleep": random.randint(1, 3),
                "name": "esc",
                "content": "",
                "action_name": "esc",
            },
            {
                "x": 491,
                "y": 159,
                "sleep": random.randint(1, 3),
                "name": "select_all_and_paste",
                "content": "",
                "action_name": "提交",
            },
            {
                "x": 408,
                "y": 250,
                "sleep": random.randint(1, 3),
                "name": "move_to_click",
                "content": "",
                "action_name": "submit",
            },
            {
                "x": 134,
                "y": 23,
                "sleep": random.randint(1, 3),
                "name": "move_to_click",
                "content": "",
                "action_name": "点击选项卡",
            },

            {
                "x": 118,
                "y": 15,
                "sleep": random.randint(1, 3),
                "name": "move_to_click",
                "content": "",
                "action_name": "切换pgy页面",
            },
        ]
        for action_item_click in action_item_click_list:
            pyautogui_action(action_item_click)
    action_page_change_list = [
        {
            "x": 1380,
            "y": 107,
            "sleep": random.randint(1, 3),
            "name": "move_to_click",
            "content": "",
            "action_name": "切换console",
        },
        {
            "x": 1230,
            "y": 140,
            "sleep": random.randint(1, 3),
            "name": "move_to_click",
            "content": "",
            "action_name": "清空信息console",
        },
        {
            "x": 1302,
            "y": 980,
            "sleep": random.randint(1, 3),
            "name": "select_all_and_copy_and_paste",
            "content": "document.getElementsByClassName(\"cm-pagination-next\")[0].click()",
            "action_name": "切换产品页",
        }
    ]
    for action_page_change in action_page_change_list:
        pyautogui_action(action_page_change)

'''
result=[]
result.push(document.getElementsByClassName("detail-box-title")[0].innerText)
result.push(document.getElementsByClassName("product-name")[0].innerText)
result.push(document.getElementsByClassName("product-code-value")[0].innerText)
result.push(document.getElementsByClassName("price-now")[0].innerText)

cxs=document.getElementsByClassName("promotion-item")
cxs_info = []
for (i=0;i<cxs.length;i++){
    cxs_info.push(cxs[i].innerText)
}
ths=document.getElementsByClassName("property-item-title")
tds=document.getElementsByClassName("property-item-value")
kv={}
for (i=0;i<ths.length;i++){
    kv[ths[i].innerText]=tds[i].innerText
}

result_info = {
    "detail-box-title":result[0],
    "product-name":result[1],
    "product-code-value":result[2],
    "price-now":result[3],
    "promotion-item":cxs_info,
    "property-item":kv,
}
console.log(result_info)
'''

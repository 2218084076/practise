import sys
import os
import pyautogui
import time
import pyperclip
# Chrome打开浏览器 https://pgy.xiaohongshu.com/solar/advertiser/patterns/kol
# 选择分类
# 打开审查元素工具 位置1160px
# 滚动屏幕至全部右下角
page_num = 0
page_num_end = 3

page_with_items = [20,20,20,5]
action_list = [
    {
        "x":136,
        "y":17,
        "sleep":1,
        "name":"move_to_click",
        "content":"",
        "action_name":"切换pgy页面",
    },
]
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

for page in page_with_items:
    action_page_change = {
        "x":136,
        "y":17,
        "sleep":1,
        "name":"move_to_click",
        "content":"",
        "action_name":"点击选项卡",
    
    }
    pyautogui_action(action_page_change)
    for item in range(0,page):
        action_item_click_list = [
            {
                "x":1435,
                "y":150,
                "sleep":1,
                "name":"move_to_click",
                "content":"",
                "action_name":"切换console",
            },
            {
                "x":1279,
                "y":177,
                "sleep":1,
                "name":"move_to_click",
                "content":"",
                "action_name":"清空信息console",
            },
            {
                "x":1467,
                "y":323,
                "sleep":5,
                "name":"select_all_and_copy_and_paste",
                "content":"document.getElementsByClassName(\"product-item-default\")[%s].children[1].click()"%(item),
                "action_name":"切换产品",
            },
            {
                "x":391,
                "y":15,
                "sleep":5,
                "name":"open_console",
                "content":"",
                "action_name":"打开控制台",
            },
            {
                "x":1435,
                "y":150,
                "sleep":5,
                "name":"select_all_and_copy_and_paste",
                "content":"",
                "action_name":"选择console",
            },
            {
                "x": 1291,
                "y": 186,
                "sleep": 1,
                "name": "move_to_click",
                "content": "",
                "action_name": "清空信息console",
            },
            {
                "x":1862,
                "y":961,
                "sleep":5,
                "name":"select_all_and_copy_and_paste",
                "content":'result=[]\n'
                          'result.push(document.getElementsByClassName("detail-box-title")[0].innerText)\n'
                          'result.push(document.getElementsByClassName("product-name")[0].innerText)\n'
                          'result.push(document.getElementsByClassName("product-code-value")[0].innerText)\n'
                          'result.push(document.getElementsByClassName("price-now")[0].innerText)\n'
                          'cxs=document.getElementsByClassName("promotion-item")\n'
                          'cxs_info = []\n'
                          'for (i=0;i<cxs.length;i++){\n'
                          '    cxs_info.push(cxs[i].innerText)\n'
                          '}\n'
                          'ths=document.getElementsByClassName("property-item-title")\n'
                          'tds=document.getElementsByClassName("property-item-value")\n'
                          'kv={}\n'
                          'for (i=0;i<ths.length;i++){\n'
                          '    kv[ths[i].innerText]=tds[i].innerText\n'
                          '}\n'
                          'result_info = {\n'
                          '    "detail-box-title":result[0],\n'
                          '    "product-name":result[1],\n'
                          '    "product-code-value":result[2],\n'
                          '    "price-now":result[3],\n'
                          '    "promotion-item":cxs_info,\n'
                          '    "property-item":kv,\n'
                          '}\n'
                          'console.log(result_info)',
                "action_name":"执行获取内容的JS",
            },
            {
                "x":1862,
                "y":961,
                "sleep": 5,
                "name": "select_all_and_copy_and_paste",
                "content": 'dom=document.createElement("div")',
                "action_name": "获取商品信息"
            },
            # document.getElementsByClassName("detail-box-title")[0].innerText
            # document.getElementsByClassName("product-name")[0].innerText
            # document.getElementsByClassName("product-code-value")[0].innerText
            # document.getElementsByClassName("price-now")[0].innerText
            {
                "x":1862,
                "y":961,
                "sleep": 5,
                "name": "select_all_and_copy_and_paste",
                "content":'dom=document.createElement("div")\n'
                          'dom.id="wlb_cover"\n'
                          'dom.style.position="fixed"\n'
                          'dom.style.top="0px"\n'
                          'dom.style.right="0px"\n'
                          'dom.style.zIndex=9999999999999999999\n',
                "action_name":"获取商品信息"
            },
            {
                "x":1862,
                "y":961,
                "sleep": 5,
                "name": "select_all_and_copy_and_paste",
                "content": rf'dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+JSON.stringify(result_info)+"</textarea>"',
                "action_name": "获取商品信息"
            },
            {
                "x":1862,
                "y":961,
                "sleep": 5,
                "name": "select_all_and_copy_and_paste",
                "content":'document.body.append(dom)',
                "action_name":"获取商品信息"
            },
            {
                "x":1130,
                "y":146,
                "sleep":5,
                "name":"select_all_and_copy",
                "content":"",
                "action_name":"copy"
            },
            {
                "x": 732,
                 "y": 13,
                 "sleep": 1,
                 "name": "move_to_click",
                 "content": "",
                 "action_name": "点击选项卡",
            },
            {
                "x": 489,
                "y": 207,
                "sleep": 1,
                "name": "select_all_and_paste",
                "content": "",
                "action_name": "提交",
            },
            {
                "x": 421,
                "y": 286,
                "sleep": 1,
                "name": "move_to_click",
                "content": "",
                "action_name": "submit",
            },
            {
                "x": 447,
                "y": 20,
                "sleep": 1,
                "name": "move_to_click",
                "content": "",
                "action_name": "点击选项卡",
            },
            {
                "x":391,
                "y":15,
                "sleep":2,
                "name":"select_item_and_close_tab",
                "content":"",
                "action_name":"关闭选项卡",
            }
        ]
        for action_item_click in action_item_click_list:
            pyautogui_action(action_item_click)
    action_page_change_list = [
            {
                "x":1435,
                "y":150,
                "sleep":1,
                "name":"move_to_click",
                "content":"",
                "action_name":"切换console",
            },
            {
                "x":1279,
                "y":177,
                "sleep":1,
                "name":"move_to_click",
                "content":"",
                "action_name":"清空信息console",
            },
            {
                "x":1467,
                "y":323,
                "sleep":5,
                "name":"select_all_and_copy_and_paste",
                "content":"document.getElementsByClassName(\"cm-pagination-next\")[0].click()",
                "action_name":"切换产品页",
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

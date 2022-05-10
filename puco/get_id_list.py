import pyautogui
import pyperclip
import time


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
        pyautogui.hotkey("ctrl", "x")
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
    elif action["name"] in ["esc"]:
        pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        pyautogui.hotkey("esc")
    print(action.get("action_name"))
    action_sleep = action.get("sleep",0)
    time.sleep(action_sleep)


while True:
    action_item_click_list = [
        {
            "x":1377,
            "y":147,
            "sleep":0.5,
            "name":"move_to_click",
            "content":"",
            "action_name":"切换console",
        },
        {
            "x":1204,
            "y":172,
            "sleep":0.5,
            "name":"move_to_click",
            "content":"",
            "action_name":"清空信息console",
        },
        {
            "x": 1282,
            "y": 995,
            "sleep": 2,
            "name": "select_all_and_copy_and_paste",
            "content":
'''
cards=document.getElementsByClassName("daren-card")
agree=[]
for (var i=0;i<cards.length;i++){
    if (cards[i].getElementsByClassName("daren-card-status").length>0){
        if (cards[i].getElementsByClassName("daren-card-status")[0].innerText=="已邀约"){
        agree.push(cards[i].getAttribute("data-item-uid"))
}
}    
}
console.log(agree)
dom=document.createElement("div")
dom.id="wlb_cover"
dom.style.position="fixed"
dom.style.top="0px"
dom.style.right="0px"
dom.style.zIndex=9999999999999999999
''',
            "action_name": "获取页面所有博主ID",
        },
        {
            "x": 1282,
            "y": 995,
            "sleep": 2,
            "name": "select_all_and_copy_and_paste",
            "content": r'''
if(JSON.stringify(agree) != '[]'){
dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+JSON.stringify(agree)+"</textarea>"
}
else{
dom.innerHTML="<textarea id=\"wlb_cover_textarea\">"+ +"</textarea>"
}
            ''',
            "action_name": "展示textarea文本框",
        },
        {
            "x": 1282,
            "y": 995,
            "sleep": 0.5,
            "name": "select_all_and_copy_and_paste",
            "content": 'document.body.append(dom)',
            "action_name": "展示textarea文本框"
        },
        {
            "x": 1023,
            "y": 152,
            "sleep": 0.5,
            "name": "esc",
            "content": "",
            "action_name": "esc"
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
            "x": 430,
            "y": 17,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "点击选项卡",
        },
        {
            "x": 527,
            "y": 196,
            "sleep": 1,
            "name": "select_all_and_paste",
            "content": '',
            "action_name": "粘贴"
        },
        {
            "x": 400,
            "y": 282,
            "sleep": 0.5,
            "name": "move_to_click",
            "content": "",
            "action_name": "submit",
        },
        {
            "x": 97,
            "y": 21,
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
            "content": 'document.getElementsByClassName("ant-pagination-item-link")[2].click()',
            "action_name": "下一页"
        },
    ]
    for action_item_click in action_item_click_list:
        pyautogui_action(action_item_click)


'''
cards=document.getElementsByClassName("daren-card")
agree=[]
for (var i=0;i<cards.length;i++){       
    if(cards[i].getElementsByTagName("div").length==32){
        if(cards[i].getElementsByTagName("div")[31].innerText=="同意合作"){
            agree.push(cards[i].getAttribute("data-item-uid"))
        else if()
}}}
'''
import random
import time

import pyautogui
import pyperclip

'''
get_data = function() {
  var i, l, result_list, _i, _len;
  result_list = [];
  l = document.getElementsByClassName("item_con job_title");
  for (_i = 0, _len = l.length; _i < _len; _i++) {
    i = l[_i];
    result_list.push(i.getElementsByTagName("a")[0].getAttribute("href"));
  }
  return result_list;
};
dom = document.createElement("div");
dom.id = "wlb_cover";
dom.style.position = "fixed";
dom.style.top = "0px";
dom.style.right = "0px";
dom.style.zIndex = 9999999999999999999;
dom.innerHTML = "<textarea id=\"wlb_cover_textarea\">" + JSON.stringify(get_data()) + "</textarea>";
document.body.append(dom);
'''
# Chrome打开浏览器 https://pgy.xiaohongshu.com/solar/advertiser/patterns/kol
# 选择分类
# 打开审查元素工具 位置920px
# 滚动屏幕至全部右下角
page_num = 0
page_num_end = 3

page_with_items = [3500]


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
    elif action["name"] in ["paste"]:
        pyautogui.moveTo(x=action.get("x", None), y=action.get("y", None), duration=0, tween=pyautogui.linear)
        pyautogui.click(x=action.get("x", None), y=action.get("y", None), clicks=1, button='left')
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')
    print(action.get("action_name"))
    action_sleep = action.get("sleep", 0)
    time.sleep(action_sleep)


for page in page_with_items:
    action_page_change = {
        "x": 118,
        "y": 22,
        "sleep": random.randint(1, 3),
        "name": "move_to_click",
        "content": "",
        "action_name": "点击选项卡",

    }
    pyautogui_action(action_page_change)
    for item in range(1, page + 1):
        action_item_click_list = [
            {
                "x": 1387,
                "y": 148,
                "sleep": random.uniform(0, 1),
                "name": "move_to_click",
                "content": "",
                "action_name": "切换console",
            },
            {
                "x": 1230,
                "y": 180,
                "sleep": random.uniform(0, 1),
                "name": "move_to_click",
                "content": "",
                "action_name": "清空信息console",
            },
            {
                "x": 1211,
                "y": 987,
                "sleep": random.randint(2, 5),
                "name": "select_all_and_copy_and_paste",
                "content": r'''
get_data = function() {
  var i, l, result_list, _i, _len;
  result_list = [];
  l = document.getElementsByClassName("item_con job_title");
  for (_i = 0, _len = l.length; _i < _len; _i++) {
    i = l[_i];
    result_list.push(i.getElementsByTagName("a")[0].getAttribute("href"));
  }
  return result_list;
};
dom = document.createElement("div");
dom.id = "wlb_cover";
dom.style.position = "fixed";
dom.style.top = "0px";
dom.style.right = "0px";
dom.style.zIndex = 9999999999999999999;
dom.innerHTML = "<textarea id=\"wlb_cover_textarea\">" + JSON.stringify(get_data()) + "</textarea>";
document.body.append(dom);
                ''',
                "action_name": "get_all_link",
            },
            {
                "x": 1046,
                "y": 150,
                "sleep": random.uniform(0, 0.5),
                "name": "select_all_and_copy",
                "content": "",
                "action_name": "copy"
            },
            {
                "x": 928,
                "y": 1045,
                "sleep": random.uniform(0, 0.5),
                "name": "paste",
                "action_name": "提交",
            },
            {
                "x": 989,
                "y": 1053,
                "sleep": random.randint(1, 3),
                "name": "move_to_click",
                "content": "",
                "action_name": "切换浏览器",
            },
            {
                "x": 1387,
                "y": 148,
                "sleep": random.uniform(0, 0.5),
                "name": "move_to_click",
                "content": "",
                "action_name": "切换console",
            },
            {
                "x": 1230,
                "y": 180,
                "sleep": random.uniform(0, 0.5),
                "name": "move_to_click",
                "content": "",
                "action_name": "清空信息console",
            },
            {
                "x": 1211,
                "y": 987,
                "sleep": random.randint(1, 3),
                "name": "select_all_and_copy_and_paste",
                "content": r'document.getElementsByClassName("next")[0].click()',
                "action_name": "next===",
            },
        ]
        for j in action_item_click_list:
            pyautogui_action(j)

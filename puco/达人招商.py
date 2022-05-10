import pyautogui
from time import sleep
import pyperclip
import os
num=0
while True:
    for n in range(0,20):
        pyautogui.moveTo(x=1665,y=177, duration=0.3)
        pyautogui.click(x=1665,y=177, button='left')
        pyautogui.moveTo(x=1665,y=177, duration=0.3)
        pyautogui.click(x=1665,y=177, button='left')
        sleep(1)
        pyautogui.moveTo(x=1703,y=940, duration=0.3)
        pyautogui.click(x=1703,y=940, button='left')
        sleep(1)
        pyautogui.typewrite(f'document.getElementsByClassName("daren-card")[{n}].click()')
        pyautogui.keyDown('enter')
        sleep(1)

        pyautogui.typewrite('document.getElementsByClassName("ant-table-cell ant-table-cell-fix-right ant-table-cell-fix-right-first")[1].getElementsByTagName("div")[0].click()')
        pyautogui.keyDown('enter')
        sleep(1)

        pyautogui.moveTo(x=1114,y=296,duration=0.3)
        pyautogui.click(x=1114,y=296, button='left')
        pyautogui.typewrite("138")
        sleep(0.5)
        pyautogui.moveTo(x=1136,y=355,duration=0.3)
        pyautogui.click(x=1136,y=355, button='left')
        pyautogui.typewrite("30")
        sleep(0.5)
        pyautogui.moveTo(x=1243,y=351,duration=0.3)
        pyautogui.click(x=1243,y=351, button='left')
        sleep(0.5)
        pyautogui.moveTo(x=1078,y=435,duration=0.3)
        pyautogui.click(x=1078,y=435, button='left')
        pyautogui.typewrite("1000000")
        sleep(0.5)
        pyautogui.moveTo(x=1152,y=758,duration=0.3)
        pyautogui.click(x=1152,y=758, button='left')
        pyperclip.copy("我们是Puco唇泥,产品质量好,在寻求合作伙伴~佣金可以谈 生产的工厂是科丝美诗,前期已经在小红书上面有一定的声量,淘系顶流店铺都已铺货,销售量客观,期待和你合作")
        pyautogui.hotkey('ctrl','v')
        sleep(1)

        pyautogui.moveTo(x=1380,y=980, duration=0.3)
        pyautogui.click(x=1380,y=980, button='left')
        sleep(1)
        pyautogui.moveTo(x=22,y=62,duration=0.3)
        pyautogui.click(x=22,y=62,button='left')
        sleep(6)

        pyautogui.moveTo(x=157,y=425,duration=0.3)
        pyautogui.click(x=157,y=425, button='left')

        pyautogui.moveTo(x=1222, y=353, duration=0.3)
        pyautogui.click(x=1222, y=353, button='left')
        sleep(2)

    if num>=1:
        num+=1
        for i in range(1,num):
            pyautogui.moveTo(x=1222, y=353, duration=0.3)
            pyautogui.click(x=1222, y=353, button='left')

            pyautogui.moveTo(x=1665, y=177, duration=0.3)
            pyautogui.click(x=1665, y=177, button='left')
            pyautogui.moveTo(x=1665, y=177, duration=0.3)
            pyautogui.click(x=1665, y=177, button='left')
            sleep(1)
            pyautogui.moveTo(x=1703, y=940, duration=0.3)
            pyautogui.click(x=1703, y=940, button='left')
            sleep(1)

            pyautogui.typewrite('scrollBy(100,9999)')
            pyautogui.keyDown('enter')
            sleep(0.5)
            pyautogui.moveTo(x=1318,y=975,duration=0.3)
            pyautogui.click(x=1318,y=975,button="left")
            sleep(1)

# Js window.location.href  获取网页url

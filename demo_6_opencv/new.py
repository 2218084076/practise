#-*-coding: utf-8 -*-

import os
import time
import random
import json

title_text = [
    'ðå£çº¢ðå¬å­£åäº«',
    'ðå£çº¢â¥',
    'ç¾å¦â¥å½è´§',
    '!åéðè¯è²',
    'ç«éæ¶èð',
    'æ°å¹´çº¢ååå¤ä¸­...',
    'ç»ç»å­ç!å£çº¢ð',
    'èå¹´éå®æ°å!æè§æ¯åå¸­è®¨çº¢åè²!',
    ''
]
content_text = [
    'YSL_12_Corail&&ðYSL_80_Chili',
    'Mac_chiliðMac_Marrakesh&&Mac_Ruby_wooðMac_Dubonnet',
    'ä¼ç§å½è´§_ç¾å¦æ°è¯è²',
    'åææ¯æ¯å¿å¤,å¹¸ç¦å å',
    '2022ææè¾è¦é½ææ¶è·',
    'å¹¸è¿ç©æ¯ä¸å®ä¸è½å°å(é³åä¸å¥½å¥½ç)å¸æä¸å¹´éçææè¾è¦é½ææ¶è·.',
    'è¿æ¬¡çæ°å¹´åéæ¯èå¹´éå®~'
    'ä¸å´çè²å·æ¯MM01&MM02&MM03&MM04...',
    'ææ´»ååä¹å·§,è¿ä¸åªä¿å»å»!!',
    'ä¸å®è½è®¨å°æ´å¤§ççº¢åð§§',
    'ç²é¾åéçè´¨å°æé½å¿è®°å¤¸è¿å¤å°åäº~åååé®åçº¹ð',
    'æ²¿éçé£æ¯ä¹å¾ç¾,ä¸è¦è®©çæ´»çç¹éçµç»ä½æ¬£èµç¾çå¿æ',
    'åå¦é½æ¯å¹³æ¶ç¶æå¥½',
    'å·¨æ¾ç½',
    'å¬å­£æ°å¹´è²å·ç»ä½ ä»¬å®æå¦'
                ]
system_list = [
    'adb -s 869e65410721 shell input tap 306 411',
    'adb -s 869e65410721 shell input tap 675 411'
               ]

json_files = r'D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\files'

def set_file_time(filename, updatetime, access_time):
    # åä¼ ä¿®æ¹æ¶é´ï¼åä¼ è®¿é®æ¶é´
    filename = os.path.abspath(filename)
    new_updatetime = time.mktime(time.strptime(updatetime, '%Y-%m-%d %H:%M:%S'))
    new_access_time = time.mktime(time.strptime(access_time, '%Y-%m-%d %H:%M:%S'))
    os.utime(filename, (new_access_time, new_updatetime))

id_list = os.listdir(r'D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\files')
# print(id_list)

num = 1
one = []
two = []
three = []
original_list = []
for original in os.listdir(r'D:\github\1\hotpoor_autoclick_xhs\demo_6_opencv\afterWork\original'):
    original_list.append(original)
for i in os.listdir(r'D:\github\1\hotpoor_autoclick_xhs\demo_6_opencv\final'):
    if '1x1' in i:
        one.append(i)
    if '2x2' in i:
        two.append(i)
    if '3x3' in i:
        three.append(i)

num = 1
print(one)
print(two)
print(three)
print(original)
for a,b,c,d in zip(one,two,three,original_list):
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if __name__ == '__main__':
        set_file_time(f'D:/github/1/hotpoor_autoclick_xhs/demo_6_opencv/final/{a}', now_time, now_time)
        set_file_time(f'D:/github/1/hotpoor_autoclick_xhs/demo_6_opencv/final/{b}', now_time, now_time)
        set_file_time(f'D:/github/1/hotpoor_autoclick_xhs/demo_6_opencv/final/{c}', now_time, now_time)
        set_file_time(f'D:\github/1/hotpoor_autoclick_xhs/demo_6_opencv/afterWork/original/{d}', now_time, now_time)
    os.system(f'adb -s 869e65410721 push D:/github/1/hotpoor_autoclick_xhs/demo_6_opencv/final/{a} /sdcard/DCIM/Camera')
    os.system(f'adb -s 869e65410721 push D:/github/1/hotpoor_autoclick_xhs/demo_6_opencv/final/{b} /sdcard/DCIM/Camera')
    os.system(f'adb -s 869e65410721 push D:/github/1/hotpoor_autoclick_xhs/demo_6_opencv/final/{c} /sdcard/DCIM/Camera')
    os.system(f'adb -s 869e65410721 push D:/github/1/hotpoor_autoclick_xhs/demo_6_opencv/afterWork/original/{d} /sdcard/DCIM/Camera')
    print(a,b,c,d)
    time.sleep(5)
    os.system('adb -s 869e65410721 shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/')
    print('æå¼å°çº¢ä¹¦\n')
    os.system("adb -s 869e65410721 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
    time.sleep(8)
    print('ç¹å»å°çº¢ä¹¦åå¸å å·\n')
    os.system("adb -s 869e65410721 shell input tap 540 2151")
    time.sleep(5)
    print("éæ©å¾ç\n")

    system = random.shuffle(system_list)
    system = system_list[:2]
    for i in system:
        os.system(f'{i}')
        time.sleep(0.5)
        print(i)
    os.system('adb -s 869e65410721 shell input tap 1037 411')
    os.system('adb -s 869e65410721 shell input tap 311 758')
    print('ä¸ä¸æ­¥\n')
    os.system("adb -s 869e65410721 shell input tap 931 2144")
    time.sleep(2)
    print('ä¸ä¸æ­¥\n')
    os.system("adb -s 869e65410721 shell input tap 998 162")
    time.sleep(3)
    print('ç­å¾ææ¡\n')

    title = random.shuffle(title_text)
    title = title_text[:3]

    content = random.shuffle(content_text)
    content = content_text[4:]

    os.system("adb -s 869e65410721 shell input tap 240 623")
    time.sleep(1)
    print("ç²è´´ææ¡")
    for t in title:
        os.system(f'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg  "{t}"')
        # os.system('adb -s 869e65410721 shell input keyevent KEYCODE_ENTER')
        time.sleep(0.5)
        print(t)
    time.sleep(1)
    os.system("adb -s 869e65410721 shell input tap 491 820")
    for c in content:
        os.system(f'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg "{c}"')
        os.system('adb -s 869e65410721 shell input keyevent KEYCODE_ENTER')
        time.sleep(0.5)
        print(c)
    os.system(f'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg "å£çº¢è¯è²ââMM01~~MM08"')


    os.system("adb -s 869e65410721 shell input tap 649 2100")
    time.sleep(2)

    print('åå¸\n')
    time.sleep(15)
    os.system("adb -s 869e65410721 shell input tap 766 2272")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 978 2137")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 978 2137")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 978 2137")
    time.sleep(2)
    os.system(f"adb -s 869e65410721 shell input swipe 533 271 647 1608 150")

    time.sleep(60 * 2)
    print('start\n')
    print(id)
    i = 1
    print(a, b, c, d)
    while i < 30:
        x1 = random.randint(86, 482)
        y1 = random.randint(1172, 1629)
        a = random.randint(2,5)
        os.system(f"adb -s 869e65410721 shell input tap {x1} {y1}")
        os.system(f"adb -s 869e65410721 shell input swipe 951 994 80 975 100")
        os.system(f"adb -s 869e65410721 shell input swipe 951 994 80 975 100")
        os.system(f"adb -s 869e65410721 shell input swipe 951 994 80 975 100")
        time.sleep(a)
        os.system(f"adb -s 869e65410721 shell input tap 766 2261")
        time.sleep(2)
        print(f'n={i} t={a} (x{x1},y{y1})')
        i += 1
    print(f"{id}\tEnd")
    print(f"num{num}")
    num += 1
    os.system("adb -s 869e65410721 shell input tap 766 2261")
    time.sleep(0.5)
    os.system("adb -s 869e65410721 shell input tap 766 2261")
    time.sleep(0.5)
    os.system("adb -s 869e65410721 shell input tap 766 2261")
    time.sleep(0.5)
    os.system("adb -s 869e65410721 shell input tap 766 2261")
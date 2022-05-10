#-*-coding: utf-8 -*-

import os
import time
import random
import json

title_text = [
    '💄口红💄冬季分享',
    '💄口红♥',
    '美妆♥国货',
    '!唇釉💄试色',
    '火速收藏👍',
    '新年红包准备中...',
    '绝绝子的!口红💄',
    '虎年限定新品!感觉是吃席讨红包色!',
    ''
]
content_text = [
    'YSL_12_Corail&&💄YSL_80_Chili',
    'Mac_chili💄Mac_Marrakesh&&Mac_Ruby_woo💄Mac_Dubonnet',
    '优秀国货_美妆新试色',
    '假期每每必备,幸福加倍',
    '2022所有辛苦都有收获',
    '幸运物是一定不能少哒(阳光下好好看)希望一年里的所有辛苦都有收获.',
    '这次的新年唇釉是虎年限定~'
    '上嘴的色号是MM01&MM02&MM03&MM04...',
    '有活力又乖巧,还不媚俗嘻嘻!!',
    '一定能讨到更大的红包🧧',
    '粉雾唇釉的质地我都忘记夸过多少回了~又哑又遮唇纹👍',
    '沿途的风景也很美,不要让生活的繁重牵绊住欣赏美的心情',
    '化妆都比平时状态好',
    '巨显白',
    '冬季新年色号给你们安排啦'
                ]
system_list = [
    'adb -s 869e65410721 shell input tap 306 411',
    'adb -s 869e65410721 shell input tap 675 411'
               ]

json_files = r'D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\files'

def set_file_time(filename, updatetime, access_time):
    # 先传修改时间，再传访问时间
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
    print('打开小红书\n')
    os.system("adb -s 869e65410721 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
    time.sleep(8)
    print('点击小红书发布加号\n')
    os.system("adb -s 869e65410721 shell input tap 540 2151")
    time.sleep(5)
    print("选择图片\n")

    system = random.shuffle(system_list)
    system = system_list[:2]
    for i in system:
        os.system(f'{i}')
        time.sleep(0.5)
        print(i)
    os.system('adb -s 869e65410721 shell input tap 1037 411')
    os.system('adb -s 869e65410721 shell input tap 311 758')
    print('下一步\n')
    os.system("adb -s 869e65410721 shell input tap 931 2144")
    time.sleep(2)
    print('下一步\n')
    os.system("adb -s 869e65410721 shell input tap 998 162")
    time.sleep(3)
    print('等待文案\n')

    title = random.shuffle(title_text)
    title = title_text[:3]

    content = random.shuffle(content_text)
    content = content_text[4:]

    os.system("adb -s 869e65410721 shell input tap 240 623")
    time.sleep(1)
    print("粘贴文案")
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
    os.system(f'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg "口红试色——MM01~~MM08"')


    os.system("adb -s 869e65410721 shell input tap 649 2100")
    time.sleep(2)

    print('发布\n')
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
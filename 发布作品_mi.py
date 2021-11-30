import os
import time
import random
import json

pic_files = os.listdir(r'D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload')
id_files = os.listdir(r'D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\files')

def set_file_time(filename, updatetime, access_time):
    # 先传修改时间，再传访问时间
    filename = os.path.abspath(filename)
    new_updatetime = time.mktime(time.strptime(updatetime, '%Y-%m-%d %H:%M:%S'))
    new_access_time = time.mktime(time.strptime(access_time, '%Y-%m-%d %H:%M:%S'))
    os.utime(filename, (new_access_time, new_updatetime))

def sentReview(a):
    #切换输入法
    os.system('adb %s shell ime set com.android.adbkeyboard/.AdbIME' % a)
    time.sleep(1)
    #点入第一篇文章
    os.system('adb %s shell input tap 800 1300' % a)
    #点击评论
    os.system('adb %s shell input tap 950 2150' % a)
    time.sleep(1)
    text(a)
    time.sleep(0.5)
    #点击发送
    os.system('adb %s shell input tap 1000 1950' % a)
    #切换回正常输入法
    os.system('adb %s shell ime set com.baidu.input_mi/.ImeService' % a)
    time.sleep(0.5)
    #左上角返回
    os.system('adb %s shell input tap 50 160' % a)

def text(a):
    #事先创建一个txt文件，里面放转发链接
    f = open('buy.txt')
    for line in f:
        os.system("adb %s shell am broadcast -a ADB_INPUT_TEXT --es msg \'%s\'" % (a, line))
    f.close()

# 选择图片
def choice_pic(img_add_num):
    # img_add_num = 4
    x_base = 1037
    x_add = 362
    y_base = 415
    y_add = 350
    for i in range(0, img_add_num):
        x = x_base - x_add * (i % 3)
        y = y_base + y_add * (int(i / 3))
        os.system("adb shell input tap %s %s" % (x, y))
        time.sleep(1)
        print(x, y)

num = 1
id_list = []
for id in id_files:
    id_list.append(id[:-5])

print(f'id_list\n{id_list}')
print(f'len(id_list)\t{len(id_list)}')
# print('\n打开小红书\n')
share_img = "D:/github/1.jpg"
n=0
while True:
    for pic in pic_files:
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # print(now_time)
        if pic.split('_')[0] == id_list[n]:
            print(id_list[n])
            path = fr'D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\{pic}'
            set_file_time(path, now_time, now_time)
            print(path)
            print("======push 上传图片======\n")
            os.system(rf'adb -s 869e65410721 push {path} /sdcard/DCIM/Camera')
            time.sleep(5)
            os.system('adb -s 869e65410721 shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/')
            time.sleep(1)
            os.remove(fr'{path}')
    print('打开小红书')
    os.system("adb -s 869e65410721 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
    time.sleep(8)
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    set_file_time(share_img, now_time, now_time)
    print('\npush share_img\n')
    os.system(rf'adb -s 869e65410721 push {share_img} /sdcard/DCIM/Camera')
    time.sleep(2)

    print('点击小红书发布加号\n')
    os.system("adb -s 869e65410721 shell input tap 540 2151")
    time.sleep(5)

    choice_pic(4) #选择图片

    print('下一步\n')
    os.system("adb -s 869e65410721 shell input tap 931 2144")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 975 155")
    time.sleep(2)

    js_path = fr'D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\files\{id}'
    print(js_path)
    data = json.load(open(js_path,encoding='utf-8'))
    title = data['title']
    content = data['content']
    content = content.replace(' ','♥')

    os.system("adb -s 869e65410721 shell input tap 231 623")
    time.sleep(0.5)
    print("粘贴文案")
    print(title)
    os.system(f'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg  "{title}"')
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 276 893")
    time.sleep(2)
    print(content)
    os.system(f'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg "{content}"')
    time.sleep(2)

    os.system("adb -s 869e65410721 shell input tap 649 2100")
    time.sleep(2)

    print('发布\n')
    os.system("adb -s 869e65410721 shell input tap 784 2097")
    time.sleep(10)
    os.system("adb -s 869e65410721 shell input tap 967 2149")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 967 2149")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 967 2149")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 967 2149")
    time.sleep(2)
    os.system(f"adb -s 869e65410721 shell input swipe 533 271 647 1608 150")

    os.system('adb -s 869e65410721 shell input tap 867 1414')
    time.sleep(2)
    os.system('adb -s 869e65410721 shell input tap 922 2126')
    time.sleep(0.5)
    os.system(f'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg "[买爆R][买爆R]快团团[自拍R][自拍R][买爆R][买爆R]"')
    # os.system(f'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg "六色无一雷品‼"')
    # os.system(fr'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg "全部自留‼🛰小程序://快团团👍👍"')
    time.sleep(1)
    os.system('adb -s 869e65410721 shell input tap 922 2126')
    os.system('adb -s 869e65410721 shell input tap 975 1942')
    os.system(f"adb -s 869e65410721 shell input tap 71 120")

    time.sleep(60*2)
    print('start\n')
    i = 1
    while i < 280:
        x1 = random.randint(86,482)
        y1 = random.randint(1172,1629)
        t = random.randint(2,5)
        os.system(f"adb -s 869e65410721 shell input tap {x1} {y1}")
        os.system(f"adb -s 869e65410721 shell input swipe 951 994 80 975 100")
        os.system(f"adb -s 869e65410721 shell input swipe 951 994 80 975 100")
        os.system(f"adb -s 869e65410721 shell input swipe 951 994 80 975 100")
        time.sleep(t)
        os.system(f"adb -s 869e65410721 shell input tap 71 120")
        time.sleep(2)
        print(f'n={i} (x{x1},y{y1})')
        i += 1
    print(f"{id}\tEnd")
    print(f"num{num}")
    num+=1
    n+=1



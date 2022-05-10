import os
import time
import json
import random

test_files = r'D:\github\1\hotpoor_autoclick_xhs\demo_6_opencv\test'
pic_list = os.listdir(r"D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\pic")


def set_file_time(filename, updatetime, access_time):
    # 先传修改时间，再传访问时间
    filename = os.path.abspath(filename)
    new_updatetime = time.mktime(time.strptime(updatetime, '%Y-%m-%d %H:%M:%S'))
    new_access_time = time.mktime(time.strptime(access_time, '%Y-%m-%d %H:%M:%S'))
    os.utime(filename, (new_access_time, new_updatetime))

def text(a):
    # 事先创建一个txt文件，里面放转发链接
    f = open('buy.txt')
    for line in f:
        os.system("adb %s shell am broadcast -a ADB_INPUT_TEXT --es msg \'%s\'" % (a, line))
    f.close()

def sentReview(a):
    # 切换输入法
    os.system('adb %s shell ime set com.iflytek.inputmethod.miui/.FlyIME' % a)
    time.sleep(1)
    # 点入第一篇文章
    os.system('adb %s shell input tap 800 1300' % a)
    # 点击评论
    os.system('adb %s shell input tap 950 2150' % a)
    time.sleep(1)
    text(a)
    time.sleep(0.5)
    # 点击发送
    os.system('adb %s shell input tap 1000 1950' % a)
    # 切换回正常输入法
    os.system('adb %s shell ime set com.baidu.input_mi/.ImeService' % a)
    time.sleep(0.5)
    # 左上角返回
    os.system('adb %s shell input tap 50 160' % a)

pic_file = os.listdir(r"D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\pic")
pic_list = os.listdir(r"D:\github\1\hotpoor_autoclick_xhs\demo_6_opencv\test")
def push_pic(js):

    path = f"D:/github/hotpoor_autoclick_xhs/mac_xialiwei_256/local_web/static/temp/{js}"
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if __name__ == '__main__':
        set_file_time(path, now_time, now_time)
    print(now_time)
    time.sleep(1)
    print("======push 上传视频======\n")
    os.system(
        f'adb -s 869e65410721 push D:/github/hotpoor_autoclick_xhs/mac_xialiwei_256/local_web/static/temp/{js} /sdcard/DCIM/Camera')
    time.sleep(8)
    os.system(
        'adb -s 869e65410721 shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/')
    time.sleep(2)

num = 1
os.system('adb -s 869e65410721 shell ime set com.android.adbkeyboard/.AdbIME')
for id in pic_list:

    # push pic
    push_pic(id)
    print(js)
    print(f"num = {num}")
    print('打开小红书\n')
    os.system("adb -s 869e65410721 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
    time.sleep(8)

    print('点击小红书发布加号\n')
    os.system("adb -s 869e65410721 shell input tap 540 2151")
    time.sleep(5)
    os.system("adb -s 869e65410721 shell input tap 537 308")
    time.sleep(2)

    print("选择视频\n")
    os.system("adb -s 869e65410721 shell input tap 306 411")
    print('下一步\n')
    os.system("adb -s 869e65410721 shell input tap 931 2144")
    time.sleep(2)
    print('选择音乐\n')
    os.system("adb -s 869e65410721 shell input tap 93 2102")
    time.sleep(3)
    os.system("adb -s 869e65410721 shell input tap 839 1873")
    time.sleep(3)
    os.system("adb -s 869e65410721 shell input tap 839 1873")
    time.sleep(3)
    os.system("adb -s 869e65410721 shell input tap 187 1231")
    time.sleep(3)

    print('下一步\n')
    os.system("adb -s 869e65410721 shell input tap 954 2114")
    time.sleep(3)
    print('等待文案\n')


    js = js.split('.mp4')[0]
    print(js)
    # os.system('adb shell ime set com.android.adbkeyboard/.AdbIME')
    # js_path = json_files + '\' + js + '.json'
    js_path = rf'{json_files}\{js}.json'
    print(js_path)
    data =json.load(open(js_path,encoding='utf-8'))
    title = data['title']
    print(title)
    content = data['content']
    content = content.replace(' ','♥')
    print(content)
    os.system("adb -s 869e65410721 shell input tap 201 886")
    time.sleep(0.5)
    print("粘贴文案")
    os.system(f'adb -s 869e65410721 shell am broadcast -a ADB_INPUT_TEXT --es msg  "{title}"')
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 549 1055")
    time.sleep(2)
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
    print(js)
    i = 1
    while i < 100:
        x1 = random.randint(86,482)
        y1 = random.randint(1172,1629)
        a = random.randint(2,10)
        os.system(f"adb -s 869e65410721 shell input tap {x1} {y1}")
        time.sleep(a)
        os.system(f"adb -s 869e65410721 shell input tap 71 120")
        time.sleep(2)
        print(f'n={i} t={a} (x{x1},y{y1})')
        i += 1
    print(f"{js}\tEnd")
    print(f"num{num}")
    num+=1
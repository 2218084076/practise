import os
import time
import json

l=['869e65410721']
video_list = os.listdir(r'D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\temp')
# js_list = [
#             '619b2257000000000102c5a4',
#             '619ccf43000000002103ac14',
#             '61961e8d0000000021039a09',
#     ]
print(video_list)
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
    #切换输入法
    os.system('adb %s shell ime set com.iflytek.inputmethod.miui/.FlyIME' % a)
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

def push_video(js):
    path = f"D:/github/hotpoor_autoclick_xhs/mac_xialiwei_256/local_web/static/temp/{js}"
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if __name__ == '__main__':
        set_file_time(path, now_time, now_time)
    print(now_time)
    time.sleep(1)
    print("======push 上传视频======\n")
    os.system(f'adb -s 869e65410721 push D:/github/hotpoor_autoclick_xhs/mac_xialiwei_256/local_web/static/temp/{js} /sdcard/DCIM/Camera')
    time.sleep(8)
    os.system('adb -s 869e65410721 shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/')
    time.sleep(2)


for js in video_list:
    # push video
    push_video(js)
    print(js)

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

    print("#打开浏览器\n")
    os.system("adb -s 869e65410721 shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1")
    time.sleep(5)
    print('刷新\n')
    os.system("adb -s 869e65410721 shell input tap 967 139")
    time.sleep(2)
    
    os.system("adb -s 869e65410721 shell input tap 155 358")
    time.sleep(2)
    js = js.split('.mp4')[0]
    print(js)
    # os.system('adb shell ime set com.android.adbkeyboard/.AdbIME')
    os.system(f'adb -s 869e65410721 shell input text "{js}"')
    time.sleep(6)
    # os.system('adb shell ime set com.iflytek.inputmethod.miui/.FlyIME')
    print('get')
    os.system("adb -s 869e65410721 shell input tap 212 473") #查询
    time.sleep(8)
    os.system('adb -s 869e65410721 shell input tap 311 1275')

    print('adb -s 869e65410721 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1\n')
    os.system("adb -s 869e65410721 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
    time.sleep(5)
    os.system("adb -s 869e65410721 shell input tap 201 886")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 336 1517")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 453 1631")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 768 2272")
    time.sleep(2)

    print("#打开浏览器\n")
    os.system("adb -s 869e65410721 shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 311 1339")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 318 632")
    time.sleep(2)

    os.system("adb -s 869e65410721 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1") #打开小红书
    time.sleep(5)
    os.system("adb -s 869e65410721 shell input tap 336 1517")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 453 1631")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 546 1496")
    print("粘贴内容")
    time.sleep(2)
    os.system("adb -s 869e65410721 shell input tap 991 1304")
    time.sleep(2)
    print('完成')
    # os.system("adb -s 869e65410721 shell input tap 615 1165")

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
    # os.system("adb -s 869e65410721 shell input tap 768 2272")

    time.sleep(60*3)
    print('start\n')
    print(js)
    i = 1
    while i < 80:
        for n in l:
            # t=random.randint(1,4)
            os.system(f"adb -s {n} shell input tap 284 1328")
            # os.system(f"adb -s {n} shell input swipe 951 994 80 975 100")
            # os.system(f"adb -s {n} shell input swipe 951 994 80 975 100")
            # os.system(f"adb -s {n} shell input swipe 951 994 80 975 100")
            time.sleep(4)
            os.system(f"adb -s {n} shell input tap 71 120")
            time.sleep(2)
            os.system(f"adb -s {n} shell input tap 800 1414")
            time.sleep(5)
            os.system(f"adb -s {n} shell input tap 71 120")
            time.sleep(2)
        print(f'n={i} ') 
        i += 1
    print(f"{js}\tEnd")

import os
import time
import random

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

id_list = []
for id in id_files:
    id_list.append(id[:-5])

for i in id_list:
	now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	for pic in pic_files:
		if pic.split('_')[0] == i:
			print(pic)
			path = fr'D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\{pic}'
			print(path)
			set_file_time(path,now_time,now_time)

	print(now_time)
	time.sleep(2)
	print("======push 上传图片======\n")
	os.system(rf'adb -s 869e65410721 push D:\github\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\{pic} /sdcard/DCIM/Camera')
	time.sleep(8)
	os.system('adb -s 869e65410721 shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/')
	time.sleep(3)

	print('打开小红书\n')
	os.system("adb -s 869e65410721 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
	time.sleep(8)

	print('点击小红书发布加号\n')
	os.system("adb -s 869e65410721 shell input tap 540 2151")
	time.sleep(5)
	os.system("adb -s 869e65410721 shell input tap 537 308")
	time.sleep(3)

	os.system('adb -s 869e65410721 shell input tap 537 308')

    # img_add_num = 4
    # x_base = 306
    # x_add = 362
    # y_base = 411
    # y_add = 350
    # for i in range(0,img_add_num):
	# 	x = x_base + x_add*(i%3)
	# 	y = y_base + y_add*(int(i/3))
	# 	os.system("adb shell input tap %s %s"%(x,y))
	# 	time.sleep(2)


# print("#打开浏览器\n")
# os.system("adb -s 869e65410721 shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1")



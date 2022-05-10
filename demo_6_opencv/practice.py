import os
import time
pic_file = os.listdir(r"D:\github\1\hotpoor_autoclick_xhs\mac_xialiwei_256\local_web\static\upload\pic")
pic_list = os.listdir(r"D:\github\1\hotpoor_autoclick_xhs\demo_6_opencv\test")
pic2 = os.listdir(r'D:\github\1\hotpoor_autoclick_xhs\demo_6_opencv\test\YSL')
l = []
for i in pic_list:
    for n in pic_file:
        j = i.split('_')[0]
        if j == n.split('_')[0]:
            path = "D:/github/1/hotpoor_autoclick_xhs/demo_6_opencv/test/"+i
            l.append(path)
            # print(path)
# print(l)
for n in range(0,len(l),9):
    l1 = l[n:n+9]
    # print(l1)
print('================')
list1=[]
for i in pic2:
    for n in pic_file:
        if i.split('_')[0] == n.split('_')[0]:
            path = "D:/github/1/hotpoor_autoclick_xhs/demo_6_opencv/test/YSL/"+i
            list1.append(path)
print(list1)
for n in range(0,len(list1),2):
    l2 = list1[n:n+2]
    for i in l2:
        os.system(
            f'adb -s 869e65410721 push D:/github/hotpoor_autoclick_xhs/mac_xialiwei_256/local_web/static/temp/{i} /sdcard/DCIM/Camera')
        time.sleep(8)
        print(f"adb -s 869e65410721 push D:/github/hotpoor_autoclick_xhs/mac_xialiwei_256/local_web/static/temp/{i} /sdcard/DCIM/Camera")
        os.system(
            'adb -s 869e65410721 shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/')
        time.sleep(2)
    print(l2)

import os
import time
import random
'''# 购物车
# 761 2271
os.system("adb -s 869e65410721 shell input tap 761 2271")
# 去结算
os.system("adb -s 869e65410721 shell input tap 893 2239")
# 提交订单
os.system("adb -s 869e65410721 shell input tap 889 2271")
# esc
os.system("adb -s 869e65410721 shell input tap 533 1408")'''
n=1

def meiri(x,y,t):
    os.system("adb -s 9038c19f shell input tap %s %s"%(x,y))

def dingdong(x,y):

    os.system("adb -s 9038c19f shell input tap %s %s"%(x,y))
n=1
while True:
    t=random.uniform(0,0.5)
    x2=random.randint(761,972)
    y2=random.randint(2225,2292)
    # x=random.randint(770,950)
    # y=random.randint(2242,2270)
    # meiri(x,y,t)\
    dingdong(x2,y2)
    print(n,'time_sleep=%s'%(t))
    n+=1
    time.sleep(t)

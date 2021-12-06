import random

system_list = ['adb -s 869e65410721 shell input tap 306 411',
               'adb -s 869e65410721 shell input tap 675 411',
               'adb -s 869e65410721 shell input tap 311 758']

system = random.shuffle(system_list)
system = system_list[:2]
for i in system:
    print(i)
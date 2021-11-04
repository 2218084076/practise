rem 打开JD商城应用
adb shell monkey -p com.jingdong.app.mall -c android.intent.category.LAUNCHER 1
rem sleep 4
ping -n 4 127.0.0.1>nul
rem 点击我
adb shell input tap 970 2124
rem sleep 2
ping -n 2 127.0.0.1>nul
rem 点击签到领豆
adb shell input tap 331 1464
rem sleep 2
ping -n 2 127.0.0.1>nul
rem 点击签到领京豆
adb shell input tap 510 501
rem sleep 2
ping -n 2 127.0.0.1>nul
rem 点击种豆瓜分京豆
adb shell input tap 510 675
rem sleep 5
ping -n 5 127.0.0.1>nul
rem 【手工点击】种豆瓜分京豆，等5秒，自动返回
adb shell input tap 84 150
rem sleep 1
ping -n 1 127.0.0.1>nul
adb shell input tap 84 150
rem sleep 1
ping -n 1 127.0.0.1>nul
adb shell input tap 500 850
rem sleep 2
ping -n 2 127.0.0.1>nul
adb shell input tap 861 1072
rem sleep 5
ping -n 5 127.0.0.1>nul
adb shell input tap 521 860
rem sleep 2
ping -n 2 127.0.0.1>nul
adb shell monkey -p com.jingdong.app.mall -c android.intent.category.LAUNCHER 1
rem sleep 2
ping -n 2 127.0.0.1>nul
adb shell input tap 904 1273


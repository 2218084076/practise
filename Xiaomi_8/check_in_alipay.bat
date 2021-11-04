adb shell monkey -p com.eg.android.AlipayGphone -c android.intent.category.LAUNCHER 1
rem sleep 5
ping -n 5 127.0.0.1>nul
rem 点击我
adb shell input tap 970 2124
rem sleep 3
ping -n 3 127.0.0.1>nul
rem 点击支付宝会员
adb shell input tap 846 534
rem sleep 3
ping -n 3 127.0.0.1>nul
rem 点击签到
adb shell input tap 550 766
rem sleep 3
ping -n 3 127.0.0.1>nul
rem 点击签到后返回
adb shell input tap 61 127
rem sleep 3
ping -n 3 127.0.0.1>nul
rem 点击全部领取
adb shell input tap 914 1012
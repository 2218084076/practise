rem 打开小红书应用
adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1
rem sleep 4
ping -n 4 127.0.0.1>nul
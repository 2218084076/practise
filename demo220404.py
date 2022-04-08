# 上面写好的方法我们在这个文件来应用
# 引入上面我们命名方法的文件
from dou_download_video import get_video,analysis_works,download_img

u = analysis_works(input('抖音分享链接\n'))
print(u)
get_video(u[0],u[1])
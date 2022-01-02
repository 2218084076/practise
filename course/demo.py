## =====> count方法 <====
# a='Hello World......@13423142'
# print(f'str(a)为\t"{a}"')
# print(f'字母H出现的次数\t{a.count("H")}次')
# print(f'数字3出现的次数\t{a.count("3")}次')
# print(f'符号"."出现的次数\t{a.count(".")}')

## ====> 计算圆形面积周长 <====
# import math
#
# radius=input("radius of cricle:")
# radius=int(radius)
# c = 2*math.pi*radius
# a=math.pi*radius*radius
#
# print ( "circumference of circle(周长): ",c)
# print ( "area of cricle(面积): ",a)

## ===> 0~50内3的倍数 <===
# l=[]
# for i in range(0,51):
#     if i>0 and i%3 == 0:
#         # print(i)
#         l.append(i)
# print(f'0~50内3的倍数为：{l}')


# ===> 贺卡 <===
# holiday = input('请输入节日：')
# To_name = input('请输入收件人姓名：')
# Fr_name = input('请输入送件人姓名：')
# print ('--*--*--*--*--*--*--*--*--*--*--')
# print('     节    日     祝       福')
# print(f'Dear {To_name}:\n')
# print('      祝您'+holiday+'快乐！\n')
# print('      身体健康，心想事成，天天快乐！\n')
# print('                      ' + Fr_name)
# print('--*--*--*--*--*--*--*--*--*--*--')


# ===> 计算门票价格 <====
# a=input('游客人数')
# a=int(a)
# if a<=5:
#     total = a*160
#     print(f'{a}*160')
# if a>5:
#     total = a*140
#     print(f'{a}*140')
# print(f'{a}人 应付{total}')



#   ===> 字典拼接 <===
# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# b=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# d = dict(zip(a,b))
# print(d)

#====> 奇偶分类 <====
# numbers = [12, 37, 5, 42, 8, 3]
# one = []
# two = []
# for n in numbers:
#     if n%2 == 0:
#         two.append(n)
#     else:
#         one.append(n)
# print(f"奇数{one}")
# print(f"偶数{two}")
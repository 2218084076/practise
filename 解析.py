import random
import os

title_text = ['放大优点化妆法','💄口红💄试色','🍓氛围感','♥民族国货好物']
content_text = ['MM01~~MM08\n',
                '\nYSL 12 Corail\nYSL 80 Chili',
                '\nMac chili\nMac Marrakesh\nMac Ruby woo\nMac Dubonnet\n',
                '\n优秀国货  美妆新试色\n',
                '\n圣诞好物推荐🎄\n',
                '\n一支带有细闪，有一点点颗粒感很滋润的茶棕色，偏暖的颜色～比较气质低调优雅！！！\n',
                '\n点都不沉闷\n'
                ]


people = ['foo', 'bar', 'baz', 'eggs', 'ham', 'spam', 'eric', 'john', 'terry']
random.shuffle(people)
car1, car2 = people[:4], people[4:]

print(car1)
print(car2)
one = []
two = []
three = []
for i in os.listdir(r'D:\github\1\hotpoor_autoclick_xhs\demo_6_opencv\final'):
    if '1x1' in i:
        one.append(i)
    if '2x2' in i:
        two.append(i)
    if '3x3' in i:
        three.append(i)
print(one)
print(two)
print(three)
for a,b,c in zip(one,two,three):
    print(a,b,c)
    break
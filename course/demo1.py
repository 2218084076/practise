str = "1:Cap 2:Low 3:Num 4:Other"
print('str=',str)
dicta = {}
for i in str:
    dicta[i] = str.count(i)
print (dicta)
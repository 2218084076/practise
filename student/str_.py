import pymysql
l=[]
def B(str):
	for i in list(str):
		print(i)
		if i != "a":
			l.append(i)
	print('remove"a" list:\n%s'%(l))
	l.sort()
	str_new = "".join(l)
	print('return_str:\t"%s"'%(str_new))
def A(str):
	for i in list(str):
		print(i)
		if i != "a":
			l.append(i)
	l.sort()
	print('remove"a" list:\n%s'%(l))
	l.reverse()
	print("l_reverse: \n%s"%(l))
	str_new = "".join(l)
	print('return_str:\t"%s"'%(str_new))
# B(input("input string\n"))

# def twoSum(nums, target):
#     lens = len(nums)
#     print(lens)
#     j=-1
#     for i in range(lens):
#         if (target - nums[i]) in nums:
#             if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):
#             #如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
#                 continue
#             else:
#                 j = nums.index(target - nums[i],i+1)
#                 #index(x,i+1)是从num1后的序列后找num2
#                 break
#     if j>0:
#         return "1",[i,j]
#     else:
#         return "0",[]
#
# print(twoSum([2,7,11,15],9))

def conndb():
	conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root@123',db='mk_base',charset='utf-8')
	cur = conn.cursor()
	# cur.execute()
	result = cur.fetchall()
	cur.close()
	conn.close()
	print(result)
conndb()
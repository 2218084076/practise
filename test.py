# a=[{"1":["2","3",{"4":["5","6"]}]},{"1":["2","3",{"4":["5","6"]}]}]
#
# b=[{"1":["2","3",{"4":["5",{"6":["7"]},"8",{"9":["10"]}]}]}]
#
# out_a=[]
# out_b=[]
#
# def check_dict(list_now,result_list=[]):
#     for i in list_now:
#         if isinstance(i,dict):
#             key = list(i.keys())[0]
#             print('i:',i)
#             print('key：',key)
#             result_list.append(key)
#             result_list = check_dict(i.get(key,[]),result_list)
#             print(result_list)
#         else:
#             result_list.append(i)
#     return result_list
# out_a = check_dict(a,out_a)
# print("----")
# print(a)
# print("out_a:",out_a)
# print("----")
# print(b)
# out_b = check_dict(b,out_b)
# print("out_b:",out_b)
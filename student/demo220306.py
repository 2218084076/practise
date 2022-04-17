import reas
n="Terry"
p=123

name = str(input("Name:\n"))
password = int(input("Password:\n"))
code = "T"
u_code = str(input("Code:\n"))

if u_code == code:
	if name == n and password == p:
		print("Ture")
	else:
		print("error")
else:
	print("no code")

print("# 在这里编辑")
# 编辑后要保存
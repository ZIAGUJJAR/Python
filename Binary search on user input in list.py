List = [1,2,3,4,5,6,7,8]
exe = 1
Len = len(List)
LenBi = Len/2
LenBi = int(LenBi)
##0---LenBi && LenBi --- Len

User_Input = int(input("Please input your number to search in list: "))

for x in range(0,LenBi):
	if User_Input == List[x]:
		print("Number found with index ",x+1)
		exe = 0
	else:
		continue
		
if exe==1:
	for i in range(LenBi,Len):
		if User_Input == List[i]:
			print("Number found with index ",i+1)
			exe = 0
		else:
			continue

if exe == 1:
	print("Number not found")
List = [1,2,3,4,5,6,7,8,9]

Len = len(List)   ###Length of List

Greatest_Num = List[0]

for x in range(0,Len):
	if Greatest_Num > List[x]:
		continue
	else:
		Greatest_Num = List[x]


print(Greatest_Num)
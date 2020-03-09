List = [1,2,0,4,5,6,7,8,9]

Len = len(List)  ###Length Of List

Lowest_Num = List[0]

for x in range(0,Len):
	if Lowest_Num < List[x]:
		continue
	else:
		Lowest_Num = List[x]

print(Lowest_Num)
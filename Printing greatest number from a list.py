
List = [1,2,3,4,5,6,12,8,9]

Greatest_Number = List[0]

for i in range(0,9):
	if Greatest_Number < List[i]:
		Greatest_Number = List[i]
	else:
		continue
print(Greatest_Number)
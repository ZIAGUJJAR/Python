
Required_Number = int(input("Please input number you want to check in database: "))

a=0

List = (1,2,3,4,5,6,7,8,9)

for x in range(0,9):
	if List[x] == Required_Number:
		print("Yes your number is in our database")
		a=1
		break
if a==0:
	print("Number not found.")

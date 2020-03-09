Table = input("Please input the number: ")
Table_int = int(Table)

if Table_int <= 12:
	for x in range(1,11):
		print(Table,' * ',x,' = ',Table_int*x)
else:
	print("Sorry your number must be less than 12.")

Number_By_User = input("Please input any number: ")  ###This number will be in string form bbcz return type of input function is string
Number_By_User_int = int(Number_By_User) ###We need to get int as input so we will cast it to int

n=0

while n<Number_By_User_int:
	n = n+1

print("The sum of numbers from 1 to ",Number_By_User_int," is = ",n)

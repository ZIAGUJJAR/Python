#Muhammad Zia Ur Rehman
#BSEF19A005

#Taking 2 int form users

num_1 = int(input("Please input first number: "))
num_2 = int(input("Please input second number: "))

if num_1%num_2 == 0 or num_2%num_1 == 0:
    print("WOW! They are multiple of each other")
else:
    print("OOPs! They are NOT multiple of each other")
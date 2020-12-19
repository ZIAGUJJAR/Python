#Muhammad Zia Ur Rehman
#BSEF19A005


# Taking 5 integers form user

num_1 = int(input("Please enter number 1: "))
num_2 = int(input("Please enter number 2: "))
num_3 = int(input("Please enter number 3: "))
num_4 = int(input("Please enter number 4: "))
num_5 = int(input("Please enter number 5: "))

# looking for greatest number
if (num_1 >= num_2) and (num_1 >= num_3) and (num_1 >= num_4) and (num_1 >= num_5):
    greates_num = num_1
elif num_2 >= num_1 and num_2 >= num_3 and num_2 >= num_4 and num_2 >= num_5:
    greates_num = num_2
elif num_3 >= num_2 and num_3 >= num_1 and num_3 >= num_4 and num_3 >= num_5:
    greates_num = num_3
elif num_4 >= num_2 and num_4 >= num_3 and num_4 >= num_1 and num_4 >= num_5:
    greates_num = num_4
elif num_5 >= num_2 and num_5 >= num_3 and num_5 >= num_4 and num_5 >= num_1:
    greates_num = num_5
else:
    pass


#looking for lowest number
if (num_1 <= num_2) and (num_1 <= num_3) and (num_1 <= num_4) and (num_1 <= num_5):
    lowest_num = num_1
elif num_2 <= num_1 and num_2 <= num_3 and num_2 <= num_4 and num_2 <= num_5:
    lowest_num = num_2
elif num_3 <= num_2 and num_3 <= num_1 and num_3 <= num_4 and num_3 <= num_5:
    lowest_num = num_3
elif num_4 <= num_2 and num_4 <= num_3 and num_4 <= num_1 and num_4 <= num_5:
    lowest_num = num_4
elif num_5 <= num_2 and num_5 <= num_3 and num_5 <= num_4 and num_5 <= num_1:
    lowest_num = num_5
else:
    pass

#printing lowest and greatestt number in group
print("(",greates_num,",",lowest_num,")" )

#Muhammad Zia Ur Rehman
#BSEF19A005

#taking 10 inputs from user
input_list = input("Please enter 10 values separated by space: ").split()

for x in range(len(input_list)):
    input_list[x] = int(input_list[x])

#printing llist of users inputs
print(input_list)

#updating the exsisting list
input_list =[x*x*x for x in input_list]

#printing llist of inputs
print(input_list)
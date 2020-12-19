
#Muhammad Zia Ur Rehman
#BSEF19A005

# getting input from user

input_numbers = input("Please enter 4 numbers: ").split(",")
print(input_numbers)

if len(input_numbers) >= 4:

    for x in range(4):
        input_numbers[x] = int(input_numbers[x])
        print(type(input_numbers[x]))
else:
    print("Please enter atleast 4 numbers")

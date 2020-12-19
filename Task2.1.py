#Muhammad Zia Ur Rehman
#BSEF19A005

#declaring strings
user_input = ''
user_string = ''

while user_input != '.':
    #taking input form user till .
    user_input = input("Please enter input for a string: ")

    #checking for users input length
    if(len(user_input) >= 10):
        user_string = user_string + user_input

    #checking for "."
    elif user_input == '.':
        pass
    else:
        print("Plese provide input of length greater than 10")
    
#printing string concatenated with all o users input
print(user_string)
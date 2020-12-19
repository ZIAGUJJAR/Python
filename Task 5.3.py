#Muhammad Zia Ur Rehman
#BSEF19A005


# reading new.txt file
file_handle = open("New.txt", "r")

# creating new dictionary
dictionary = {}

# looping through file
for x in file_handle:

    # extracting data from file
    key = x[0:5]
    value = x[6:8]

    # making dictionary
    dictionary[key] = value

length = len(dictionary)
# updating dictionary


key = input("Please enter a KEY: ")
value = int(input("Please enter a VALUE: "))

key_list = dictionary.keys()

error = False

for i in key_list:
    if key == i:
        dictionary[key] = value
        error = False
        break
    else:
        error = True
print(dictionary)
if error == True:
    print("Sorry this KEY doesn't exsists")

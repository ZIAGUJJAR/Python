#Muhammad Zia Ur Rehman
#BSEF19A005


#reading new.txt file
file_handle = open("New.txt","r")

#creating new dictionary

dictionary = {}

#looping through file
for x in file_handle:

    #extracting data from file
    key = x[0:5]
    value = x[6:8]
    
    # making dictionary
    dictionary[key] = value

print(dictionary)

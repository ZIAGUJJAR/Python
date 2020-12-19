#Muhammad Zia Ur Rehman
#BSEF19A005

#taking input from user of lenght greater than4

substring = ''
while len(substring) <= 4: 
    substring = input("Please enter a input greater than 4: ")

#slicing and inserting the same string between 3 & 4 indexex
print(substring[:4] + substring + substring[4:])
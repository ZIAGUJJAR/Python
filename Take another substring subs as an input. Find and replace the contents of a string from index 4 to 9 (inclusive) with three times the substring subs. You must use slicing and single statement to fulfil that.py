#Muhammad Zia Ur Rehman
#BSEF19A005

#taking input from user of lenght greater than 9

substring = ''
while len(substring) <= 9: 
    substring = input("Please enter a input greater than 9: ")

#slicing and three times the substring
print(substring.replace(substring[4:10],(substring[4:10] + substring[4:10] + substring[4:10])))
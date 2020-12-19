#Muhammad Zia Ur Rehman
#BSEF19A005


#importing library for generating random number
import random

#opening new file
file_handle = open('New.txt',"w")


#looping 10 times to write 10 lines to file
for x in range(10):
    
    #generating random numbers
    num1 = str(random.uniform(0,1))
    num1 = num1[:5]
    num2 = str(random.randint(10,50))

    #putting these numbers into file
    line = num1+","+num2+"\n"
    file_handle.write(line)

file_handle.close
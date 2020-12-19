#Muhammad Zia Ur Rehman
#BSEF19A005

num = 1

for x in range(1, 7):
    for i in range(1, 7):
        if x == 1:
            print(i, " ", end="")

        else:
            print(num," ", end="")
            num = num + x

    num = 1
    print("\n")
    

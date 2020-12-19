#Muhammad Zia Ur Rehman
#BSEF19A005


#importing module for fractions
import fractions

#getting users input for preparing fractions
numerator_F1 = int(input("Please enter numerator for F1: "))
denominator_F1 = int(input("Please enter numerator for F1: "))

numerator_F2 = int(input("Please enter numerator for F2: "))
denominator_F2 = int(input("Please enter numerator for F2: "))

#making fractions
F1 = fractions.Fraction(numerator_F1,denominator_F1)
F2 = fractions.Fraction(numerator_F2,denominator_F2)

#adding and subtracting fractions
add = F1+F2
subtract = F1-F2

#printing addition and subtraction
print(add)
print(subtract)
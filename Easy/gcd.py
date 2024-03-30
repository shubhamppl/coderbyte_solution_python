#  Have the function Division(num1,num2) take both parameters being passed and return the Greatest Common Factor.
# That is, return the greatest number that evenly goes into both numbers with no remainder. For example: 12 and 16 both
# are divisible by 1, 2, and 4 so the output should be 4. The range for both parameters will be from 1 to 10^3.
import math as m
def Division(num1,num2):
     
    return m.gcd(num1,num2)
    
print(Division(16, 12))   # Expected output: 4
print(Division(45, 15))   # Expected output: 15
print(Division(100, 25))  # Expected output: 25
print(Division(81, 27))   # Expected output: 27
print(Division(7, 3))     # Expected output: 1 (since 7 and 3 are coprime)
    

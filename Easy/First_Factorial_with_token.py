'''First Factorial
Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer.
Examples
Input: 4
Output: 24
Input: 8
Output: 40320 
replace x in every 3rd position after output token=jamtof1gze75 
final output =  40X20XamXofXgzX75 '''

import math as m
def dd(p):
    k=int(p)
    kp=m.factorial(k)
    token='jamtof1gze75'
    res= str(kp) +token
    res=list(res)
    for i in range(2,len(res),3):
        res[i] ='X'
        
    
    return ''.join(res)
print(dd('8'))

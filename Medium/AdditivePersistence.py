'''// // have the function AdditivePersistence(num) take the num parameter being passed which will always be a positive integer and return its additive persistence 
which is the number of times you must add the digits in num until you reach a single digit.
For example: if num is 2718 then your program should return 2 because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you stop at 9. 

'''
def AdditivePersistence(s):
    c = 0  # Initialize a counter to keep track of the number of iterations
    while s > 9:  # Continue the loop until the number becomes a single-digit number
        s = sum(int(x) for x in str(s))  # Convert the integer s to a string, iterate over its digits, convert them back to integers, and sum them up
        c += 1  # Increment the counter for each iteration
    return c  # Return the additive persistence
print(AdditivePersistence(199))
print(AdditivePersistence(2718))

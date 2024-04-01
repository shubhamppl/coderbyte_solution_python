#19 is Happy Number,
#1^2 + 9^2 = 82
#8^2 + 2^2 = 68
#6^2 + 8^2 = 100
#1^2 + 0^2 + 0^2 = 1
#As we reached to 1, 19 is a Happy Number.
def is_happy_number(n):
    for i in range(100):
        n = sum(int(x)**2 for x in str(n))
        if n == 1:
            return True
    return False


# Test cases
print(is_happy_number(19))  # Expected to return True, as 19 is a happy number
print(is_happy_number(2))   # Expected to return False, as 2 is not a happy number


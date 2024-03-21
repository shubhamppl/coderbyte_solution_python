#def SearchingChallenge(str): check print(SearchingChallenge("3gy41d216"))  # Output:
# true print(SearchingChallenge("f09r27i8e67"))  # Output: false #sum of 2 number is even or not
'''input and checks if there are two consecutive digits in the string such that when those two digits are concatenated
and converted to an integer, the resulting number is even'''
def SearchingChallenge(s):
    s=list(s)
    for i in range(len(s)-1):
        if s[i].isdigit() and s[i+1].isdigit():
            num = str(s[i])+str(s[i+1])
            num=int(num)
            if (num)%2 ==0:
                return True 
    return False

print(SearchingChallenge('f09r2w7i8w1'))
print(SearchingChallenge("3gy41d216"))

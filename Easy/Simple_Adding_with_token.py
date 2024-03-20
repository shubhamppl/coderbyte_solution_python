#The function MathChallenge(num) adds up all the numbers from 1 to num. For example, if the input is 4, 
#the program should return 10 because 1 + 2 + 3 + 4 = 10. The parameter num will be any number from 1 to 1000. 
#After the function is working, the final output string should be combined with the ChallengeToken in reverse order
# and separated by a colon. For example, for input 12, the output is 78, and the final output is 87:739mn58rog. 
#For input 140, the output is 9870, and the final output is 0789:739mn58rog.
def MathChallenge(num):
    k=0
    token='739mn58rog'
    for i in range(num+1):
        k += i
    res =str(k)[::-1]+':'+token
    return res
    
print(MathChallenge(140))

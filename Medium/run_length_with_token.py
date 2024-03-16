'''Given an input string, write a function that returns a compressed version of the string using the Run-length encoding algorithm. 
This algorithm works by taking the occurrence of each repeating character and outputting that number along with a single character of the repeating sequence. 
For example: “wwwggopp” would return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.'''
# Output: "3w2g1o2p:b24g5olgW"
def runlen(s):
    ful=''
    c=1
    k=list(s)
    for i in range(len(s)-1):
        if k[i]==k[i+1]:
            c+=1
        else:
            ful +=  str(c)+k[i]
            c =1
    ful += str(c)+ k[-1]        
    return f'{ful}:b24g5olgW'
        
print(runlen('wwwggopp'))
#3w2g1o2p:b24g5olgW

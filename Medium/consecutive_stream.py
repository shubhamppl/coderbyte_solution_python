'''determine if there is a consecutive stream of digits of at least N length where N is the actual digit value. If so, 
return the string true, otherwise return the string false. For example: if at is 6539923335
" then your program should return the string true because there is a consecutive stream of 3's of length 3. 
The input string will always contain at least one digit

Examples

Input: "5556293383563665"

Output: false'''
def consecutive(s):
    s=list(s)
    c=1
    for i in range(len(s)-1):
        if s[i] ==s[i+1]:
            c += 1
            if int(s[i])==c:
                return True
        
    c=1

    return False
print(consecutive('6539923352333'))
print(consecutive('5556293383563665555'))

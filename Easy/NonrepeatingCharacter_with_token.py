'''def NonrepeatingCharacter(s):
# Step 1: Convert each character to its ASCII value and increment it by 1
# Step 2: Reverse the string
# Step 4: Remove spaces and special characters from the final output
# Step 3: Combine the reversed string with the ChallengeToken
challenge_token = "c06tpnosw'''
'''
tfnjU Ovg:c06tpnOsw
3 pmmfI:c06tpnOsw
capatelize 
  # Step 1: Convert each character to its ASCII value and increment it by 1
# Step 2: Reverse the string
# Step 4: Remove spaces and special characters from the final output
   # Step 3: Combine the reversed string with the ChallengeToken#
    #tfnjU Ovg:c06tpnOsw
#3 pmmfI:c06tpnosw
#    challenge_token = "c06tpnosw"
#caatalise aeiou
#correct code
#red'''

def NonrepeatingCharacter(s):
    token = "c06tpnosw"
    k=list(s)
    ful=''
    g='aeiou'
    p='!@#$%^&*()_+=-[]{;:.>,</?}'
    for i in k:
        if i.isspace():
            ful += ' '
        elif i.isalpha():
            if i.islower():
                ful+= chr((ord(i)-ord('a')+1)%26+ord('a'))
            elif i.isupper():
                ful+= chr((ord(i)-ord('A')+1)%26+ord('A'))
        else:
            ful+= i 
    a=[x if x not in p else' ' for x in ful]
    a=a[::-1]
    if a[0].isspace():
        a.pop(0)
    a=[x.upper() if x in g else x for x in a]
    a=''.join(a)
    return f'{a}:{token}'
print(NonrepeatingCharacter("fun times!"))  # tfnjU Ovg:c06tpnosw
print(NonrepeatingCharacter("hello*3"))     #3 pmmfI:c06tpnosw

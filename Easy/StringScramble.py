#  Using the Python language, have the function StringScramble(str1,str2) take both parameters being passed and return
# the string true if a portion of str1 characters can be rearranged to match str2, otherwise return the string false.
# For example: if str1 is "rkqodlw" and str2 is "world" the output should return true. Punctuation and symbols will
# not be entered with the parameters.
def StringScramble(str1,str2):
    k=list(str1)
    c=str2
    a=[x for x in c if x not in k]
    if len(a)==0:
        return 'true'
    return 'fasle'
        
test_cases = [
    ('rkqodlw', 'world'),  # True, can be rearranged to form 'world'
    ('hello', 'billion'),  # False, 'hello' doesn't contain 'b', 'i', 'n'
    ('supercalifragilisticexpialidocious', 'pseudoclassical'),  # True
    ('abcde', 'edcba'),  # True, same characters different order
    ('123456789', '987654321'),  # True, same digits different order
]

# Check each test case
results = [StringScramble(tc[0], tc[1]) for tc in test_cases]
results


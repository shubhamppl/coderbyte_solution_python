'''Questions Marks
Have the function QuestionsMarks(str) take the str string parameter, which will  single digit numbers, letters, 
and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If
so, then your program should return the string true, otherwise it should return the string false. If there 
aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true becacontainuse there are exactly 3
question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.
Examples
Input: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true
complete the code:'''
def QuestionsMarks(s):
        s=list(s)
        par=False
      
        for i in range(len(s)):
            if s[i].isdigit():
                num1=s[i]
                for j in range(i+1,len(s)):
                    if s[j].isdigit():
                        num2=s[j]
                        r=int(num1)+int(num2)
                        if r==10:
                            par =True 
                            if s[i+1:j].count('?') !=3:
                                return False
        if par:
            return True
        else:
            return False

            
print(QuestionsMarks("arrb6???4xxbl5???eee5"))  # Expected output: true
print(QuestionsMarks("aa6?9"))                  # Expected output: false
print(QuestionsMarks("acc?7??sss?3rr1??????5")) # Expected output: true

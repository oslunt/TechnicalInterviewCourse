# Write a function that checks if a string is a palindrome using recursion

def checkPalindrom(string):
    return string == reverse(string)

def reverse(string):
    if string == "":
        return ""
    else:
        return (reverse(string[1:]) + string[0])


def recursivePalindrome(string):
    if len(string) == 1 or len(string) == 0:
        return True
    if string[0] == string[len(string) - 1]:
        return recursivePalindrome(string[1:-1])
    return False
        

print(checkPalindrom("racecar"))
print(recursivePalindrome("racecar"))
# Given an integer n, return True if it is a power of 2. 
# An integer n is a power of two, if there exists an integer x such that n == 2^x

# Examples:

# Input: n = 4
# Output: True
# 2^2 = 4

# Input : n = 16
# Output : True
# 2^4 = 16

# Input : n = 13
# Output : False

def isPowerOfTwo(n):
    if(n == 2):
        return True
    else:
        if(n % 2 == 0):
            return isPowerOfTwo(n / 2)
        else:
            return False

n = 4096
print(isPowerOfTwo(n))
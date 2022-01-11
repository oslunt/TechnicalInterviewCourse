# Write a program that creates a portion of the fibonacci sequence iteratively

def fibseq(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return fibseq(n-1) + fibseq(n-2)

print(fibseq(7))

# O(branches^depth)
# so fibonacci sequence is O(2^n)
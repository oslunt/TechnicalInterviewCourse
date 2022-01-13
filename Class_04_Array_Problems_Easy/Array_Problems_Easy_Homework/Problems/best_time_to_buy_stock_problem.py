# Say you have an array for which the ith element is the price of a given stock on day i
# If you were only permitted to complete at most one transaction (i.e, buy one and 
# sell one share of the stock) design an algorithm to find the maximum profit
# This problem came from leetcode.com

# brute force

def bruteForce(lst):
    max = 0
    cur = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            cur = lst[j] - lst[i]
            if cur > max:
                max = cur
    return max

def optimized(lst):
    max = 0
    min = lst[0]
    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]
        else:
            if (lst[i] - min) > max:
                max = lst[i] - min
    return max


input_array = [7, 1, 5, 3, 6, 4]
print(bruteForce(input_array))
print(optimized(input_array))
# Output = 5
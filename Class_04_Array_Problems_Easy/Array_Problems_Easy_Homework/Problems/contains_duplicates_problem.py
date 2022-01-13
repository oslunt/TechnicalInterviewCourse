# Given an array of integers, find if the array contains any duplicates
# Your function should return false if every element is distinct.
# This problem came from leetcode.com

def bruteForce(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                if lst[i] == lst[j]:
                    return True
    return False

def optimized(lst):
    no_dupes = set()
    for i in range(len(lst)):
        no_dupes.add(lst[i])  
    return len(lst) != len(no_dupes)

input_array = [1, 2, 3, 3, 4]
print(bruteForce(input_array))
print(optimized(input_array))
# Output = True
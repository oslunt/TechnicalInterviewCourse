# Given an array nums of n integers where n > 1, return an array output such that output[i]
# is equal to the product of all the elements of nums except nums[i]
# Note: Please solve it without division
# This problem came from leetcode.com

from audioop import mul


def bruteMult(input_array):
    prod = 1
    lst = []
    for i in range(len(input_array)):
        for j in range(len(input_array)):
            if i != j:
                prod = input_array[j] * prod
        lst.append(prod)
        prod = 1
    
    return lst

def optMulti(input_array):
    prod = 1
    for i in range(len(input_array)):
        prod = prod * input_array[i]
    lst = []
    for i in range(len(input_array)):
        lst.append(prod // input_array[i])
    
    return lst

input_array = [1, 2, 3, 4]
print(bruteMult(input_array))
print(optMulti(input_array))

# Output = [24, 12, 8, 6]
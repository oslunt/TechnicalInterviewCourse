# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand. You may assume no duplicate exists in the array.
# This problem came from leetcode.com

def findMin(input_array):
    left = 0
    right = len(input_array) - 1
    while left <= right:
        half = (right + left)//2
        if input_array[half] < input_array[left] and input_array[half] < input_array[right]:
            return input_array[half]
        elif input_array[half] < input_array[left]:
            right = half - 1
        else:
            left = half + 1
    if input_array[len(input_array) - 1] < input_array[0]:
        return input_array[len(input_array) - 1]
    else:
        return input_array[0]

input_array = [5, 6, 1, 2, 3, 4,]
print(findMin(input_array))
# Output = 1
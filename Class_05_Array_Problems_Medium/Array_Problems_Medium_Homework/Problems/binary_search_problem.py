# Search an array of numbers to find a target number using binary search.
# The function should return the index of the target number if the target number is found
# or a -1 if the target is not found in the array.

def binSearch(input_array, input_target):
    lower = 0
    upper = len(input_array) - 1

    while lower <= upper:
        half = int((lower + upper)/2)
        if input_array[half] == input_target:
            return half
        elif input_array[half] > input_target:
            upper = half - 1
        else:
            lower = half + 1
    
    return -1

input_array = [1, 2, 5, 9, 11, 12, 15, 21, 28, 99, 100, 117]
input_target = 117

print(binSearch(input_array, input_target))
# Output = 2
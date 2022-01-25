#Given an integer array, give the maximum product of a triplet in an array.
#
#Examples:
#Input = [10, 3, 5, 6, 20]
#Output = 1200 (product of 10, 6, and 20)
#
#Input:  [-10, -3, -5, -6, -20]
#Output: -90
#
#Input:  [1, -4, 3, -6, 7, 0]
#Output: 168

def maxProd(input_array):
    input_array = merge(input_array)
    i = len(input_array) - 1
    j = 0
    prod = 1
    while j < 3:
        prod = prod * input_array[i]
        i -= 1
        j += 1
    prod2 = input_array[0] * input_array[1] * input_array[len(input_array) - 1]
    if prod < prod2:
        return prod2
    else:
        return prod


def merge(input_array):
    if len(input_array) > 1:
        half = len(input_array) // 2
        left = input_array[:half]
        right = input_array[half:]

        merge(left)
        merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                input_array[k] = left[i]
                i += 1
            else:
                input_array[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            input_array[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            input_array[k] = right[j]
            j += 1
            k += 1
    return input_array

factors1 = [10, 3, 5, 6, 20] # 1200
factors2 = [-10, -3, -5, -6, -20] # -90
factors3 = [1, -4, 3, -6, 7, 0] # 168

print(maxProd(factors1))
print(maxProd(factors2))
print(maxProd(factors3))
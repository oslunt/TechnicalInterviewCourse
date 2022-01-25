# Given an array nums of size n, return the majority element. 
# The majority element is an element that appears more than [n/2] times. 
# You may assume that the majority element always exists in the array.
#
# Input = [3, 2, 3]
# Output = 3
#
# Input = [2, 2, 1, 1, 1, 2, 2]
# Output = 2

def majElement(input_array):
    dct = {}
    for i in range(len(input_array)):
        if input_array[i] in dct:
            dct[input_array[i]] += 1
        else:
            dct[input_array[i]] = 1
    
    index = 0
    max = 0
    for k in dct.items():
        if k[1] > max:
            index = k[0]
            max = k[1]
    return index

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

arr1 = [3, 2, 3] # 3
arr2 = [2, 2, 1, 1, 1, 2, 2] # 2

print(majElement(arr1))
print(majElement(arr2))

print(merge(arr1)[len(arr1) // 2])
print(merge(arr2)[len(arr2) // 2])

#Given a dictionary, sort the keys by the sum of their values in descending order. Return an array with the sorted pairs.
#
#Example:
#old_dict = { 'A' : [1, 2, 3], 'B' : [1, 7, 3], 'C' : [100, 3, 7], 'D' : [6, 50, 4]}
#output = [['C', 110], ['D', 60], ['B', 11], ['A', 6]]

def reverseVals(dct):
    retval = []

    for key, val in dct.items():
        temp = []
        total = 0
        for i in range(len(val)):
            total += val[i]
        temp.append(key)
        temp.append(total)
        retval.append(temp)
    
    sorted = []
    sorted.append(retval[0])
    for i in range(1, len(retval)):
        for j in range(len(sorted)):
            if retval[i][1] > sorted[j][1]:
                sorted.insert(j, retval[i])
                break
    return sorted

    #total = {}

    #for key, val in dct.items():
    #    tempTotal = 0
    #    for i in range(len(val)):
    #        tempTotal += val[i]
    #    total[key] = tempTotal
    
    #retval = sorted(total.items(), key=lambda x: x[1], reverse= True)
    #return retval


dict = { 'A' : [1, 2, 3], 'B' : [1, 7, 3], 'C' : [100, 3, 7], 'D' : [6, 50, 4]}

print(reverseVals(dict))
print()

# Write a function that calculates the sum of an array of numbers using recursion. You must use recursion to gain full credit for this question.
#
# Example:
# input = [3,6,2,9,9,4]
# output = 33

def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        half = len(arr) // 2
        left = arr[:half]
        right = arr[half:]
        return sum(left) + sum(right)

input = [3,6,2,9,9,4]
print(sum(input))
print()


# Given a n x m binary matrix image, flip the image horizontally, then invert it, then return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0, 1, 1] results in [1, 0, 0].
# Examples:
#
# Input =  [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
# Output = [[1, 0, 0,], [0, 1, 0], [1, 1, 1]]
# Explanation:
# First reverse each row: [[0, 1, 1], [1, 0, 1], [0, 0, 0]]
# Then invert the image: [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

def flipInvert(arr):
    for i in range(len(arr)):
        arr[i].reverse()
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                arr[i][j] = 0
            else:
                arr[i][j] = 1
    return arr

def recurFlipInvert(arr):
    if isinstance(arr[0], int):
        arr.reverse()
        for i in range(len(arr)):
            if arr[i] == 1:
                arr[i] = 0
            else :
                arr[i] = 1
        return arr
    else:
        for i in range(len(arr)):
            recurFlipInvert(arr[i])
        return arr

Input =  [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(flipInvert(Input))
Input =  [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(recurFlipInvert(Input))
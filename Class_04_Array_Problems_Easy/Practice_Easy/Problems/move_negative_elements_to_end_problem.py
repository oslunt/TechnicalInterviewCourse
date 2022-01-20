# Write a function that moves all negative elements to the end of an array

def negativeEnd(input_array):
    positive = []
    negative = []
    for i in range(len(input_array)):
        if input_array[i] < 0:
            negative.append(input_array[i])
        else:
            positive.append(input_array[i])
    
    return positive + negative

def betterNegEnd(input_array):
    #for i in range(len(input_array)):
    right = len(input_array) - 1
    left = 0
    while left < len(input_array) and left < right:
        if input_array[left] < 0:
            temp = input_array[left]
            input_array[left] = input_array[right]
            input_array[right] = temp
            right = right - 1
        left = left + 1
    
    return input_array

input_array = [-1, 2, -3, 4, 5, 7]
print(negativeEnd(input_array))
print(betterNegEnd(input_array))
# Output = [2, 4, 5, 7, -3, -1]
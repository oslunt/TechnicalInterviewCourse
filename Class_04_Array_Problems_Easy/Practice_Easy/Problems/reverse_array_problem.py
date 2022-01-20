# Write a function that reverses an array

def reverse(input_array):
    lst = []
    for i in range(len(input_array) -1, -1, -1):
        lst.append(input_array[i])
    
    return lst

def better_reverse(input_array):
    for i in range(0, int(len(input_array)/2)):
        temp = input_array[i]
        input_array[i] = input_array[len(input_array) -1 -i]
        input_array[len(input_array) -1 -i] = temp
    
    return input_array

input_array = [1, 2, 3, 4, 5, 6, 7, "a"]
print(reverse(input_array))
print(better_reverse(input_array))

# Output = ["a", 7, 6, 5, 4, 3, 2, 1]
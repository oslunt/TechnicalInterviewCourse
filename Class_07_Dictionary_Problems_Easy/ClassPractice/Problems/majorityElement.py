# Given an array nums of size n, return the majority element. 
# The majority element is an element that appears more than [n/2] times. 
# You may assume that the majority element always exists in the array.
#
# Input = [3, 2, 3]
# Output = 3
#
# Input = [2, 2, 1, 1, 1, 2, 2]
# Output = 2

def majCount(input_array):
    retval = {}
    for i in range(len(input_array)):
        if input_array[i] in retval:
            retval[input_array[i]] += 1
        else:
            retval[input_array[i]] = 1
    
    max = retval[input_array[0]]
    maj = list(retval.keys())[0]

    for k,v in retval.items():
        if v > max:
            maj = k
            max = v
    
    return maj

arr1 = [3, 2, 3] # 3
arr2 = [2, 2, 1, 1, 1, 2, 2] # 2

print(majCount(arr1))
print(majCount(arr2))
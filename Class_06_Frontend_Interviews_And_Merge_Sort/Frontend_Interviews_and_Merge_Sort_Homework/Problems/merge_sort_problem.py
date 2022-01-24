# Write a merge sort algorithm to sort an array. 
# The function should return the sorted array.

def mergeSort(arr):
    if len(arr) > 1:
        half = len(arr) // 2
        left = arr[:half]
        right = arr[half:]
        
        mergeSort(left)
        mergeSort(right)
        
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1   

# two examples
array1 = [45, 98, 3, 24, 15, 77, 9, 50] # output: [3, 9, 15, 24, 45, 50, 77, 98]
array2 = [18, 16, 27, 4, 12] # output: [4, 12, 16, 18, 27]

mergeSort(array1)
print(array1)

mergeSort(array2)
print(array2)

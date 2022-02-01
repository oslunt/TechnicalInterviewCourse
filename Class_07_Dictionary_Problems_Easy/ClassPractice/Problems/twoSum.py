# Given an array nums and an integer target, return the indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1] (because nums[0] + nums[1]  == 9)
#
# Input: nums = [3,2,4], target = 6
# Output: [1, 2] 
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

def twoSum(input_array, target):
    dct = {}
    for i, v in enumerate(input_array):
        diff = target - v

        if diff in dct:
            return [dct[diff], i]
        
        dct[v] = i

nums1 = [2, 7, 11, 15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3, 3]
target3 = 6

print(twoSum(nums1,target1))
print(twoSum(nums2,target2))
print(twoSum(nums3,target3))
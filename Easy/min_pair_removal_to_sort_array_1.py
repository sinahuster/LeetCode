"""
Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

Constraints:
1 <= nums.length <= 50
-1000 <= nums[i] <= 1000
"""

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        in_order = False
        operations = 0 

        while not in_order:
            in_order = True 
            length = len(nums)
            min_sum = float('inf')
            index = 0
            for i in range(1, length): 
                curr_sum = nums[i - 1] + nums[i]
                if curr_sum < min_sum:
                    min_sum = curr_sum 
                    index = i
                if nums[i] < nums[i - 1]:
                    in_order = False
            if not in_order:
                nums[index - 1]  = min_sum
                nums = nums[:index] + nums[index + 1:]  
                operations += 1  
            print(nums)      

        return operations


# This has time complexity O(n^2) and space complexity O(1)
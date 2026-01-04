"""
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. 
If there is no such integer in the array, return 0.

Constraints:
1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5
"""

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        divisors = {}
        divisor = 1
        
        for i in range(len(nums)):
            divisors[i] = []

        maximum = sqrt(max(nums))

        while divisor <= maximum:
            delete = []
            for index in divisors:
                if nums[index] % divisor == 0:
                    if divisor not in divisors[index]:
                        divisors[index].append(divisor)
                    second = int(nums[index] / divisor)
                    if second not in divisors[index]:
                        divisors[index].append(second)
                    if len(divisors[index]) > 4:
                        delete.append(index)
            for index in delete:
                del(divisors[index])
            divisor += 1
        
        total = 0
        print(divisors)

        for index in divisors:
            if len(divisors[index]) == 4:
                total += sum(divisors[index])
        
        return total
        

# This has time complexity O(n * m), where n is the length of nums and m is the sqrt(max(nums))
# This has time complexity O(n)
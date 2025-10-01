/*
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
*/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize) {
    int *sum = malloc(sizeof(int) * numsSize);

    *returnSize = numsSize;

    sum[0] = nums[0];

    for (int i = 1; i < numsSize; i++)
    {
        sum[i] = sum[i - 1] + nums[i];
    }

    return sum;
}
/*
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
*/



/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortedSquares(int* nums, int numsSize, int* returnSize) {

   int *result = malloc(sizeof(int) * numsSize);
   *returnSize = numsSize;
   int left = 0;
   int right = numsSize - 1;
   int position = numsSize - 1;

    while (left <= right)
    {
        int leftVal = nums[left] * nums[left];
        int rightVal = nums[right] * nums[right];
        if (leftVal > rightVal)
        {
            result[position] = leftVal;
            left++;
        }
        else 
        {
            result[position] = rightVal;
            right--;
        }

        position--;
    }

    return result;
}
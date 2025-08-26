/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
*/

#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize);

int main(void)
{
    int nums[] = {1, 2, 3, 4, 8};
    int numsSize = sizeof(nums)/sizeof(nums[0]);

    int resultSize;
    int *result = twoSum(nums, numsSize, 7, &resultSize);

    printf("Result: %d %d - %d\n", result[0], result[1], resultSize);

    free(result);

    return 0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) 
{
  int* result = (int*)malloc(2 * sizeof(int));
    for (int i = 0; i < numsSize; i++)
    {
      for (int j = i + 1; j < numsSize; j++)
      {
        if (nums[i] + nums[j] == target)
        {
          result[0] = i;
          result[1] = j;
          *returnSize = 2;
        }
      }
    }
    return result;
}

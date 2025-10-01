/*
You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.

Constraints:
2 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
*/

#include <stdio.h>

int waysToSplitArray(int* nums, int numsSize);

typedef struct 
{
    int *nums;
    int numsSize;
    int expected;
}Test;

int main(void)
{
    int arr1[] = {10,4,-8,7};
    int arr2[] = {2,3,1,0};
    int arr3[] = {-2,-1};
    int arr4[] = {2,3,4};

    Test tests[] = 
    {
        {arr1, 4, 2},
        {arr2, 4, 2},
        {arr3, 2, 0},
        {arr4, 3, 1},
    };

    int testSize = sizeof(tests) / sizeof(tests[0]);

    for (int i = 0; i < testSize; i++)
    { 
        int result = waysToSplitArray(tests[i].nums, tests[i].numsSize);
        printf("The number of ways to split the array is %d", result);
        if (result == tests[i].expected)
        {
            printf(" as expected.");
        }
        printf("\n");
    }

}



int waysToSplitArray(int* nums, int numsSize) {
    
    long long prefix[numsSize];
    prefix[0] = nums[0];
    int split = 0;

    for (int i = 1; i < numsSize; i++)
    {
        prefix[i] = (long long)nums[i] + prefix[i-1];
    }

    for (int i = 0; i < numsSize - 1; i++)
    {
        long long right  = prefix[numsSize - 1] - prefix[i];
        if (prefix[i] >= right)
        {
            split++;
        }
    }
    return split;
}
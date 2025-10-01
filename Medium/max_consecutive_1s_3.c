/*
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length
*/

#include <stdio.h>

int longestOnes(int* nums, int numsSize, int k);

typedef struct 
{
    int *nums;
    int numsSize;
    int k;
    int expected;
} Test;

int main(void)
{
    int arr1[] = {1,1,1,0,0,0,1,1,1,1,0};
    int arr2[] = {0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1};

    Test tests[] = {
        {arr1, 11, 2, 6},
        {arr2, 19, 3, 10}
    };

    int testSize = sizeof(tests) / sizeof(tests[0]);

    for (int i = 0; i < testSize; i++)
    {
        int result = longestOnes(tests[i].nums, tests[i].numsSize, tests[i].k);
        printf("The longest subarray with %d 0s is %d ", tests[i].k, result);
        if (result == tests[i].expected)
        {
            printf("as expected.\n");
        }
    }
}

int longestOnes(int* nums, int numsSize, int k) 
{
    int length = 0;
    int left = 0;
    int right = 0;
    int zeros = 0;

    while (right < numsSize)
    {
        if (nums[right] == 0)
        {
            zeros++;
        }
        if (zeros > k)
        {
            while (nums[left] == 1)
            {
                left++;
            }
            left++;
            zeros--;
        }   

        if (length < (right - left + 1))
        {
            length = right - left + 1;
        }

        right++;   
    }

    return length;
}
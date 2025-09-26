/*
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Constraints:
1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
*/

#include <stdio.h>

int numSubarrayProductLessThanK(int* nums, int numsSize, int k);

typedef struct 
{
    int *nums;
    int numsSize;
    int k;
    int expected;
}Test;

int main(void)
{

    int arr1[] = {10, 5, 2, 6};
    int arr2[] = {1, 2, 3};

    Test tests[] = {
        {arr1, 4, 100, 8},
        {arr2, 3, 0, 0},
    };

    int testSize = sizeof(tests) / sizeof(tests[0]);

    for (int i = 0; i < testSize; i++)
    {
        int result = numSubarrayProductLessThanK(tests[i].nums, tests[i].numsSize, tests[i].k);

        printf("The number of valid sub-arrays where the product is less than %i is %i ", tests[i].k, result);

        if (result == tests[i].expected)
        {
            printf("as expected");
        }

        printf("\n");
    }    

}

int numSubarrayProductLessThanK(int* nums, int numsSize, int k) {

    int left = 0;
    int product = 1;
    int valid = 0;
    
    for (int right = 0; right < numsSize; right++)
    {
        product *= nums[right];
        while (product >= k && left <= right)
        {
            product /= nums[left];
            left++;
        }
        valid += right - left + 1;
    }

    return valid;
}
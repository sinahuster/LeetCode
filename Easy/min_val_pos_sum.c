/*
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

Constraints:
1 <= nums.length <= 100
-100 <= nums[i] <= 100
*/

#include <stdio.h>
#include <stdbool.h>

int minStartValue(int* nums, int numsSize);

typedef struct 
{
    int *nums;
    int numsSize;
    int expected;
} Test;

int main(void)
{
    int arr1[] = {-3,2,-3,4,2};
    int arr2[] = {1,2};
    int arr3[] = {1,-2,-3};

    Test tests[] = 
    {
        {arr1, 5, 5},
        {arr2, 2, 1},
        {arr3, 3, 5},
    };

    int testsSize = sizeof(tests) / sizeof(tests[0]);

    for (int i = 0; i < testsSize; i++)
    {
        int result = minStartValue(tests[i].nums, tests[i].numsSize);
        printf("The minimum start value needed is %d ", result);
        if (result == tests[i].expected)
        {
            printf("as expected.");
        }
        printf("\n");
    }
}

int minStartValue(int* nums, int numsSize) 
{

    bool pos = false;
    int start = 1;

    while (!pos)
    {
        int sum = start;
        pos = true;
        for (int i = 0; i < numsSize; i++)
        {
            sum += nums[i];
            if (sum <= 0)
            {
                start++;
                pos = false;
                break;
            }
        }
    }

    return start;
}
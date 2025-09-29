/*
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.

Constraints:
n == nums.length
1 <= k <= n <= 10^5
-10^4 <= nums[i] <= 10^4
*/

#include <stdio.h>

typedef struct
{
    int *nums;
    int numsSize;
    int k;
    double expected;
} Test;

double findMaxAverage(int* nums, int numsSize, int k);

int main(void)
{
    int arr1[] = {1,12,-5,-6,50,3};
    int arr2[] = {5};

    Test tests[] = 
    {
        {arr1, 6, 4, 12.75000},
        {arr2, 1, 1, 5.00000},
    }; 

    int testSize = sizeof(tests) / sizeof(tests[0]);

    for (int i = 0; i < testSize; i++)
    {
        double result = findMaxAverage(tests[i].nums, tests[i].numsSize, tests[i].k);
        printf("The max average sub-array is %f ", result);
        if (result == tests[i].expected)
        {
            printf("as expected.");
        }
        printf("\n");
    }
}


double findMaxAverage(int* nums, int numsSize, int k) {

    double current =  0;

    for (int i = 0; i < k; i++)
    {
        current += nums[i];
    }

    double answer = current;

    for (int i = k; i < numsSize; i++)
    {
        current = current + (nums[i] - nums[i - k]);
        if (answer < current)
        {
            answer = current;
        }
    }
    
    answer /= k;

    return answer;
}
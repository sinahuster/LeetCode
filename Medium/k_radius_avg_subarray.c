/*
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.

Constraints:
n == nums.length
1 <= n <= 10^5
0 <= nums[i], k <= 10^5
*/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getAverages(int* nums, int numsSize, int k, int* returnSize) {
    
    int *result = malloc(sizeof(int) * numsSize);
    *returnSize = numsSize;
    int window = 2 * k + 1;

    long long *sum = malloc(sizeof(long long) * ( numsSize + 1));

    sum[0] = 0;

    for (int i = 0; i < numsSize; i++)
    {
        sum[i+ 1] = sum[i] + nums[i];
    }

    if (k == 0)
    {
        for (int i = 0; i < numsSize; i++)
        {
            result[i] = nums[i];
        }
    }
    else if (k > numsSize)
    {
        for (int i = 0; i < numsSize; i++)
        {
            result[i] = -1;
        }
    }
    else
    {

        for (int i = 0; i < numsSize; i++)
        {
            if (i <= k - 1)
            {
                result[i] = -1;
            }
            else if (i >= numsSize - k)
            {
                result[i] = -1;
            }
            else
            {
               long long avg = sum[i + k + 1] - sum[i - k];
                avg /= window;
                result[i] = avg;
            }
        }
    }
    free(sum);
    return result;
}
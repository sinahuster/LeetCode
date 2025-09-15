/*
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
*/

#include <stdio.h>

int searchInsert(int* nums, int numsSize, int target) {
    
    int start = 0;
    int end = numsSize - 1;

    while (start <= end)
    {
        int middle = start + (end - start) / 2;

        if (nums[middle] == target)
        {
            return middle;
        }
        else if (nums[middle] < target)
        {
            start = middle + 1;
        }
        else 
        {
            end = middle - 1;
        }   
    }
    return start;
}
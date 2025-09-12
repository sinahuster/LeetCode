/*
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.

 - Return k.
*/

#include <stdio.h>

int removeDuplicates(int* nums, int numsSize);

int main(void)
{
    int array1[] = {1,1,2};
    int Size1 = 3;
    int array2[] = {0,0,1,1,1,2,2,3,3,4};
    int Size2 = 10;

    printf("The number of non-duplicates in ");

    for (int i = 0; i < Size1; i++)
    {
        printf("%i", array1[i]);
    }

    printf(" is %i\n", removeDuplicates(array1, Size1));


    printf("The number of non-duplicates in ");

    for (int i = 0; i < Size2; i++)
    {
        printf("%i", array2[i]);
    }

    printf(" is %i\n", removeDuplicates(array2, Size2));
    
}

int removeDuplicates(int* nums, int numsSize) {

    int stored = 0; 

    for (int i = 1; i < numsSize; i++)
    {

        if (nums[stored] != nums[i])
        {
            stored++;
            nums[stored] = nums[i];
        }
    }
    return stored + 1;
}
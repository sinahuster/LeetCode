/* 
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
*/


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize) {

    int n = 0;
    int *new = (int *)malloc(sizeof(int) * digitsSize);

    for (int i = digitsSize - 1; i >= 0 && digits[i] == 9; i--)
    {
        n++;
    }
    if (n == digitsSize)
    {
        new = (int *)realloc(new, (digitsSize + 1) * sizeof(int));
        new[0] = 1;
        for (int i = 1; i < digitsSize + 1; i++)
        {
            new[i] = 0;
        }
        *returnSize = digitsSize + 1;
    }
    else 
    {
        for (int i = 0; i < digitsSize; i++)
        {
            new[i] = digits[i];
        }

        if (n != 0)
        {
            for (int i = digitsSize - n; i < digitsSize; i++)
            {
                new[i] = 0;
            }
        }
        
        new[digitsSize - n - 1]++;

        *returnSize = digitsSize;
    }
    
    return new;
}
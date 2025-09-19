/*
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

0 <= x <= 2^31 - 1
*/

#include <stdio.h>

int mySqrt(int x);

typedef struct 
{
    int x;
    int expected;
} test;

int main(void)
{
    test tests[] = 
    {
        {4, 2},
        {8, 2},
        {1, 1},
        {1024, 32},
    };

    int size = sizeof(tests) / sizeof(tests[0]);

    for (int i = 0; i < size; i++)
    {
        int result = mySqrt(tests[i].x);
        printf("The sqrt of %i is %i", tests[i].x, result);
        if (result == tests[i].expected)
        {
            printf(" as expected.");
        }
        printf("\n");
    }
}


int mySqrt(int x) {

    int start = 0;
    int end = x;

    while (start <= end)
    {
        long middle = start + (end - start) / 2;

        if (middle * middle == x)
        {
            return middle;
        }
        else if (middle * middle < x)
        {
            if ((middle + 1) * (middle + 1) > x)
            {
                return middle;
            }
            start = middle + 1;
        }
        else 
        {
            end = middle - 1;
        }   
    }
    return start;
}

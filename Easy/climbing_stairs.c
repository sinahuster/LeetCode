/*
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

1 <= n <= 45
*/

#include <stdio.h>

int climbStairs(int n);

typedef struct 
{
    int n;
    int expected;
} test;

int main(void)
{
    test tests[] =
    {
        {2, 2},
        {3, 3},
        {40, 165580141},
        {45, 1836311903},
    };

    int size = sizeof(tests) / sizeof(tests[0]);

    for (int i = 0; i < size; i++)
    {
        int result = climbStairs(tests[i].n);
        printf("The number of ways to climb %i steps is %i", tests[i].n, result);
        if (tests[i].expected == result)
        {
            printf(" as expected.");
        }
        printf("\n");
    }
    
    return 0;
}

int climbStairs(int n) {
    
    int i = 0;
    long firstNum = 0;
    long secondNum = 1;
    long sum;

    while(i < n)
    {
        sum = firstNum + secondNum;
        firstNum = secondNum;
        secondNum = sum;
        i++;
    }

    return(sum);
}

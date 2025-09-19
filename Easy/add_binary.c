/*
Given two binary strings a and b, return their sum as a binary string.

1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char* addBinary(char* a, char* b);

typedef struct 
{
    char *a;
    char *b;
    char *expected;
}test;


int main(void)
{
    test tests[] = 
    {
        { "11", "1", "100"},
        { "1010", "1011", "10101"},
        { "100", "1", "101"},
    };
    
    int size = sizeof(tests) / sizeof(tests[0]);

    for (int i = 0; i < size; i++)
    {
        char *result = addBinary(tests[i].a, tests[i].b);
        printf("%s + %s = %s", tests[i].a, tests[i].b, result);
        if (strcmp(result, tests[i].expected) == 0)
        {
            printf(" as expected");
        }
        printf("\n");
    }

}


char *addBinary(char* a, char* b)
{
    int sizeA = strlen(a);
    int sizeB = strlen(b);
    int sizeMax = sizeA < sizeB ? sizeB : sizeA;

    char *result = malloc(sizeof(char) * (sizeMax + 2));
    result[sizeMax + 1] = '\0';

    int a_i = sizeA - 1;
    int b_i = sizeB - 1;
    int res_i = sizeMax;

    int carry = 0;

    while (a_i >= 0 || b_i >= 0)
    {
        int a_val, b_val;

        if (a_i < 0)
        {
            a_val = 0;
        }
        else
        {
            a_val = (a[a_i] - '0');
        }
        if (b_i < 0)
        {
            b_val = 0;
        }
        else 
        {
            b_val = (b[b_i] - '0');
        }
        int value = a_val + b_val + carry;

        result[res_i] = (value % 2) + 48;
        carry = value / 2;

        a_i--;
        b_i--;
        res_i--;
    }

    if (carry == 1)
    {
        result[res_i] = '1';
        return result;
    }
    
    return result + 1;

}
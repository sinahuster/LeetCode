/*
Given an integer x, return true if x is a palindrome, and false otherwise.
*/

#include <stdio.h>
#include <stdbool.h>

bool isPalindrome(int x);

typedef struct {
    int num;
    bool expected;
} tests; 

int main(void)
{   
    tests test[] = {
        {1, true},          // Single digit 
        {121, true},        // Palindrome
        {120, false},       // Not a palindrome 
        {12321, true},      // Palindrome 
        {-343, false},      // Negative number 
        {1234567890, false} // Large number to test overflow 
    };

    int size_test = sizeof(test) / sizeof(test[0]);

    for (int i = 0; i < size_test; i++)
    {
        bool result = isPalindrome(test[i].num);

        if (result == test[i].expected)
        {
            if(result)
            {
                printf("%i is a palindrome, as expected\n", test[i].num);
            }
            else
            {
                printf("%i is not a palindrome, as expected\n", test[i].num);
            }
        }
        else
        {
            printf("Error - the result does not match the expected value");
        }
    }

    return 0;
}

bool isPalindrome(int x) 
{
    unsigned int reverse = 0;
    int original = x;
    while(x > 0)
    {
        reverse *= 10;
        int digit = x % 10;
        reverse += digit;
        x /= 10;
    }
    if (reverse == original)
    {
        return true;
    }
    return false; 
}
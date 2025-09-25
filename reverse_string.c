/*
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
*/

#include <stdio.h>
#include <string.h>

void reverseString(char* s, int sSize);

typedef struct 
{
    char *s;
    int sSize;
    char *expected;
} Test;

int main(void)
{
    Test tests[] = {
        {(char[]){"hello"}, 5, "olleh"},
        {(char[]){"Hannah"}, 6, "hannaH"},
    };

    int test_Size = sizeof(tests) / sizeof(tests[0]);

    for (int i = 0; i < test_Size; i++)
    {
        char *original = tests[i].s;
        reverseString(tests[i].s, tests[i].sSize);
        if (strcmp(tests[i].s, tests[i].expected) == 0)
        {
            printf("The reverse of %s is %s as expected.\n", original, tests[i].s);
        }
        else 
        {
            printf("We do not have the correct reversal of %s.\n", original);
        }
    }


}

// We use two pointers to swap the characters in the string. left starts at the start and right starts at the end.
// We then swap the characters and move the pointers inwards until they reach the middle. 
void reverseString(char* s, int sSize) 
{
    int left = 0;
    int right = sSize - 1;

    while (left < right)
    {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left++;
        right--;
    }

}
/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
*/

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isValid(char* s);

typedef struct 
{
    char *input;
    bool expected;

}tests;

int main(void)
{
    tests test[] = 
    {
        {"()", true}, {"()[]{}", true}, {"(]", false}, {"([])", true}, {"([)]", false}, 
        {"(((((((((())))))))))", true}, {")", false}, {"(", false}
    };

    int test_size = sizeof(test)/sizeof(test[0]);
    for (int i = 0; i < test_size; i++)
    {
        bool result = isValid(test[i].input);
        if (result == test[i].expected)
        {
            if(result)
            {
                printf("%s is valid, as expected\n", test[i].input);
            }
            else
            {
                printf("%s is invalid, as expected\n", test[i].input);
            }
        }
        else
        {
            printf("Error - the result does not match the expected value \n");
        }
    }

    return 0;
}

bool isValid(char* s) {

        int len = strlen(s);

    // create a string to store the opened parantheses. 
    char brackets[10000] = {}; 
    int end = -1;

    // iterate through the string
    for (int i = 0; i < len; i++)
    {
        // check if the character is an open parentheses, if yes, 
        // add it to the string.
        char current = s[i];
        if (current == '(' || current == '[' || current == '{')
        {
            brackets[++end] = current;
        }
        // check if the character is a closing parentheses, if yes,
        // check that it matches to the last opened parentheses. 
        // If not, return false. 
        else
        {
            if (end == -1)
            {
                return false;
            }
            if (current == ')' && brackets[end] != '(' || 
                current == ']' && brackets[end] != '[' || 
                current == '}' && brackets[end] != '{')
            {
                return false; 
            }

            end--;
        }

    }
    return end == -1;
}
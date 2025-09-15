/*
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
*/

#include <stdio.h>

int lengthOfLastWord(char* s);

typedef struct 
{
    char *s;
    int expected;
}test;


int main(void)
{
    test tests[] = {
        {"Hello World", 5},
        {"   fly me   to   the moon  ", 4},
        {"luffy is still joyboy", 6}
    };

    int size = sizeof(tests) / sizeof(tests[0]);

    for (int i = 0; i < size; i++)
    {
        int result = lengthOfLastWord(tests[i].s);
        printf("In %s the last word has %i letters ", tests[i].s, result);
        if (result == tests[i].expected)
        {
            printf("as expected.");
        }
        printf("\n");
    }

    return 0;  
}

int lengthOfLastWord(char* s) {

    char space = ' ';
    int i = 0;
    int length = 0;
    
    while(s[i] != '\0')
    {
        if (s[i] != space)
        {
            int j = 0;
            while (s[i + j] != space && s[i + j] != '\0')
            {
                j++;
            }
            length = j;
            i += j;
        }
        else 
        {
            i++;
        }
    }

    return length;
}
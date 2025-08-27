/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* longestCommonPrefix(char** strs, int strsSize);

typedef struct 
{
    char** input;
    int inputSize;
    char* expected;
}tests;

int main(void)
{
    tests test[] = {
        {
            (char*[]){"flower","flow","flight"}, 3, "fl",
        }, 
        {
            (char*[]){"dog","racecar","car"}, 3, "",
        }
    };

    int test_size = sizeof(test)/sizeof(test[0]);
    for (int i = 0; i < test_size; i++)
    {
        char* result = longestCommonPrefix(test[i].input, test[i].inputSize);
        printf("{ ");
        for (int j = 0; j < test[i].inputSize; j++) 
        {
            printf("%s ", test[i].input[j]);
        }
        printf("} has a longest prefix '%s' ", result);
        if (strcmp(result, test[i].expected) == 0)
        {
            printf("as expected");
        }
        printf("\n");
    }
    
    return 0;
}

char* longestCommonPrefix(char** strs, int strsSize) 
{
    char* prefix = malloc(strlen(strs[0]) + 1);
    strcpy(prefix, strs[0]);

    for (int i = 0; i < strlen(prefix); i++)
    {
        char letter = strs[0][i];
        for (int j = 1; j < strsSize; j++)
        {
            if (strs[j][i] == 0 || strs[j][i] != letter)
            {
                prefix[i] = 0;
                return prefix;
            }
        }
    }

    return prefix;
}
/*
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
*/

#include <stdio.h>

int strStr(char* haystack, char* needle) {
    
    int i = 0;
    int first = -1;

    // A loop until the end of the haystack is reached
    while (haystack[i] !=  '\0')
    {
        // If the haystack is equal to the start of the needle 
        if (haystack[i] == needle[0])
        {
            int j = 0;
            // Iterate through until we reach the end of the needle, haystack or the values are no longer equal
            while(haystack[i+j] == needle[j] && needle[j] != '\0' && haystack[i+j] != '\0')
            {
                j++;
            }
            // If we reached the end of the needle, we return the value of the index at the start 
            if (needle[j] == '\0')
            {
                return i;
            }
        }
        
        i++;
    }

    return -1;
}
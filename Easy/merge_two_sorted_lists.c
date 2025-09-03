/*
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode {
   int val;
   struct ListNode *next;
};

typedef struct {
    int list1[50];
    int list1Size;
    int list2[50];
    int list2Size;
    int expected[100];
}test;

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2);

int main(void)
{

    test tests [] = {
        {{1, 2, 4}, 3, {1, 3, 4}, 3, {1, 1, 2, 3, 4, 4}}, 
        {{}, 0, {}, 0, {}}, 
        {{}, 0, {0}, 1, {0}},
    };

    int size_test = sizeof(tests) / sizeof(tests[0]);

    for (int i = 0; i < size_test; i++)
    {
       struct ListNode *one = NULL;
       struct ListNode *tail1 = NULL;
       struct ListNode *two = NULL;
       struct ListNode *tail2 = NULL;

       for (int j = 0; j < tests[i].list1Size; j++)
       {
            struct ListNode *new = malloc(sizeof(struct ListNode));
            new->val = tests[i].list1[j];

            if (one == NULL) 
            {
                one = new;
                tail1 = new;
            } 
            else 
            {
                tail1->next = new;
                tail1 = new;
            }
        }

        for (int j = 0; j < tests[i].list2Size; j++)
       {
            struct ListNode *new = malloc(sizeof(struct ListNode));
            new->val = tests[i].list2[j];

            if (two == NULL)
            {
                two = new;
                tail2 = new;
            } 
            else 
            {
                tail2->next = new;
                tail2 = new;
            }
        }

        struct ListNode *result = mergeTwoLists(one, two);
       
        int compare[50];
        int k = 0;
        while (result != NULL)
        {
            compare[k] = result->val;
            k++;
            result = result->next;
        }

        bool same = true;

        if (k != tests[i].list1Size + tests[i].list2Size)
        {
            same = false;
        }
        else 
        {
            for (int j = 0; j < k; j++)
            {
                if (compare[j] != tests[i].expected[j])
                {
                    same = false;
                }
            }

            if (same)
            {
                printf("We got the expected result\n");
            }
            else
            {
                printf("We didn't get the expected result.\n");
            }
        }

    }
    return 0;
}


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {

    struct ListNode *merged = NULL;
    struct ListNode *tail = NULL;

    int val_1, val_2;

    // deal with if either list is NULL
    if (list1 == NULL)
    {
        return list2;
    }
    if (list2 == NULL)
    {
        return list1;
    }

    while (list1 != NULL || list2 != NULL)
    {
        struct ListNode *new = malloc(sizeof(struct ListNode));

        if (list1 == NULL)
        {
            val_1 = 101;
        }
        else
        {
            val_1 = list1->val;
        }
        if (list2 == NULL)
        {
            val_2 = 101;
        }
        else
        {
            val_2 = list2->val;
        }

       if (val_1 <= val_2)
        {
            new->val = list1->val;
            new->next = NULL;
            list1 = list1->next;
        }
        else
        {
            new->val = list2->val;
            new->next = NULL;
            list2 = list2->next;
        }
        if (merged == NULL)
            {
                merged = new;
                tail = new;
            }
        else
        {
            tail->next = new;
            tail = new;

        }

    }
    return merged;
}
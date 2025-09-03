/*
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.
*/

#include <stdio.h>
#include <stdlib.h> 

struct ListNode 
{
    int val;
    struct ListNode *next;
};

struct ListNode* deleteDuplicates(struct ListNode* head);
void list_append(struct ListNode **list, int value);
void list_print(struct ListNode *list);
void list_free(struct ListNode **list);

typedef struct
{
    int input[300];
    int InputSize;
    int expected[300];
}tests;

int main(void)
{
    tests test [] = 
    {
        {{1, 1, 2}, 3, {1, 2}},
        {{1, 1, 2, 3, 3}, 5, {1, 2, 3}},
        {{1}, 1, {1}},
        {{}, 0, {}},
        {{1, 1, 1}, 3, {1}},
    };

    int testSize = sizeof(test)/sizeof(test[0]);
    for (int i = 0; i < testSize; i++)
    {
        struct ListNode *list = NULL;
        for (int j = 0; j < test[i].InputSize; j++)
        {
            list_append(&list, test[i].input[j]);
        }

        printf("The original list was ");
        list_print(list);
        struct ListNode *result = deleteDuplicates(list);
        printf("and the result is ");
        list_print(result);
        printf("\n");
        list_free(&list);

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
struct ListNode* deleteDuplicates(struct ListNode* head) {

    // empty list 
    if (head == NULL)
    {
        return head;
    }

    struct ListNode *prev = head;
    struct ListNode *current = prev->next; 
    
    // while we haven't reached the end of the list 
    while (current != NULL)
    {
        // if the value is the same, skip over the cuurent element 
        // and move the current element along.
        if (prev->val == current->val)
        {
            prev->next = current->next;
            current = current->next;
        }
        // if not the same, increment both prev and current
        else 
        {
            prev = prev->next;
            if (current == NULL)
            {
                break;
            }
            current = current->next;
        }
    }

    return head;
}

void list_append(struct ListNode **list, int value)
{
    struct ListNode *new = malloc(sizeof(struct ListNode));
    new->next = NULL;
    new->val = value;

    if (*list == NULL)
    {
        *list = new;
        return;
    }

    struct ListNode *tail = *list;

    while (tail->next != NULL)
    {
        tail = tail->next;
    }

    tail->next = new;

    return;   
}

void list_print(struct ListNode *list)
{
    while (list != NULL)
    {
        printf("%i, ", list->val);
        list = list->next;
    }

    return;
}

void list_free(struct ListNode **list)
{
    while (*list != NULL)
    {
        struct ListNode *ptr = *list;
        *list = (*list)->next;
        free(ptr);
    }
    
    return;
}
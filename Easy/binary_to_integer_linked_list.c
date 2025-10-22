/*
Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

Constraints:
The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int getDecimalValue(struct ListNode* head) {

    struct ListNode *curr = head;
    int length = 0;
    int value = 0;

    while(curr)
    {
        length++;
        curr = curr->next;
    }

    curr = head;

    int power = (int)pow(2, length - 1);

    for (int i = 0; i < length; i++)
    {
        value += power * curr->val;
        power /= 2;
        curr = curr->next;
    }

    return value;
}

// This has time complexity O(n) as we traverse the list twice in seperate loops and space complexity O(1). 
/*
Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *current = head, *next = NULL, *prev = NULL;

    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next; 
    }

    return prev;
}

// 
/*
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    
    struct ListNode *end = head, *middle = head;
    if (head != NULL)
    {
        end = end->next;
    }

    while (end && end->next)
    {
        middle = middle->next;
        end = end->next->next;
    }

    struct ListNode *prev = NULL, *next = NULL, *curr = middle;
    curr = curr->next;

    while (curr)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    middle->next = prev;
    middle = middle->next;

    struct ListNode *start = head;

    while (middle)
    {
        if (middle->val != start->val)
        {
            return false;
        }
        middle = middle->next;
        start = start->next;
    }

    return true; 
}

// This has time complexity O(n) and space complexity O(1)
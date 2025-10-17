/*
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

Constraints:
The number of nodes in the list is in the range [1, 10^5].
1 <= Node.val <= 10^5
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    
    struct ListNode *slow = head; 
    if (head->next == NULL)
    {
        return NULL;
    }
    struct ListNode *fast = head->next;

    while (fast && fast->next)
    {
        fast = fast->next->next;
        if (fast)
        {
            slow = slow->next;
        }
    }

    struct ListNode *tmp = slow->next;
    slow->next = tmp->next;

    return head;
}

// This has time complexity O(n) and space complexity O(1)
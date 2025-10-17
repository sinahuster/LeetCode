/*
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {

    struct ListNode dummy;
    dummy.next = head;

    struct ListNode *before = &dummy, *end = &dummy;

    for (int i = 0; i < n; i++)
    {
        end = end->next;
    }

    while (end->next)
    {
        before = before->next;
        end = end->next;
    }

    before->next = before->next->next;

    return dummy.next;
}

// This has time complexity O(n) and space complexity O(1)
/*
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {

    if (!head || left == right) 
    {
        return head;
    }

    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *prev = &dummy;

    // Move prev to the node before left
    for (int i = 1; i < left; i++)
    {
        prev = prev->next;
    }

    struct ListNode *curr = prev->next;
    struct ListNode *following = curr->next;

    for (int i = left; i < right; i++)
    {
        following = curr->next;
        curr->next = following->next;
        following->next = prev->next;
        prev->next = following;
    }

    return dummy.next;
}


// This has time complexity O(n), where n is the length of the linked list, and space complexity O(1)
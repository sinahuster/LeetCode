/*
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 10^5
0 <= Node.val <= 100
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapNodes(struct ListNode* head, int k) {
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *prev_second = &dummy, *prev_first = &dummy, *end = dummy.next;

    for (int i = 1; i < k; i++)
    {
        prev_first = prev_first->next;
        end = end->next;
    }

    while (end->next)
    {
        end = end->next;
        prev_second = prev_second->next;
    }

    struct ListNode *first = prev_first->next, *second = prev_second->next;

    //checking if we are at the center of the list
    if (first == second)
    {
        return dummy.next;
    }

    struct ListNode* firstNext = first->next;
    struct ListNode* secondNext = second->next;

    // adjacent nodes with first then second
    if (first->next == second)
    {
        prev_first->next = second;
        second->next = first;
        first->next = secondNext;
    }
    // adjacent nodes with second then first 
    else if (second->next == first)
    {
        prev_second->next = first;
        first->next = second;
        second->next = firstNext;
    }
    // non-adjacent nodes 
    else
    {
        prev_first->next = second;
        prev_second->next = first;
        second->next = firstNext;
        first->next = secondNext;
    }

    return dummy.next;
}

// This has time complexity O(n) and space complexity O(1)
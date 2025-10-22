/*
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Constraints:
The number of nodes in the linked list is in the range [0, 10^4].
-10^6 <= Node.val <= 10^6
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head) {
    
    if (head == NULL || head->next == NULL)
    {
        return head;
    }

    struct ListNode *odd = head, *even = head->next, *first_even = even;

    while (even && even->next)
    {
        odd->next = even->next;
        even->next = even->next->next;
        odd = odd->next;
        odd->next = first_even;
        even = even->next;
    }

    return head;
}

// This has time complexity O(n), where n is the length of the list, and space complexity O(1)
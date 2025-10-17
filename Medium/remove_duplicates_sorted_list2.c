/*
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. 
Return the linked list sorted as well.

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    
    // Empty list or one node 
    if (head == NULL || head->next == NULL)
    {
        return head;
    }

    struct ListNode dummy;
    dummy.next = head;

    struct ListNode *prev = &dummy, *curr = dummy.next;
    int value = 0;

    while (curr && curr->next)
    {
        if (curr->val == curr->next->val)
        {
            value = curr->val;
           while (curr && curr->val == value)
            {
                prev->next = curr->next;
                curr = curr->next;
            }
        }
        else
        {
            curr = curr->next;
            prev = prev->next;
        }
    }

    return dummy.next;
}

// This has time complexity O(n) and space complexity O(1)
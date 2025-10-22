/*
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Constraints:
The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    
    struct ListNode dummy;
    dummy.next = head;

    struct ListNode *curr = &dummy;

    if (head == NULL)
    {
        return head;
    }
    struct ListNode *following = curr->next;

    while(following)
    {
        if (following->val == val)
        {
            following = following->next;
            curr->next = following;
        }
        else 
        {
            curr = following;
            following = following->next;
        }
    }

    return dummy.next;
}

// This has time complexity O(n) where n is the length of the list, and space complexity O(1). 
/*
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode* fast = head;
    struct ListNode* slow = head;
    int length = 0;
    int count = 0;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
        length += 2;
        count++;
    }
    if (fast != NULL)
    {
        length++;
    }

    if (length / 2 > count)
    {
        slow = slow->next;
    }

    return slow;
}

// This has time complexity O(n), where n is the length of the list, and space complexity O(1).
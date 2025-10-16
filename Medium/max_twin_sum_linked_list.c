/*
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Constraints:
The number of nodes in the list is an even integer in the range [2, 10^5].
1 <= Node.val <= 10^5
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int pairSum(struct ListNode* head) {
    
    struct ListNode *slow = head, *fast = head;

    while (fast != NULL && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    struct ListNode *next = NULL, *prev = NULL;
    while (slow)
    {
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next; 
    }

    int max = 0;
    struct ListNode *first = head, *second = prev;

    while (second)
    {
        int sum = first->val + second->val;
        if (sum > max)
        {
            max = sum;
        }
        first = first->next;
        second = second->next;
    }

    return max;
}

/*
This has time complexity O(n) and space complexity O(1)
*/
/*
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    
    if (head == NULL || head->next == NULL)
    {
        return head;
    }

    struct ListNode *new_head = head->next; 
    struct ListNode *prev = NULL;

    while (head != NULL && head->next != NULL)
    {
        if (prev != NULL)
        {
            prev->next = head->next;
        }
        prev = head;

        struct ListNode *next_node = head->next->next;
        head->next->next = head;

        head->next = next_node;
        head = next_node;
    }

    return new_head;
}

/*
This has time complexity O(n) and space complexity O(1). 
*/
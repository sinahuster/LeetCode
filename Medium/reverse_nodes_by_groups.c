/*
You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,

The 1st node is assigned to the first group.
The 2nd and the 3rd nodes are assigned to the second group.
The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.

Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 10^5
*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *reverseSection(struct ListNode *before, int length)
{
    if (!before || !before->next || length <= 0)
    {
        return before;
    }

    struct ListNode *curr = before->next, *prev = NULL, *following = NULL, *tail = curr;

    for (int i = 0; i < length; i++)
    {
        following = curr->next;
        curr->next = prev;
        prev = curr;
        curr = following;
    }

    before->next = prev; 
    tail->next = following;

    return tail;
}

struct ListNode* reverseEvenLengthGroups(struct ListNode* head) {
    
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *start = &dummy, *end = start->next;

    int group = 1;
    int length; 

    while (start)
    {
        if (start->next == NULL)
        {
            break;
        }
        end = start->next; 

        length = 0;
        for (int i = 0; i < group; i++)
        {
            if (end == NULL)
            {
                break;
            }
            length++;
            end = end->next;
        }

        if (length % 2 == 0)
        {
            start = reverseSection(start, length);
        }
        else 
        {
            for (int i = 0; i < length; i++)
            {
                start = start->next;
            }
        }

        group++;
    }

    return head;
}

// start with group 1, incrementing group each time. 
// until we reach the end, check each group exists in full, if yes reverse it if even else just traverse. 
// for the last group, check how long it is, determine what to do with it


// This has time complexity O(n), as we only touch each node once, and space complexity O(1)
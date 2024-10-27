#include <stdbool.h>


// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    struct ListNode newHead;
    newHead.next = head;

    struct ListNode *cur = head;
    struct ListNode *prev = &newHead;
    struct ListNode *interlist;
    struct ListNode *interListTail;

    int i = 0;
    while(true) {
        i += 1; 

        if (interlist != 0) {
            struct ListNode *next = cur->next;
            cur->next = interlist;
            interlist = cur;
            cur = next;
        }

        if (i == left) {
            interlist = cur;
            interListTail = cur;
            prev->next = 0;
        }

        if (i == right) {
            struct ListNode *next = cur->next;
            cur->next = interlist;
            interlist = cur;

            prev->next = interlist;
            interListTail->next = next;
            break;
        }

        if (interlist == 0) {
            cur = cur->next;
            prev = prev->next;
        }
        
    }
    return newHead.next;
};

int main() {
    struct ListNode a;
    a.val = 5;
    a.next = 0;

    struct ListNode b;
    b.val = 4;
    b.next = &a;

    struct ListNode c;
    c.val = 3;
    c.next = &b;

    struct ListNode d;
    d.val = 2;
    d.next = &c;

    struct ListNode head;
    head.val = 1;
    head.next = &d;

    head.next = 0;

    // struct ListNode* head2 = reverseBetween(&head, 2, 4);
    // struct ListNode* head3 = reverseBetween(&head, 1, 3);
    struct ListNode* head2 = reverseBetween(&head, 1, 1);

    return 0;
};
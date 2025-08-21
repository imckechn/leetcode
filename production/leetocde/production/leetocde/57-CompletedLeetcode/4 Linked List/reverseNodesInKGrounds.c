#include <stdbool.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    struct ListNode newHead;
    newHead.next = head;

    struct ListNode *cur = head;
    struct ListNode *prev = &newHead;
    struct ListNode *interlist;
    struct ListNode *interListTail;

    int i = 0;
    while(cur != 0) {
        i += 1; 

        if (interlist != 0) {
            struct ListNode *next = cur->next;
            cur->next = interlist;
            interlist = cur;
            cur = next;
        }

        if (i == 1) {
            interlist = cur;
            interListTail = cur;
            cur = cur->next;
        }

        if (i == k) {
            prev->next = interlist;
            interListTail->next = cur;
            prev = interListTail;
            interlist = 0;
            interListTail = 0;
            i = 0;
            continue;
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

    // struct ListNode* head2 = reverseBetween(&head, 2, 4);
    struct ListNode* head2 = reverseKGroup(&head, 2);
    // struct ListNode* head2 = reverseBetween(&head, 1, 1);

    return 0;
};
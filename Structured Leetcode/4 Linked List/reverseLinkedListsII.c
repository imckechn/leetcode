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


    while(true) {

        if (cur->val == left) {
            interlist = cur;
            interListTail = cur;

        } else if (cur->val == right) {
            struct ListNode copy;
            copy.val = cur->val;
            copy.next = interlist;
            interlist = &copy;

            prev->next = interlist;
            interListTail->next = cur->next;
            break;

        } else if (interlist != 0) {
            struct ListNode copy;
            copy.val = cur->val;
            copy.next = interlist;
            interlist = &copy;
        }
    
        cur = cur->next;
        if (interlist == 0) {
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
    struct ListNode* head2 = reverseBetween(&head, 1, 3);

    return 0;
};
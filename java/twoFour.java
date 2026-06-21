/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

public class twoFour {
    public ListNode swapPairs(ListNode head) {
        if (head == null) {
            return head;
        }

        ListNode newHead = new ListNode();
        newHead.next = head;

        ListNode first = newHead;
        ListNode second = head;
        ListNode third = head.next;

        while (second.next != null && third != null) {
            first.next = third;
            second.next = third.next;
            third.next = second;

            second = first.next;
            third = second.next;

            for (int i = 0; i < 2; i++) {
                if (third == null) {
                    break;
                }

                first = second;
                second = third;
                third = third.next;
            }
        }

        return newHead.next;
    }
}

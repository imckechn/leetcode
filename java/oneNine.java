public class oneNine {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode newHead = new ListNode();
        newHead.next = head;
        ListNode start = newHead;
        ListNode nextRemoved = newHead;

        for (int i = 0; i < n; i++) {
            if (start.next == null) {
                break;
            }
            start = start.next;
        }

        while (start.next != null) {
            start = start.next;
            nextRemoved = nextRemoved.next;
        }

        nextRemoved.next = nextRemoved.next.next;
        return newHead.next;
    }
}

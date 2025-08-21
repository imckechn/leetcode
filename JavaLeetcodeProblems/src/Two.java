public class Two {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode();
        head.next = new ListNode();

        ListNode ref = head;

        boolean carryOver = false;

        while (l1 != null || l2 != null) {
            ref.next = new ListNode();
            ref = ref.next;

            var a = l1 != null? l1.val : 0;
            var b = l2 != null? l2.val : 0;
            int val = a + b;

            if (carryOver) {
                val += 1;
            }

            if (val >= 10) {
                val -= 10;
                carryOver = true;
            } else {
                carryOver = false;
            }

            if (l1 != null) {
                l1 = l1.next;
            }

            if (l2 != null) {
                l2 = l2.next;
            }

            ref.val = val;
        }

        if (carryOver) {
            ref.next = new ListNode();
            ref.next.val = 1;
        }

        return head.next;
    }
}



public class Two {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;

        ListNode sum = new ListNode();

        boolean carryOver = false;
        do {
            int val = l1.val + l2.val;
            if (carryOver) {
                val += 1;
            }

            if (val > 10) {
                val -= 10;
                carryOver = true;
            } else {
                carryOver = false;
            }

            sum.val = val;
        } while (l1.next != null || l2.next != null);

        return sum;
    }
}



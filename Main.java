public class Main {
    public void Main() {
        //First
        ListNode a = new ListNode();
        a.val = 3;

        ListNode b = new ListNode();
        b.val = 3;
        a.next = b;

        ListNode c = new ListNode();
        c.val = 3;
        b.next = c;

        //Second
        ListNode x = new ListNode();
        x.val = 3;

        ListNode y = new ListNode();
        y.val = 3;
        x.next = b;

        ListNode z = new ListNode();
        z.val = 3;
        y.next = b;

        //Main
        ListNode ans = Two.addTwoNumbers(a, x)

    }
}

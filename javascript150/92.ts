
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}


function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
    let newHead = new ListNode(0, head)
    let lp = newHead, rp = newHead

    for (let i = 0; i < right-left+1; i++) {
        rp = rp!.next!
    }

    for (let i = 0; i < left-1; i++) {
        lp = lp!.next!
        rp = rp!.next!
    }

    for (let i = 0; i < right-left; i++) {
        let next = lp!.next
        lp!.next = next!.next

        next!.next = rp!.next
        rp!.next = next
    }

    return newHead.next
};

let a = new ListNode(5)
let b = new ListNode(4, a)
let c = new ListNode(3, b)
let d = new ListNode(2, c)
let e = new ListNode(1, d)

reverseBetween(b, 1, 2)
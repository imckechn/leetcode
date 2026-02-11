class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let carryOver = 0
    let first = 0
    let answer = new ListNode(0);
    let current = answer

    while (l1 != null || l2 != null) {
        first = l1?.val? l1?.val: 0
        first += l2?.val? l2?.val: 0

        first += carryOver
        carryOver = Math.floor(first/10)
        first %= 10

        
        current.next = new ListNode(first)
        current = current.next

        l1 = l1?.next? l1?.next: null
        l2 = l2?.next? l2?.next: null
    }

    if (carryOver != 0) {
        current.next = new ListNode(carryOver)
    }

    return answer.next
}
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    let newList = new ListNode()
    let head = newList

    while (list1 != null || list2 != null) {
        let a = list1? list1.val: null
        let b = list2? list2.val: null

        if (a != null && b != null) {
            newList.next = new ListNode(Math.min(a, b))
            newList = newList.next
            
            if (newList.val == a) {
                list1 = list1!.next
            } else {
                list2 = list2!.next
            }

        } else if (a != null) {
            newList.next = new ListNode(a)
            newList = newList.next
            list1 = list1!.next

        } else if (b != null) {
            newList.next = new ListNode(b)
            newList = newList.next
            list2 = list2!.next
        }
    }
    return head.next
};

let a = new ListNode(4)
let b = new ListNode(2, a)
let c = new ListNode(1, b)

let x = new ListNode(4)
let y = new ListNode(3, x)
let z = new ListNode(1, y)

mergeTwoLists(z, c)
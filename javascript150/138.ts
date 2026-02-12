class _Node {
    val: number
    next: _Node | null
    random: _Node | null

    constructor(val?: number, next?: _Node, random?: _Node) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
        this.random = (random===undefined ? null : random)
    }
}


let visited = new Map()
function copyRandomList(head: _Node | null): _Node | null {
    if (!head) return null
    if (visited.has(head)) return visited.get(head)

    let newHead = new _Node(head?.val)
    visited.set(head, newHead)

    newHead.next = head!.next?copyRandomList(head!.next): null
    newHead.random = head!.random?copyRandomList(head!.random): null
    return newHead
};
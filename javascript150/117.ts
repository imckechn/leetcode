class _Node {
    val: number
    left: _Node | null
    right: _Node | null
    next: _Node | null

    constructor(val?: number, left?: _Node, right?: _Node, next?: _Node) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
        this.next = (next===undefined ? null : next)
    }
}



function connect(root: _Node | null): _Node | null {
    if (!root) return null;
    let current = root
    let stack: [_Node, number][] = []
    let rightLine: _Node[] = []
    let level = 0

    while (current) {
        if (rightLine.length > level) {
            current.next = rightLine[level]
            rightLine[level] = current
        } else {
            rightLine.push(current)
        }

        if (current.left) {
            stack.push([current.left, level+1])
        }

        if (current.right) {
            current = current.right 
            level += 1
        } else if (stack.length >= 1) {
            let pair = stack.pop()!
            current = pair[0]
            level = pair[1]
        } else {
            break
        }
    }

    return root
};

let left = new _Node(4)
let mid = new _Node(5)
// let right = new _Node(7)
let midLeft = new _Node(2, left, mid)
let midRight = new _Node(3)
let head = new _Node(1, midLeft, midRight)

connect(head)
// class TreeNode {
//     val: number
//     left: TreeNode | null
//     right: TreeNode | null
//     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
//         this.val = (val===undefined ? 0 : val)
//         this.left = (left===undefined ? null : left)
//         this.right = (right===undefined ? null : right)
//     }
// }


function flatten(root: TreeNode | null): void {
    if (!root) return

    let order: TreeNode[] = []
    let queue: TreeNode[] = []
    let current = root

    while (current) {
        order.push(current)
        
        if (current.right) queue.push(current.right);

        if (current.left) {
            current = current.left
        } else if (queue.length != 0) {
            current = queue.pop()!
        } else {
            break
        }
    }

    for (let i = 0; i < order.length-1; i++) {
        order[i].left = null
        order[i].right = order[i+1]
    }

    order[order.length-1].left = null
    order[order.length-1].right = null
};

let left = new TreeNode(3)
let mid = new TreeNode(4)
let right = new TreeNode(6)
let midLeft = new TreeNode(2, left, mid)
let midRight = new TreeNode(5, right)
let head = new TreeNode(1, midLeft, midRight)
flatten(head)
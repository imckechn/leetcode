class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

class FindKSmallest {
    count: number = 0

    constructor() {
        this.count = 0
    }

    discover(root:TreeNode | null, k: number): number {
        if (!root) return -1

        let ans = this.discover(root.left, k)
        if (ans != -1) return ans

        this.count += 1
        if (this.count == k) return root.val

        return this.discover(root.right, k)
    }
}

function kthSmallest(root: TreeNode | null, k: number): number {
    let finder = new FindKSmallest()
    return finder.discover(root, k)
};


let a = new TreeNode(1)
let b = new TreeNode(2, a)
let c = new TreeNode(4)
let d = new TreeNode(3, b, c)
let e = new TreeNode(5)
let head = new TreeNode(5, d, e)

// console.log(kthSmallest(head, 1))
// console.log(kthSmallest(head, 2))
console.log(kthSmallest(head, 3))
console.log(kthSmallest(head, 4))
console.log(kthSmallest(head, 5))
console.log(kthSmallest(head, 6))
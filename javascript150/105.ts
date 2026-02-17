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


function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    if (inorder.length == 0) return null

    let root = new TreeNode(preorder.splice(0, 1)[0])
    
    if (inorder.length == 1) return root

    root.left = buildTree(preorder, inorder.slice(0, inorder.indexOf(root.val)))
    root.right = buildTree(preorder, inorder.slice(inorder.indexOf(root.val)+1))
    return root
};

let newAns = buildTree([3,1,2,4], [1,2,3,4])
// let newAns = buildTree([1,2], [1,2])
let ans = buildTree([3,9,20,15,7], [9,3,15,20,7])
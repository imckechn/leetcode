/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function check(left: TreeNode | null, right: TreeNode | null): boolean {
    if (!left && !right) {
        return true

    } else if (!left && right || left && !right || left!.val != right!.val) {
        return false
    
    } else {
        return check(left!.left, right!.right) && check(left!.right, right!.left)
    }
}

function isSymmetric(root: TreeNode | null): boolean {
    if (!root) return true;
    return check(root.left, root.right)
};
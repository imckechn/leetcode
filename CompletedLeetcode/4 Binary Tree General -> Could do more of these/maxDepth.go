
// Definition for a binary tree node.
type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	var l, r int

    if root == nil {return 0}

	if root.Left != nil {
		l = maxDepth(root.Left)
	}

	if root.Right != nil {
		r = maxDepth(root.Right)
	}

	if r > l {
		return r+1
	}

	return l+1
}
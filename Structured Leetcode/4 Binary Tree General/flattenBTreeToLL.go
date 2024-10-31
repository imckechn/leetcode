package main

func main() {
	head := TreeNode{}
	head.Val = 1

	a := TreeNode{}
	a.Val = 2
	head.Left = &a

	b := TreeNode{}
	b.Val = 4
	a.Right = &b

	c := TreeNode{}
	c.Val = 3
	a.Left = &c

	d := TreeNode{}
	d.Val = 5
	head.Right = &d

	e := TreeNode{}
	e.Val = 6
	d.Right = &e

	flatten(&head)
}

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

//func (t TreeNode) setRightChild(temp *TreeNode) {
//	iter := t.Right
//
//	for iter.Right != nil {
//		iter = iter.Right
//	}
//
//	iter.Right = temp
//}

func setRightChild(t, temp *TreeNode) {
	iter := t.Right

	for iter.Right != nil {
		iter = iter.Right
	}

	iter.Right = temp
}

func flatten(root *TreeNode) {
	if root == nil || (root.Right == nil && root.Left == nil) {
		return
	}

	if root.Right != nil {
		flatten(root.Right)
	}

	if root.Left != nil {
		flatten(root.Left)
	} else {
		return
	}

	temp := root.Right
	root.Right = root.Left
	root.Left = nil

	setRightChild(root, temp)
}

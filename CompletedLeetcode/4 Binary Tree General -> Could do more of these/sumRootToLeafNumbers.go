package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs(root *TreeNode, count int) int {
	count *= 10
	if root == nil {
		return 0
	} else if root.Right == nil && root.Left == nil {
		count += root.Val
		return count
	}

	countA := dfs(root.Right, count+root.Val)
	countB := dfs(root.Left, count+root.Val)
	return countA + countB
}

func sumNumbers(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return dfs(root, 0)
}

func main() {
	root := &TreeNode{
		Val: 1,
		Left: &TreeNode{
			Val: 2,
		},
		Right: &TreeNode{
			Val: 3,
		},
	}

	newRoot := &TreeNode{
		Val:   1,
		Right: root,
	}

	fmt.Println(sumNumbers(newRoot))
}

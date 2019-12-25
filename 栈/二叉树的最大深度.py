# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDefpt = self.maxDepth(root.right)
        return max(leftDepth, rightDefpt) + 1

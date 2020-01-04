# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True

        def Tree_depth(node: TreeNode) -> int:
            if node == None:
                return 0
            left_depth = Tree_depth(node.left) + 1
            right_depth = Tree_depth(node.right) + 1
            if abs(left_depth - right_depth) > 1:
                self.res = False
            return max(left_depth, right_depth)

        Tree_depth(root)
        return self.res

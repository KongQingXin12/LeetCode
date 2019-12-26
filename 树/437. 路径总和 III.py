# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if sum == 0:
            self.res += 1
        if not root: return 0
        
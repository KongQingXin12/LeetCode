# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        while True:
            if p.val <= root.val and q.val >= root.val:
                break
            if q.val < root.val:
                root = root.left
            elif p.val > root.val:
                root = root.right
        return root

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         def preorder(root: TreeNode) -> List:
#             if not root: return []
#             stack = []
#             res = []
#             while True:
#                 while root:
#                     res.append(root.val)
#                     stack.append(root.right)
#                     root = root.left
#                 root = stack.pop()
#                 if root: res.append(root.val)
#                 if not stack: break
#             return res
#
#         return preorder(p) == preorder(q)

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None: return True
        if p == None or q == None: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    S = Solution()
    print(S.isSameTree(p, q))

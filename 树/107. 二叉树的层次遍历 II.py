# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            m = len(stack)
            temp = []
            for i in range(m):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            if res:
                res.insert(0, temp)
            else:
                res.append(temp)
        return res


# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
#         res = []
#         cur = [root]
#         while cur:
#             cur_layer_val = []
#             next_layer_node = []
#             for node in cur:
#                 if node:
#                     cur_layer_val.append(node.val)
#                     next_layer_node.extend([node.left, node.right])
#             if cur_layer_val:
#                 res.insert(0, cur_layer_val)
#             cur = next_layer_node
#         return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    S = Solution()
    print(S.levelOrderBottom(root))

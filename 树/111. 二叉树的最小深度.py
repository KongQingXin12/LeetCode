# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def minDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0
#
#         children = [root.left, root.right]
#         # if we're at leaf node
#         if not any(children):
#             return 1
#
#         min_depth = float('inf')
#         for c in children:
#             if c:
#                 min_depth = min(self.minDepth(c), min_depth)
#         return min_depth + 1


# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         res = 0
#         cur = [root]
#         temp = []
#         while cur:
#             next_layer_node = []
#             for node in cur:
#                 if node:
#                     next_layer_node.extend([node.left, node.right])
#             temp.append(cur)
#             cur = next_layer_node
#         layers_len = 1
#         for t in temp:
#             if len(t) == 1:
#                 res += 1
#             else:
#                 layers_len = len(t)
#
#         return res

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        else:
            stack, min_depth = [(1, root)], float('inf')

        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):  # 判断叶节点
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))

        return min_depth


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    S = Solution()
    print(S.minDepth(root))

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        stack = []
        res = []
        i = 1
        stack.append(root)
        while stack:
            temp = []
            for j in range(len(stack)):
                if stack[0].left: stack.append(stack[0].left)
                if stack[0].right: stack.append(stack[0].right)
                temp.append(stack[0].val)
                stack = stack[1:]
            if i % 2 == 1:
                res.append(temp)
            else:
                res.append(temp[::-1])
            i += 1
        return res


if __name__ == '__main__':
    S = Solution()
    head = TreeNode(3)
    head.left = TreeNode(9)
    head.right = TreeNode(20)
    head.right.left = TreeNode(15)
    head.right.right = TreeNode(7)
    print(S.zigzagLevelOrder(head))

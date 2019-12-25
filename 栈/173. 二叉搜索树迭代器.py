# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class BSTIterator:
#
#     def __init__(self, root: TreeNode):
#         self.root = root
#         self.InorderList = self.InOrder()
#         self.i = 0
#
#     def InOrder(self, ) -> List[int]:
#         node = self.root
#         res = []
#         stack = []
#         while 1:
#             while node is not None:
#                 stack.append(node)
#                 node = node.left
#             if stack == []: break
#             node = stack.pop()
#             res.append(node.val)
#             node = node.right
#         return res
#
#     def next(self) -> int:
#         """
#         @return the next smallest number
#         """
#         res = self.InorderList[self.i]
#         self.i += 1
#         return res
#
#     def hasNext(self) -> bool:
#         """
#         @return whether we have a next smallest number
#         """
#         if self.i < len(self.InorderList):
#             return True
#         return False

from collections import deque


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.head = root
        self.stack = deque()

        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """

        cur = self.stack.pop()
        root = cur.right
        while root:  # 使用了循环，复杂度不应该为O(1)?
            self.stack.append(root)
            root = root.left

        return cur.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == '__main__':
    head = TreeNode(7)
    head.left = TreeNode(3)
    head.right = TreeNode(15)
    head.right.left = TreeNode(9)
    head.right.right = TreeNode(20)
    S = BSTIterator(head)
    print(S.next())
    print(S.next())
    print(S.hasNext())
    print(S.next())
    print(S.hasNext())
    print(S.next())
    print(S.hasNext())
    print(S.next())
    print(S.hasNext())

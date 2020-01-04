from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         if not nums:
#             return None
#
#         # 找到中点作为根节点
#         mid = len(nums) // 2
#         node = TreeNode(nums[mid])
#
#         # 左侧数组作为左子树
#         left = nums[:mid]
#         right = nums[mid + 1:]
#
#         # 递归调用
#         node.left = self.sortedArrayToBST(left)
#         node.right = self.sortedArrayToBST(right)
#
#         return node

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) >> 1
        node = TreeNode(nums[mid])

        left = nums[:mid]
        right = nums[mid + 1:]

        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)

        return node


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    S = Solution()
    node = S.sortedArrayToBST(nums)

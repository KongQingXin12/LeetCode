# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        s = []
        while 1:
            while root:
                s.append(root)
                root = root.left
                if root and root.left == None and root.right == None:
                    res += root.val
            if not s:
                break
            root = s.pop()

            root = root.right

        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    S = Solution()
    print(S.sumOfLeftLeaves(root))

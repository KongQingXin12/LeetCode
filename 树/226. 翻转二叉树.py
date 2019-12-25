# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        s = [root]
        while s:
            for i in range(len(s)):
                r = s.pop(0)
                if r == None: continue
                t = r.left
                r.left = r.right
                r.right = t
                s.extend([r.left, r.right])
            if not any(s):
                break
        return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    S = Solution()
    ans = S.invertTree(root)

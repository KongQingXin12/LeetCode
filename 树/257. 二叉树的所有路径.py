# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        res = []
        temp = []
        temp.append(root.val)

        def FindPath(node: TreeNode):
            if node.left == None and node.right == None:
                res.append(temp[:])
            if node.left:
                temp.append(node.left.val)
                FindPath(node.left)
                temp.pop()
            if node.right:
                temp.append(node.right.val)
                FindPath(node.right)
                temp.pop()

        FindPath(root)
        res_str = []
        for r in res:
            s = ''
            for node in r:
                s += str(node)
                s += '->'
            res_str.append(s[:-2])
        return res_str


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    S = Solution()
    print(S.binaryTreePaths(root))

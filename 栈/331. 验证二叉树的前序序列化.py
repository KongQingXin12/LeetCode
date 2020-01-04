# class Solution:
#     def isValidSerialization(self, preorder: str) -> bool:
#         if len(preorder) == 1 and preorder == '#': return True
#         if len(preorder) < 3: return False
#         stack = []
#         temp = ''
#         for i, node in enumerate(preorder):
#             while stack and node == '#' and stack[-1] == '#':
#                 if len(stack) < 2: return False
#                 stack.pop()
#                 stack.pop()
#             if node == ',' and temp != '':
#                 stack.append(temp)
#                 temp = ''
#             if node != ',' and i != len(preorder) - 1:
#                 temp += node
#             elif len(stack) == 0 and i < len(preorder) - 1:
#                 return False
#         if len(stack) == 0: return True
#         return False

# # 思路一的精简版
# class Solution:
#     def isValidSerialization(self, preorder: str) -> bool:
#         preorder = preorder.split(',')
#         if not preorder:
#             return False
#         stack = []
#         for c in preorder:
#             while stack and stack[-1] == '#' and c == '#':
#                 stack.pop()
#                 if not stack:
#                     return False
#                 stack.pop()
#             stack.append(c)
#         return len(stack) == 1 and stack[0] == '#'

# 思路3 入度等于出度
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        count = 1
        for c in preorder.split(','):
            count -= 1
            if count < 0: return False
            if c != '#':
                count += 2
        return count == 0


if __name__ == '__main__':
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    S = Solution()
    print(S.isValidSerialization(preorder))

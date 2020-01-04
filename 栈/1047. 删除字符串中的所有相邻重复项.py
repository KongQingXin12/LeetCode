class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = ['0']
        for s in S:
            if s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
        return ''.join(stack[1:])


if __name__ == '__main__':
    S = Solution()
    Str = "abbaca"
    print(S.removeDuplicates(Str))

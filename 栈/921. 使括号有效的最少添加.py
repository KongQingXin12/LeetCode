class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        res = 0
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                if stack:
                    stack.pop()
                else:
                    res += 1
        res += len(stack)
        return res


if __name__ == '__main__':
    Str = "())"
    S = Solution()
    print(S.minAddToMakeValid(Str))

class Solution:
    def decodeString(self, S: str) -> str:
        stack = []
        res = ''
        for s in S:
            if s == ']':
                temp = ''
                times = ''
                while stack[-1] != '[':
                    temp += stack.pop()
                stack.pop()
                temp = "".join(list(temp)[::-1])
                while stack and '0' <= stack[-1] and stack[-1] <= '9':
                    times += stack.pop()
                times = "".join(list(times)[::-1])
                if '[' in stack:
                    stack += list((int(times) * temp))
                else:
                    res += int(times) * temp
            else:
                if s >= 'a' and s <= 'z' and '[' not in stack:
                    res += s
                else:
                    stack.append(s)
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.decodeString("sd2[f2[e]g]i"))

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        n = len(s)
        res = [0] * n
        t = '1'
        for i in range(n - 1, -1, -1):
            temp = s[i] + t
            if temp == '00' or (int(temp) > 26 and int(temp) % 10 == 0):
                return 0
            if s[i] == '0':
                if i == n - 1:
                    res[i] = 0
                else:
                    res[i] = res[i + 1]
                t = s[i]
                continue
            if i == n - 1:
                if s[i] == '0':
                    res[i] = 0
                else:
                    res[i] = 1
            elif i == n - 2:
                if (temp == '10' or temp == '20' or int(temp) > 26):
                    res[i] = 1
                else:
                    res[i] = 2
            else:
                if temp == '10' or temp == '20' or int(temp) > 26:
                    res[i] = res[i + 1]
                else:
                    res[i] += (res[i + 1] + res[i + 2])

            t = s[i]

        return res[0]


if __name__ == '__main__':
    s = "1010"
    S = Solution()
    print(S.numDecodings(s))

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        n1 = list(num1[::-1])
        n2 = list(num2[::-1])
        numZero = abs(len(n1) - len(n2))
        if len(n1) > len(n2):
            n2.extend(['0'] * numZero)
        elif len(n1) < len(n2):
            n1.extend(['0'] * numZero)
        i = 0
        j = 0
        jinwei = 0
        while i < len(n1) and j < len(n2):
            he = int(n1[i]) + int(n2[j]) + jinwei
            ans.append(str(he % 10))
            jinwei = he // 10
            i += 1
            j += 1
        if jinwei == 1:
            ans.append('1')
        return "".join(ans[::-1])


if __name__ == '__main__':
    num1 = input()
    num2 = input()
    s = Solution()
    print(s.addStrings(num1, num2))

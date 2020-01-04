class Solution:

    def isHappy(self, n: int) -> bool:
        ss = set()
        while True:
            if n == 1:
                return True
            total = 0
            while n:
                total += (n % 10) * (n % 10)
                n //= 10
            if total in ss:
                return False
            ss.add(total)
            n = total


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(1))

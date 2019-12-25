from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if low < 0:
            low = 1
        if high < 0:
            return []
        slow = str(low)
        shigh = str(high)
        l = len(slow)
        r = len(shigh)
        ans = []
        for k in range(l, r + 1):
            for i in range(10 - k + 1):
                if i + k > 10:
                    break
                temp = ''
                for j in range(k):
                    temp += str(numList[i + j])
                if int(temp) >= low and int(temp) <= high and len(str(int(temp))) == k:
                    ans.append(int(temp))
                elif int(temp) > high:
                    break

        return ans


if __name__ == '__main__':
    low = 0
    high = 3456
    S = Solution()
    S.sequentialDigits(low, high)

from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        m = len(T)
        res = [0] * m
        temp = []
        for t, temperature in enumerate(T):
            while temp and temperature > T[temp[-1]]:
                res[temp[-1]] = t - temp[-1]
                temp = temp[:-1]
            temp.append(t)
        return res


if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    S = Solution()
    print(S.dailyTemperatures(T))

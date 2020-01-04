from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0

        for point in points:
            calculate = {}
            for check in points:
                if check != point:
                    x = abs(check[0] - point[0])
                    y = abs(check[1] - point[1])
                    l = x ** 2 + y ** 2
                    if l in calculate:
                        calculate[l] += 1
                    else:
                        calculate[l] = 1
            for key in calculate:
                if calculate[key] > 1:
                    res += calculate[key] * (calculate[key] - 1)
        return res


if __name__ == '__main__':
    points = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
    S = Solution()
    S.numberOfBoomerangs(points)

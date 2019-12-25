from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 将三个数由小到大排列
        def Sort_xyz(x, y, z, ) -> List:
            l = [x, y, z]
            l.sort()
            return l

        # 求最大公约数
        def Gcd(x, y, z) -> int:

            x, y, z = Sort_xyz(x, y, z)
            while y != 0:
                temp = y
                y = x % y
                x = temp

            if x < z:
                temp = x
                x = z
                z = temp

            while z != 0:
                temp = z
                z = x % z
                x = temp
            return x

        # 计算直线公式：ax+b-cy=0
        def calculate_slope(x, y):
            a = x[1] - y[1]
            b = x[0] * y[1] - x[1] * y[0]
            c = x[0] - y[0]
            gcd = Gcd(abs(a), abs(b), abs(c))
            return (a // gcd, b // gcd, c // gcd) if a > 0 else (-1 * a // gcd, -1 * b // gcd, -1 * c // gcd)

        if len(points) <= 1: return len(points)

        res = 0
        slopes = []
        for X in points:
            for Y in points:
                if X != Y:  # 相同点不计算斜率
                    slope = calculate_slope(X, Y)
                    if slope not in slopes:
                        slopes.append(slope)

        if len(slopes) == 0:
            return len(points)

        for slope in slopes:
            temp_res = 0
            a, b, c = slope
            for point in points:
                if a * point[0] + b - c * point[1] == 0:
                    temp_res += 1
            res = max(res, temp_res)

        return res


if __name__ == '__main__':
    points = [[0, 0], [0, 0]]
    S = Solution()
    print(S.maxPoints(points))

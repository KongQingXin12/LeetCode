from typing import List


# class Solution:
#     def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
#         m = len(mat)
#         n = len(mat[0])
#         boundary = min(m, n)
#         if boundary == 1:
#             return 0
#         res = 0
#
#         def bfs(x: int, y: int, k: int) -> bool:
#             if x + k > m or y + k > n:
#                 return False
#             res = 0
#             for i in range(x, x + k + 1):
#                 for j in range(y, y + k + 1):
#                     res += mat[i][j]
#                     if res > threshold:
#                         return False
#             if res > threshold:
#                 return False
#             return True
#
#         for k in range(1, boundary):
#             i = 0
#             j = 0
#             while i < m - k:
#                 if j < n - k and bfs(i, j, k):
#                     res = k
#                 if res == k:
#                     break
#                 j += 1
#                 i += j // n
#                 j %= n
#         if res:
#             return res + 1
#         return 0
class Solution():

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if not mat or not mat[0]: return 0
        row = len(mat)
        col = len(mat[0])
        # 把前i行j列组成的矩形的面积求出来
        prefix = [[0] * (col + 1) for _ in range(row + 1)]

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]
        left = 0
        right = min(row, col)

        def check(mid):
            for i in range(row - mid + 1):
                for j in range(col - mid + 1):
                    if threshold >= prefix[i + mid][j + mid] - prefix[i + mid][j] - prefix[i][j + mid] + prefix[i][j]:
                        return True
            return False

        while left <= right:
            # print(left, right)
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right


if __name__ == '__main__':
    mat = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    threshold = 6
    S = Solution()
    print(S.maxSideLength(mat, threshold))

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = list()
        q.append([n, 0])
        visited = [False for i in range(n + 1)]
        visited[n] = True

        while any(q):
            num, step = q.pop(0)

            i = 1
            tNum = num - i ** 2
            while tNum >= 0:
                if tNum == 0:
                    return step + 1

                if not visited[tNum]:
                    q.append((tNum, step + 1))
                    visited[tNum] = True

                i += 1
                tNum = num - i ** 2


# class Solution:
#     res = 10e10
#     visited = []
#
#     def numSquares(self, n: int) -> int:
#         self.visited = [False for i in range(n + 1)]
#
#         def dfs(num: int, step: int):
#             if num == 0:
#                 self.res = step
#                 return
#             if self.res > step:
#                 for i in range(int(num ** 0.5), 0, -1):
#                     dfs(num - i ** 2, step + 1)
#
#         if n % 4 == 0:
#             n //= 4
#         dfs(n, 0)
#         return self.res


if __name__ == '__main__':
    n = int(input('请输入一个数字：'))
    S = Solution()
    print(S.numSquares(n))

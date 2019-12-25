from typing import List


# class Solution:
#     def sumSubarrayMins(self, A: List[int]) -> int:
#         stack_min = []
#         res = sum(A) % int((10e9 + 7))
#         for i, a in enumerate(A):
#             while stack_min and stack_min[-1][1] > a:
#                 stack_min.pop(-1)
#             stack_min.append((i, a))
#         end = 0
#         for j in range(2, len(A) + 1):
#             for start in range(len(A)):
#                 if start + j > len(A):
#                     break
#                 for Min in stack_min:
#                     if Min[0] >= start and Min[0] < start + j:
#                         res = (res + Min[1]) % int((10e9 + 7))
#                         break
#         return res

# class Solution:
#     def sumSubarrayMins(self, A: List[int]) -> int:
#         res = 0
#         for i, a in enumerate(A):
#             Min = a
#             for b in A[:i + 1]:
#                 if b <= Min:
#                     Min = b
#                 res += Min
#         return res

# class Solution:
#     def sumSubarrayMins(self, A: List[int]) -> int:
#         M = int(1e9 + 7)
#         sum = [0] * len(A)
#         stack = []
#         res = 0
#
#         for i, a in enumerate(A):
#             while stack and A[stack[-1]] >= a:
#                 stack.pop()
#             if not stack:
#                 sum[i] = A[i] * (i + 1)
#             else:
#                 sum[i] = sum[stack[-1]] + A[i] * (i - stack[-1])
#             sum[i] %= M
#             res += sum[i]
#             res %= M
#             stack.append(i)
#         return res

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        s = []
        res = 0
        A = [-9999999999] + A + [-999999999]
        n = len(A)
        for i in range(n):
            while s and A[s[-1]] > A[i]:
                t = s.pop()
                temp = A[t] * (i - t) * (t - s[-1])
                res = (res + A[t] * (i - t) * (t - s[-1])) % mod
            s.append(i)

        return res


if __name__ == '__main__':
    A = [3, 1, 2, 4]
    S = Solution()
    print(S.sumSubarrayMins(A))

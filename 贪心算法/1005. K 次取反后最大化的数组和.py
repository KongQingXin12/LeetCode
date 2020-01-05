from typing import List


# class Solution:
#     def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
#         A.sort()
#         i = 0
#         for i in range(K):
#             A[0] = -A[0]
#             A.sort()
#             if A[0] >= 0:
#                 break
#         if (K - i) % 2 == 0:
#             A[0] = -A[0]
#         return sum(A)


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for i in range(len(A)):
            if A[i] < 0 and K > 0:
                A[i] = -A[i]
                K -= 1
        A.sort()
        while K > 0:
            A[0] = -A[0]
            K -= 1
        return sum(A)


if __name__ == '__main__':
    A = [5, 6, 9, -3, 3]
    K = 2
    S = Solution()
    print(S.largestSumAfterKNegations(A, K))

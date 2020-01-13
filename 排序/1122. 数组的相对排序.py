from typing import List


# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         t = []
#         count = {}
#         res = []
#         for a1 in arr1:
#             if a1 in arr2:
#                 if a1 in count:
#                     count[a1] += 1
#                 else:
#                     count[a1] = 1
#             else:
#                 t.append(a1)
#         for a2 in arr2:
#             res += [a2] * count[a2]
#         t.sort()
#         res += t
#         return res

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        fltrd_not = sorted([i for i in arr1 if i not in arr2])
        out = []
        for i in arr2:
            cnt = arr1.count(i)
            out.extend([i] * cnt)
        out.extend(fltrd_not)
        return out


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    S = Solution()
    print(S.relativeSortArray(arr1, arr2))

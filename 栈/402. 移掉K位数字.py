# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         if k == 0:
#             return num
#         if k == len(num) - 1:
#             res = num[0]
#             for ss in num:
#                 res = min(res, ss)
#             return res
#         if k >= len(num): return '0'
#         stack = []  # 维护一个递增站
#         m = len(num)
#         res = ""
#         for i, s in enumerate(num):
#             if len(stack) == m - k:
#                 if s < stack[-1]:
#                     stack[-1] = s
#                 continue
#             while stack and len(stack) + m - 1 - i >= m - k and s <= stack[-1]:
#                 if s == stack[-1] and len(stack) < m - k:
#                     i += 1
#                     continue
#                 else:
#                     stack.pop()
#             # if cnt == k:
#             #     if stack:
#             #         res += "".join(stack)
#             #         stack = []
#             #     res += s
#             stack.append(s)
#         res = str(int("".join(stack)))
#         return res

# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         res = []
#         m = len(num) - k
#         start = 0
#         for i in range(m):
#             end = k + i + 1 if k + i + 1 < len(num) else len(num)
#             Min = min(num[start:end])
#             res.append(Min)
#             while Min in num[start:end]:
#                 start = num[start:end].index(Min) + 1 + start
#         return int("".join(res))

# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         len_num = len(num)
#         if k == len_num:
#             return '0'
#
#         new_num = []
#         for n in num:
#             while new_num and k > 0 and n < new_num[-1]:
#                 new_num.pop(-1)
#                 k -= 1
#
#             new_num.append(n)
#
#         if k > 0:
#             new_num = new_num[:-k]
#
#         no_zero_num = self._erase_zero_in_left(new_num)
#         return ''.join(no_zero_num)
#
#     @staticmethod
#     def _erase_zero_in_left(new_str_list):
#         while len(new_str_list) > 1:
#             if new_str_list[0] == '0':
#                 new_str_list.pop(0)
#                 continue
#
#             break
#
#         return new_str_list

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0: return num
        if len(num) <= k: return "0"
        res = []
        for n in num:
            while res and n < res[-1] and k > 0:
                res.pop(-1)
                k -= 1
            res.append(n)
        if k > 0:
            res = res[:-k]
        return str(int("".join(res)))


if __name__ == '__main__':
    num = "1432219"
    k = 3
    S = Solution()
    print(S.removeKdigits(num, k))

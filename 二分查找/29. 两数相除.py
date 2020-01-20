# class Solution:
#     def divide(self, divd: int, dior: int) -> int:
#         res = 0
#         sign = 1 if divd ^ dior >= 0 else -1
#         # print(sign)
#         divd = abs(divd)
#         dior = abs(dior)
#         while divd >= dior:
#             tmp, i = dior, 1
#             while divd >= tmp:
#                 divd -= tmp
#                 res += i
#                 i <<= 1
#                 tmp <<= 1
#         res = res * sign
#         return min(max(-2 ** 31, res), 2 ** 31 - 1)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor: return 1
        if dividend == abs(divisor) or abs(dividend) == divisor: return -1
        sign = 1 if dividend ^ divisor > 0 else -1
        res = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        res *= sign
        return min(2 ** 31 - 1, max(-2 ** 31, res))


if __name__ == '__main__':
    S = Solution()
    divd = 1
    dior = 1
    print(S.divide(divd, dior))

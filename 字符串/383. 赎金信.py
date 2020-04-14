# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         c1 = {}
#         c2 = {}
#         for r in ransomNote:
#             if r in c1:
#                 c1[r] += 1
#             else:
#                 c1[r] = 1
#         for m in magazine:
#             if m in c2:
#                 c2[m] += 1
#             else:
#                 c2[m] = 1
#
#         for c in c1:
#             if c in c2:
#                 if c2[c] < c1[c]:
#                     return False
#             else:
#                 return False
#
#         return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n = 0
        while n < 26:
            if ransomNote.count()


if __name__ == '__main__':
    S = Solution()
    ransomNote = 'aa'
    magazine = 'aab'
    print(S.canConstruct(ransomNote, magazine))

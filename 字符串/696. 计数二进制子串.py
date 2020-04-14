from xlwings import xrange


class Solution(object):
    def countBinarySubstrings(self, s):
        groups = [1]
        for i in xrange(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in xrange(1, len(groups)):
            ans += min(groups[i - 1], groups[i])
        return ans


if __name__ == '__main__':
    s = Solution()
    test = "00110011"
    print(s.countBinarySubstrings(test))

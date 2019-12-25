from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        LeftStack = []
        for num in asteroids:
            if num > 0: stack.append(num)
            if num < 0:
                temp = num
                while stack and temp:
                    if stack[-1] + temp > 0:
                        temp = 0
                    elif stack[-1] + temp == 0:
                        temp = 0
                        stack.pop()
                    else:
                        stack.pop()
                if temp:
                    LeftStack.append(temp)
        return LeftStack + stack


if __name__ == '__main__':
    asteroids = [-2, -1, 1, 2]
    S = Solution()
    print(S.asteroidCollision(asteroids))

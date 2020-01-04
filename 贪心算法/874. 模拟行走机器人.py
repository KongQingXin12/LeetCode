from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        '''
        :param commands:
        :param obstacles:
        x:横坐标
        y:纵坐标
        机器人初始状态 y+
        :return:
        '''
        x = 0
        y = 0
        direction = 'y+'

        def SwitchDirection(direc: str, turn: int) -> str:
            res = ''
            if direc == 'y+':
                if turn == -1:
                    res = 'x+'
                if turn == -2:
                    res = 'x-'
            elif direc == 'y-':
                if turn == -1:
                    res = 'x-'
                if turn == -2:
                    res = 'x+'
            elif direc == 'x+':
                if turn == -1:
                    res = 'y-'
                if turn == -2:
                    res = 'y+'
            elif direc == 'x-':
                if turn == -1:
                    res = 'y+'
                if turn == -2:
                    res = 'y-'
            return res

        for l in commands:
            if l == -1 or l == -2:
                direction = SwitchDirection(direction, l)
            else:
                if direction == 'y+':
                    y += l
                elif direction == 'y-':
                    y -= l
                elif direction == 'x+':
                    x += l
                elif direction == 'x-':
                    x -= l
